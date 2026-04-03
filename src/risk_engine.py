import argparse
import json
import sys
from dotenv import load_dotenv
from datetime import datetime, timedelta
from google import genai
from location_engine import get_segmentInfo

load_dotenv()

#1. Reuseable risk calculator, used to escalate.
def calculate_risk_score(reports_48h: int, total_severity: int, traffic_multiplier: float) -> float:
    if reports_48h > 0:
        average_severity = total_severity / reports_48h
        volume_penalty = reports_48h * 1.2
        return (average_severity + volume_penalty) * traffic_multiplier
    return 0.0

#2. Everything below this line ONLY runs if this file is executed directly from the terminal. It will NOT run when imported.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Park Hazard Aggregator & Escalation Engine")
    parser.add_argument("--segment", type=int, required=True)
    args = parser.parse_args()

    try:
        with open("hazard_db.json", "r") as f:
            db = json.load(f)
    except FileNotFoundError:
        print("Error: No database found. Run analysis.py first to generate data.")
        sys.exit(1)

    now = datetime.now()
    reports_48h = 0
    total_severity = 0
    recent_hazards = [] 

    loc_info = get_segment_info(args.segment)
    traffic_multiplier = loc_info["traffic_multiplier"]
    segment_name = loc_info["name"]

    for report in db:
        if report["trail_segment"] == args.segment:
            try:
                report_time = datetime.strptime(report["reported_timestamp"], "%Y-%m-%d %H:%M")
                if now - report_time <= timedelta(hours=48):
                    reports_48h += 1
                    total_severity += report["severity_rating"]
                    cat = report.get('hazard_type', 'Unknown')
                    recent_hazards.append(f"Hazard: {cat} (Severity {report['severity_rating']}) - {report['ai_description']}")
            except ValueError:
                continue

    # 3. Call the risk score calculator
    risk_score = calculate_risk_score(reports_48h, total_severity, traffic_multiplier)

    print(f"Segment: {args.segment} - {segment_name}")
    print(f"Location Multiplier: {traffic_multiplier}x")
    print(f"Reports (48h): {reports_48h}")
    print(f"Risk Score: {risk_score:.1f}")

    if risk_score >= 10.0:
        print("\nEscalation: TRUE")
        
        client = genai.Client()
        hazards_text = "\n".join(recent_hazards)
        
        prompt = f"""
        You are an automated dispatch assistant for a state park. 
        Trail Segment {args.segment} ({segment_name}) has reached a critical Risk Score of {risk_score:.1f}.
        
        Hazards in last 48h:
        {hazards_text}
        
        Write a single, concise sentence explaining why this segment is high priority and needs immediate attention. Prioritize the highest severity hazard.
        Do not use introductory filler. Just write the warning.
        """
        
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            print(f"AI Escalation Note: {response.text.strip()}")
        except Exception as e:
            print(f"API error: {e}")
    else:
        print("\nEscalation: FALSE")