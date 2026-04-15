# Sprint 3 Plan — Venture 8: TrailGuard

**Sprint Duration:** April 15 – April 21, 2026
**Sprint Goal:** Make the full system demo-ready. Close the documentation gaps, align the schema, rebalance contributions, and rehearse the 4/29 presentation end-to-end.
**Final Demo:** April 29, 2026

---

## Context

Sprint 2 fixed the critical backend bugs and shipped a working three-page Streamlit dashboard (Submit Hazard, Risk Engine + Hazard Database filters, Briefings) wired into the real pipeline. That is the demo surface for 4/29. What is left is stabilization, documentation honesty, and presentation polish. Two risks to address this sprint: (1) `evaluation_results.md` still reports "100%/Y/Y" with no methodology, which is the kind of claim that gets flagged at finals, and (2) collincan2 had only 2 commits in Sprint 2, repeating the M2 imbalance. Sprint 3 distributes the highest-value tasks to collincan2 on purpose.

---

## Sprint 3 Tasks

### P0 — Demo Blockers (Days 1–2, Apr 15–16)

| Task | Owner | Description |
|---|---|---|
| Align `validateschema.json` with `validator.py` | AndCplusplus | Add `"Other"` to `hazard_type` enum, add `user_notes` as a required or optional string field, change `trail_segment` from `string` to `integer` (1–7). Verify a Submit Hazard run validates against both Pydantic and the JSON schema. |
| End-to-end smoke test log | AndCplusplus | Launch `streamlit run src/frontview/app.py`, submit 3 real images across 3 segments, run Risk Engine live on each, generate one daily briefing. Capture the run in `docs/sprint_3_smoke_test.md` with screenshots and any errors. |
| Rewrite `evaluation_results.md` | collincan2 | Remove the "100%/Y/Y" table. Replace with: (a) methodology section (how runs were executed, how Hazard Type and Risk Range correctness were judged), (b) raw per-case results with predicted vs expected hazard type and predicted severity, (c) failure analysis for any misses, (d) escalation rate section covering at least 3 scored scenarios. Honest numbers beat perfect numbers. |
| Add escalation test cases | collincan2 | Add 3 new rows to `evaluation_test_cases.md` that are explicitly designed to cross the 10.0 escalation threshold (for example, multiple severity-4/5 hazards clustered on Segment 5 which has the highest traffic multiplier). Note expected scores. |

### P1 — Dashboard Polish (Days 2–4, Apr 16–18)

