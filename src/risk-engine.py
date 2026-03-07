import argparse
import json
import sys
from datetime import datetime, timedelta
# Usage: python risk-engine.py --segment x

# 1. Parse the input to risk-engine
parser = argparse.ArgumentParser(description="Risk Engine and Escalation")
parser.add_argument("--segment", type=int, required=True)
args = parser.parse_args()

# 2. Load databse of reports
try:
    with open("hazard_db.json", "r") as f:
        db = json.load(f)
except FileNotFoundError:
    print(" Error: No database found. Run analysis.py first to generate data.")
    sys.exit(1)

# 3. Initialize Tracking Variables
now = datetime.now()
reports_48h = 0
total_severity = 0
escalation = "FALSE"

# 4. Process the Data
for report in db:
    #Only look at the segment the user requested
    if report["trail_segment"] == args.segment:
        
        #Parse the timestamp (Requires format: YYYY-MM-DD HH:MM)
        try:
            report_time = datetime.strptime(report["reported_timestamp"], "%Y-%m-%d %H:%M")
            
            # Check if the report is less than or equal to 48 hours old
            if now - report_time <= timedelta(hours=48):
                reports_48h += 1
                total_severity += report["severity_rating"]
                
        except ValueError:
            print("Invalid values, check risk-engine instructions")
            continue

# 5. CUMULATIVE risk score
# Formula: (Average Severity) + (Volume of Reports * 1.2 Multiplier)
if reports_48h > 0:
    average_severity = total_severity / reports_48h
    volume_penalty = reports_48h * 1.2
    risk_score = average_severity + volume_penalty
else:
    risk_score = 0.0

if risk_score >= 10:
    escalation = "TRUE"

# 6. Print the Final Report
print(f"Segment: {args.segment}")
print(f"Reports (48h): {reports_48h}")
print(f"Risk Score: {risk_score:.1f}")
print(f"Escalated: {escalation}")
