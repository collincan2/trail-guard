# Risk Scoring Methodology

The risk scoring formula is documented below. It contains the details on how the risk scoring works, and how that information is processed to the end user.

## Segmentation Scoring
Risk scores exist to help the program give a measurement of prioritization for any given issue that arises.  If the risk score is high enough, an escalation request is sent to the end user, which signals a high priority area to address.

It is important to note that the current implementation uses *segments* to organize the scoring. This means that a park will be pre-defined by these areas according to the park's standards, and issues will be reported based on the park segment they occur in or affect.  The pilot park uses a segment count of 7.

## Scoring Process
Several variables are collected in risk-engine.py.
\- The current date and time
\-  The total amount of reports for a given segment in a 48hr. time period (reports_48h)
\- The total, final severity rating (total_severity)
\- Recent Hazards file appended for further AI context
\- Segment being analyzed 

If the time of the reported issue has occurred within 48 hours of the current system time, then the reports_48h variable increases by one, to show the count of recent reports for that segment.

The total_severity variable is also increased by the severity_rating for the current issue. This means something like a mud patch will have a lower score like "1", which keeps the total severity low; a large tree blockade will have a higher base score like "4", which will cause the total severity to be higher.

At this point, some details of the hazard are appended to a database file for further analysis or retrieval. 

### Final Scoring

*The score defaults to a 0.0 if there are no reports in a 48h window for this segment.*

 Otherwise, the risk score is made by taking the total_severity (so far!) and dividing it by the amount of reports in the 48h window for that segment. This gives you an average severity. 

For example, if you had the above mud patch example, you are sitting at a 1, and if you also had the tree blockade example happen in the same segment, you'd have a total_severity of 5 so far. Dividing this by 2, you'd have 2.5 as the average. 

There is a volume penalty that accounts for the amount of continuous reports that occur in a short time frame. This is calculated by multiplying 1.2 to the reports_48h variable. Per our example, this would be (2 * 1.2) = 2.4.

Finally, adding both this volume penalty to the average severity gives you the total, reported severity. In our above example, this translates to (2.4 volume penalty + 2.5 average severity) = 4.9 total risk score.

## Usage
Currently, risk scoring is used mostly to look at escalations. If the final, total risk score is equal to or greater than 7.0, than an **_escalation_** is required. 

This is a more direct alert that the particular affected segment needs immediate or special attention.



