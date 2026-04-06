# Sprint Plan: Week 1 Toward MVP

  ## Sprint Goal
  Make the current system reliable enough to demo one complete end-to-end MVP workflow.

  ## This Week's Feasible Targets
  1. Finalize one consistent report schema across the whole project.
  2. Make validation actually run before any report is saved.
  3. Add a simple location layer for the 7 pilot segments.
  4. Document the risk scoring formula in `docs/risk_scoring.md`.
  5. Improve the risk engine so location affects the score.
  6. Add a minimal ranger daily briefing output:
     - top 3 priority segments
     - main hazard categories
     - recommended focus areas
  7. Clean the README so another team member can run the pipeline without guessing.

  ## Definition of Done
  - One sample image can go through analysis, validation, scoring, aggregation, and briefing.
  - The repo has no missing required MVP files for this path.
  - The team can explain why a segment was prioritized.

  ## Out of Scope This Week
  - UI polish
  - multi-park support
  - extra features beyond the MVP path

  ## Instructor Expectation
  Do not add new scope this week. Finish the missing core pieces and make the existing pipeline dependable enough for a live MVP demo.
