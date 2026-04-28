# Sprint 3 Grade, Venture 8: TrailGuard

**Graded:** April 28, 2026
**Sprint Window:** April 15 – April 24, 2026 (extended from April 21)
**Final Demo:** April 29, 2026
**Final Deliverables Due:** May 3, 2026

---

## Overall Grade: 83/100

**Note on individual grades:** This is the venture-level grade. Members who severely under-contributed during Sprint 3 may receive a reduced individual grade applied separately.

**Note on grading scope:** Final-presentation prep items (demo script as a written deliverable, rehearsal logs, slide deck drafts, pitch deck refreshes, backup recordings) are not counted against the Sprint 3 grade. They appear in the "Items to Complete by May 3" section instead.

---

## Summary

Sprint 3 shipped a substantial amount of code and documentation, but the contribution split during the extended sprint window was 47-vs-1, and the documentation tasks assigned to collincan2 mostly missed the extended deadline (they landed Apr 25-26 rather than by Apr 24 EOD). The venture-level grade reflects both what shipped on time and what did not.

What landed on time: `validateschema.json` was aligned with `validator.py` (added `Other` hazard type, made `trail_segment` an integer 1-7, added optional `user_notes`). The smoke-test log is in the repo. The Park-Wide Overview tab now shows all seven segments with risk score, reports in last 48h, escalation state, and color coding. `hazard_db.json` is anchored to `src/` for absolute-path stability. `tests/test_risk_engine.py` covers four scenarios (zero reports, single low-severity, clustered high-severity escalation, boundary at 10.0). The evaluation methodology rewrite landed Apr 23 (within the extended window): no more "100%/Y/Y" claim, real per-case results, real failure analysis.

What missed the extended deadline (and counts against the Sprint 3 grade): the README rewrite (Apr 26) and the three explicit escalation test cases (Apr 25). The "RISK ESCALATION TRIGGERD" typo on line 87 of `2_Risk_Engine.py` is still present despite being a P1 task. The mid-sprint contribution check on Apr 18 (which the plan explicitly built in to catch drift early) did not happen.

What is treated as final-prep and does not affect the Sprint 3 grade: the demo script, the rehearsal log, and the pitch deck refresh. The demo script and pitch deck did land Apr 25-26 (in the repo for the final demo). The rehearsal is still pending. All three appear in the May 3 deliverables section.

This is the third sprint in a row with a severe contribution imbalance. Sprint 2 was 20-vs-2 and the Sprint 3 plan was deliberately structured to balance that by assigning the highest-visibility documentation tasks to collincan2 and the deep engineering to AndCplusplus. The result was 47-vs-1 during the sprint window and 47-vs-21 only after Apr 25-26 work landed (still imbalanced cumulatively).

The grade is 83 because:

- Most P0 and P1 venture-level tasks have shipped on time.
- The schema alignment, Park-Wide Overview, absolute paths, smoke test, and unit tests are all real engineering work landed on time.
- The README rewrite (P1) and the explicit escalation test cases (P0) missed the extended deadline.
- The DoD requirement "both members 5+ commits this sprint" was not met during the sprint window or the extended window (1 commit by collincan2 through Apr 24).
- The typo fix (a 30-second change on a P1 line) is still in the source code.

---

## Category Breakdown

### 1. Task Completion (37/40)

**P0 (3 of 4 complete on time, 1 late):**
- Align `validateschema.json` with `validator.py`: shipped (AndCplusplus, Apr 21). `Other` enum added, `trail_segment` integer 1-7, `user_notes` optional. There is a trailing-comma issue in the JSON in the `optional` array; minor but should be cleaned up.
- End-to-end smoke test log: shipped (`docs/sprint_3_smoke_test.md`, AndCplusplus, Apr 21). Thin at 23 lines but present.
- Rewrite `evaluation_results.md`: shipped (collincan2, Apr 23, within extended window). 169 lines with methodology, per-case results, failure analysis.
- Add 3 escalation test cases: late (collincan2, Apr 25, after extended cutoff). Counts as a Sprint-3 miss for grading purposes.

