
### TRAIL GUARD: 
An app designed to provide a dashboard for those who are park management or on a volunteer basis. The project contains a way for people to
upload photos and descriptions of problems, while management can see things laid out for easy, actionable task creation.

*Collin Cantu - Reports, Dataset Analysis, Design* 

*Andrew Cadena - Interface, Risk Assessment, Data Implementation*

## RUNNING THE APP:
### Setup:
1. Open a terminal in the project folder.
2. Create a virtual environment for organization: python -m venv .venv
3. Activate the environment: .\.venv\Scripts\Activate.ps1 (Windows) or source .venv/bin/activate (Mac/Linux)
4. Install all required dependencies: python -m pip install -r requirements.txt

5. Make sure the 4 example images are in same folder:
(Cracked.jpg, Mudpuddle.jpg, FallenTree.jpg, wasp-nest.jpg)

### Analyze Photo:
Example Analysis of Photo:
python analysis.py FallenTree.jpg --segment 2 --time "08:30 AM" --desc "Large collapsed tree blocking the bridge, blocks the main path!" 

   FallenTree.jpg → image to analyze
   --segment 2 → location/area (1–7)
   --time → time of report
   --desc → optional description of the issue
   
### Segmented Issue Summary with Action Report:
Summary of issues and suggested action based on marker segments. 
_NOTE: You must run the above Analyze Photo command at least **3** times before continuing!_
python summary_engine.py --segment <1-7> 

### Risk Engine:
Calculates risk for escalation purposes.
python risk-engine.py --segment <1-7>

## OBJECTIVE CORRESPONDENCE:
Milestone objectives are listed, and their respective file that satisfies this requirement. <br>
#1 - Hazard Extraction in analysis.py<br>
#2 - JSON Validation Layer in validateschema.json and is run during analysis.py<br>
#3 - Risk scoring done in risk-engine.py<br>
#4 - Found in summary_engine.py<br>
#5 - Found in risk-engine.py<br>
#6 - Found in risk-engine.py<br>
#7 - excluded -- see below<br>
#8- Evaluation_Test_Cases is the pilot file<br>
#9 - PRD updated<br>
#10 - Under docs/Architecture.png<br>
#11 - video submitted in blackboard<br>


### LINKS TO DOCS:
[to be added -- slides are currently offline]

### PROJECT SPECIFIC NOTES:
-Spike Plan stress test was completed successfully in class. Therefore, there is *no* results file for this.  
-The .env is on A's computer, and was ignored by github because it contains the API key needed to run, and that any file that uses the AI includes a "load_dotenv()" to use it.
- We did not do OBJ #7. It was a little out of scope for the project and how we score risk for this milestone.
