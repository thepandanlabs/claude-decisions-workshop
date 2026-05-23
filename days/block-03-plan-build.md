# Block 3 — Run, Observe, Improve

**Time:** 00:40 – 01:25
**Goal:** Every attendee has run v0.1, identified a gap in the output, picked a stub, edited the spec, and built the enhancement. The tool on their laptop is now better than the one that shipped.

<!-- participant-start -->
## Block 3 — What to do

45 minutes. Work on your own laptop. The facilitator circulates.

**Phase 1 (00:40–00:55) — Run v0.1 and observe**

1. Run `decisions add inbox/` — processes all 5 sample transcripts
2. Run `decisions query` — look at what was captured
3. Note what's missing: action items? Tags? Confidential handling? Deadline formatting?

**Phase 2 (00:55–01:00) — Pick a stub**

1. Open `PRD.md` and read the stub sections
2. Pick the stub that matches the gap you noticed — Stub A (action items) is the recommended starting point

**Phase 3 (01:00–01:25) — Plan, implement, verify**

1. Edit your chosen stub in `PRD.md` — fill in the requirements in plain English
2. Update `CLAUDE.md` with any extraction rules the stub needs
3. Enable Plan Mode (Shift + Tab twice), then run `/plan` — read and approve the plan
4. Exit Plan Mode, then run `/implement` — Claude builds the enhancement
5. Run `decisions add inbox/` again and compare the new output to Phase 1
<!-- participant-end -->

## Block shape

This is the longest block — 45 minutes. Most of it is working on individual laptops. The facilitator circulates, troubleshoots quietly, and resists the urge to narrate.

| Time | Activity |
|---|---|
| 00:40 – 00:48 | **Facilitator demos Plan Mode live.** Approve a plan together. |
| 00:48 – 00:55 | **Run v0.1.** Every attendee runs `decisions add inbox/` on all five sample transcripts. Observe the output. Find the gaps. |
| 00:55 – 01:00 | **Pick a stub.** Each attendee chooses one enhancement from the PRD stub list. |
| 01:00 – 01:20 | **Edit spec → plan → implement.** Edit the PRD stub. Update the CLAUDE.md rule. Run `/plan` → `/implement`. |
| 01:20 – 01:25 | **Pause.** Verify the stub closed its gap. Look at before vs after on the relevant transcript. |

## The Plan Mode demo

Read this aloud as you do it, project the screen.

> *"Open the repo. Run `claude`. You'll see the prompt. Press Shift+Tab once — the footer says `accept edits on`. Press Shift+Tab again — it says `plan mode on`. On Windows, if Shift+Tab skips Plan Mode, the slash command `/plan` does the same thing.*
>
> *In Plan Mode, Claude physically cannot edit files, run commands, or modify anything. It can only read, search, and ask questions. This is enforced at the tool level — it's not a polite suggestion.*
>
> *I'm running `/prime` first. It reads `PRD.md` and `CLAUDE.md` and tells me what it understood. If anything in the readback is wrong, I edit the files — not the prompt.*
>
> *Now I'm running `/plan`. The plan comes back as a numbered list of steps. I'm reading it line by line. If I see anything wrong, I push back now — not after the code is written.*
>
> *I approve the plan. Claude exits Plan Mode and executes the steps in order. Watch the diffs (the change summary: green lines are code being added, red lines removed). The discipline now is: read the diffs."*

## Phase 1 — Run v0.1, find the gaps (00:48–00:55)

Every attendee runs:

```bash
decisions add inbox/
```

What v0.1 produces on the five sample transcripts:
- sample-01 (MCIT): 3 decisions extracted. No action items. Deadline stored as "before end of month" — not a date.
- sample-02 (Aramco): 1 decision — but it's conditional ("pending CFO sign-off") and should be a `pending_decision`, not a `decision`.
- sample-03 (SAMA): 2 decisions. Deadline for one is "after Eid Al-Adha" — stored verbatim, not convertible to a date.
- sample-04 (Ops plan): 4 decisions. 0 action items — Ahmed's hiring proposal, Fatima's budget submission, Khalid's vendor review are all missing.
- sample-05 (Career/Nora): 0 decisions (correct). 2 action items. BUT: the report includes the content of the performance discussion — sensitive.

**Facilitator: do NOT explain the gaps. Ask.**

> *"Look at the output for sample-05. What's wrong?"*

Wait. Let the room find it. Someone will notice the career conversation content appears in the report. That moment of discovery — not instruction — is what makes the gap stick.

