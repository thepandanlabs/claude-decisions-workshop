# Block 1 — Setup & The Thesis

**Time:** 00:00 – 00:20
**Goal:** Every laptop verified working. Every attendee understands why a chat box and a tool are structurally different — not in capability, but in what persists.

## The shape

| Time | Activity |
|---|---|
| 00:00 – 00:10 | Soft start. Tool check. Coffee. Late arrivals. |
| 00:10 – 00:18 | The three claims. The bad-prompt demo. |
| 00:18 – 00:20 | Q&A — one or two questions. Park the rest. |

## Tool check — first 10 minutes

While people are arriving and getting coffee, ask everyone to run:

```bash
claude --version    # should print a version number
claude doctor       # should show green checkmarks
python --version    # should be 3.11 or higher
```

And confirm the seed repo is cloned and `decisions add` is available:

```bash
cd decisions-seed-repo
decisions --help
```

If someone's setup is broken: pair them with a working neighbour immediately. Don't spend group time on one person's install. Fix it at the break.

## Opening reframe (say this before anything else at 00:10)

Before the three claims, address what people think they signed up for. Many in the room heard "How to Code with AI" and imagined typing Python or JavaScript. Correct that immediately — not apologetically, but as a reveal:

> *"Before we start — a quick reframe on what 'coding with AI' actually means.*
>
> *Traditional coding: you type instructions that a computer executes.*
>
> *Coding with AI: you write a spec precise enough that an AI can execute it without guessing. The AI types the instructions. You make the decisions that matter — what to build, what the rules are, what counts as correct. That's the skill. And it turns out managers are often better at it than developers, because you already know the domain.*
>
> *Today you're going to write a spec, approve a plan, and verify an outcome. Claude Code will write every line of Python. By the end, you'll have a working tool — and you'll understand exactly which part of that process you owned."*

This reframe does three things: it catches the people who feel out of their depth, it resets expectations correctly, and it makes Claim 2 land harder.

## The three claims

State each one. Don't rush past them — they are the thesis.

**Claim 1: What you paste into a chat box disappears when the session ends.**

> *"You've used Claude or ChatGPT to summarise a meeting. You got a good output. Then you closed the tab. Next week, you opened a new session and pasted a new transcript. That session had no idea what last week's decisions were. No ledger. No memory. No accountability trail.*
>
> *What we're building today persists. Every meeting you process adds to the ledger. Every commitment is searchable by owner, deadline, and entity — across weeks, across meetings, across stakeholders. The chat tab is a notebook with no pages. What you build today is a ledger."*

**Claim 2: The spec is the product — and managers write better specs than most developers.**

> *"We're going to write a PRD — a one-page spec for the tool. Claude will read it and build what it says. The more precisely you describe what you want, the closer you get to what you need.*
>
> *Here's the thing: for a decisions tracker, you know exactly what fields matter. You know which meetings are sensitive. You know that 'pending CFO sign-off' is not a decision. You know that Eid Al-Adha is a deadline. A developer building this from scratch would have to ask you every one of those questions. You don't. You already know. That knowledge goes into the spec."*

**Claim 3: Verification makes it real.**

> *"At some point today, you'll run the tool on a transcript and check whether it caught the decisions that were actually made. That check — known input, known right answer, pass or fail — is an eval. It's the same discipline developers use with automated tests, just without the code. 'It looked right' is not a test. 'It matched the hand-labelled answer' is."*

## The bad-prompt demo (do this live, on screen)

Open a fresh Claude.ai session. Type, verbatim:

```
build me a decisions tracker for my meeting transcripts
```

Watch what happens. Claude will:
- Invent a schema. Plausible fields — date, decision, owner — but no knowledge of your meetings, your confidentiality rules, your entity types.
- Produce something. It may even work.
- Forget everything the moment the session ends.

Ask the room:

> *"What's missing?"*

Wait. Don't answer. Someone will say: *"It doesn't know what a good answer looks like for our meetings."* Or: *"There's no memory."* That sentence — whichever version surfaces — is the thesis of the workshop.

Now close the tab. Say:

> *"That output is gone. If I open a new session and run it again, it starts from scratch. No ledger, no deduplication, no way to ask 'what did Ahmed commit to this week across all meetings.' We're going to fix all three of those things in the next 90 minutes."*

## What the room should leave Block 1 knowing

- Coding with AI means writing a spec, not typing syntax. Claude writes the code. You make the decisions that determine whether the code is right.
- A chat session forgets. A tool accumulates. These are structural differences, not quality differences.
- The PRD and CLAUDE.md are the decisions that matter. Claude writes the code.
- Verification is not a techie concept — it's "did it catch what actually happened?"

[← Back to home](../index.html)
