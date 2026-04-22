import json
import sys
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from google import genai
from location_engine import get_segmentInfo
from risk_engine import calculate_risk_score

load_dotenv()

print("Calculating park-wide metrics and generating Daily Briefing...\n")

# Anchor DB to src/
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "hazard_db.json")

try:
    with open(db_path, "r") as f:
        db = json.load(f)
except FileNotFoundError:
    print("Error: No database found. Run analysis.py first.")
    sys.exit(1)

now = datetime.now()
segment_scores = []
all_categories = set()

for seg_id in range(1, 8):
    reports_48h = 0
    total_severity = 0
    hazards = []
    
    for report in db:
        if report["trail_segment"] == seg_id:
            try:
                report_time = datetime.strptime(report["reported_timestamp"], "%Y-%m-%d %H:%M")
                if now - report_time <= timedelta(hours=48):
                    reports_48h += 1
                    total_severity += report["severity_rating"]
                    
                    cat = report.get('hazard_type', 'Unknown')
                    all_categories.add(cat)
                    hazards.append(f"{cat} (Sev {report['severity_rating']})")
            except ValueError:
                continue
    
    loc_info = get_segmentInfo(seg_id)
    multiplier = loc_info["traffic_multiplier"]
    
    # Calculates risk score for Ranger briefing
    score = calculate_risk_score(reports_48h, total_severity, multiplier)
        
    segment_scores.append({
        "id": seg_id,
        "name": loc_info["name"],
        "score": score,
        "hazards": hazards
    })

segment_scores.sort(key=lambda x: x["score"], reverse=True)
top_3 = segment_scores[:3]

briefing_context = ""
for rank, seg in enumerate(top_3, 1):
    briefing_context += f"#{rank} Priority: Segment {seg['id']} ({seg['name']}) - Score: {seg['score']:.1f}\n"
    briefing_context += f"   Recent Hazards: {', '.join(seg['hazards']) if seg['hazards'] else 'None'}\n"

prompt = f"""
You are the Chief Park Ranger AI. Based on the calculated risk scores, generate the Daily Ranger Briefing.

Top 3 High-Priority Segments Data:
{briefing_context}

Overall Hazard Categories Detected Park-Wide Today: {', '.join(all_categories) if all_categories else 'None'}

Format the output cleanly using Markdown with these exact sections:
1. Top 3 Priority Segments
2. Why Each Segment is Prioritized (Explain the high risk based on the specific hazards listed)
3. Main Hazard Categories Observed
4. Suggested Operational Focus Areas for the Day (How should dispatch allocate teams?)
"""

client = genai.Client()
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    # Anchor output file to src/
    date_str = now.strftime("%Y-%m-%d")
    filename = f"daily_briefing_{date_str}.txt"
    filepath = os.path.join(script_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Ranger Daily Briefing - {now.strftime('%A, %B %d, %Y')}\n")
        f.write("=" * 60 + "\n\n")
        f.write(response.text.strip())
        f.write("\n\n" + "=" * 60 + "\n")
        
    print(f"The daily briefing has been generated and saved to: {filepath}")
    
except Exception as e:
    print(f"API error: {e}")