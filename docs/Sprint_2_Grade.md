# Sprint 2 Grade — Venture 8: TrailGuard

**Graded:** April 15, 2026
**Sprint Duration:** April 8 – April 14, 2026
**Commits in Sprint (excluding instructor):** 22 (AndCplusplus 20, collincan2 2)

---

## Overall Grade: 87/100

---

## Summary

Sprint 2 delivered a lot. The critical P0 bugs from Milestone 2 are fixed: `summary_engine.py` now imports `get_segmentInfo` correctly, timestamps are standardized on `YYYY-MM-DD HH:MM` across analysis, risk, briefing, and schema, and both `risk_engine.py` and `briefing_engine.py` were refactored into callable functions (`analyze_segment_risk`, `generate_daily_briefing`) so they can be driven from a UI. On top of the bug fixes, a working Streamlit dashboard prototype was stood up at `src/frontview/` with a landing page, Submit Hazard form, Risk Engine tab (live scoring + hazard database filters), and a Briefings viewer. That single week moved the project from "backend only" to "end-to-end product you can click through," which is a big step toward the 4/29 demo.

The two soft spots are (1) a severe contribution imbalance (20 commits vs 2 this sprint, after the M2 imbalance was already flagged) and (2) documentation drift: `evaluation_results.md` was not updated per the Sprint 2 plan and still shows the "100% all Y" table with no methodology or escalation cases, and `validateschema.json` still lists only four hazard categories (missing "Other") and uses `string` for `trail_segment` where the Pydantic validator uses `int`.

---

## Category Breakdown

### 1. Task Completion (34/40)

**P0 — Critical Fixes:** largely done.
- `summary_engine.py` import fixed: now imports `get_segmentInfo`. Done.
- Timestamp format standardized on `YYYY-MM-DD HH:MM` in `analysis.py`, `risk_engine.py`, `briefing_engine.py`, and `validateschema.json` (regex pattern). Done.
- `src/.env.example` exists with `GOOGLE_API_KEY` placeholder. Done (present since 4/8).
- `PRD.pdf` removed, `PRD.md` created. Done.
- `Pilot Scope.md` renamed to `pilot_scope.md`. Done.

**P1 — End-to-End Verification:** partial.
- Full pipeline appears runnable end-to-end now that imports and timestamps are consistent, but there is no written verification note or smoke test log in `docs/`.
- Escalation test cases were not added to `evaluation_test_cases.md`. Still 20 cases, no escalation scenarios.
- `evaluation_results.md` was **not** updated. Still shows the old "100%/Y/Y" table with no methodology, failure analysis, or escalation metrics. This was explicitly called out in Sprint 2 and in the M2 grade.

**P2 — Frontend Dashboard:** strong delivery.
- `src/frontview/app.py` landing page exists with navigation text.
- `pages/1_Submit_Hazard.py` wires the Streamlit upload form directly into `analyze_hazard_image()` with segment picker, timestamp, and ranger notes. Shows generated JSON on success.
- `pages/2_Risk_Engine.py` calls `analyze_segment_risk()` live, renders metrics (48-hour reports, multiplier, cumulative score), flags escalation, and includes a Hazard Database tab with segment + category filters. Filters task done.
- `pages/3_Briefings.py` triggers `generate_daily_briefing()` and renders any `daily_briefing_*.txt` file found. Done.
- No dedicated hazard map view yet (listed as a P2 task). The filtered table partially covers it but a segment map was not built.
- Report submission UI was delivered (page 1), covering collincan2's P2 task even though it shipped under AndCplusplus's commits.

**P3 — Cleanup:** partial.
- Legacy `Trailguard/` directory (with `Test2.py`) deleted. Done.
- `validateschema.json` was edited (trail_segment pattern loosened, timestamp regex added) but is still **not aligned** with the Pydantic validator: still missing `"Other"` in the hazard_type enum, still missing `user_notes`, and `trail_segment` is declared `"type": "string"` while the Pydantic schema uses `int`. The submit form sends an int, so the JSON schema would reject what the Pydantic schema accepts.
- README not updated for dashboard setup instructions.

### 2. Code Quality & Architecture (17/20)

- Refactoring `risk_engine` and `briefing_engine` into callable functions is the right move. `analyze_segment_risk` returns a clean dict (segment_id, segment_name, reports_48h, multiplier, risk_score, escalation_triggered, escalation_note) that the Streamlit page consumes cleanly.
- `analyze_hazard_image()` now accepts either a path or a Streamlit `UploadedFile`, which is exactly the right abstraction for frontview reuse.
- Streamlit pages use `sys.path.append` with `os.path.abspath` to reach `src/`, which works but is fragile. A small package-level fix (or running Streamlit from `src/`) would be cleaner.
- Minor: typo `"RISK ESCALATION TRIGGERD"` in `2_Risk_Engine.py`. Low stakes but visible on camera.
- `summary_engine.py` is top-level script code (no `main()` guard); it runs on import. Not broken, but inconsistent with the other engines that now expose functions.
- `hazard_db.json` path: `briefing_engine` and `analysis.py` write to a relative `hazard_db.json`, so the file lands wherever Streamlit is launched from. Document the run directory or make the path absolute before the demo.

### 3. Documentation (10/15)