**P1 (3 of 4 complete on time, 1 late, 1 still missing):**
- Hazard map / Park-Wide Overview: shipped (AndCplusplus, Apr 21). Tab structure with all 7 segments, color-coded.
- Fix typo `TRIGGERD` → `TRIGGERED` in `2_Risk_Engine.py` line 87: not done. Still in code.
- Absolute paths for data files: shipped (AndCplusplus, Apr 21). `hazard_db.json` anchored.
- README rewrite: late (collincan2, Apr 26, after extended cutoff). AndCplusplus did smaller README edits Apr 22 but the substantive rewrite landed late.

**P2 (1 of 3 complete on time, 1 missed entirely, 1 partial):**
- Unit tests for risk_engine: shipped (`tests/test_risk_engine.py`, AndCplusplus, Apr 21).
- Baseline comparison note: not visible in `evaluation_results.md`.
- Mid-sprint contribution review on Apr 18: did not happen.

**P3 (final-prep, not graded):**
- Demo script: deferred to final-prep (May 3 deliverables). Did land Apr 25-26.
- Demo rehearsal: deferred to final-prep (May 3 deliverables).
- Pitch deck update: deferred to final-prep (May 3 deliverables). Did land Apr 25.

### 2. Code Quality (17/20)

- `tests/test_risk_engine.py` covers the four scenarios the plan called for; the engine is now testable.
- Park-Wide Overview implementation is clean.
- Absolute path anchoring is the right fix.
- `validateschema.json` has a trailing-comma syntax issue in the `optional` array.
- The "TRIGGERD" typo remains in `2_Risk_Engine.py` line 87 despite multiple sprints of opportunity.
- AndCplusplus's frontend rename (`app.py` → `Home.py`) is reasonable but introduces churn.

### 3. Documentation (13/15)

- `evaluation_results.md` rewrite is substantial and honest. The "100%/Y/Y" claim is gone; methodology and per-case data are present.
- `sprint_3_smoke_test.md` is thin but documents real runs with screenshots.
- README rewrite landed but Apr 26, after extended cutoff. It is in the repo now.
- Demo script and pitch deck both landed Apr 25-26 (final-prep, not graded against Sprint 3).

### 4. Testing / Evaluation (13/15)

- Four unit tests on risk_engine.
- Smoke test with real images and screenshots.
- Honest methodology in evaluation_results.md.
- Three explicit escalation test cases landed Apr 25 (after the extended cutoff).

### 5. Team Contribution (3/10)

| Member | In-window Commits (Apr 15-24) | Sprint 3 Work | Signal |
|---|---|---|---|
| AndCplusplus | 47 | Schema alignment, Park-Wide Overview, absolute paths, smoke test, unit tests, README iteration, frontview reorg | Strong but solo |
| collincan2 | 1 | Single Apr 23 commit on `evaluation_results.md` rewrite | **Severe imbalance** |

Cumulative through Apr 28 (including post-cutoff work): AndCplusplus ~52, collincan2 ~21.

The Sprint 3 plan was structured specifically to address the Sprint 2 imbalance: the highest-visibility documentation tasks (evaluation rewrite, README, demo script, pitch deck) were assigned to collincan2, and a mid-sprint check on Apr 18 was put on the calendar to catch drift early. Neither happened in time. This is the third consecutive sprint with severe imbalance. The team will demo on Apr 29 with all features working, so the venture is demo-ready, but the contribution pattern is a serious issue for a two-person team.

---

## Per-Task Completion Status

