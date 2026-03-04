#!/usr/bin/env python3

import os
from google import genai
from pydantic import BaseModel, Field
from PIL import Image

# 1. Define your desired JSON structure using Pydantic
# This acts as a strict blueprint that Gemini MUST follow.
class HazardReport(BaseModel):
    hazard_type: str = Field(description="The category of the park hazard, e.g., 'Broken Equipment', 'Trip Hazard'.")
    severity_rating: int = Field(description="Rate the severity from 1 (minor) to 10 (critical/life-threatening).")
    description: str = Field(description="A brief description of the hazard.")

# 2. Initialize the Gemini Client
# The client automatically picks up the GEMINI_API_KEY environment variable.
client = genai.Client(api_key="AIzaSyCmRI-3ogYQ6gG0X62Qr2ZSv6jUgdeWbNY") #Fix this later

# 3. Load your images (Examples and the Target image)
# In your actual web app, these would be the files users upload.
example_img_1 = Image.open("FallenTree.jpg")
example_img_2 = Image.open("Mudpuddle.jpg")
target_img = Image.open("Cracked.jpg")

# 4. Construct the Few-Shot Prompt
# We pass an array containing instructions, the examples, and the final target.
contents = [
    "You are an expert park safety inspector. Your job is to analyze images of park hazards and rate their severity from 1 to 10.",
    
    # --- Few-Shot Example 1 ---
    "Example 1 Image:",
    example_img_1,
    "Example 1 Output: {'hazard_type': 'Broken Equipment', 'severity_rating': 9, 'description': 'The chain on the swing is snapped, posing an immediate danger to children.'}",
    
    # --- Few-Shot Example 2 ---
    "Example 2 Image:",
    example_img_2,
    "Example 2 Output: {'hazard_type': 'Slippery Surface', 'severity_rating': 2, 'description': 'A small mud puddle near the drinking fountain. Low risk.'}",
    
    # --- The Actual Request ---
    "Now, analyze this new user-submitted image and provide the JSON output according to the schema:",
    target_img
]

# 5. Call the API
# We use Gemini 2.5 Flash as it is incredibly fast and cheap for visual tasks.
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents=contents,
    config={
        "response_mime_type": "application/json",
        "response_schema": HazardReport,
    }
)

# 6. Use the data in your app!
print(response.text)