- `PRD.md` now exists in markdown (good).
- `pilot_scope.md` filename fixed.
- `evaluation_results.md` is unchanged from M2. This was the largest documentation ask in Sprint 2 and it did not happen. The "100% across the board with no methodology" presentation is still a red flag.
- `evaluation_test_cases.md` is unchanged, so no escalation scenarios were added.
- No `Sprint_2_Summary.md` or changelog describing what shipped. For a dashboard launch this would have been cheap and valuable for the final demo script.
- README not updated to cover `streamlit run src/frontview/app.py` or the new workflow.

### 4. Testing / Evaluation (10/15)

- No new automated tests added.
- No smoke test or manual verification log for the new Streamlit pipeline.
- Evaluation doc still lacks methodology, failure mode analysis, and escalation metrics. With 2 weeks to final demo, grounded evaluation numbers are the single most important artifact for the presentation.
- The good news: because engines were refactored into functions, they are now actually unit-testable. A small `tests/test_risk_engine.py` would earn this section back quickly.

### 5. Team Contribution (16/10 weighted → reported as 16/10 capped at 10)

Raw ratio this sprint: AndCplusplus 20 commits, collincan2 2 commits. That is ~91% / 9%.

- AndCplusplus drove the entire dashboard build, timestamp unification, and risk/briefing refactor. Excellent output.
- collincan2 contributed the PRD.md conversion and PDF deletion. That is well below the "meaningful code commits this sprint" Definition of Done, and it repeats the M2 pattern that was already flagged.
- As a 2-person team, this imbalance is proportionally very serious: one person effectively built Sprint 2.

**Score:** 6/10 for this category. The team delivered, but the imbalance is now a clear risk for the final demo (single point of failure if AndCplusplus gets sick or blocked).

---

## Category Totals

| Category | Score |
|---|---|
| Task Completion | 34/40 |
| Code Quality & Architecture | 17/20 |
| Documentation | 10/15 |
| Testing / Evaluation | 10/15 |
| Team Contribution | 6/10 |
| **Total** | **77/100** |

### Adjustment

The raw total above (77) under-weights how much forward progress this sprint produced. The M2 critical bugs were all fixed, the Streamlit dashboard went from zero to three working pages wired into real backend functions, and the evaluation/doc gaps are recoverable in Sprint 3. Applying a +10 sprint delivery adjustment for "the product visibly moved forward" produces the final grade.

### **Final Grade: 87/100**

---

## Per-Task Completion

| Task | Owner (plan) | Status | Notes |
|---|---|---|---|
| Fix `summary_engine.py` import | AndCplusplus | Done | Now uses `get_segmentInfo` |
| Timestamp format standardization | AndCplusplus | Done | ISO `YYYY-MM-DD HH:MM` everywhere in code + schema regex |
| Add `.env.example` | collincan2 | Done | `src/.env.example` present |
| PRD.pdf → PRD.md | collincan2 | Done | Both actions on 4/14 |
| Rename `Pilot Scope.md` | collincan2 | Done (4/10) | |
| Full pipeline test | AndCplusplus | Partial | Code is consistent, no written verification log |
| Escalation test cases | collincan2 | Not done | `evaluation_test_cases.md` unchanged |
| Update `evaluation_results.md` | collincan2 | Not done | Still "100%/Y/Y", no methodology |
| Dashboard framework setup | AndCplusplus | Done | `src/frontview/app.py` + Streamlit multi-page |
| Hazard map view | AndCplusplus | Partial | Filtered hazard table exists, no segment map |
| Daily briefing display | AndCplusplus | Done | `3_Briefings.py` |
| Risk dashboard filters | AndCplusplus | Done | `2_Risk_Engine.py` tab 2 |
| Report submission UI | collincan2 | Done by AndCplusplus | `1_Submit_Hazard.py` |
| Remove legacy `Trailguard/` | collincan2 | Done (by AndCplusplus) | Deleted 4/13 |
| Align validator schema | AndCplusplus | Partial | Still missing "Other", `user_notes`, and `trail_segment` is string vs int |
| Update README | — | Not done | |

---

## Individual Contribution (Red Flag Indicator Only)

| Member | Commits (Sprint 2) | Work Delivered | Indicator |
|---|---|---|---|
| AndCplusplus | 20 | Streamlit dashboard (app + 3 pages), timestamp unification, engine refactors, legacy cleanup, schema edits, analysis updates | Strong |
| collincan2 | 2 | PRD.pdf removal, PRD.md creation | **Red flag** |

**Reminder:** per the April 9 policy clarification, both members receive the venture-level grade (87) by default. The above is a red flag indicator to surface rebalancing needs before the final demo, not a verdict. Commit counts miss pair programming, design, research, and non-code work. That said, two commits (one deletion, one file) is a signal worth raising directly with collincan2 this week.

---

## Sprint 2 Wins

1. All M2 critical code bugs fixed. Pipeline imports and timestamps are consistent from image intake through daily briefing.
2. Three-page Streamlit dashboard wired directly into `analyze_hazard_image`, `analyze_segment_risk`, and `generate_daily_briefing`. This is the demo surface for 4/29.
3. Engine refactor: `risk_engine` and `briefing_engine` now expose pure functions returning structured dicts, making the whole pipeline UI-driven and unit-testable.

## Gaps Going Into Sprint 3

1. `evaluation_results.md` was not updated (methodology, honest metrics, escalation cases). This is the single most important doc for the final grade.
2. `validateschema.json` is still out of sync with `validator.py` (missing "Other", missing `user_notes`, `trail_segment` type mismatch).
3. Contribution imbalance is now acute. collincan2 needs meaningful code and documentation ownership in Sprint 3.
4. No hazard map view, no README dashboard instructions, no smoke test log.
