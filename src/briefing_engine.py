import json
import sys
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from google import genai
from location_engine import get_segment_info
from risk_engine import calculate_risk_score

load_dotenv()

def generate_daily_briefing():
    try:
        with open("hazard_db.json", "r") as f:
            db = json.load(f)
    except FileNotFoundError:
        return False, "No database found. Please submit a report first."

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
        
        loc_info = get_segment_info(seg_id)
        multiplier = loc_info["traffic_multiplier"]
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
    2. Why Each Segment is Prioritized
    3. Main Hazard Categories Observed
    4. Suggested Operational Focus Areas for the Day
    """

    client = genai.Client()
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        # Save to the root directory
        date_str = now.strftime("%Y-%m-%d")
        filename = f"daily_briefing_{date_str}.txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Ranger Daily Briefing - {now.strftime('%A, %B %d, %Y')}\n")
            f.write("=" * 60 + "\n\n")
            f.write(response.text.strip())
            f.write("\n\n" + "=" * 60 + "\n")
            
        return True, filename
        
    except Exception as e:
        return False, f"API error: {e}"

# CLI Guard for terminal testing
if __name__ == "__main__":
    print("Creating briefing...")
    success, result = generate_daily_briefing()
    if success:
        print(f" Success! Briefing saved to: {result}")
    else:
        print(f"Failed: {result}")
