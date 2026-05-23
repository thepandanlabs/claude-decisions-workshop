# Block 2 — Structured Intent

**Time:** 00:20 – 00:40
**Goal:** Everyone has read the PRD, understood the CLAUDE.md extraction rules, and knows what the four slash commands do. No tool has been run yet except to verify setup.

## What happens in this block

1. **00:20 – 00:28 — Walk the PRD aloud.** Section by section. Pause at the stub sections. Tell the room: "These are the gaps you'll fill in Block 3."
2. **00:28 – 00:35 — Walk the CLAUDE.md aloud.** Focus on the extraction rules — the section most managers will want to edit. Establish the rule: **"If removing a line wouldn't cause a mistake, cut it."**
3. **00:35 – 00:38 — Tour the slash commands.** Four commands, one sentence each.
4. **00:38 – 00:40 — Q&A.** Three questions maximum. Park anything bigger to Block 6.

## The PRD in 60 seconds

Open `PRD.md` in the seed repo. Read it aloud — it's short by design.

The PRD says: a CLI called `decisions` that takes a folder of meeting transcripts, calls Claude to extract decisions and action items, appends them to a SQLite database (a lightweight database that lives as a single file on your machine — no server needed), skips transcripts it has already processed (deduplication — no double-counting), and generates weekly briefing reports.

Three commands: `add`, `query`, `report`. Out of scope: login systems, email sending (that's Track A), Arabic transcript support (Track B), Slack integration (Track C), Claude Desktop connection (Track D).

### The stub sections

The PRD ships with five clearly marked gaps. Point them out:

> *"See these `[STUB]` sections? v0.1 doesn't do these things yet. In Block 3, you'll pick one, write the spec for it, and build it. Each one is 30–40 minutes. You're not starting from scratch — you're extending a working tool."*

The five stubs:
- **Stub A — Action items.** v0.1 only extracts decisions. Action items with owners and deadlines are missing entirely.
- **Stub B — Government tagging.** No way to mark or filter government-entity meetings separately.
- **Stub C — Confidential handling.** Career and performance transcripts currently leak their content into reports.
- **Stub D — Islamic calendar conversion.** Deadlines like "after Eid Al-Adha" are stored verbatim — not sortable or queryable.
- **Stub E — Pending decisions.** Conditional approvals ("pending CFO sign-off") are mis-labelled as decisions.

### The acceptance criteria

Five lines. All testable without code knowledge:

- `decisions add inbox/` on the five sample transcripts produces records in the ledger.
- Re-running it adds zero new records and reports five files skipped.
- `decisions query --owner "Ahmed"` returns only items where Ahmed is named.
- `decisions report --week 2026-W21` produces a markdown briefing.
- The chosen stub: its gap is closed and verifiable on the relevant sample transcript.

## The CLAUDE.md in 60 seconds

Open `CLAUDE.md`. Read it. That's the brief.

Point out two things specifically:

**1. The extraction rules section.** This is the part that's written in plain English. Not Python, not code — business rules that any manager can understand, edit, and own:

```
- Capture WHO decided, not just what was decided.
  If owner is unclear, use the function name and flag [UNCLEAR-OWNER].
- Conditional approvals ("pending CFO", "subject to committee"):
  type pending_decision — not decision. Do not omit them.
- Career/performance conversations: tag [CONFIDENTIAL].
  Reports: show action items and owners only. No decision content.
- Zero decisions in a meeting: output an empty list.
  Note "no formal decisions recorded." Never invent decisions.
```

> *"You can edit this file. If you find a rule that's wrong for your organisation, change it. That change will affect every future extraction — not just the next one. This is why the CLAUDE.md is yours, not Claude's."*

**2. The "what to ask me about" section.** Claude will not change the database schema, add a new dependency, or change how output is formatted — without asking first. This is the stop-and-confirm discipline that prevents Claude from going rogue mid-build.

## The four slash commands

Slash commands (commands that start with `/`) are reusable prompts that live in `.claude/commands/` as plain text files. Type one in the Claude Code session and it runs. Four ship with the seed repo:

| Command | What it does |
|---|---|
| `/prime` | Reads `PRD.md` and `CLAUDE.md` and confirms what it understood. If the readback is wrong, fix the file — not the prompt. |
| `/plan` | Produces a written, numbered plan. Does not write code. Stops and waits for your approval. |
| `/implement` | Executes the approved plan, step by step. |
| `/verify` | Runs the verification checklist on the relevant transcript and reports gaps. |

## Common questions in this block

- **"Can I change the PRD before we start?"** Yes — that's the point. The PRD is yours. But make deliberate changes, not impulsive ones. Every change to the PRD changes what gets built.
- **"What if I want to track something the PRD doesn't cover?"** That's a stub. Add it. The discipline is: write it down before you ask Claude to build it.
- **"Who writes the CLAUDE.md for my real project?"** You do. Start with this template. After a week of use, prune anything that turned out to be obvious. Add anything Claude kept getting wrong. It should be under 100 lines — a memo, not a manual.

[← Back to home](../index.html)
