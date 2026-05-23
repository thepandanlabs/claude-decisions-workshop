# Block 2 — Structured Intent

**Time:** 00:20 – 00:40
**Goal:** Everyone has read the PRD, and everyone has written at least one extraction rule in the CLAUDE.md. Not read it — written it. That shift from reader to author is the central beat of this block.

## What happens in this block

1. **00:20 – 00:28 — Walk the PRD aloud.** Section by section. Pause at the stubs.
2. **00:28 – 00:37 — Live rule-writing exercise.** Read one transcript excerpt aloud. Ask the room what rule is missing. They dictate it. You type it into `CLAUDE.md`. Five minutes. Two or three rules.
3. **00:37 – 00:39 — Tour the slash commands.** Four commands, one sentence each.
4. **00:39 – 00:40 — Q&A.** Three questions maximum. Park the rest to Block 6.

---

## The PRD in 60 seconds (00:20 – 00:28)

Open `PRD.md` in the seed repo. Read it aloud — it's short by design.

The PRD says: a CLI called `decisions` that takes a folder of meeting transcripts, calls Claude to extract decisions and action items, appends them to a SQLite database (a lightweight database that lives as a single file on your machine — no server needed), skips transcripts it has already processed (deduplication — no double-counting), and generates weekly briefing reports.

Three commands: `add`, `query`, `report`. Out of scope: login systems, email sending (Track A), Arabic transcript support (Track B), Slack integration (Track C), Claude Desktop connection (Track D).

### The stub sections

The PRD ships with five clearly marked gaps. Point them out:

> *"See these stub sections? v0.1 doesn't do these things yet. In Block 3, you'll pick one, write the spec for it, and build it. Each one is 30–40 minutes. You're not starting from scratch — you're extending a working tool."*

The five stubs:
- **Stub A — Action items.** v0.1 only extracts decisions. Action items with owners and deadlines are missing entirely.
- **Stub B — Government tagging.** No way to mark or filter government-entity meetings separately.
- **Stub C — Confidential handling.** Career and performance transcripts currently leak content into reports.
- **Stub D — Islamic calendar conversion.** Deadlines like "after Eid Al-Adha" are stored verbatim — not sortable or queryable.
- **Stub E — Pending decisions.** Conditional approvals ("pending CFO sign-off") are mis-labelled as confirmed decisions.

### Acceptance criteria

Five lines. All testable without code knowledge:

- `decisions add inbox/` on the five sample transcripts produces records in the ledger.
- Re-running it adds zero new records and reports five files skipped.
- `decisions query --owner "Ahmed"` returns only items where Ahmed is named.
- `decisions report --week 2026-W21` produces a markdown briefing.
- The chosen stub: its gap is closed and verifiable on the relevant sample transcript.

---

## Live rule-writing exercise (00:28 – 00:37)

This is the block's central moment. Do not skip it or convert it to a readthrough.

**What the seed CLAUDE.md ships with:** the Stack, Layout, Conventions, and Determinism sections filled in. The Extraction rules section has one pre-written example rule — showing the format — and a blank space below it.

**The exercise:**

Open `CLAUDE.md` in the editor (or project it on screen). Read the example rule aloud:

> *"Capture WHO committed, not just what was committed. If the owner is unnamed, use the function or role and flag [UNCLEAR-OWNER]."*

Then read this excerpt from `sample-01-mcit-licensing.txt` aloud:

> *"The committee will need to sign off on the full licence before anything proceeds. No date was given for that."*

Ask the room:

> *"Based on what you just heard — what rule is missing? What should the tool do with this?"*

Wait. Someone will say: *"It should mark that as 'pending', not a done decision."*

Type the rule into `CLAUDE.md`, in the room, as they dictate it. Roughly:

```
- Conditional approvals ("pending sign-off", "subject to committee",
  "approved in principle"): type pending_decision — not decision.
  Do not omit them; they are the highest-risk open items.
```

Then read the excerpt from `sample-05-career-promotion.txt`:

> *"Nora's performance feedback, the salary band discussion, the concerns the manager raised — none of that should show up in the weekly briefing."*

Ask again:

> *"What rule covers this?"*

They'll get it: confidentiality. Type the rule they give you. Approximately:

```
- Career and performance conversations: tag [CONFIDENTIAL].
  Reports: show action items and owners only. No discussion content.
```

Stop after two or three rules. Don't try to write all five — that's what Block 3 is for.

**What just happened:** attendees have written business rules that directly govern AI behaviour. No code. The insight to land:

> *"The CLAUDE.md is yours to own. If the tool gets something wrong, the fix belongs here — not in the prompt, not in the code. You just wrote the spec. Claude builds to it."*

### If the room is slow to respond

Don't fill the silence with your own answer. Ask a more specific question:

> *"The committee hasn't approved this yet. Should the tool call it a decision or something else?"*

Someone will say: *"Something else — it's pending."* That's enough. Type it.

### What not to do

- Don't read a pre-filled CLAUDE.md aloud as if it were a textbook. The insight only lands when they write the rule.
- Don't write all five rules. Leave the room wanting to write more — they will in Block 3.
- Don't let someone shout out technical terminology ("use an enum"). Redirect: *"What does the tool need to know? Write it as you'd tell a new analyst."*

---

## The four slash commands (00:37 – 00:39)

Slash commands are reusable prompts that live in `.claude/commands/` as plain text files. Type one in a Claude Code session and it runs. Four ship with the seed repo:

| Command | What it does |
|---|---|
| `/prime` | Reads `PRD.md` and `CLAUDE.md` and confirms what it understood. If the readback is wrong, fix the file — not the prompt. |
| `/plan` | Produces a written, numbered plan. Does not write code. Stops and waits for your approval. |
| `/implement` | Executes the approved plan, step by step. |
| `/verify` | Runs the verification checklist on the relevant transcript and reports gaps. |

One thing to say about `/prime`:

> *"If Claude's readback of your CLAUDE.md misses a rule you wrote, that rule is not clear enough. Fix the writing, not the prompt. Claude is reading exactly what you wrote — it's a mirror."*

---

## Common questions in this block

- **"Can I change the PRD before we start?"** Yes. The PRD is yours. But write the change down first — then build it. Don't prompt first and write the spec afterwards.
- **"Who writes the CLAUDE.md for my real project?"** You do. Start with this skeleton. After a week of use, cut anything that turned out to be obvious. Add anything Claude kept getting wrong. Keep it under 100 lines — a memo, not a manual.
- **"What if a rule I write is wrong?"** Run it on a sample transcript and check. If the output is wrong, fix the rule. That feedback loop is the whole discipline.

[← Back to home](../index.html)
