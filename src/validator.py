import json
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import Literal

# 1. Define the Allowed Set for Hazard Categories
allowedHazards = Literal[
    'Park Infrastructure',
    'Debris',
    'Animal',
    'Fire Hazard',
    'Other'
]

# 2. Define our final report schema
class HazardReportSchema(BaseModel):
    trail_segment: int = Field(description="The trail segment ID.")
    reported_timestamp: str = Field(description="The exact timestamp.")
    hazard_type: allowedHazards = Field(description="Must exactly match an allowed category.")
    severity_rating: int = Field(ge=0, le=5, description="Severity from 1 to 5, 0 if its invalid.")
    ai_description: str 
    user_notes: str 
    recommended_action: str = Field(min_length=10, description="Recommended action.")

    # Ensures recommended action isnt empty
    @field_validator('recommended_action')
    def check_action_not_empty(cls, value):
        if not value or value.strip() == "":
            raise ValueError("recommended_action cannot be empty or whitespace.")
        return value
