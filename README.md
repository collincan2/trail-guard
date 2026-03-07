### TRAIL GUARD: 
An app designed to provide a dashboard for those who are park management or on a volunteer basis. The project contains a way for people to
upload photos and descriptions of problems, while management can see things laid out for easy, actionable task creation.

*Collin Cantu - Reports, Dataset Analysis, Design* 

*Andrew Cadena - Interface, Risk Assessment, Data Implementation*

### RUNNING THE APP:
[placeholder]

Run this in terminal, make sure the 4 example images are in same folder:

Analysis of Photo:
python analysis.py image.jpg --segment <1-7> --time "08:30 AM" --desc "Insert user desc here, or remove --desc"

Summary of issues and suggested action based on marker segments:
python summary_engine.py --segment <1-7> [please get at least 3 reports with analysis.py]

Risk Engine:
python risk-engine.py --segment <1-7>

### OBJECTIVE CORRESPONDENCE:
Milestone objectives are listed, and their respective file that satisfies this requirement.
#1 - Hazard Extraction in analysis.py
#2 - JSON Validation Layer in validateschema.json and is run during analysis.py
#3 - Risk scoring done in risk-engine.py
#4 - Found in summary_engine.py
#5 - Found in risk-engine.py
#6 - Found in risk-engine.py
#7 - excluded -- see below
#8- Evaluation_Test_Cases is the pilot file
#9 - PRD updated
#10 - Under docs/Architecture.png
#11 - video submitted in blackboard


### LINKS TO DOCS:
[to be added -- slides are currently offline]

### PROJECT SPECIFIC NOTES:
-Spike Plan stress test was completed successfully in class. Therefore, there is *no* results file for this.  
-The .env is on A's computer, and was ignored by github because it contains the API key needed to run, and that any file that uses the AI includes a "load_dotenv()" to use it.
- We did not do OBJ #7. It was a little out of scope for the project and how we score risk for this milestone.
