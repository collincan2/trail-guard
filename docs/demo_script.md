## Demo Script

**(1) problem + pitch** (COLLIN)
*Introduction of Collin, Andrew*

Our app is Trail Guard, an app designed for park management and visitors. Parks are usually diverse in scale, climate, and staffing, and this app aims to enhance organization for park issues so that dispatched rangers are able to prioritize their workload. 

**(2) submit a hazard image live** (ANDREW)  

To start, I will take a hazard that has occurred in the test park [Mustang Park], and upload it to the app. The app will analyze the issue, and then recommend a course of action. Additionally, it will sort it under the park segment where it was reported, categorize it by issue type [Examples: Fire Hazard, Debris], assign it a risk level based on danger or hazard intensity, and timestamp it for reference.

 *Upload test image*

  **(3) show JSON validation** (COLLIN)

We also had to make sure we could validate any request. In other words, we had to make sure it did these things above, and if it couldn't, return an error instead of saving an incomplete report. These things include hazard type, risk level, trail segment number, timestamp, and AI description.

*show JSON validator file*

If it did, it would save in a database, which could be accessed to see issues reported and to aggregate reports, such as briefings or escalations [more on that later].

*show JSON database*

**(4) run risk engine live on a high-traffic segment** (ANDREW)

Here's an example of a high traffic segment -- some parts of a park are more busy than others. In these cases, additional variables can be added to reflect this. For example, in the North Metal Bridge [Segment 5], there is a traffic multiplier of 1.5x to show that issues here are more serious than in the parking lot/front entrance area.

*run risk engine on HTS, with live analysis*

**(5) show escalation triggered** (COLLIN)

In some cases, an escalation will trigger. These are to indicate an area or segment of a park that has had a wide influx of major issues in a short time period [48h]. If this happens, the rangers will be notified of these issue with a higher visibility than that of other issues. For this example, you can see that segments [1,5] are in need of urgent assistance. [You can upload the brush fire image to demonstrate ESC for segment 2]

*show risk engine for these segments*

For this project, issues uploaded are assigned a rating. When multiple issues arise, combined with the traffic multiplier, these ratings can exceed a threshold that triggers such a warning. After enough time passes, the escalation trigger will drop slowly as the issues themselves start being reduced/solved.

**(6) generate and read daily briefing** (ANDREW)

Ranger briefings are also able to be generated, to better assist the staffing with assignments, keeping it simple.
Here's an example:

*run briefing generator, open file and highlight key points*

**(7) show one honest eval result.** (COLLIN)

Here's our evaluation results for the testing we did -- we made a few cases and ran them so that we could test how accurate the system runs. 

*show table, show cases*
*explain result methodology -- these are run using the above categories, here are the results, here is what one such result means, etc.*

