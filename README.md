
### TRAIL GUARD: 
An app designed to provide a dashboard for those who are park management or on a volunteer basis. The project contains a way for people to
upload photos and descriptions of problems, while management can see things laid out for easy, actionable task creation.

*Collin Cantu - Reports, Dataset Analysis, Design* 

*Andrew Cadena - Interface, Risk Assessment, Data Implementation*

## RUNNING THE APP:
### Setup:
1. Open a terminal in the project folder, specifically src folder.
3. Install all required dependencies: python -m pip install -r src/requirements.txt
4. Move any .pngs files into the src folder, along with a .env containing an API key
5. create a .env file in the src folder, and fill it with 'GEMINI_API_KEY=<your_api_key_here>'
7. Start the program with streamlit run src/frontview/app.py, then after a couple reports move onto briefing_engine.py

### Analyze Photo:
Example Analysis of Photo:
python analysis.py FallenTree.jpg --segment 2 --time "08:30 AM" --desc "Large collapsed tree blocking the bridge, blocks the main path!" 

   FallenTree.jpg → image to analyze<br>
   --segment 2 → location/area (1–7)<br>
   --time → time of report<br>
   --desc → optional description of the issue<br>
   
### Segmented Issue Summary with Action Report:
Summary of issues and suggested action based on marker segments. <br>
_NOTE: You must run the above Analyze Photo command at least **3** times before continuing!_ <br>

python summary_engine.py --segment <1-7><br>
Simply choose the segment you wish to analyze issues for and run the command. It needs to fit in the segment range for your park.

### Risk Engine:
Calculates risk for escalation purposes.
python risk-engine.py --segment <1-7><br>
Simply choose the segment you wish to analyze risk for and run the command. It needs to fit in the segment range for your park.

### Ranger Daily Briefing
Creates a daily briefing for rangers.
python briefing_engine.py
This will create a dated .txt file containing top 3 priority segments,main hazard categories observed, why each top segment is prioritized, and suggested operational focus areas for the day


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

## OBJECTIVE CORRESPONDENCE: MILESTONE 2
#1 - ReadMe updated. 
#2 - Files validated to exist, and are named per deliverable instructions.
#3 - /docs/report_schema.md created, and includes deliverable components.
#4 - /docs/risk_scoring.md includes deliverable components.
#5 - ranger briefing functional and includes output matching deliverable components.
#6 - /docs/evaluation_test_cases.md was correct. the /docs/evaluation_results exists now, and is confirmed to be accurate.
#7 - general renaming of repo files to match lowercase consistency and formatting.

### LINKS TO DOCS:
[to be added -- slides are currently offline]

### PROJECT SPECIFIC NOTES:
-Spike Plan stress test was completed successfully in class. Therefore, there is *no* results file for this.  
-The .env is on A's computer, and was ignored by github because it contains the API key needed to run, and that any file that uses the AI includes a "load_dotenv()" to use it.
- We did not do OBJ #7. It was a little out of scope for the project and how we score risk for this milestone.
