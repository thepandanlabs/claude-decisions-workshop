# CLAUDE.md Template

This is the `CLAUDE.md` that ships with the seed repo. Under 80 lines. That's the brief.

The discipline: **if removing a line wouldn't cause a mistake, cut it.** Claude re-reads this file at the start of every turn, alongside your message and any files it has opened. But reading something is not the same as reliably following it. The more lines you write, the more the rules that matter compete with padding that doesn't. A focused 80-line CLAUDE.md gets followed. A sprawling 400-line CLAUDE.md gets skimmed.

---

```markdown
# CLAUDE.md — decisions CLI

## What this is
A local Python CLI that reads meeting transcripts from a folder,
extracts decisions and action items via the Claude API, and maintains
a SQLite ledger. See PRD.md for the full spec — read it before planning.

## Stack
- Python 3.11+
- Click for the CLI interface (handles subcommands and flags)
- SQLite via the stdlib sqlite3 module (no ORM — no extra database library)
- anthropic Python SDK for extraction
- pytest for tests
- uv for dependency management

## Layout
- src/decisions/cli.py      — Click entry points (add, query, report)
- src/decisions/ledger.py   — SQLite read/write, deduplication
- src/decisions/extract.py  — Claude API call, structured extraction
- src/decisions/report.py   — weekly briefing generator
- migrations/               — database schema, applied at startup
- tests/                    — pytest suite
- inbox/                    — sample transcripts shipped with the repo

## Extraction rules
These rules determine what the tool extracts from each transcript.
Edit them when the tool gets something wrong or misses something.

- Capture WHO decided or committed, not just what was decided.
  If owner is unclear, use the function name and flag [UNCLEAR-OWNER].
- Conditional approvals ("pending CFO sign-off", "subject to committee"):
  type pending_decision — not decision. Do not omit them.
- Government entity meetings (any transcript naming a ministry,
  authority, or regulator): tag [GOV] on every extracted record.
- Islamic calendar deadlines ("after Eid", "before Ramadan"):
  convert to an approximate Gregorian date and note the original phrasing.
  Example: "before Ramadan" → deadline: 2027-02-17 (note: "before Ramadan")
- Career and performance conversations: tag [CONFIDENTIAL].
  In reports: surface action items and owners only. No decision content.
- If a meeting has zero decisions, output an empty list.
  Note: "no formal decisions recorded." Never invent decisions.

## Conventions
- Data output to stdout. Logs and errors to stderr.
- Exit code 0 on success. Exit code 1 on any error.
- Deduplication: sha256 hash of the source file path. Same file
  processed twice = zero new records the second time.
- Never call Claude inside a test. Tests use recorded fixtures.

## Determinism
Sort output by (date ASC, source_file ASC). No timestamps in output.
The report command must produce identical output for identical ledger state.

## When you change behaviour, also update
- PRD.md acceptance criteria, if scope shifted
- README.md usage section
- Any relevant test if the output format changed

## What to ask me about — never assume
- New dependencies
- Database schema changes
- Changes to the extraction output format
- Anything that would change what existing records look like
```

---

## Why each section earns its place

- **What this is.** Three sentences. Points at the PRD. Tells Claude where to start.
- **Stack.** Names the libraries so Claude doesn't invent a different one. Annotations remove jargon for anyone reading this file.
- **Layout.** Tells Claude where things go before it has to ask. Prevents "everything in one file."
- **Extraction rules.** The centrepiece for the decisions tool. Written in plain English — a manager can read, edit, and own these rules without knowing Python. This is where your domain expertise lives.
- **Conventions.** The smallest set of rules that prevent the most common mistakes.
- **Determinism.** Required for reliable verification — same ledger, same report.
- **When you change behaviour, also update.** The maintenance discipline. Without it, the PRD and the code diverge inside a week.
- **What to ask me about.** Forces a stop-and-confirm before structural changes.

## What's deliberately *not* in this file

- Long explanations of what Click or SQLite are. Claude knows.
- A description of every business meeting type you might encounter. Too much context crowds the rules that matter.
- Anything that should be in the PRD instead.
- Marketing language. It doesn't help Claude and it doesn't help you.

## Building your own

Start blank. Write only the rules that would prevent a specific mistake you'd otherwise expect Claude to make on day one. Focus the extraction rules section on what's specific to *your* domain — your entity types, your confidentiality rules, your deadline conventions.

After a week of use, prune anything that turned out to be obvious. Add anything Claude kept getting wrong. Keep it under 100 lines.

[← Back to home](../index.html)
