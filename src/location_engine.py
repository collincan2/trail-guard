
# Trail segments and their ids/names
SEGMENT = {
    1: {"name": "Playground/Trailhead", "traffic_multiplier": 1.5},
    2: {"name": "Picnic Area", "traffic_multiplier": 1.3},
    3: {"name": "Close Paved Loops", "traffic_multiplier": 1.0},
    4: {"name": "South Culvert Crossing", "traffic_multiplier": 1.0},
    5: {"name": "North Metal Bridge", "traffic_multiplier": 1.5}, #Large metal bridge used to safely cross rough ground
    6: {"name": "Valley Crossing", "traffic_multiplier": 1.0},
    7: {"name": "Deeper Forest Trail", "traffic_multiplier": 0.6}
}

def get_segmentInfo(segment_id: int) -> dict:
    return SEGMENT.get(segment_id, {"name": "Unnamed Segment", "traffic_multiplier": 1.0})