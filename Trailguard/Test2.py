import sys
import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
from PIL import Image

# 1. Check arguments entered
# sys.argv is a list of the words you typed in the terminal.
# sys.argv[0] is "test.py"
# sys.argv[1] will be the image name you type next to it
if len(sys.argv) < 2:
    print("ERROR: You forgot to provide an image!")
    print("Usage: test2.py <image_file.jpg>")
    sys.exit(1) # Stop the script

target_image_path = sys.argv[1]

# 2. Try to open file, if not, stops
try:
    target_img = Image.open(target_image_path)
    print(f" Analyzing {target_image_path}...")
except FileNotFoundError:
    print(f"ERROR: Could not find the file '{target_image_path}' in this folder.")
    sys.exit(1)

# 3. Define JSON response of Hazard Report. To add more fields, follow similiar structure. 
# Use JSON seperator/intepreter later
class HazardReport(BaseModel):
    hazard_type: str = Field(description="The category of the park hazard, e.g., 'Broken Equipment', 'Trip Hazard'.")
    severity_rating: int = Field(description="Rate the severity from 1 (minor) to 10 (critical/life-threatening).")
    description: str = Field(description="A brief description of the hazard.")
    recommended_action: str = Field(description="Actionable steps or personnel assignments to resolve the hazard, e.g., 'Dispatch maintenance with a chainsaw', 'Assign employees to rebuild fence'.")

# 4. Initializes Gemini
load_dotenv()
client = genai.Client()
##client = genai.Client(api_key="AIzaSyCmRI-3ogYQ6gG0X62Qr2ZSv6jUgdeWbNY") #Fix this later

# 5. Load the Few-Shot Examples/ Data-set. Add at least 5 for proper severity accuracy
try:
    example_img_1 = Image.open("FallenTree.jpg")
    example_img_2 = Image.open("Mudpuddle.jpg")
except FileNotFoundError:
    print("ERROR: Keep 'FallenTree.jpg' and 'MudPuddle.jpg' in the folder for the AI's training examples!")
    sys.exit(1)

# 6. Construct the Few-Shot Prompt
contents = [
    "You are an expert park safety inspector. Your job is to analyze images of park hazards, rate their severity from 1 to 5, and recommend a solution.",
    
    "Example 1 Image:", example_img_1,
    "Example 1 Output: {'hazard_type': 'Path blockage', 'severity_rating': 3, 'description': 'There is a large tree fallen on a path.', 'recommended_action': 'Assign maintenance staff to use a chainsaw on the tree.'}",
    
    "Example 2 Image:", example_img_2,
    "Example 2 Output: {'hazard_type': 'Slippery Surface', 'severity_rating': 2, 'description': 'A small mud puddle near the fountain.', 'recommended_action': 'Assign groundskeeping to lay down woodchips or monitor for drainage issues.'}",
    
    "Now, analyze this new user-submitted image and provide the JSON output according to the schema:",
    target_img 
]

# 7. Calls gemini flash, specifys how to respond, forces categories 
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents=contents,
    config={
        "response_mime_type": "application/json",
        "response_schema": HazardReport,
    }
)

# 8. Prints out final JSON
print("\n Analysis Complete:")
print(response.text)