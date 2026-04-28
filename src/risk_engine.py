import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv
from google import genai
from location_engine import get_segmentInfo

load_dotenv()

def calculate_risk_score(reports_48h: int, total_severity: int, traffic_multiplier: float) -> float:
    if reports_48h > 0:
        average_severity = total_severity / reports_48h
        volume_penalty = reports_48h * 1.2
        return (average_severity + volume_penalty) * traffic_multiplier
    return 0.0

def analyze_segment_risk(segment_id: int):
    # Anchor DB to src/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "hazard_db.json")
    
    try:
        with open(db_path, "r") as f:
            db = json.load(f)
    except FileNotFoundError:
        return {"error": "No database found. Run analysis.py first to generate data."}

    now = datetime.now()
    reports_48h = 0
    total_severity = 0
    recent_hazards = [] 

    loc_info = get_segmentInfo(segment_id)
    traffic_multiplier = loc_info["traffic_multiplier"]
    segment_name = loc_info["name"]

    for report in db:
        if report["trail_segment"] == segment_id:
            try:
                report_time = datetime.strptime(report["reported_timestamp"], "%Y-%m-%d %H:%M")
                if now - report_time <= timedelta(hours=48):
                    if report.get("severity_rating") == 0:
                        continue
                    reports_48h += 1
                    total_severity += report["severity_rating"]
                    cat = report.get('hazard_type', 'Unknown')
                    recent_hazards.append(f"Hazard: {cat} (Severity {report['severity_rating']}) - {report['ai_description']}")
            except ValueError:
                continue

    risk_score = calculate_risk_score(reports_48h, total_severity, traffic_multiplier)
    
    # Package the results nicely for Streamlit
    result = {
        "segment_id": segment_id,
        "segment_name": segment_name,
        "multiplier": traffic_multiplier,
        "reports_48h": reports_48h,
        "risk_score": risk_score,
        "escalation_triggered": False,
        "escalation_note": ""
    }

    # Trigger AI Escalation if the score crosses the threshold
    if risk_score >= 10.0:
        result["escalation_triggered"] = True
        client = genai.Client()
        hazards_text = "\n".join(recent_hazards)
        
        prompt = f"""
        You are an automated dispatch assistant for a state park. 
        Trail Segment {segment_id} ({segment_name}) has reached a critical Risk Score of {risk_score:.1f}.
        
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
            result["escalation_note"] = response.text.strip()
        except Exception as e:
            result["escalation_note"] = f"API Error generating escalation note: {e}"

    return result

#Testing VVVV
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Park Hazard Aggregator & Escalation Engine")
    parser.add_argument("--segment", type=int, required=True)
    args = parser.parse_args()

    data = analyze_segment_risk(args.segment)
    
    if "error" in data:
        print(data["error"])
        sys.exit(1)

    print(f"Segment: {data['segment_id']} - {data['segment_name']}")
    print(f"Location Multiplier: {data['multiplier']}x")
    print(f"Reports (48h): {data['reports_48h']}")
    print(f"Risk Score: {data['risk_score']:.1f}")

    if data['escalation_triggered']:
        print("\nEscalation: TRUE")
        print(f"AI Escalation Note: {data['escalation_note']}")
    else:
        print("\nEscalation: FALSE")
