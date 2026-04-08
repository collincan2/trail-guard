# Sprint 2 Plan — Venture 8: TrailGuard

**Sprint Duration:** April 8 – April 14, 2026
**Sprint Goal:** Fix critical bugs, complete missing deliverables, and begin frontend dashboard development.
**Final Demo:** April 29, 2026

---

## Context

After Milestone 2, the backend pipeline (analysis → validation → risk scoring → briefing) is architecturally sound but has runtime bugs and missing deliverables. The frontend (dashboard for rangers) has not been started. With ~3 weeks until the final demo, Sprint 2 focuses on stabilizing the backend and launching dashboard work.

---

## Sprint 2 Tasks

### P0 — Critical Fixes (Days 1–2)

| Task | Owner | Description |
|---|---|---|
| Fix summary_engine.py import | AndCplusplus | Change `get_segment_info` → `get_segmentInfo` to match location_engine.py export |
| Resolve timestamp format | AndCplusplus | Standardize on one format across validateschema.json, analysis.py, risk_engine.py, briefing_engine.py. Recommend ISO 8601 (`YYYY-MM-DD HH:MM`) everywhere |
| Add .env.example | collincan2 | Create .env.example with GOOGLE_API_KEY placeholder |
| Convert PRD.pdf → PRD.md | collincan2 | Convert to markdown for consistency |
| Fix pilot_scope filename | collincan2 | Rename `Pilot Scope.md` → `pilot_scope.md` |

### P1 — End-to-End Verification (Days 2–3)

| Task | Owner | Description |
|---|---|---|
| Full pipeline test | AndCplusplus | Run complete flow: image → analysis → validation → risk scoring → briefing. Document any failures |
| Escalation test cases | collincan2 | Add test scenarios that trigger escalation (score ≥ 10.0) to evaluation_test_cases.md |
| Update evaluation_results.md | collincan2 | Add methodology description, failure analysis, and honest metrics. Remove "100% perfect" claims unless backed by measurement details |

### P2 — Frontend Dashboard (Days 3–7)

| Task | Owner | Description |
|---|---|---|
| Dashboard framework setup | Jacob | Set up web framework (Flask/Streamlit) in `src/frontview/`. Create basic layout with navigation |
| Hazard map view | Jacob | Display reported hazards on a segment map with color-coded risk levels |
| Daily briefing display | Jacob | Show daily ranger briefing in dashboard with top-3 priority segments |
| Risk dashboard filters | AndCplusplus | Add date range, segment, and hazard category filters to dashboard |
| Report submission UI | collincan2 | Basic form for uploading photos and submitting reports through the dashboard |

### P3 — Cleanup (Day 7)

| Task | Owner | Description |
|---|---|---|
| Remove legacy Trailguard/ | collincan2 | Delete old Test2.py prototype directory |
| Align validator schema | AndCplusplus | Sync `validateschema.json` with Pydantic validator (add `user_notes`, align `Other` category) |
| Update README | Jacob | Document dashboard setup and full workflow |

---

## Definition of Done (Sprint 2)

- [ ] `summary_engine.py` runs without import errors
- [ ] Full pipeline runs end-to-end with consistent timestamps
- [ ] `.env.example` exists with all required keys
- [ ] PRD.md and pilot_scope.md have correct filenames
- [ ] At least 2 escalation test cases documented
- [ ] Dashboard prototype renders with at least hazard list and briefing view
- [ ] Each team member has meaningful code commits this sprint

---

## Contribution Expectations

Jacob currently has only 4 documentation-only commits. **Sprint 2 is Jacob's opportunity to take ownership of the frontend dashboard.** This is a substantial, visible deliverable that will be central to the final demo. Equal contribution is expected from all team members going forward.

---

## Remaining Sprints Overview

| Sprint | Dates | Focus |
|---|---|---|
| Sprint 2 (this sprint) | Apr 8–14 | Bug fixes, missing deliverables, dashboard prototype |
| Sprint 3 | Apr 15–21 | Dashboard polish, park view, demo rehearsal |
| Sprint 4 | Apr 22–28 | Final integration, presentation prep, final deliverables |
| **Final Demo** | **Apr 29** | **Presentation and live demo** |
| Final Deliverables Due | May 3 | All documentation and code finalized |
