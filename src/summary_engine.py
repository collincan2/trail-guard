import argparse
import json
import sys
import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
#python summary_engine.py --segment x
#Recommend generating at least 3 reports with analysis.py

# 1. Set up the CLI
parser = argparse.ArgumentParser(description="Park Hazard Pattern Recognition Engine")
parser.add_argument("--segment", type=int, required=True)
args = parser.parse_args()

# 2. Load the Database
try:
    with open("hazard_db.json", "r") as f:
        db = json.load(f)
except FileNotFoundError:
    print("Error: No database found. Run analysis.py first to generate data.")
    sys.exit(1)

# 3. Filter and Format the Data for the LLM
segment_reports = []
for report in db:
    if report["trail_segment"] == args.segment:
        clue = f"- {report['reported_timestamp']} | Severity: {report['severity_rating']} | Type: {report['hazard_type']} | Details: {report['ai_description']}"
        if report.get('user_notes') and report['user_notes'] != "No user notes provided.":
            clue += f" | User Note: {report['user_notes']}"
        segment_reports.append(clue)

# 4. Handle empty reports
if not segment_reports:
    print(f"No reports found in the database for Segment {args.segment}.")
    sys.exit(0)

# 5. We instruct the AI to act as an analyst, looking for root causes rather than just listing hazards.
prompt = f"""
You are a Senior Park Operations Analyst. Review the following incident reports from Trail Segment {args.segment}.

Incident Log:
{chr(10).join(segment_reports)}

Task:
1. Identify any patterns or clusters in the types of hazards.
2. Summarize the likely underlying root cause of these incidents.
3. Suggest a high-level operational or engineering recommendation to solve the root cause.

Format your output as a single, concise, professional paragraph. 
Example Output: "Multiple erosion-related incidents and exposed roots in Segment 3 suggest severe slope instability and poor drainage. Recommend deploying an engineering team to install retaining walls and reroute water runoff."
"""

# 6. Call the AI Engine
print(f"Analyzing {len(segment_reports)} reports for Segment {args.segment}...\n")

client = genai.Client()

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt
    )
    print("Pattern Analysis:")
    print(response.text.strip())

except Exception as e:
    print(f"API Error: {e}")