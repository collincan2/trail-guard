PRD ver. 1.2

### Problem and Target Users
Park management can utilize modern dashboard interfaces to better assess risk and
allocate tasks to employees. Those who are visiting or frequent the area can volunteer
to add to the dashboard via personal uploads. This will benefit those who use the areas,
like tourists and locals, as well as the park management, and those who work with
them.
Goal and Success Metrics
 * Be able to correctly identify photos, possibly given a description, with a (tentative)
 * 80% accuracy into categories of issues a park might face.
 * Dashboard filters, functions, and displays all information intuitively and in working order.

### MVP User Stories
* As a park staff member, I want to be able to filter and see structured issues in a
modern format, so that I can delegate tasks efficiently.
* As a park visitor, I want to be able to contribute easily to the workflow with a snap and
a sentence, so that the park can continue to improve and my time here is enjoyable.
* As an employee, I want to be able to understand my role and day-at-a glance, so that
I have a way to plan my shift and responsibilities.
* As a ranger, I want to be able to understand how risk assessment and categorization
is completed, that I may understand how these tasks are organized, and make
manual changes if needed.
* As a tourist, infrequent visitor, or a general park goer, who may not use the app
whatsoever, I might not do much in the way of contribution, but I can aways quickly
use an anonymous report and appreciate the park staying in good shape.

### MVP Scope vs. Non-Goals
* We WILL be looking for photo recognition, sentence entry, and categorization of issue
on the user side of the application.
* We WILL be looking for basic date/risk/category filters, dashboard viewpoint, and
clean visuals for the management side of the application.
* We WILL NOT be adding specific park constraints, we will be working with a test
sample of parks (moderate trail, desert region) and not all types, and this will not have
additional categories yet.
* In the future, we’d like to add more categories, customization for per-park basis, and
a cleaner, more streamlined dashboard/user interface.

### Acceptance Criteria
Pass:
* AI needs to get at least 50-75% of the test examples, aiming for higher end of range
* Output is structured, and easily understandable
* System produces a good priority level and categories are sortable
  
Fail:
* AI outputs are too inconsistent, vague, or unusual
* Too much manual correction needed
* Cannot see or view screen/dashboard
* Doesn’t categorize or sort correctly

### Assumptions and Constraints
* Data: Federal and State levels do have some existing guidelines for risk levels and
priority assessments, but we will have to create a version of our own since they’re not
fleshed out (besides wildfires).
* Time: We cannot go overboard - with our team ‘staff’, we have to stay realistic, and
focus on functions first, followed by polish. If there’s time after, we can then add
features.
* Ethics: Photo uploads and user privacy needs to be considered. How are the photos
scanned when they’re personal? How long are they stored, if they are at all? There are
some things to think about, but that would be the extent.

### Risk Scoring
A severity assignment is given during the analysis process, between 1-5. The AI decides
this based on risk to the park staff or visitors.

* 1-2: Low risk, mostly cosmetic or non-harmful. Animal feces and parking line visibility
are examples in this range.
* 3-4: Potential hazard, if not treated, could cause light to severe bodily damage.
Sidewalk cracks and signage issues are on the lower end, fallen trees and fire hazards
on the higher end.
* 4-5: Urgent. These issues include large animals, expensive infrastructure repairs, or
warning signage missing. If not treated quickly, these issues can quickly turn in to
damage or loss of life.

Once a severity score has been given, a risk score is analyzed solely off of the fact of
how often the sector reports issue in a small timeframe (48hrs). We would like to extend
this functionality to single incidents of high severity irrespective of report frequency.
If this risk score beats a threshold (>7.0) then that sector is ESCALATED.

### ESC Logic
Once a segment of a park has been ESCALATED, that sector is given priority on the
dashboard for staff. From this view, the sector is flagged and reasoning with action
requirements is visible.  

The goal of this is to quickly prioritize near-non emergency reports — this does NOT
replace emergency services or the park rangers themselves. Rather, it can let the
application decide that some photos that were taken would be better served
immediately, but the visitor can always call services and the management can always
override the priority levels.

### Acceptance Criteria, Restated
If the analysis meets the .JSON file that validates the fields and makes sure that they
can be used and fit the constraints, ie., severity rating present and a integer between
1-5, the file will then attempt to organize the issue using the photo and an optional
description.  

The severity level (1-5 scale), Hazard Type (Debris, Fire Hazard, etc.), and escalation
parameters are then checked. As long as the .JSON test is passed, the severity is in
range (±1), and the Hazard Type is accurate, then the photo is considered to have been
sorted correctly. Currently, ESC will only occur based on sector data, so it is not
necessarily counted in those tests yet — but it will be able to handle individual cases
later.
