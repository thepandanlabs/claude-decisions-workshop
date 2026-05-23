# Block 6 — Wrap

**Time:** 01:50 – 02:00
**Goal:** Close cleanly. Every attendee names one thing they'll do differently. The room remembers what it just built and why.

<!-- participant-start -->
## Block 6 — What to do

Be ready to share with the room. No prep needed.

- What's one decision from this week's meetings that would have been missed without the tool?
- What rule would you add to `CLAUDE.md` before using this with real transcripts?
<!-- participant-end -->

## The shape

| Time | Activity |
|---|---|
| 01:50 – 01:55 | One-line takeaways from around the room. |
| 01:55 – 01:58 | The three files that mattered. |
| 01:58 – 02:00 | Where to read next. Open Q&A while people finish coffee. |

## Takeaways — go around the room

Read aloud:

> *"In one sentence: what's the one thing you're going to do differently the next time you finish a meeting?"*

No editorialising. Just listen. Most answers will land in one of three buckets:

- *"I'm going to export the transcript and run it through the tool."*
- *"I'm going to write down the right answer before I check the output."*
- *"I'm going to write a spec before I ask Claude to build anything."*

That's the workshop. If a third of the room says one of those three things, the session worked.

## The three files that mattered

Hold this up (on screen or printed):

```
PRD.md
CLAUDE.md
decisions.db
```

> *"Everything you did today rotates around these three files. The PRD says what we're building. The CLAUDE.md says how this tool recognises decisions, action items, sensitive conversations, and conditional approvals — in plain English, owned by you, not by a developer. The database is the ledger that accumulates across every meeting you'll ever run through this tool.*
>
> *You didn't write a single line of code. You wrote the rules. Claude wrote the code. The discipline is in the spec, not the syntax. Steal that for the next thing you build."*

## Where to read next

Three things, no more:

1. **Anthropic's official Claude Code Quickstart** — `code.claude.com/docs/en/quickstart`. The canonical getting-started guide.
2. **Hamel Husain's "Your AI Product Needs Evals"** — `hamel.dev/blog/posts/evals/`. The single best 30-minute read on building tools that are verifiably correct, not just impressively fluent.
3. **Boris Cherny + Alex Albert, "A conversation on Claude Code"** — YouTube, ~21 minutes. The creator of Claude Code on how he uses it — the Plan Mode workflow in his own words.

These three are about 90 minutes of reading and watching. That's a Friday evening. Encourage it.

## Open Q&A — until coffee is finished

Take any question that didn't fit earlier. Some that will land here:

- **"What about other AI tools — Copilot, Gemini, GPT-4?"** Same principle applies to any AI with tool-use capabilities. The discipline — write the spec, verify the output, accumulate in a ledger — transfers to any platform. Claude Code is the vehicle we used today; the methodology is the asset.
- **"How do I convince my team?"** Show them `decisions query --owner "Ahmed" --open` pulling two commitments from two different meetings they all attended. Don't argue about AI — show the cross-meeting query. That's the gap that lands.
- **"Can I use this for Arabic transcripts?"** Not in v0.1 — the extraction prompts are English-only. Claude handles Arabic well, but mixed Arabic/English transcripts need careful prompt design. That's Track B — the first thing to build after the workshop.
- **"How much will this cost?"** Claude Pro ($20/month) covers a tool this size comfortably. The `decisions add` command calls Claude once per transcript — for a team processing 20 meetings a week, that's roughly 20 API calls. Well within Pro limits.
- **"What if I want to build something completely different?"** Same loop. Write a PRD for what you want. Write a CLAUDE.md for how it should behave. Run `/plan` → `/implement` → verify. The decisions tool was the worked example. Your problem is the next one.

If a question is too large — *"how do we build our organisation's entire knowledge management system?"* — defer to follow-up. *"That's a different workshop. Come to the next one."*

## The send-off

Read aloud, then stop:

> *"You came in this morning with a chat tab. You're leaving with a CLI that has state, extraction rules, a verification discipline, and a workflow. The ledger is yours. From Pandan Labs — go build something."*

Photos. Done.

## Outputs from this block

- Every attendee has spoken one sentence aloud.
- Every attendee leaves with three reading recommendations.
- The room has a shared memory of the three files that anchored the work.

[← Back to home](../index.html)
