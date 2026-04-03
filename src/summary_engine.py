import argparse
import json
import sys
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Set up CLI arguments
parser = argparse.ArgumentParser(description="Per-Segment Hazard Solution Reasoning")
parser.add_argument("--segment", type=int, required=True, help="Segment ID to analyze (1-7)")
args = parser.parse_args()

# Load the database
try:
    with open("hazard_db.json", "r") as f:
        db = json.load(f)
except FileNotFoundError:
    print(" Error: No database found. Run analysis.py first.")
    sys.exit(1)

# Filter for the requested segment
segment_reports = [r for r in db if r["trail_segment"] == args.segment]

if not segment_reports:
    print(f"No reports found in the database for Segment {args.segment}.")
    sys.exit(0)

print(f"Analyzing Solutions for Segment {args.segment}...\n")
client = genai.Client()

# Loop through each hazard and generate reasoning
for i, report in enumerate(segment_reports, 1):
    hazard_type = report.get('hazard_type', 'Unknown')
    description = report['ai_description']
    action = report['recommended_action']
    
    prompt = f"""
    You are a Senior Park Safety Instructor. 
    
    Hazard Type: {hazard_type}
    Description: {description}
    Recommended Action: {action}
    
    Write a brief, 1-to-2 sentence explanation of EXACTLY WHY this recommended action is the appropriate and safest operational response to this specific hazard. Focus on the logical reasoning.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        print(f"Incident #{i}: {hazard_type}")
        print(f"Action: {action}")
        print(f"Reasoning: {response.text.strip()}\n")
        print("-" * 60 + "\n")
    except Exception as e:
        print(f" API Error: {e}")
