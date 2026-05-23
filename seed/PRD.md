# decisions CLI — Product Requirements Document

## Problem

I attend 8–12 meetings a week across government entities, enterprise clients, banks, and internal teams. After each meeting, decisions and action items get distributed across chat threads, email follow-ups, and notes apps — and then lost. I want a CLI that reads transcript files from a folder, extracts decisions and action items via Claude, and keeps them in a queryable ledger that accumulates across weeks.

## Users

A single user, on their own laptop. No multi-tenant, no auth.

## In scope (v0.1)

1. `decisions add <folder>` — read every `.txt` file in the folder, call Claude to extract structured records, write to ledger, skip files already processed.
2. `decisions list` — print all records in the ledger to stdout, one per line.
3. `decisions query --owner <name>` — print records where owner matches name (case-insensitive substring match).
4. `decisions query --open` — print records with no `completed_date`.
5. `decisions query --tag <tag>` — print records with the specified tag (GOV, CONFIDENTIAL, UNCLEAR-OWNER).
6. `decisions report --week YYYY-Www` — print a markdown briefing for the specified ISO week: decisions made, action items by owner, pending decisions.
7. Idempotency: re-running `add` on the same folder produces zero new rows.

## Out of scope (v0.1)

- Auth, multi-user, cloud sync
- Image or audio transcription
- Real-time meeting capture
- Email sending (Track A extension)
- Drive/Notion integration (Track B extension)
- Slack integration (Track C extension)
- MCP server (Track D extension)

## Extracted record schema

Claude must return a JSON array. Each element is one of:

```json
{
  "type": "decision | action_item | pending_decision",
  "content": "string — what was decided or committed",
  "owner": "string — name as spoken, or function name if unnamed",
  "deadline": "YYYY-MM-DD | TBD | null",
  "tags": ["GOV", "CONFIDENTIAL", "UNCLEAR-OWNER"],
  "source_file": "string — filename",
  "meeting_date": "YYYY-MM-DD | null"
}
```

## Storage

SQLite at `~/.decisions/decisions.db`. Schema in `migrations/0001_init.sql`. Primary key = SHA-256 hash of source file bytes (deduplication key).

## Acceptance criteria

- [ ] `pytest tests/` is green
- [ ] `decisions add inbox/` on the five sample transcripts produces at least 10 decisions across the five files
- [ ] Re-running `decisions add inbox/` adds zero records and reports "5 files skipped (already processed)"
- [ ] `decisions query --owner "Ahmed" --open` returns records where owner contains "Ahmed"
- [ ] `decisions report --week 2026-W21` prints a structured markdown briefing
- [ ] `--help` is informative on every subcommand

---

<!-- STUB A — Action items

Currently: the tool only extracts records with type: decision. Action items
are silently ignored.

Missing: action_item as a second record type. An action item is a commitment
made by a named person (or function) to do something by a deadline.

Add to this PRD:
- Define action_item as a valid type alongside decision and pending_decision.
- Fields: content, owner (name as spoken), deadline (YYYY-MM-DD or "TBD").
- If deadline is implied but not explicitly stated, use "TBD".
- If only a function is named ("the legal team"), use that name and add
  [UNCLEAR-OWNER] to tags.

Also add to CLAUDE.md extraction rules:
- Extract action items alongside decisions. An action item is a commitment
  made by a named person (or function) to do something by a deadline.

Test: decisions add inbox/sample-04-ops-plan-2027.txt
      Before: 4 decisions, 0 action items
      After:  4 decisions, 6 action items — Ahmed's hiring proposal appears
              with owner: "Ahmed" and deadline: "2026-06-15"
-->

<!-- STUB B — Government entity tagging

Currently: no [GOV] tag is applied to any records.

Missing: detection of government entity meetings and tagging of all records
from those meetings with [GOV].

A "government entity meeting" is any transcript where the counterparty is a
ministry, authority, or regulator. Examples in the sample transcripts:
MCIT (Ministry of Communications and IT), SAMA (Saudi Arabian Monetary
Authority), CITC.

Add to this PRD:
- If a transcript is identified as a government entity meeting, tag ALL
  extracted records with [GOV].
- Identification rule: transcript text names a ministry, authority, or
  Saudi regulator as a participant or counterparty.

Also add to CLAUDE.md extraction rules:
- Government entity meetings: tag [GOV] on every extracted record.
  A meeting qualifies if the transcript names a ministry, authority,
  or Saudi regulator as a participant or counterparty.

Test: decisions add inbox/sample-01-mcit-licensing.txt
      After: all records have tags: ["GOV"]
-->

<!-- STUB C — Confidential handling

Currently: career and performance conversations are processed like any
other meeting. Discussion content appears in reports.

Missing: [CONFIDENTIAL] tag detection and report filtering.

A "confidential meeting" is any transcript covering career path,
performance review, or promotion discussions.

Add to this PRD:
- Tag [CONFIDENTIAL] on every record extracted from a confidential meeting.
- In reports: surface action items and owners only from confidential records.
  Never include decision content or discussion details.
- Zero-decision confidential meetings should still output action items.

Also add to CLAUDE.md extraction rules:
- Career and performance conversations: tag [CONFIDENTIAL].
  Reports: surface action items and owners only — no decision content,
  no discussion details.

Test: decisions add inbox/sample-05-career-promotion.txt
      Before: discussion content may appear in report
      After:  report shows only: "Manager → submit promotion assessment
              to HR (deadline: 2026-06-30)" and Nora's action item.
              No other content.
-->

<!-- STUB D — Islamic calendar deadline conversion

Currently: deadlines stated in Islamic calendar terms ("after Eid",
"before Ramadan") are stored verbatim — not queryable by date.

Missing: conversion of Islamic calendar references to approximate
Gregorian dates, with the original phrasing preserved.

Add to this PRD:
- Islamic calendar deadlines must be converted to an approximate Gregorian
  date. Store both: deadline: "2026-06-06", deadline_note: "after Eid Al-Adha".
- If the exact date cannot be determined, use a reasonable approximation
  and note uncertainty.

Also add to CLAUDE.md extraction rules:
- Islamic calendar deadlines ("after Eid", "before Ramadan"):
  convert to an approximate Gregorian date and note the original phrasing.
  Example: "after Eid Al-Adha" → deadline: "2026-06-06" (note: "after Eid Al-Adha")

Test: decisions add inbox/sample-03-sama-partnership.txt
      Before: deadline stored as "after Eid Al-Adha"
      After:  deadline: "2026-06-06", deadline_note: "after Eid Al-Adha"
-->

<!-- STUB E — Pending decisions

Currently: conditional approvals ("pending CFO sign-off", "approved in
principle") are labelled as decision — which they are not.

Missing: pending_decision as a distinct type for approvals that are
conditional on a future action.

Add to this PRD:
- pending_decision: a decision that has been agreed in principle but
  requires a further step (approval, signature, committee vote) before
  it is final.
- Conditions are commonly: "pending CFO sign-off", "subject to committee",
  "approved in principle", "awaiting board approval".
- pending_decision records must NOT be included in the "decisions made"
  section of reports — they belong in "pending" section only.

Also add to CLAUDE.md extraction rules:
- Conditional approvals ("pending CFO sign-off", "subject to committee",
  "approved in principle"): type pending_decision — not decision.
  Do not omit them; they are the highest-risk open items.

Test: decisions add inbox/sample-02-aramco-pilot.txt
      Before: item 1 labelled as decision
      After:  item 1 labelled as pending_decision, appears in "Pending
              decisions" section of report, not in "Decisions made"
-->
