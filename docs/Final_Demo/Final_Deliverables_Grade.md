# Final Deliverables Grade, Venture 8: TrailGuard

**Graded:** May 12, 2026
**Deadline:** May 3, 2026 (end of day)
**Final Demo:** April 29, 2026

---

## Overall Grade: 95/100

---

## Required Deliverables

The final-deliverables rubric expects four artifacts under `docs/Final_Demo/`: slides, demo video, runbook, and final code on `main`.

| Deliverable | Status | Location |
|---|---|---|
| Slides | **broken on `main`** | `docs/Final_Demo/Trail Guard.pdf` is a 2-byte file containing only `\r\n` |
| Demo video | landed | `docs/Final_Demo/FinalDemo.mp4` (9.7 MB) |
| Runbook | not in repo | (no `Runbook.md` in `docs/Final_Demo/`; an empty `fill.txt` placeholder is present) |
| Final code on `main` | landed | deterministic risk scoring, escalation, briefing, Streamlit dashboard, schema-aligned validator |

---

## Deduction

**−5: Slides broken on `main`.** Commit `de24467` (May 3 17:10) was titled "Rename docs/Trail Guard.pdf to docs/Final_Demo/Trail Guard.pdf", but the operation landed a 2-byte file containing only a CRLF newline. The real 5.4 MB version uploaded April 25 (commit `484b946`) is in git history but no longer in HEAD. Likely cause: the GitHub web UI was used to upload an empty placeholder over the real file.

To fix, recover the working version from history:

```
git show "484b946:docs/Trail Guard.pdf" > "docs/Final_Demo/Trail Guard.pdf"
git add "docs/Final_Demo/Trail Guard.pdf"
git commit -m "Restore Trail Guard.pdf from 484b946"
git push
```

Or re-upload the PDF from your local copy.

---

## Notes

`docs/Final_Demo/fill.txt` (1 byte) is a leftover placeholder. Worth removing on the same push that restores the slides.

A `Runbook.md` is not in the repo. For this grading pass only the broken-slides line item was scored as a deduction. A short `docs/Final_Demo/Runbook.md` (install, env vars, dashboard pages, smoke test) would close the remaining gap.

The video and final code are present, and the live demo went well. The slide-deck recovery is a five-minute fix once you have access.
