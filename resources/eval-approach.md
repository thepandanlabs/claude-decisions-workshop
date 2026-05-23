# The Eval Approach

**What is an eval?** An eval (short for evaluation) is a saved input, the known-right answer, and a check that they match. For the decisions tool: one meeting transcript (the input), a hand-labelled table of what decisions and action items were actually in it (the known-right answer), and the comparison between what the tool extracted and what the label says (the check).

Nothing more. No code required.

## The three questions

Every eval for an extraction tool answers three questions:

**1. Did it catch everything? — Recall**

Did the tool surface every decision and action item that was actually in the transcript? If a commitment was made and the tool missed it, that's a recall failure — something was there and the tool didn't find it.

*What causes recall failures:* The CLAUDE.md extraction rule for that type is too narrow or ambiguous. Tighten the rule.

**2. Did it invent anything that wasn't there? — Precision**

Did the tool add any records that don't correspond to something actually said in the transcript? If the tool reports a decision that wasn't made, that's a precision failure — hallucination.

*What causes precision failures:* The extraction rule is too broad, or the prompt doesn't have a strong enough "if in doubt, don't extract" constraint. Add one.

**3. Is the output the same if you run it twice? — Determinism**

Run `decisions add` on the same file twice. The second run should produce zero new records. If it doesn't, the deduplication logic has a bug.

*Why this matters:* A tool that produces different results on the same input is not trustworthy. You can't build a reliable ledger on a non-deterministic foundation.

## How to run an eval without code

The facilitator pre-labels `sample-01-mcit-licensing.txt` before the workshop. The label is a simple table:

| # | Type | Content | Owner | Deadline |
|---|---|---|---|---|
| 1 | decision | Proceed with regulatory sandbox application | Mohammed | 2026-05-31 |
| 2 | pending_decision | Full licensing approval | MCIT committee | TBD |
| 3 | action_item | Submit technical documentation to MCIT portal | Mohammed | 2026-05-31 |
| 4 | action_item | Legal team to review data localisation clauses | [UNCLEAR-OWNER] | 2026-06-07 |

Run the tool:

```bash
decisions add inbox/sample-01-mcit-licensing.txt
decisions list
```

Compare the output to the label. Count the matches. Note the mismatches. Answer the three questions.

This is an eval. It took five minutes to run and required no code to interpret.

## Why the label must be written before running the tool

The discipline is: **write down the right answer before you check the output.**

If you run the tool first and then decide what the right answer is by reading the output, you're not testing the tool — you're rationalising it. The tool will always produce *something*. The question is whether *something* is *correct*, and you can only answer that if you had an opinion before you ran it.

This applies to AI-powered tools in exactly the same way it applies to a junior analyst's first report: you should know what good looks like before you read their work.

## Scaling the eval for ongoing use

Once the workshop is done, you can build a running eval set:

1. Each time you process a transcript, spot-check one decision or action item.
2. If it's wrong, note the correction in a text file alongside the transcript.
3. After ten transcripts, you have ten corrections — patterns in what the tool gets wrong.
4. Update the CLAUDE.md extraction rules to address the patterns.
5. Re-run the tool on the original transcripts and check whether the corrections now match.

That's a simple, non-technical eval loop. No code. No framework. Just: input, label, compare, fix the rule, check again.

## The connection to what developers do

Developers run the same three-question eval, just with code instead of a printed table:

- **Recall / precision:** checked by "golden file" tests — a saved correct output that the tool's output is compared against automatically.
- **Determinism:** checked by running the same command twice in a test suite and confirming identical output.

The principle is identical. The code ceremony is different. The discipline is what matters — and the discipline doesn't require the code.

[← Back to home](../index.html)
