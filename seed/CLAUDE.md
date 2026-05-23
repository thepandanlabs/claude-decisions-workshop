# CLAUDE.md — decisions CLI

## What this is

A local Python CLI that reads meeting transcripts from a folder, extracts decisions and action items via the Claude API, and maintains a SQLite ledger. See PRD.md for the full spec — read it before planning.

## Stack

- Python 3.11+
- Click for the CLI interface (handles subcommands and flags)
- SQLite via the stdlib `sqlite3` module (no ORM — no extra database library)
- `anthropic` Python SDK for extraction
- `pytest` for tests
- `uv` for dependency management

## Layout

- `src/decisions/cli.py`     — Click entry points (add, query, report)
- `src/decisions/ledger.py`  — SQLite read/write, deduplication
- `src/decisions/extract.py` — Claude API call, structured extraction
- `src/decisions/report.py`  — weekly briefing generator
- `migrations/`              — database schema, applied at startup
- `tests/`                   — pytest suite
- `inbox/`                   — sample transcripts shipped with the repo

## Extraction rules

These rules tell Claude what to extract from each transcript, and how.
Write them in plain English — you don't need to know Python to own this section.
If the tool gets something wrong, the fix belongs here, not in the prompt.

One rule is pre-written as an example of the format:

- **Capture WHO committed, not just what was committed.** If the owner
  is unnamed, use the function or role ("legal team") and flag [UNCLEAR-OWNER].

---

_Add your rules below. Each rule should answer: in what situation does this
apply, and what should Claude do?_

<!--
Rules to consider writing during the workshop (Block 2 exercise):
  - How should conditional approvals be handled?
  - What makes a meeting "government" and what should happen to those records?
  - What if a deadline is given in the Islamic calendar?
  - What should happen to career or performance conversations?
  - What if a meeting has no decisions at all?
-->

## Conventions

- Data output to stdout. Logs and errors to stderr.
- Exit code 0 on success. Exit code 1 on any error.
- Deduplication: SHA-256 hash of the source file bytes. Same file processed twice = zero new records the second time.
- Never call Claude inside a test. Tests use recorded fixtures.

## Determinism

Sort output by `(date ASC, source_file ASC)`. No timestamps in output. The report command must produce identical output for identical ledger state.

## When you change behaviour, also update

- `PRD.md` acceptance criteria, if scope shifted
- `README.md` usage section
- Any relevant test if the output format changed

## What to ask me about — never assume

- New dependencies
- Database schema changes
- Changes to the extraction output format
- Anything that would change what existing records look like