| Task | Owner | Description |
|---|---|---|
| Hazard map / segment overview | AndCplusplus | Add a segment overview view (doesn't need real maps). A grid or table of all 7 segments showing name, current risk score, reports in last 48h, escalation state, color-coded red/yellow/green. This is the "park-wide" view the demo needs. |
| Fix typo + polish UI | collincan2 | Fix `"RISK ESCALATION TRIGGERD"` → `"RISK ESCALATION TRIGGERED"` in `2_Risk_Engine.py`. Add page icons and titles consistently. Replace emoji placeholders where they render oddly. |
| Absolute paths for data files | AndCplusplus | `hazard_db.json` and daily briefing `.txt` files currently resolve relative to the launch directory. Anchor both to `src/` so the dashboard works regardless of where Streamlit is started. |
| README rewrite | collincan2 | Document the full workflow: how to set up `.env`, how to run the Streamlit dashboard, how to run the CLI engines (`analysis.py`, `risk_engine.py`, `briefing_engine.py`), and where outputs land. This is the document a grader opens first. |

### P2 — Evaluation & Testing (Days 3–5, Apr 17–19)

| Task | Owner | Description |
|---|---|---|
| Unit tests for `risk_engine` | AndCplusplus | Add `tests/test_risk_engine.py` with at least 4 cases: zero reports, single low-severity report, clustered high-severity triggering escalation, and a boundary case at exactly 10.0. Now that the engine is a pure function this is straightforward. |
| Baseline comparison note | collincan2 | Add a short section to `evaluation_results.md` describing what would happen without the few-shot examples and without the Pydantic retry loop. Does not need to be re-run; a qualitative paragraph grounded in one A/B example is sufficient. |
| Contribution balance review | Both | Mid-sprint check-in on 4/18: both members confirm at least 5 commits each. If collincan2 is below, AndCplusplus hands off a concrete task before 4/19. |

### P3 — Demo Prep (Days 5–7, Apr 19–21)

| Task | Owner | Description |
|---|---|---|
| Demo script | collincan2 | Write `docs/demo_script.md`: 5-minute walkthrough covering (1) problem + pitch, (2) submit a hazard image live, (3) show JSON validation, (4) run risk engine live on a high-traffic segment, (5) show escalation triggered, (6) generate and read daily briefing, (7) show one honest eval result. One sentence per beat, who speaks what. |
| Demo rehearsal | Both | One full dry run on 4/20 with a fresh clone, fresh `.env`, fresh browser. Time it. Capture any issues in `docs/rehearsal_notes.md`. |
| Pitch deck update | collincan2 | Refresh `docs/Pitch Deck.key` (or export to PDF) with Sprint 3 screenshots and the real evaluation numbers from the rewritten `evaluation_results.md`. |

---

## Definition of Done (Sprint 3)

- [ ] `validateschema.json` validates every report produced by the live Streamlit Submit Hazard page.
- [ ] `evaluation_results.md` contains methodology, per-case results, and at least 3 escalation scenarios. No unsupported 100% claims.
- [ ] Segment overview / park-wide risk view renders in the dashboard.
- [ ] Smoke test log committed at `docs/sprint_3_smoke_test.md`.
- [ ] README documents the dashboard workflow.
- [ ] At least one unit test file for `risk_engine`.
- [ ] Demo script exists and has been rehearsed once end-to-end.
- [ ] Both team members have at least 5 meaningful commits this sprint.

---

## Contribution Expectations

Sprint 2 ended with a 20-vs-2 commit split. That cannot repeat. This plan deliberately assigns the highest-visibility documentation tasks (evaluation rewrite, README, demo script) and several UI polish items to collincan2, and the deep engineering to AndCplusplus. Both workstreams are roughly equal in effort and visibility. A mid-sprint check on 4/18 is on the calendar specifically to catch drift early.

If collincan2 is blocked on any task, raise it in the team channel by 4/17 so it can be rescoped. The goal is not to punish anyone, it's to make sure the team shows up to the 4/29 demo as a team.

---

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Streamlit file path issues surface only during live demo | P1 absolute-path task + smoke test log on day 1–2 |
| Evaluation numbers get questioned at finals | P0 rewrite replaces "100%" with grounded methodology before anyone asks |
| Dashboard breaks on a fresh clone | Demo rehearsal from a fresh clone on 4/20 |
| Single-person bus factor | Both members work on dashboard + docs this sprint so knowledge transfers |

---

## Remaining Sprints Overview

| Sprint | Dates | Focus |
|---|---|---|
| Sprint 3 (this sprint) | Apr 15–21 | Schema alignment, eval rewrite, dashboard polish, demo script |
| Sprint 4 | Apr 22–28 | Final integration, presentation prep, full rehearsals, deliverables freeze |
| **Final Demo** | **Apr 29** | **Presentation and live demo** |
| Final Deliverables Due | May 3 | All documentation and code finalized |

---

## Final Demo Day Heads-Up (April 29)

Two weeks out. Rehearse toward this format during Sprint 3 and Sprint 4.

**12 minutes per team, hard cap.** I will cut you off at 12:00 to keep all 8 teams on schedule, so rehearse to 10:30 or 11:00 to leave margin. Suggested split:

1. **About 3 min: overall design.** What the product does, the core pipeline, and the architectural decisions that matter (deterministic risk scoring, escalation engine, refusal policy). No code walkthroughs.
2. **About 4 min: individual contributions.** Each team member speaks briefly about what they personally owned this semester. For a 2-person team, plan roughly 90 seconds each.
3. **About 4 min: live demo of the highlights.** Pick 2 or 3 scenarios from your existing demo script. Required: at least one refusal or failure case and at least one end-to-end grounded answer. Do not spend this time on UI polish.
4. **About 1 min: Q&A**, included in the 12 minutes.

**Running order** is Venture 1 through Venture 8 in order, so TrailGuard presents last.

**Backup plan:** have a prerecorded screen capture of the working path ready in case the live demo fails. Internet or API hiccups are not an excuse on demo day.

**Slides and runbook:** not due before the presentation, but both are required artifacts in the final deliverables package due May 3. Save them under `docs/Final_Demo/` in your repo.

**Avoid:** narrating code, reading slides verbatim, skipping the refusal case, opening with missing features. Present the version you are proud of.

Rehearse the full 12 minutes end to end at least twice, at least once with a timer.
