import json
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import Literal

# 1. Define the Allowed Set for Hazard Categories
llowedHazards = Literal[
    'Park Infrastructure',
    'Debris',
    'Animal',
    'Fire Hazard',
    'Other'
]

# 2. Define the Strict Schema
class HazardReportSchema(BaseModel):
    trail_segment: int = Field(description="The trail segment ID.")
    reported_timestamp: str = Field(description="The exact timestamp.")
    hazard_category: allowedHazards = Field(description="Must exactly match an allowed category.")
    severity_rating: int = Field(ge=1, le=5, description="Severity from 1 to 5.")
    ai_description: str 
    user_notes: str 
    recommended_action: str = Field(min_length=10, description="Recommended action.")

    # Ensures recommended action isnt empty
    @field_validator('recommended_action')
    def check_action_not_empty(cls, value):
        if not value or value.strip() == "":
            raise ValueError("recommended_action cannot be empty or whitespace.")
        return value