Run it twice:

```bash
decisions add inbox/
```

Second run: `0 new records. 5 files skipped (already processed).`

**This is the idempotency moment.** Pause for it.

> *"You could run this a hundred times. The ledger stays correct. No duplicates, no double-counting. A chat tab cannot do this. Every session starts blank. This tool remembers."*

## Phase 2 — Pick a stub (00:55–01:00)

Read the stubs aloud from the PRD. Ask each attendee which gap bothered them most in phase 1. That's usually the right stub to pick.

Default recommendation: **Stub A (action items)** — it affects the most common meeting type and the before/after is visible immediately on sample-04.

| Stub | Who should pick it |
|---|---|
| A — Action items | Anyone who tracked who said they'd do what |
| B — Government tagging | Anyone with frequent government entity meetings |
| C — Confidential handling | Anyone with HR, career, or sensitive conversations |
| D — Islamic calendar conversion | Anyone whose deadlines are Hijri-relative |
| E — Pending decisions | Anyone who tracks "almost decisions" separately |

If someone wants two stubs: pick one for today. Add the second tomorrow.

## Phase 3 — Edit spec → plan → implement (01:00–01:20)

### What attendees do

**Step 1: Edit the PRD stub.**

Open `PRD.md`. Find the stub they chose. The stub has a comment block like:

```
<!-- STUB A — Action items
Currently: the tool only extracts decisions (type: decision).
Missing: action items — things someone committed to do, with an owner and deadline.

Add the following to this PRD section:
- Define action_item as a record type alongside decision.
- Fields: content, owner (person who committed), deadline (YYYY-MM-DD or "TBD").
- If deadline is implied but not stated, write "TBD" — never omit the field.
- Owner field: use the name as spoken. If only a function is named ("legal team"),
  use that and flag [UNCLEAR-OWNER].

Test: run decisions add on sample-04-ops-plan-2027.txt
      Confirm Ahmed's hiring proposal appears with owner: Ahmed and a deadline.
-->
```

The attendee reads this, then writes the actual PRD text below the comment. One paragraph. In their own words.

**Step 2: Update the CLAUDE.md extraction rule.**

The stub comment also tells them which rule to add to CLAUDE.md. For Stub A:

```
- Extract action items alongside decisions. An action item is a commitment
  made by a named person (or function) to do something by a deadline.
  Fields: content, owner, deadline (YYYY-MM-DD or TBD).
  Use the name as spoken. If unclear, use function name + [UNCLEAR-OWNER].
```

**Step 3: Run `/prime` → `/plan` → `/implement`.**

```bash
> /prime
```

Claude reads the updated PRD and CLAUDE.md and confirms the change. If the readback is wrong, the file is wrong — fix the file.

```bash
> /plan
```

Plan comes back. Read it. If a step says something the attendee didn't intend, push back now.

```bash
> /implement
```

Claude executes. Watch the diffs. The whole change should be 20–50 lines — a new extraction schema, an updated prompt, a new output section.

**Step 4: Run on the test transcript.**

```bash
decisions add inbox/sample-04-ops-plan-2027.txt
```

Before (v0.1): 4 decisions, 0 action items.
After (Stub A): 4 decisions, 6 action items — Ahmed's hiring proposal, Fatima's budget submission, Khalid's vendor review, and three others. Owners named. Deadlines recorded.

That before/after is the proof the stub worked.

## Phase 4 — Pause and surface (01:20–01:25)

Stop the room. Ask two or three people to read out loud what they built:

- "I added action item extraction. Sample-04 now shows 6 items with owners."
- "I handled confidential transcripts. The career conversation now shows actions only — no decision content."
- "I added government tagging. `decisions query --tag GOV` now works."

The room hears different stubs producing different results. This is the point: the spec change drove the behaviour change. Claude wrote the code; they wrote the rules.

## When someone is stuck

1. **"Did you edit both the PRD and the CLAUDE.md?"** Missing one of the two is the most common error. The PRD says *what* to extract; the CLAUDE.md says *how* to recognise it.
2. **"Run `/prime` and read the readback."** If Claude misunderstood the spec, the readback will show it. Fix the file, not the prompt.
3. **"What does `decisions add inbox/sample-XX.txt` output?"** Get a real error or real output before guessing.
4. **"Let's `/rewind` and re-plan."** `/rewind` undoes Claude's last set of changes — restores files to where they were before `/implement`. Don't be sentimental about 20 lines Claude wrote two minutes ago.

[← Back to home](../index.html)
