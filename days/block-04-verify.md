# Block 4 — Verify

**Time:** 01:25 – 01:40
**Goal:** Every attendee answers three verification questions about their enhanced tool, using a pre-labelled transcript. The discipline of "right, not just plausible" becomes concrete — without requiring any code knowledge.

## Why this block exists

A tool that "looks right" is not a tool. It's a demo.

The difference: a tool that *is* right has been checked against a known-correct answer. You know what should come out. You ran it. You compared. It either matched or it didn't.

That check is an eval (short for evaluation). It's the same discipline a development team uses with automated tests — just without the code ceremony. The principle is identical: **saved input + known-right answer + pass/fail check.**

For a decisions tracker in a business context, an eval is something any manager can run. The only thing you need is the willingness to write down what the right answer is before you run the tool.

## What the facilitator prepared before the session

The facilitator pre-labelled `sample-01-mcit-licensing.txt` — the MCIT regulatory sandbox meeting transcript.

The label is a simple table, printed on paper or on a shared screen:

| # | Type | Content | Owner | Deadline |
|---|---|---|---|---|
| 1 | decision | Proceed with regulatory sandbox application | Mohammed | 2026-05-31 |
| 2 | pending_decision | Full licensing approval | MCIT committee | TBD |
| 3 | action_item | Submit technical documentation to MCIT portal | Mohammed | 2026-05-31 |
| 4 | action_item | Legal team to review data localisation clauses | [UNCLEAR-OWNER] | 2026-06-07 |

This is the ground truth. Four records. Hand-labelled by the facilitator from reading the transcript.

## The three verification questions

Ask every attendee to run:

```bash
decisions add inbox/sample-01-mcit-licensing.txt
decisions list
```

Then answer three questions:

**Question 1 — Did it catch everything? (Recall)**

> *"Does your output contain all four records from the label? If any are missing, the tool has a recall problem — it didn't surface something that was there."*

Count them. A missing action item means the extraction prompt didn't recognise it as one. That's a spec problem — the CLAUDE.md rule needs to be clearer.

**Question 2 — Did it invent anything that wasn't there? (Precision)**

> *"Does your output contain anything that isn't in the label? If the tool added a fifth record that doesn't correspond to anything in the transcript, it hallucinated. That's worse than missing something — you now have false data in your ledger."*

Check each output record against the label. One extra? Find it in the transcript or delete it.

**Question 3 — Is the output the same if you run it twice? (Determinism)**

```bash
decisions add inbox/sample-01-mcit-licensing.txt
```

Run it again. The answer should be: `0 new records. 1 file skipped (already processed).`

> *"Same input, same result, every time. That's what makes the tool trustworthy — not just today, but six months from now when someone asks 'did we agree to do this?' and you can point to the record."*

## What a good result looks like

If an attendee's tool produces all four records, no extras, and deduplicates correctly: they're done. That's the bar.

If it's missing one: look at the CLAUDE.md extraction rule for that type. Is the rule clear enough that Claude would recognise the missed item? Probably not — tighten it.

If it invented one: look at the transcript. Is there anything that could have been misread as a decision or action item? Update the rule to add a counter-example.

## The three-question framework, restated

Write these on the whiteboard or say them aloud:

> **1. Did it catch everything?** — Recall
> **2. Did it invent anything?** — Precision
> **3. Does it produce the same result twice?** — Determinism

These three questions are the entire eval framework for an LLM-powered extraction tool. No code. No test runner. No configuration. Just: do you know what the right answer is, and did you get it?

The discipline — writing down the right answer before running the tool — is the part that's hard. The tool will always produce *something*. The question is whether *something* is *correct*.

## What to call out from the front of the room

> *"Every team that ships AI-powered tools has a version of this process. The difference between a demo and a product is not the model — it's whether anyone wrote down what 'right' looks like. You just did. That's the whole discipline."*

## Outputs from this block

- Every attendee has compared tool output to a pre-labelled ground truth.
- Every attendee can articulate the difference between recall failure (missed item) and precision failure (hallucinated item).
- Every attendee has confirmed deduplication works on a real transcript.
- The three verification questions are named and understood.

[← Back to home](../index.html)
