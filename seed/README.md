# decisions — seed repo

Starting point for the "From Meetings to Decisions" workshop. v0.1 ships working. You'll observe the gaps in Block 3 and implement one enhancement.

## Quick start

```bash
# Install (requires Python 3.11+ and uv)
uv tool install --editable .

# Process the sample transcripts
decisions add inbox/

# Query the ledger
decisions query --open
decisions query --owner "Ahmed"

# Generate a weekly briefing
decisions report --week 2026-W21
```

## What's in here

```
PRD.md          — the spec; read this first
CLAUDE.md       — extraction rules and conventions
inbox/          — 5 KSA meeting transcripts
src/decisions/  — the implementation (stubs — Claude builds this)
tests/          — pytest suite
.claude/        — /prime, /plan, /implement, /verify slash commands
```

## Before the workshop

```bash
git clone <url-from-facilitator>
cd decisions-seed-repo
uv tool install --editable .
decisions add inbox/
```

If `decisions add inbox/` prints output for 5 transcripts, you're ready.
