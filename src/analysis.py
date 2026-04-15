import os
import json
import argparse
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field, ValidationError
from validator import HazardReportSchema
from PIL import Image

# Initialize Environment
load_dotenv()

def analyze_hazard_image(image_input, segment_id: int, timestamp: str, description: str):
    
    #Analyzes a hazard image and saves it to the database. Returns a tuple: (success_boolean, message_or_data)    
    # 1. Try to open the target image (handles both file paths and Streamlit UploadedFiles)
    try:
        target_img = Image.open(image_input)
    except Exception as e:
        return False, f"Error opening image: {e}"

    client = genai.Client()

    # 2. Load Few-Shot Examples 
    # This automatically finds the exact folder where analysis.py is sitting
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # And looks for the 'examples' folder right next to it
    EXAMPLE_DIR = os.path.join(current_dir, "examples")

    try:
        example_img_1 = Image.open(os.path.join(EXAMPLE_DIR, "FallenTree.jpg"))
        example_img_2 = Image.open(os.path.join(EXAMPLE_DIR, "Mudpuddle.jpg"))
        example_img_3 = Image.open(os.path.join(EXAMPLE_DIR, "Cracked.jpg"))
        example_img_4 = Image.open(os.path.join(EXAMPLE_DIR, "wasp-nest.jpg"))
    except FileNotFoundError:
        return False, f"Error: Keep the 4 examples in the '{EXAMPLE_DIR}' folder!"

    # 3. Format the User's Metadata
    user_context = f"Trail Segment: {segment_id}\nTimestamp: {timestamp}\nUser Description: {description}"

    # 4. Construct the Prompt 
    contents = [
        "You are an expert park safety inspector. Analyze the image and the user's metadata to create a report.",
        
        "Example 1 Image:", example_img_1,
        "Example 1 Metadata:\nTrail Segment: 2\nTimestamp: 2026-04-14 10:00\nUser Description: This huge fallen tree is blocking the main metal bridge path to the rest of the park.",
        "Example 1 Output: {'trail_segment': 2, 'reported_timestamp': '2026-04-14 10:00', 'hazard_type': 'Debris', 'severity_rating': 5, 'ai_description': 'The tree is blocking the path.', 'user_notes': 'This huge fallen tree is blocking the main metal bridge path to the rest of the park.', 'recommended_action': 'Assign maintenance with a chainsaw to cut and move tree immediately.'}",
        
        "Example 2 Image:", example_img_2,
        "Example 2 Metadata:\nTrail Segment: 4\nTimestamp: 2026-04-14 14:15\nUser Description: No user notes provided.",
        "Example 2 Output: {'trail_segment': 4, 'reported_timestamp': '2026-04-14 14:15', 'hazard_type': 'Park Infrastructure', 'severity_rating': 1, 'ai_description': 'A small mud puddle near the fountain.', 'user_notes': 'No user notes provided.', 'recommended_action': 'Assign groundskeeping to lay down woodchips.'}",
        
        "Example 3 Image:", example_img_3,
        "Example 3 Metadata:\nTrail Segment: 1\nTimestamp: 2026-04-14 16:15\nUser Description: Broken uneven dirty path, I couldve tripped and hurt my knees.",
        "Example 3 Output: {'trail_segment': 1, 'reported_timestamp': '2026-04-14 16:15', 'hazard_type': 'Park Infrastructure', 'severity_rating': 2, 'ai_description': 'The path consists of broken and uneven paving stones, loose gravel, and weeds, creating a tripping hazard along the curb.', 'user_notes': 'Broken uneven dirty path, I couldve tripped and hurt my knees.', 'recommended_action': 'Assign maintenance to repair and re-level the paved path, securing all stones and clearing debris and weeds.'}",

        "Example 4 Image:", example_img_4,
        "Example 4 Metadata: \nTrail Segment: 1\nTimeStamp: 2026-04-14 18:30\nUser Description: Very large wasp nest next to the playground area at the entrance to the park!",
        "Example 4 Output: {'trail_segment': 1, 'reported_timestamp': '2026-04-14 18:30', 'hazard_type': 'Animal', 'severity_rating': 3, 'ai_description': 'Wasp nest, at least a week old, full of wasps and in close proximity to playing children', 'user_notes': 'Very large wasp nest next to the playground area at the entrance to the park!', 'recommended_action': 'Assign maintenance with wasp clearing gear to disperse wasps'}",

        "Now, analyze this new user-submitted image and metadata:",
        user_context,
        target_img 
    ]

    # 5. Call Gemini with Self-Correcting Validation Loop
    max_retries = 3
    attempt = 0
    final_valid_data = None

    while attempt < max_retries:
        attempt += 1
        
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=contents,
                config={
                    "response_mime_type": "application/json",
                    "response_schema": HazardReportSchema,
                }
            )
            
            try:
                # Force JSON string through Pydantic validator rules
                valid_data = HazardReportSchema.model_validate_json(response.text)
                final_valid_data = valid_data.model_dump()
                break # Escape the loop on success
                
            except ValidationError as e:
                error_details = [f"Field '{err.get('loc', [''])[0]}': {err.get('msg', '')}" for err in e.errors()]
                error_feedback = f"Your last attempt failed validation: {error_details}. Please fix these exact errors and output valid JSON."
                
                # Prevent appending feedback infinitely
                if attempt == 1:
                    contents.append(error_feedback)
                else:
                    contents[-1] = error_feedback

        except Exception as e:
             return False, f"API Error on attempt {attempt}: {e}"

    # 6. Handle Failure
    if not final_valid_data:
        return False, "CRITICAL ERROR: Model failed to produce valid data after 3 attempts."

    # 7. SAVE reports to database
    db_filename = "hazard_db.json"
    try:
        with open(db_filename, "r") as f:
            db = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        db = []
        
    db.append(final_valid_data)
    
    with open(db_filename, "w") as f:
        json.dump(db, f, indent=2)
        
    return True, final_valid_data


#TEST section VVVVV
if __name__ == "__main__":
    import sys
    
    parser = argparse.ArgumentParser(description="Trailguard CLI Analysis")
    parser.add_argument("image", help="Path to the hazard image")
    parser.add_argument("--segment", type=int, choices=[1, 2, 3, 4, 5, 6, 7], required=True)
    parser.add_argument("--time", required=True, help="MUST be 'YYYY-MM-DD HH:MM' format")
    parser.add_argument("--desc", type=str, default="No user notes provided.")

    args = parser.parse_args()

    print(f" Analyzing {args.image} at Segment {args.segment}...")
    
    # Call the new function
    success, result = analyze_hazard_image(args.image, args.segment, args.time, args.desc)
    
    if success:
        print("\n Final Approved Report:\n")
        print(json.dumps(result, indent=2))
        print("\n💾This report has been securely saved to hazard_db.json")
    else:
        print(f"\n❌ Pipeline Failed: {result}")
        sys.exit(1)
