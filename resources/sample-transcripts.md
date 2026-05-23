# Sample Transcripts

Five meeting transcripts that ship in the seed repo's `inbox/` folder. Each one is realistic to KSA business context and designed to surface a specific extraction challenge.

The facilitator pre-labels `sample-01` before the workshop — that label is the ground truth for Block 4's eval exercise.

---

## sample-01-mcit-licensing.txt

**Meeting context:** A technology company meets with representatives from the Ministry of Communications and Information Technology (MCIT) to discuss eligibility for the regulatory sandbox programme. The meeting is formal, conducted in the ministry's offices.

**Decisions and actions in this transcript:**

| # | Type | Content | Owner | Deadline |
|---|---|---|---|---|
| 1 | decision | Proceed with regulatory sandbox application | Mohammed | 2026-05-31 |
| 2 | pending_decision | Full licensing approval | MCIT committee | TBD |
| 3 | action_item | Submit technical documentation to MCIT portal | Mohammed | 2026-05-31 |
| 4 | action_item | Legal team to review data localisation clauses | [UNCLEAR-OWNER] | 2026-06-07 |

**Extraction challenges:**
- Decision-maker for item 2 is "the committee" — unnamed, role-based → [UNCLEAR-OWNER] or function name
- Item 2 is conditional ("pending CITC sign-off") → must be `pending_decision`, not `decision`
- Item 4 owner is "the legal team" — a function, not a named person
- One deadline is stated as a date; one is relative to an end-of-month reference

This is the transcript the facilitator pre-labels for Block 4. Attendees compare their tool's output to this table.

---

## sample-02-aramco-pilot.txt

**Meeting context:** A software vendor meets with Aramco Digital to discuss expanding a current pilot from 2 sites to 3 sites, with a full rollout contingent on pilot results. The meeting is semi-formal, in a hybrid format.

**Decisions and actions in this transcript:**

| # | Type | Content | Owner | Deadline |
|---|---|---|---|---|
| 1 | pending_decision | 3-site pilot expansion approved in principle | CFO (unnamed) | TBD |
| 2 | action_item | Send updated SLA to procurement | Omar | 2026-06-01 |
| 3 | action_item | Technical integration plan from vendor side | [UNCLEAR-OWNER] | 2026-06-15 |
| 4 | action_item | Internal compliance review on data handling | Aramco security team | TBD |

**Extraction challenges:**
- Item 1 is "approved in principle pending CFO sign-off" → must be `pending_decision`
- Item 3 owner is "the technical team" on the vendor side — present in the meeting but unnamed
- Full rollout timeline (Q1 2027) is mentioned but is not a decision — it's a planning horizon

---

## sample-03-sama-partnership.txt

**Meeting context:** A fintech company in discussions with a SAMA-regulated bank about a payment processing partnership. Compliance and Islamic finance constraints are discussed explicitly.

**Decisions and actions in this transcript:**

| # | Type | Content | Owner | Deadline |
|---|---|---|---|---|
| 1 | decision | Proceed with T+2 settlement model (Murabaha structure) | Joint agreement | 2026-05-28 |
| 2 | pending_decision | Final partnership MOU signature | Legal (both parties) | TBD |
| 3 | action_item | Bank to complete internal compliance review | Bank compliance officer | After Eid Al-Adha → 2026-06-06 (approx) |
| 4 | action_item | Fintech to provide sandbox environment access | Tariq | 2026-06-10 |

**Extraction challenges:**
- Item 3 deadline is "after Eid Al-Adha" — must be converted to approximate Gregorian date
- Item 3 owner is the bank's compliance officer, who was not present in the meeting
- Murabaha (an Islamic finance structure that avoids interest) appears in item 1 — the tool doesn't need to understand Islamic finance, but should not strip the term from the record

---

## sample-04-ops-plan-2027.txt

**Meeting context:** Annual operational planning session for a regional technology company. Leadership team of six people. Multiple tracks discussed: hiring, budget, office expansion, vendor partnerships, product roadmap.

**Decisions and actions in this transcript:**

| # | Type | Content | Owner | Deadline |
|---|---|---|---|---|
| 1 | decision | Increase marketing budget by 30% for H2 2026 | CFO (Fatima) | 2026-07-01 |
| 2 | decision | Hire 3 engineers in Q3 2026 | VP Engineering (Khalid) | 2026-09-30 |
| 3 | decision | Defer Jeddah office expansion to 2028 | CEO | N/A |
| 4 | pending_decision | Strategic vendor partnership with Elm | Board approval needed | TBD |
| 5 | action_item | Submit hiring plan to HR | Ahmed | 2026-06-15 |
| 6 | action_item | Prepare revised budget model for board | Fatima | 2026-06-20 |
| 7 | action_item | Shortlist three engineering candidates | Khalid | 2026-07-15 |
| 8 | action_item | Draft Elm partnership proposal | Omar | 2026-06-30 |
| 9 | action_item | Research Jeddah co-working options for interim use | Reem | TBD |

**Extraction challenges:**
- Richest file — 4 decisions + 5 action items with named owners and deadlines
- Item 3 is a deferral, not a traditional decision — still should be captured as a decision
- Item 4 is conditional on board approval → `pending_decision`
- Jeddah office discussion generates both a decision (item 3) and an action item (item 9)
- Multiple owners across all items — tests whether the tool captures each correctly

**This is the test transcript for Stub A (action items).** v0.1 produces 4 decisions and 0 action items. After Stub A is implemented, the tool should produce 4 decisions and 5+ action items.

---

## sample-05-career-promotion.txt

**Meeting context:** A one-on-one conversation between a manager and Nora, a senior associate, about her career path and readiness for promotion. The conversation is candid — not a formal decision-making session.

**Decisions and actions in this transcript:**

| # | Type | Content | Owner | Deadline |
|---|---|---|---|---|
| — | — | *No formal decisions made in this meeting* | — | — |
| 1 | action_item | Manager to submit promotion assessment to HR | Manager | 2026-06-30 |
| 2 | action_item | Nora to present to leadership team as stretch assignment | Nora | 2026-09-15 |

**Extraction challenges:**
- Zero formal decisions — the tool must output an empty decisions list and note "no formal decisions recorded" rather than inventing decisions
- This transcript should trigger the [CONFIDENTIAL] tag (if Stub C is implemented)
- Reports should surface action items and owners only — no discussion content
- The performance discussion content (feedback given, career concerns raised) must NOT appear in any report

**This is the test transcript for Stub C (confidential handling).** With v0.1, the report may include sensitive discussion content. After Stub C is implemented, only the two action items appear in reports — no other content.

---

## Notes for facilitators

The transcripts are fictional but realistic. Names, organisations, and business contexts are representative of KSA corporate life without being drawn from any real situation.

You can replace the sample transcripts with real transcripts from your organisation — with appropriate anonymisation. If you do, update the pre-labelled ground truth for sample-01 to match your actual content. The eval exercise in Block 4 depends on that label being accurate.

[← Back to home](../index.html)
