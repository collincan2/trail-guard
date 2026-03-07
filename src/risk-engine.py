import argparse
import json
import sys
from dotenv import load_dotenv
from datetime import datetime, timedelta
from google import genai #This is for section #6
load_dotenv()

# 1. Set up the parser
parser = argparse.ArgumentParser(description="Park Hazard Aggregator & Escalation Engine")
parser.add_argument("--segment", type=int, required=True)
args = parser.parse_args()

# 2. Load the hazard database
try:
    with open("hazard_db.json", "r") as f:
        db = json.load(f)
except FileNotFoundError:
    print("Error: No database found. Run analysis.py first to generate data.")
    sys.exit(1)

# 3. Initialize Tracking Variables
now = datetime.now()
reports_48h = 0
total_severity = 0
recent_hazards = [] # Give the AI context

# 4. Process the Data
for report in db:
    if report["trail_segment"] == args.segment:
        try:
            report_time = datetime.strptime(report["reported_timestamp"], "%Y-%m-%d %H:%M")
            if now - report_time <= timedelta(hours=48):
                reports_48h += 1
                total_severity += report["severity_rating"]
                # Save the hazard details for the AI to read later
                recent_hazards.append(f"Hazard: {report['hazard_type']} (Severity {report['severity_rating']}) - {report['ai_description']}")
                
        except ValueError:
            continue

# 5. Calculate the cumulative score ADJUST LATER!!!
if reports_48h > 0:
    average_severity = total_severity / reports_48h
    volume_penalty = reports_48h * 1.2
    risk_score = average_severity + volume_penalty
else:
    risk_score = 0.0

# 6. Print the Base Report
print(f"Segment: {args.segment}")
print(f"Reports (48h): {reports_48h}")
print(f"Risk Score: {risk_score:.1f}")

#THIS is #6 Risk Explanation Layer
if risk_score >= 7.0:
    print("\n Escalation: TRUE")
    
    # Initialize the client
    client = genai.Client()
    hazards_text = "\n".join(recent_hazards)
    
    # Instruct the AI to write the summary
    prompt = f"""
    You are an automated dispatch assistant for a state park. 
    Trail Segment {args.segment} has reached a critical Risk Score of {risk_score:.1f}.
    
    Here are the specific hazards reported in the last 48 hours:
    {hazards_text}
    
    Write a single, concise sentence explaining why this segment is high priority and needs immediate attention. 
    Do not use introductory filler (like "Here is the summary"). Just write the warning.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        print(f"AI Escalation Note: {response.text.strip()}")
    except Exception as e:
        print(f"Warning: Could not generate AI escalation note due to API error: {e}")
else:
    print("Escalation: FALSE")