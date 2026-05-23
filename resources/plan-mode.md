# Plan Mode Walkthrough

Plan Mode is not a feature. It's the entire workflow.

When you enter Plan Mode, Claude **physically cannot edit files, run commands, or modify anything**. It can only read files, search, ask you questions, and produce a written plan. This is enforced at the tool level — the edit and bash tools are simply unavailable. It isn't a polite suggestion you can talk Claude out of.

The result: before a single line of code is written, you have a plan you read and approved. If the plan is wrong, you catch it here — not after the implementation is done.

## How to enter Plan Mode

In a Claude Code session, press **Shift + Tab** twice. Watch the bottom of the terminal:

- After one press: `accept edits on` (Claude edits without asking each time)
- After two presses: `plan mode on` (Claude can't edit anything)

If Shift+Tab skips Plan Mode on Windows (a known terminal binding issue with some PowerShell setups), use the slash command instead:

```text
/plan
```

Same result. Always works.

## The loop, step by step

### 1. Open the repo, start Claude

```bash
cd decisions-seed-repo
claude
```

### 2. Enter Plan Mode

Shift+Tab, Shift+Tab. Confirm the footer reads `plan mode on`.

### 3. Prime the context

```text
/prime
```

This runs the `.claude/commands/prime.md` slash command, which reads `PRD.md` and `CLAUDE.md` and reads them back to you. If the readback is wrong — Claude misunderstood a rule, or missed a section — the file is wrong, not the prompt. Fix the file.

### 4. Ask for a plan

```text
/plan implement the v0.1 acceptance criteria from PRD.md
```

Claude reads, thinks, produces a numbered plan. The plan is saved to `~/.claude/plans/` (a folder in your home directory) with a random name. It survives `/clear` and long sessions.

### 5. Read the plan, line by line

Out loud if you're alone. With a colleague if you're not. What you're looking for:

- Are the steps in the right order? (The database schema — the blueprint defining what fields a record contains — should be created before the code that reads from it.)
- Are there verification steps between phases? (Without them, errors compound.)
- Is anything missing from the PRD that the plan should have covered?
- Is anything in the plan that's not in the PRD? (Scope creep — things that weren't agreed on. Push back before any code gets written.)

### 6. Edit the plan if needed

Press **Ctrl + G**. The plan opens in your editor. Edit it. Save. Come back to the terminal.

You can also just type back in chat: *"Change step 4 to verify the extraction schema before writing the ledger."* Both work.

### 7. Approve and implement

When the plan is right, exit Plan Mode (Shift+Tab once more to land on `accept edits on`) and say:

```text
Implement the plan.
```

Claude executes the steps in order. Watch the diffs (the change summary: green lines are code being added, red lines are code being removed). The discipline now is: *read the diffs* — don't approve everything blindly.

### 8. If it drifts mid-build

Drop back into Plan Mode (Shift+Tab twice) and ask:

```text
The implementation has drifted from step 4 of the plan. Re-plan from
the current state to finish the acceptance criteria.
```

You get a new plan. You read it. You approve it. The loop continues.

## When to use Plan Mode

**Always Plan Mode:**
- Any new feature or stub implementation
- Anything that spans more than one file
- Any time you'd want a second opinion before proceeding

**Skip Plan Mode:**
- One-line typo fixes
- "Run the tool and tell me what the output is"
- Exploring the codebase with no edits

**Use Auto-Accept (one Shift+Tab) but not full Plan Mode:**
- Renaming something consistently across every file (mechanical refactors where the plan is obvious)
- After you've already approved a Plan Mode plan and you trust the rest of the execution

The right default for the workshop build block: **always Plan Mode**. Speed is not the goal today — the habit is.

## The collaborator model

Plan Mode is where "collaborator, not genie" becomes concrete.

A genie executes wishes. You say "build me a decisions tracker" and it builds something. You get what it built, not necessarily what you wanted.

A collaborator works from a brief. You produce a PRD. You write the CLAUDE.md extraction rules. Claude reads them, produces a plan, and you read the plan — together. If the plan is wrong, you catch it before any code is written. If the implementation drifts, you re-plan.

At every step, Claude is executing something you agreed to.

**Correct via files, not arguments.** If Claude keeps extracting something incorrectly — wrong type, wrong owner field, including content it shouldn't — the fix is a line in `CLAUDE.md`, not a longer prompt next time. Files persist across turns. Prompt arguments evaporate.

## A note on speed

Plan Mode feels slow the first three times. You write a plan, read it, edit it — none of which is the thing being built.

After the third project, the calculation flips. Two minutes of planning saves twenty minutes of unwinding the wrong implementation. You'll start to feel impatient *without* a plan.

That impatience is the point.

[← Back to home](../index.html)
