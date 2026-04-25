# Test Case File
In this document, 20 test cases will be presented. These are to be run and evaluated to their expected end results, based on accuracy.  

There is a evaluation chart that shows the most recent test results completed in evaluation_results.  

NOTE: There is not an escalation rate category, because that would not be possible without segment aggregation. See below for notes on ESC rate testing.

|ID|Desc.  | Risk |Hazard Type|Marker Segment|
|--|--|--|--|--|
| 1 | Fallen Tree| 2-3 |Debris | #1 |
| 2 | Trash | 1-2 |Debris | #1 |
| 3 | Overgrown Foliage| 2-3 | Debris  | #2 |
| 4 | Fallen Tree| 2-3 | Debris | #2 |
| 5 | Overgrown Foliage| 2-3| Debris | #3 |
| 6 | Park Bench Damage| 1-2 |Park Infrastructure | #3 |
| 7 | Cracked Sidewalk| 2-3 | Park Infrastructure | #4 |
| 8 | Cracked Sidewalk| 2-3| Park Infrastructure | #4 |
| 9 | Water Pipe Burst| 4-5 | Park Infrastructure | #5 |
| 10 | Marker Post Damage| 3-4 |Park Infrastructure | #6 |
| 11 | Bridge Plank Damage| 4-5 |Park Infrastructure | #5 |
| 12 | Broken Fence | 1-2 |Park Infrastructure | #6 |
| 13 | Rock Blocking Trail| 1-2 | Debris | #1 |
| 14 | Faded Parking Lines | 1-2 |Park Infrastructure | #2 |
| 15 | Park Gate Paint Chipping | 1-2 |Park Infrastructure | #3 |
| 16 | Buck (Aggressive, Large Antlers) | 4-5 |Animal | #5 |
| 17 | Animal Droppings| 1-2 | Animal | #4 |
| 18 | Black Bear Sighting | 4-5 | Animal | #5 |
| 19 | Non-Native Fox Sighting (Non-Agressive) | 1-2 | Animal | #7 |
| 20 | Stacked Dry Brush| 3-4 | Fire Hazard | #7 |

# Escalation Test Cases:
The segments 1,5, are already set to exceed ESC rates. By running the above, these segments will show a trigger.  

By adding the following cases, segment 2 will also cross the required 10.0 Risk Score threshold and trigger an ESC warning.  

|ID|Desc.  | Risk |Hazard Type|Marker Segment|
|--|--|--|--|--|
| 20.1 | Park Brush Fire | 4-5 |Fire Hazard | #2 |  

* Segments 1, 2, and 5 will all show ESC triggers. Expected scores are 10.4, 10.5, and 14.3, respectively.
