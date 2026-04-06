# Milestone 2 Deliverables
## Team: Trail Guard
### Focus: MVP Demo of a Reliable Single-Park Incident Intelligence System

---

# Milestone 2 Objective

One week from now, on **April 5, 2026**, you must demonstrate a working MVP for the same single-park pilot.

The standard is no longer "we have most of the pieces." The standard is:

> A teammate can run the repo, process multiple reports, produce segment priorities, trigger at least one escalation, and generate a daily ranger briefing from aggregated data.

Milestone 2 is about **reliability, completeness, and demo readiness**.

---

# MVP Definition

Your MVP must support this exact end-to-end workflow:

1. Ingest a report with:
   - image
   - optional user description
   - trail segment
   - timestamp
2. Generate structured hazard output.
3. Validate the output before saving.
4. Save reports in one consistent schema.
5. Aggregate reports by segment across time.
6. Compute deterministic risk scores with location sensitivity.
7. Trigger escalation when threshold conditions are met.
8. Generate:
   - a per-segment reasoning summary
   - a risk explanation for escalated segments
   - a daily briefing of the top 3 priority segments

If any step only works manually, inconsistently, or with undocumented assumptions, the MVP is not complete.

---

# Required Milestone 2 Deliverables

## 1. Reliable End-to-End Demo Path

You must provide a clean demo path that works from a fresh clone.

Required:
- Updated [README.md](/home/zcao/Projects/senior_project/trail-guard/README.md) with exact setup and run steps
- Correct file paths and command examples
- One consistent timestamp format used everywhere
- No broken imports or filename mismatches in the MVP path

Demo must show:
- one single-report flow
- one multi-report segment aggregation flow
- one escalation case
- one daily briefing output

---

## 2. Final MVP Code Components

The following files must exist and match the actual implementation:

- `/src/analysis.py`
- `/src/validator.py`
- `/src/location_engine.py`
- `/src/risk_engine.py`
- `/src/summary_engine.py`
- `/src/briefing_engine.py` or equivalent clearly named file for the daily briefing step

Required expectations:
- deterministic logic stays deterministic
- LLM output is used for reasoning/explanation/briefing, not for hidden scoring math
- all saved reports follow one schema

---

## 3. Fixed Data Contract

You must submit and use a single report schema.

Create:

`/docs/report_schema.md`

Include:
- final JSON schema
- allowed hazard categories
- required fields
- timestamp format
- one valid example report
- one invalid example report and why it fails

This schema must match the validator and the saved database format.

---

## 4. Updated Risk Scoring Spec

Update:

`/docs/risk_scoring.md`

Must include:
- final scoring formula
- meaning of each factor
- location sensitivity mapping
- escalation threshold
- one worked example from raw reports to final segment score
- explanation of how recency is handled

Your documentation must match the code exactly.

---

## 5. Daily Ranger Briefing

This is now required for MVP completion.

Your system must generate a daily briefing based on aggregated reports across all segments.

Output must include:
- top 3 priority segments
- main hazard categories observed
- why each top segment is prioritized
- suggested operational focus areas for the day

This must be generated from real current report data, not static text.

---

## 6. Evaluation Evidence

Update:

`/docs/evaluation_test_cases.md`

Must include:
- at least 20 test cases
- image reference
- input metadata
- expected hazard category or acceptable range
- expected severity range
- assigned segment
- expected escalation result when relevant

Also create:

`/docs/evaluation_results.md`

Include measured results for your MVP:
- JSON validity rate
- hazard classification consistency
- risk scoring correctness checks
- escalation trigger accuracy
- notes on failure cases

Do not report perfect metrics unless you can show how they were measured.

---

## 7. Pilot Scope And Repo Cleanup

Your repository must match the required structure and naming.

Required docs:
- `/docs/pilot_scope.md`
- `/docs/PRD.md`
- `/docs/report_schema.md`
- `/docs/risk_scoring.md`
- `/docs/evaluation_test_cases.md`
- `/docs/evaluation_results.md`
- `/docs/architecture.png`

Required repo support files:
- root `README.md`
- dependency file in the location referenced by the README
- `.env.example`

If you keep alternative filenames or PDFs, that is fine, but the required deliverable filenames must also exist.

---

# Required Live Demo For Milestone 2

You must demonstrate all of the following live:

1. Setup from documented instructions.
2. A report being analyzed and validated.
3. The saved JSON report.
4. Aggregation across multiple reports in one segment.
5. Deterministic risk score calculation.
6. One escalation trigger.
7. One risk explanation for a high-priority segment.
8. One daily ranger briefing across all segments.
9. A short explanation of what is deterministic versus generative in your architecture.

UI polish is still optional. Reliability is not optional.

---

# What Will Count As "Done"

Milestone 2 is complete only if:

- the MVP path runs without manual patching during the demo
- the repo filenames and docs match the actual implementation
- the team can justify why a segment is prioritized using code and data
- the daily briefing is generated from aggregated segment data
- at least one escalation case is demonstrated end to end

---

# Priority Guidance For This Week

Do these first:

1. Fix the timestamp and saved-schema inconsistency.
2. Fix the risk engine runtime issues and filename mismatches.
3. Implement the missing daily briefing path.
4. Make the README accurate enough for another teammate to run.
5. Produce measurable evaluation evidence.

Do not add new scope until those five are complete.
