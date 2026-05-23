# Bad vs Good Prompts

The emotional anchor of the workshop. Same task, two prompts, audibly different outcomes.

---

## ❌ The bad prompt

Run this in a fresh Claude.ai session (the chat web interface) with no context:

```text
build me a decisions tracker for my meeting transcripts
```

### What you'll see Claude do

- Invent a schema (the blueprint defining what fields a record contains). Plausible fields — date, decision, owner — but no knowledge of your entity types, your confidentiality rules, or what "pending CFO sign-off" means in your organisation.
- Produce something. It may even run on one transcript.
- Have no memory of the conversation when you close the tab. No ledger. No deduplication. No way to query across meetings.

The output will look reasonable. It is not a tool — it's a one-time answer. **You cannot tell what's missing because you never said what you needed.**

---

## ✅ The good prompt

Run this in the seed repo with `PRD.md` and `CLAUDE.md` present, with Plan Mode on (Shift+Tab twice):

```text
Read PRD.md and CLAUDE.md. Then plan the minimum implementation that
satisfies the v0.1 acceptance criteria. Do not write code in this turn.
Produce a numbered plan listing the files you will create or modify,
in the order you will modify them, and what you will verify after each
step. Stop after the plan and wait for my approval.
```

### What you'll see Claude do

- Read `PRD.md`. Read `CLAUDE.md`. Reference both in the plan.
- Produce a 6–8 step plan, in order:
  1. Apply `migrations/0001_init.sql` to create `decisions.db` with the correct schema.
  2. Implement `extract.py` with the extraction schema from PRD.md, including the deduplication hash.
  3. Record test fixtures — saved API responses for the sample transcripts.
  4. Implement `ledger.py` — SHA-256 keyed idempotent insert (insert only if file hash not already in ledger).
  5. Implement `cli.py` `add` subcommand. Verify with the idempotency test.
  6. Implement `report.py` weekly briefing generator.
  7. Implement `cli.py` `query` and `report` subcommands. Run full test suite.
  8. Confirm all acceptance criteria from PRD.md pass.
- Stop. Wait for your approval.

*(The individual steps look technical — that's the point. The plan is Claude's breakdown of what it intends to build. You don't need to understand every line to review it; you need to spot anything that's missing, in the wrong order, or wasn't in the PRD.)*

Nothing is written to disk yet. You have a plan you can read, edit, and approve before anything is built.

---

## What changed between the two prompts

Not the prompt engineering — the good prompt is *shorter*. The difference is:

| Surface | Bad prompt | Good prompt |
|---|---|---|
| Project context | None | `PRD.md` + `CLAUDE.md` |
| Mode | Default (writes immediately) | Plan Mode (read-only) |
| Output shape | "A decisions tracker" | "A numbered plan with verification steps" |
| Reversibility | Code is written; you read diffs | Plan is text; you read text |
| Persistence | Forgotten when tab closes | Rules live in files; re-read every turn |

**The good prompt can be short because the structure carries the load.** The PRD says what to build. The CLAUDE.md says how it should behave. The good prompt just asks Claude to read those files and plan from them.

---

## Why this lands harder than reading about it

When you read this page, it's a tidy comparison. When you watch it live, you watch Claude *struggle visibly* with the bad prompt — asking clarifying questions, making arbitrary choices, producing something generic. That visible struggle is the part that sticks.

If you're facilitating this workshop yourself: don't skip the live run. Don't fast-forward through the bad prompt. The moment while Claude is deciding which fields to include — with no guidance from you — is the lesson.

[← Back to home](../index.html)