| Priority | Task | Owner | Status (by Apr 24 EOD) |
|---|---|---|---|
| P0 | Align validateschema.json with validator.py | AndCplusplus | Done (minor JSON cleanup needed) |
| P0 | End-to-end smoke test log | AndCplusplus | Done |
| P0 | Rewrite evaluation_results.md | collincan2 | Done (Apr 23, in window) |
| P0 | Add 3 escalation test cases | collincan2 | Late (Apr 25) |
| P1 | Hazard map / Park-Wide Overview | AndCplusplus | Done |
| P1 | Fix typo TRIGGERD → TRIGGERED | collincan2 | Not done |
| P1 | Absolute paths for data files | AndCplusplus | Done |
| P1 | README rewrite | collincan2 | Late (Apr 26) |
| P2 | Unit tests for risk_engine | AndCplusplus | Done |
| P2 | Baseline comparison note | collincan2 | Not visible |
| P2 | Mid-sprint contribution review (Apr 18) | Both | Did not happen |
| P3 | Demo script | collincan2 | Deferred to final-prep |
| P3 | Demo rehearsal | Both | Deferred to final-prep |
| P3 | Pitch deck update | collincan2 | Deferred to final-prep |

---

## Definition of Done (Sprint 3) Check

- [x] `validateschema.json` validates every report from Submit Hazard
- [x] `evaluation_results.md` contains methodology, per-case results, escalation scenarios (escalation cases landed Apr 25)
- [x] Segment overview / park-wide risk view renders in the dashboard
- [x] Smoke test log committed at `docs/sprint_3_smoke_test.md`
- [~] README documents the dashboard workflow (landed Apr 26, after cutoff)
- [x] At least one unit test file for `risk_engine`
- [~] Demo script exists and has been rehearsed once end-to-end (deferred to final-prep)
- [ ] Both team members have at least 5 meaningful commits this sprint (AndCplusplus 47, collincan2 1)

---

## Items to Complete by May 3 (Final Deliverables)

The May 3 package is required to be under `docs/Final_Demo/` in the repo. Save the following items there:

1. **Final demo slides** (PDF or PPTX) under `docs/Final_Demo/`. Refresh the existing `Trail Guard.pdf` / pitch deck with the actual numbers from the rewritten `evaluation_results.md`, the Park-Wide Overview screenshot, and the live-demo plan (submit hazard → JSON validation → risk engine → escalation → daily briefing → one honest eval result).
2. **Runbook** at `docs/Final_Demo/Runbook.md`. Cover: prerequisites, env setup, how to launch the Streamlit dashboard, how to run the CLI engines (`analysis.py`, `risk_engine.py`, `briefing_engine.py`), where outputs land, the JSON schema layout. The README rewrite from Apr 26 is good source material to consolidate.
3. **Final demo video** at `docs/Final_Demo/Final_Demo_Video.mp4`.
4. **Final code on `main`**. Confirm `main` reflects the demo state.

Sprint 3 carryovers that must land before May 3:

5. **Fix the `TRIGGERD` → `TRIGGERED` typo** on `2_Risk_Engine.py` line 87. This was a P1 task in Sprint 3, takes about 30 seconds, and is the kind of detail a grader will catch on the live demo.
6. **Add 3 explicit escalation test cases** to `evaluation_test_cases.md` (multi-severity-4/5 hazards clustered on Segment 5, etc.). The Apr 25 commits added some content; verify the three explicit rows are there with expected scores.
7. **Demo rehearsal**. Run the full demo on a fresh clone with a fresh `.env` and a fresh browser. Capture timing and any issues in `docs/Final_Demo/rehearsal_notes.md`.
8. **Baseline comparison note** in `evaluation_results.md`. A short qualitative paragraph (one A/B example) describing what would happen without the few-shot examples and without the Pydantic retry loop.
9. **Clean up `validateschema.json`**. Trailing-comma in the `optional` array breaks strict JSON parsers.

The team-level priority through May 3 is to run the rehearsal together (item 7), so both members touch the same demo flow on the same machine before Apr 29. This addresses both the rehearsal gap and the mid-sprint contribution check that did not happen on Apr 18.
