# Milestone 2 Grade — Venture 8: TrailGuard

**Graded:** April 8, 2026
**Deadline:** April 5, 2026 (end of day)
**Late Commits:** None — all 105 commits are on or before 4/5/2026.

---

## Overall Grade: 88/100

---

## Summary

TrailGuard has built a solid backend pipeline for park hazard reporting: image analysis via Gemini, Pydantic-based validation, deterministic risk scoring with traffic multipliers, and a daily ranger briefing generator. The architecture cleanly separates LLM reasoning from deterministic scoring, which is a strong design decision. The evaluation dataset of 20 test images and cases is thorough. However, there are code bugs that would prevent parts of the pipeline from running end-to-end (import mismatch in summary_engine.py, timestamp format inconsistencies), some missing deliverables (.env.example, PRD format), and a significant contribution imbalance.

### Video Review Notes
The demo video is ~17 minutes — thorough walkthrough. **Strengths:** Full pipeline demonstrated from fresh clone: image analysis → validation (with retry attempts) → structured JSON output → risk scoring → escalation triggering (score 10.7 > threshold 10.0 with AI escalation note) → daily ranger briefing with 4 well-structured sections. Setup from scratch shown (venv, pip install, .env). Both escalation TRUE and FALSE cases demonstrated. Location engine with 7 segments and traffic multipliers shown in code. **Areas to improve for final demo:** (1) Ensure all hazard categories are in validator.py before demo (the "overgrown" category was added mid-demo). (2) Polish the risk engine — presenter noted it needs improvement. (3) Install all requirements before first run. (4) Show documentation deliverables on screen.

---

## Category Breakdown

### 1. End-to-End Demo Path (23/25)
- The core pipeline (analysis → validation → risk scoring → briefing) is architecturally sound.
- `analysis.py` works with Gemini 2.5 Flash and uses few-shot prompting with retry logic — well done.
- `risk_engine.py` implements deterministic scoring with CLI interface.
- `briefing_engine.py` generates daily ranger briefings from aggregated data.
- **Issue:** `summary_engine.py` has a fatal import bug (`get_segment_info` vs `get_segmentInfo`) — this module will crash at runtime.
- **Issue:** Timestamp format inconsistency between `validateschema.json` (expects "HH:MM AM/PM") and `risk_engine.py`/`briefing_engine.py` (parse `%Y-%m-%d %H:%M`). This likely breaks the pipeline at the risk scoring stage.
- README has clear run instructions, which is good.

### 2. Code Quality & Architecture (18/20)
- Clean separation of concerns across 6 modules.
- Pydantic-based validation with `HazardReportSchema` is a strong pattern.
- 7 location segments with traffic multipliers for Mustang Park is well thought out.
- Deterministic risk formula: `(avg_severity + volume_penalty) * traffic_multiplier` — appropriate separation from LLM reasoning.
- Escalation logic at score ≥ 10.0 with AI-generated explanation.
- Legacy `Trailguard/Test2.py` directory should be cleaned up.
- `frontview/` and `parkview/` are placeholder-only — unfinished UI components.

### 3. Documentation & Deliverables (20/25)
- `risk_scoring.md` — has formula, worked example, variable definitions, escalation threshold. ✓
- `report_schema.md` — has JSON schema, required fields, valid/invalid examples. ✓
- `evaluation_test_cases.md` — 20 test cases with hazard type, risk range, segment. ✓
- `evaluation_results.md` — claims 100% pass rate on all 20 cases with no failure analysis or methodology notes. The milestone instructions say "Do not report perfect metrics unless you can show how they were measured." This is a concern.
- **Missing:** `.env.example` — required by Milestone 2 deliverable #7.
- **Issue:** PRD is a PDF (`PRD.pdf`), not the required `PRD.md`.
- **Issue:** `Pilot Scope.md` has a space in the filename — requirement says `pilot_scope.md`.
- No escalation test cases documented in evaluation.

### 4. Data Contract & Schema (10/10)
- `report_schema.md` defines the JSON schema clearly.
- `validateschema.json` provides draft-07 JSON Schema.
- Allowed hazard categories defined (Park Infrastructure, Debris, Animal, Fire Hazard, Other).
- Minor inconsistency: validator allows "Other" but schema docs don't list it.

### 5. Evaluation Evidence (10/10)
- 20 test cases meet the requirement.
- 20 pilot photos present in `src/PilotPhotos/`.
- Results documented (though overly optimistic).

### 6. Repository Hygiene (10/10)
- `.gitignore` present.
- `requirements.txt` present.
- Clear project structure.
- README with setup/run instructions.

---

## Individual Grades

| Team Member | Commits | Contribution Area | Grade |
|---|---|---|---|
| collincan2 | 62 | Documentation, test cases, photos, risk scoring spec, schema work | 93/100 |
| AndCplusplus | 39 | Core code implementation (analysis, risk engine, summary, briefing, validator) | 95/100 |

**Note:** collincan2 and AndCplusplus led the development workload.

---

## Key Recommendations for Sprint 2
1. Fix the `summary_engine.py` import bug immediately (`get_segment_info` → `get_segmentInfo`).
2. Resolve timestamp format inconsistency across all modules.
3. Add `.env.example` file.
4. Convert PRD.pdf to PRD.md and fix pilot_scope filename.
5. Begin building the frontend dashboard (frontview/parkview are still placeholders).
6. Add escalation test scenarios to evaluation.
