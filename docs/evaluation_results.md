## Results from Test Cases
Here are the results from the test cases, ran manually.  

The image reference ID can be found as a suffix on the images in src/PilotPhotos.  

NOTE: There is not an escalation rate category, because that would not be possible without segment aggregation.  

|ID| JSON Validity| Risk | Hazard Type |

### Methodology
- how runs were executed
To determine validity and correct execution of the program, twenty test cases were built and documented in evaluation_test_cases.md.
These are organized with an ID, a general description of the image/issue, asserted risk level, hazard type categorization, and the
associated marker segement. The testing is per issue, and will be judged on how accurately the actual results are to the expected
ratings.

To clarify, risk scores have a range of +/-1 depending on expected severity. Trash and debris may be slightly higher than the bottom
range, and wild animals may not be scored at the highest severity. For the MVP, this is OK - the idea is that our team can prove
expected ranges are close to actual values, as well as the application doing it's expected function within reasonable limits.
* Hazard Type doesn't have a range - this is important to us as categorization sorting is feature, although it is understood that
it may get slightly off - we're looking for completely inaccurate answers (Animal classified as a Fire Hazard).

Below are the recently ran results ran per case, sorted numerically by ID. This can be checked against the evaluation_test_cases.md  
file, which showcases the expected results for each ID.

Case 1: Fallen Tree
Trail Segment: 1
Hazard Type: Debris
Severity Rating: 5
Full Accuracy: NO: Risk is outside range (2-3 vs. 5).

Case 2: Trash
Trail Segment: 1
Hazard Type: Debris
Severity Rating: 3
Full Accuracy: NO: Risk is outside range (1-2 vs. 3)

Case 3: Overgrown Foliage
Trail Segment: 2
Hazard Type: Park Infrastructure
Severity Rating: 2
Full Accuracy: NO: Hazard Type is incorrect (Debris expected vs. Park Infrastructure reported)

Case 4: Fallen Tree
Trail Segment: 2
Hazard Type: Debris
Severity Rating: 4
Full Accuracy: NO: Risk is outside range (2-3 vs 4)

Case 5: Overgrown Foliage
Trail Segment: 3
Hazard Type: Park Infrastructure
Severity Rating: 2
Full Accuracy: NO: Hazard Type is incorrect (Debris expected vs. Park Infrastructure reported)

Case 6: Park Bench Damage
Trail Segment: 3
Hazard Type: Park Infrastructure
Severity Rating: 4
Full Accuracy: NO: Risk is outside range (1-2 vs. 4)

Case 7: Cracked Sidewalk
Trail Segment: 4
Hazard Type: 3
Severity Rating: Park Infrastructure
Full Accuracy: YES

Case 8: Sidewalk
Trail Segment: 4
Hazard Type: Park Infrastructure
Severity Rating: 3
Full Accuracy: YES

Case 9: Water Pipe Burst
Trail Segment: 5
Hazard Type: Park Infrastructure
Severity Rating: 5
Full Accuracy: YES

Case 10: Marker Post Damage
Trail Segment: 6
Hazard Type: Park Infrastructure
Severity Rating: 3
Full Accuracy: YES

Case 11: Bridge Plank Damage
Trail Segment: 5
Hazard Type: Park Infrastructure
Severity Rating: 5
Full Accuracy: YES

Case 12: Broken Fence
Trail Segment: 6
Hazard Type: Park Infrastructure
Severity Rating: 2
Full Accuracy: YES

Case 13: Rock Blocking Trail
Trail Segment: 1
Hazard Type: Debris
Severity Rating: 2
Full Accuracy: YES

Case 14: Faded Parking Lines
Trail Segment: 2
Hazard Type: Park Infrastructure
Severity Rating: 2
Full Accuracy: YES

Case 15: Park Gate Paint Chipping
Trail Segment: 3
Hazard Type: Park Infrastructure
Severity Rating: 4
Full Accuracy: NO: Risk is outside range (1-2 vs. 4)

Case 16: Buck (Aggressive, Large Antlers)
Trail Segment: 5
Hazard Type: Animal
Severity Rating: 4
Full Accuracy: YES

Case 17: Animal Droppings
Trail Segment: 4
Hazard Type: Animal
Severity Rating: 2
Full Accuracy: YES

Case 18: Black Bear Sightings
Trail Segment: 5
Hazard Type: Animal
Severity Rating: 5
Full Accuracy: YES

Case 19: Non-Native Fox Sighting (Non-Agressive)
Trail Segment: 7
Hazard Type: Animal
Severity Rating: 3
Full Accuracy: NO: Risk is outside range (1-2 vs. 3)

Case 20: Stacked Dry Brush
Trail Segment: 7
Hazard Type: Fire Hazard
Severity Rating: 3
Full Accuracy: YES

Total: 12/20 have 100% accuracy. 8/20 with at least one discrepancy. 

FAIL ANALYSIS
Most of the misses here were risk oriented, with only a few categorization misses.  
Out of those that were categorization based (2), they were understandably moved to Park Infrastructure instead of Debris,  
for the same issue (Overgrown Foliage). This is OK - they were both under the same category, and as trail management is a big part  
of any park, it makes sense why it was done this way. As it was the only time this happned, and isn't completely incorrect,  
this is an acceptable result.

As for the remaining 6 that incorrectly assesed risk for their respective issues, some things that were rated as less of a problem  
ended up being higher than expected (Paint Chipping being a 4) and some were rated higher than the results expected (Trash debris  
being a 3).

This shows something interesting with the expectations: our system of risk needs to be refined to better suit how the risk score  
representation actually displays. Trash should not be a 3, but this is because we do not denote this as something that poses a  
major risk to infrastructure, human or animal life, or constitutes an immediate temporal issue. 

This isn't necessarily a fault with the program -- it correctly prioritizes the risk according to it's standards, which are shown  
in the resolution details. For example, in Case 19 (Fox Sighting), it summarizes that the fox needs to immediately be detained and  
moved, which is true, but it does not cause direct harm to any trail-goers according to the input description. 

In summary, the errors were mostly with risk assessment, and can be fixed by feeding a better blueprint for the initial risk levels  
for the AI. By doing this, it'll be able to better distinguish what the damage/danger levels are for a given issue.

