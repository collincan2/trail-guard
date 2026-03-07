import argparse
import os
import sys
import json
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
from validator import validate_and_parse, HazardReportSchema
from PIL import Image

# 1. Set up the CLI Argument Parser
parser = argparse.ArgumentParser(description="Trailguard")
parser.add_argument("image")
parser.add_argument("--segment", type=int, choices=[1, 2, 3, 4, 5, 6, 7], required=True)
parser.add_argument("--time", required=True)## MUST be "2026-03-04 10:00" format
parser.add_argument("--desc", type=str, default="No user notes provided.")

# Parse the commands typed in the terminal
args = parser.parse_args()

# 2. Try to open the target image
try:
    target_img = Image.open(args.image)
    print(f" Analyzing {args.image} at Segment {args.segment}...")
except FileNotFoundError:
    print(f" Error: Could not find the file '{args.image}'")
    sys.exit(1)

#3. Initalize API
load_dotenv()
client = genai.Client()

# 4. Load Few-Shot Examples
try:
    example_img_1 = Image.open("FallenTree.jpg")
    example_img_2 = Image.open("Mudpuddle.jpg")
    example_img_3 = Image.open("Cracked.jpg")
    example_img_4 = Image.open("wasp-nest.jpg")
except FileNotFoundError:
    print(" Error: Keep the 4 examples in the folder for the AI's training examples!!")
    sys.exit(1)

# 5. Format the User's Metadata
user_context = f"Trail Segment: {args.segment}\nTimestamp: {args.time}\nUser Description: {args.desc}"

# 6. Construct the Prompt
contents = [
    "You are an expert park safety inspector. Analyze the image and the user's metadata to create a report.",
    
    "Example 1 Image:", example_img_1,
    "Example 1 Metadata:\nTrail Segment: 2\nTimestamp: 10:00 AM\nUser Description: This huge fallen tree is blocking the main metal bridge path to the rest of the park.",
    "Example 1 Output: {'trail_segment': 2, 'reported_timestamp': '10:00 AM', 'hazard_type': 'Debris', 'severity_rating': 5, 'ai_description': 'The tree is blocking the path.', 'user_notes': 'This huge fallen tree is blocking the main metal bridge path to the rest of the park.', 'recommended_action': 'Assign maintenance with a chainsaw to cut and move tree immediately.'}",
    
    "Example 2 Image:", example_img_2,
    "Example 2 Metadata:\nTrail Segment: 4\nTimestamp: 02:15 PM\nUser Description: No user notes provided.",
    "Example 2 Output: {'trail_segment': 4, 'reported_timestamp': '02:15 PM', 'hazard_type': 'Park Infrastructure', 'severity_rating': 1, 'ai_description': 'A small mud puddle near the fountain.', 'user_notes': 'No user notes provided.', 'recommended_action': 'Assign groundskeeping to lay down woodchips.'}",
    
    "Example 3 Image:", example_img_3,
    "Example 3 Metadata:\nTrail Segment: 1\nTimestamp: 04:15 PM\nUser Description: Broken uneven dirty path, I couldve tripped and hurt my knees.",
    "Example 3 Output: {'trail_segment': 1, 'reported_timestamp': '04:15 PM', 'hazard_type': 'Park Infrastructure', 'severity_rating': 2, 'ai_description': 'The path consists of broken and uneven paving stones, loose gravel, and weeds, creating a tripping hazard along the curb.', 'user_notes': 'Broken uneven dirty path, I couldve tripped and hurt my knees.', 'recommended_action': 'Assign maintenance to repair and re-level the paved path, securing all stones and clearing debris and weeds.'}",

    "Example 4 Image:", example_img_4,
    "Example 4 Metadata: \nTrail Segment: 1\nTimeStamp: 06:30pm\nUser Description: Very large wasp nest next to the playground area at the entrance to the park!",
    "Example 4 Output: {'trail_segment': 1, 'reported_timestamp': '06:30 PM', 'hazard_type': 'Animal', 'severity_rating': 3, 'ai_description': 'Wasp nest, at least a week old, full of wasps and in close proximity to playing children', 'user_notes': 'Very large wasp nest next to the playground area at the entrance to the park!', 'recommended_action': 'Assign maintenance with wasp clearing gear to disperse wasps'}",

    "Now, analyze this new user-submitted image and metadata:",
    user_context,
    target_img 
]

# 7. Call Gemini
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=contents,
        config={
            "response_mime_type": "application/json",
            "response_schema": HazardReportSchema,
        }
    )
    print("\n Analysis Complete:\n")
    
    parsed_json = json.loads(response.text)
    print(json.dumps(parsed_json, indent=2))
    # SAVE reports to database for riskengine to analyze
    db_filename = "hazard_db.json"
    #Try to open the existing database, or create an empty list if it doesn't exist
    try:
        with open(db_filename, "r") as f:
            db = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        db = []
        
    # Add the new report to the list
    db.append(parsed_json)
    
    # Save it back to the file, then confirm
    with open(db_filename, "w") as f:
        json.dump(db, f, indent=2)
    print("This report has been saved to hazard_db.json")
    
except Exception as e:
    print(f"\n API Error: {e}")