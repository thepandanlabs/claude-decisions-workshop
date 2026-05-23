# The Seed Repository

The seed is the starting point every attendee clones before the workshop. It ships with a working v0.1 of the `decisions` tool and everything you need to build on it.

The seed lives in the `seed/` subfolder of this workshop repo — attendees clone one repo and navigate into `seed/`. No separate clone needed.

## What's in it

```
decisions-seed-repo/
├── PRD.md                          # one-page spec, with five stub sections
├── CLAUDE.md                       # extraction rules and conventions
├── README.md                       # quick-start guide
├── pyproject.toml                  # Python package config
├── .claude/
│   └── commands/
│       ├── prime.md                # /prime — read and confirm the spec
│       ├── plan.md                 # /plan — produce a numbered plan
│       ├── implement.md            # /implement — execute the approved plan
│       └── verify.md               # /verify — run the verification checklist
├── inbox/
│   ├── sample-01-mcit-licensing.txt
│   ├── sample-02-aramco-pilot.txt
│   ├── sample-03-sama-partnership.txt
│   ├── sample-04-ops-plan-2027.txt
│   └── sample-05-career-promotion.txt
├── src/
│   └── decisions/
│       ├── cli.py                  # add, query, report subcommands
│       ├── ledger.py               # SQLite read/write, deduplication
│       ├── extract.py              # Claude API call, structured extraction
│       └── report.py              # weekly briefing generator
├── migrations/
│   └── 0001_init.sql               # database schema — run at startup
└── tests/
    ├── conftest.py                 # test setup, API fixtures
    ├── test_idempotent.py          # confirms double-add produces zero new records
    └── test_schema.py              # confirms extraction output has all required fields
```

## v0.1 — what's implemented

The working baseline that ships in the repo:

- `decisions add <folder>` — processes `.txt` transcript files, extracts decisions (not yet action items), writes to `decisions.db`. Skips files already processed.
- `decisions list` — shows all records in the ledger.
- `decisions query --owner <name>` — filters by the named owner.
- `decisions report --week YYYY-Www` — generates a markdown weekly briefing.

**What v0.1 does NOT do** (the stub sections):
- Extract action items (Stub A)
- Tag government entity meetings [GOV] (Stub B)
- Handle confidential conversations separately (Stub C)
- Convert Islamic calendar deadlines to Gregorian dates (Stub D)
- Distinguish pending decisions from confirmed decisions (Stub E)

## The five stub sections in PRD.md

Each stub is a commented block in `PRD.md` that describes a gap in v0.1, explains what needs to be added, and tells you which sample transcript to use to verify the enhancement. In Block 3, attendees pick one stub, write its spec text, update the CLAUDE.md extraction rule, and build the enhancement.

Example (Stub A):

```
<!-- STUB A — Action items
Currently: the tool only extracts decisions (type: decision).
Missing: action items — commitments made by a named person to do something by a deadline.

Add the following to this PRD section:
- Define action_item as a second record type alongside decision.
- Fields: content, owner (name as spoken), deadline (YYYY-MM-DD or "TBD").
- If deadline is implied but not stated explicitly, write "TBD".
- If only a function is named ("legal team"), use that and flag [UNCLEAR-OWNER].

Also add to CLAUDE.md extraction rules:
- Extract action items alongside decisions. An action item is a commitment
  made by a named person (or function) to do something by a deadline.

Test: decisions add inbox/sample-04-ops-plan-2027.txt
      Before: 4 decisions, 0 action items
      After:  4 decisions, 6 action items — Ahmed's hiring proposal appears
              with owner: Ahmed and a deadline.
-->
```

## The five sample transcripts

Five realistic KSA-context meeting transcripts. Each one surfaces different extraction challenges.

| File | Meeting context | Key extraction challenge |
|---|---|---|
| `sample-01-mcit-licensing.txt` | MCIT regulatory sandbox licensing discussion | Unnamed decision-maker ("the committee"), Islamic calendar deadline, conditional approval |
| `sample-02-aramco-pilot.txt` | Aramco Digital pilot expansion | "In principle" approval = `pending_decision`, ambiguous owner "the technical team" |
| `sample-03-sama-partnership.txt` | SAMA-regulated fintech partnership | Islamic finance constraint, deadline "after Eid Al-Adha", absent owner |
| `sample-04-ops-plan-2027.txt` | Annual operational planning, leadership team | Richest file: 4 decisions, 6 action items, 1 deferral, unclear budget owner |
| `sample-05-career-promotion.txt` | Career path conversation, manager and Nora | Zero formal decisions (graceful handling), 2 action items, [CONFIDENTIAL] required |

`sample-05` is specifically designed to test graceful handling of a "no decisions" meeting. The tool must output an empty list — not invent decisions.

## Running v0.1

After cloning:

```bash
cd decisions-seed-repo
uv tool install --editable .   # installs the decisions command
decisions --help
decisions add inbox/
```

Expected output on the five sample transcripts:

```
Processing 5 transcripts...
✓ sample-01-mcit-licensing.txt    3 decisions  0 action items
✓ sample-02-aramco-pilot.txt      1 decision   0 action items
✓ sample-03-sama-partnership.txt  2 decisions  0 action items
✓ sample-04-ops-plan-2027.txt     4 decisions  0 action items
✓ sample-05-career-promotion.txt  0 decisions  0 action items
────────────────────────────────────────────────────────────
10 decisions  0 action items  written to decisions.db
```

*(Action items are the 0s — that's what Stub A adds.)*

Run it again:

```
0 new records. 5 files skipped (already processed).
```

Deduplication works. That's the idempotency moment — the same result, every time, however many times you run it.

[← Back to home](../index.html)
