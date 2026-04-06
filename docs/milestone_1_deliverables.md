# Milestone 1 Deliverables  
## Team: Trail Guard  
### Focus: Single-Park Pilot + Intelligent Incident Reasoning System  

---

# Pilot Scope (Required)

You must focus on **one park as a pilot example**.

Create:

/docs/pilot_scope.md

Include:
- Park name
- 6–12 trail segments (simple map or description)
- Sensitive zones (entrance, bridges, steep slopes, water crossings)
- Assumptions about ranger workflow

Milestone 1 is a pilot intelligence system for this park only.

---

# Milestone 1 Objective

By Milestone 1, your system must demonstrate:

- Structured hazard extraction from image (+ optional text)
- Location-aware risk scoring
- Multi-report aggregation
- Escalation logic
- AI-generated ranger summary
- Risk explanation layer
- Output validation
- Structured evaluation dataset
- Clean GitHub structure + walkthrough video

This is no longer just an image classifier.

---

# 1. Hazard Extraction (AI Perception Layer)

Input:
- Image
- Optional short description
- Trail segment ID
- Timestamp

Output (strict JSON):

- hazard_category (predefined set)
- severity (1–5)
- recommended_action
- confidence (optional)

Implement:
/src/analysis.py

---

# 2. JSON Validation Layer (Required)

Implement:
/src/validator.py

Must validate:
- hazard_category in allowed set
- severity integer 1–5
- required fields present
- action plan not empty

If invalid → regenerate or flag.

---

# 3. Location-Aware Risk Scoring (Deterministic)

Implement:
/src/location_engine.py  
/ src/risk_engine.py

Define and document in:

/docs/risk_scoring.md

Example structure:

Risk Score =
(Severity × SeverityWeight)
+ FrequencyModifier
+ LocationSensitivityModifier
+ RecencyModifier

LocationSensitivityModifier examples:
- Entrance zone → +2
- Bridge / slope → +1.5
- Low traffic zone → +0.5

Must compute:
- Incident-level risk
- Segment-level aggregated risk

---

# 4. Multi-Report Aggregation & Escalation (LLM + Deterministic)

Your system must:

- Track reports per segment
- Escalate when threshold exceeded (e.g., 3+ reports in 48h)
- Compute cumulative risk per segment

Output example:

Segment: North Ridge  
Reports (48h): 4  
Risk Score: 14.2  
Escalated: TRUE  

---

# 5. LLM Multi-Report Reasoning (Smarter Layer)

Using grouped reports from same segment, LLM must:

- Identify patterns (e.g., erosion cluster)
- Summarize likely underlying cause
- Suggest operational recommendation

Example output:

“Multiple erosion-related incidents in North Ridge following rainfall suggest slope instability.”

This is reasoning beyond single-image classification.

Implement:
/src/summary_engine.py

---

# 6. Risk Explanation Layer (Explainable AI)

For each high-risk segment, LLM must generate:

- Why the segment is high priority
- Which factors contributed to risk score
- Which incidents influenced the escalation

Example:

“This segment is high priority because it has 3 severity-4 hazards in the past 24 hours and is located near the main entrance.”

---

# 7. Ranger Daily Briefing Generator (LLM)

System must generate:

- A daily summary of top 3 priority segments
- Major hazard categories observed
- Suggested operational focus areas

This must be based on aggregated data — not generic text.

---

# 8. Evaluation Starter Kit (Minimum 20 Reports)

Create:

/docs/evaluation_test_cases.md

Include:
- 20 structured reports (image + metadata)
- Expected hazard category (or acceptable range)
- Expected severity range
- Assigned segment
- Expected priority bucket
- Escalation scenario cases (at least 3)

Required metrics:
- JSON schema validity rate (should be 100% after validation)
- Classification consistency
- Risk scoring correctness
- Escalation trigger accuracy

---

# 9. Updated PRD-Lite (1–2 pages)

Must define:

> A single-park pilot intelligence system that prioritizes ranger response using structured hazard detection, deterministic risk scoring, and AI-driven multi-report reasoning.

Must include:
- Risk scoring formula
- Escalation logic
- Multi-report reasoning
- Ranger briefing component
- Acceptance criteria (testable)

---

# 10. Architecture Diagram

Create:

/docs/architecture.png

Must show:

Image + Metadata Input  
→ LLM Hazard Extraction  
→ JSON Validation  
→ Location Mapping  
→ Risk Engine  
→ Aggregation  
→ LLM Summary & Explanation  
→ Prioritized Output  

Clearly label deterministic vs generative components.

---

# 11. Technical Walkthrough Video (5–8 minutes)

Must demonstrate:

- Pilot segmentation file
- Single report processing
- Validator running
- Risk score calculation
- Aggregation across multiple reports
- Escalation trigger
- Generated ranger summary

UI polish not required.

---

# 12. GitHub Repository Requirements

Must include:

/docs/PRD.md  
/docs/pilot_scope.md  
/docs/report_schema.md  
/docs/risk_scoring.md  
/docs/spike_results.md  
/docs/evaluation_test_cases.md  
/docs/architecture.png  

/src/analysis.py  
/src/validator.py  
/src/location_engine.py  
/src/risk_engine.py  
/src/summary_engine.py  

Plus:
- Updated README
- requirements.txt
- .env.example
- Meaningful commits per member
- Issue board with owners

---

# Required Live Demo for Milestone 1

You must demonstrate:

1. Report ingestion (image + metadata)
2. Structured hazard output
3. Validator pass
4. Risk score calculation
5. Segment aggregation
6. Escalation case
7. AI-generated ranger daily briefing

---

# Milestone 1 Standard

Your system must evolve from:

“We classify hazards from images.”

To:

“We engineered a single-park pilot incident intelligence system with validation, location-aware risk scoring, aggregation, multi-report reasoning, and AI-generated operational briefings.”
