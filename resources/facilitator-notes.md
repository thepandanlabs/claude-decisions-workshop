# Facilitator Notes

For anyone running this workshop in their own organisation or city. Read before you facilitate.

## Tone and framing

You are not selling AI. The room has already paid $20 for a Pro subscription — they're sold. You are selling **the workflow** that makes the $20 produce something a chat tab cannot.

Open with:

> *"Everyone here has pasted a meeting transcript into a chat box and got a good summary. By the time we wrap, you will have built a tool that keeps that summary — and every future one — in a ledger you can query by person, by date, by entity. The difference is not the model. It's the three files on your laptop."*

That's the whole pitch. Don't expand it.

## Where to pause

Three moments are non-negotiable.

**1. After the bad prompt (≈ 0:15).**

Don't rescue. Let the room watch Claude produce something generic that doesn't know their entity types, their confidentiality rules, or what "pending CFO sign-off" means. Ask:

> *"What's missing here?"*

Wait. Don't fill the silence. Someone will say: *"It doesn't know anything about how we actually work."* That sentence is the workshop in one line.

**2. After the idempotency run (≈ 0:53).**

Run `decisions add inbox/` a second time. Zero new records. Pause. Say:

> *"You could run this a hundred times. The ledger stays correct. A chat tab cannot do this — every session starts from nothing. This tool remembers."*

**3. After someone runs `decisions query --owner` across multiple meetings (≈ 1:15).**

Ask them to read the output aloud. Two or three commitments from two different meetings, one command. Let that sit for a moment before moving on.

## Mixed-skill survival rules

The audience is uneven. Lean into it.

- **Operations and planning managers win the PRD phase.** They are better at writing specs for their own domain than most developers would be. Lean on them. If someone finishes editing their stub early, pair them with someone who's still reading the PRD.
- **HR and people managers own the CLAUDE.md extraction rules.** They understand immediately why the confidential handling rule matters. Let them shape it.
- **Finance managers catch the pending_decision distinction faster than anyone.** "Approved in principle pending CFO sign-off" is something they live with. Use them to explain Stub E to the room.
- **Technical managers will want to look at the code.** That's fine — Claude Code wrote it. But redirect: the code isn't the lesson. The extraction rules in CLAUDE.md are.
- **Never let one person's broken environment block the room.** If Claude won't authenticate at minute 8, pair the attendee with a working neighbour. Fix their laptop at the break.

## Coffee-shop-specific pitfalls

**1. Wi-Fi craters.**

Pre-cache everything before arrival via the prerequisites sheet. The Claude API still needs network, but cloning and installing are done at home.

**2. No projector, or the projector is at the wrong angle.**

Print the PRD, the CLAUDE.md, the bad-vs-good prompts page, and the agenda. Hand them out. The printed pack is the projector. The website is the second projector — bookmark on every laptop.

**3. The shared SSID throttles.**

The prereq sheet says: install Claude Code at home, clone seed repo at home, verify `claude --version` at home. Re-state this verbally at minute 0.

**4. Power.**

A two-hour workshop running Claude Code will drain a laptop to ~30%. Tell attendees to arrive at 100%. Bring a power strip if the venue allows it.

**5. Late arrivals.**

The first ten minutes are buffer. Don't restart Block 1 for a latecomer. Hand them the printed pack and a neighbour.

**6. The barista shouting orders.**

Reserve a back room or corner table. Brew92, Camel Step, and Half Million in Riyadh have larger branches with quieter rooms — call ahead.

## When someone is stuck

Order of escalation:

1. **"Did you edit both the PRD and the CLAUDE.md?"** Editing only one is the most common error — the PRD says *what* to extract, the CLAUDE.md says *how* to recognise it.
2. **"Run `/prime` and read the readback."** If Claude misunderstood the spec change, the readback will show it. Fix the file, not the prompt.
3. **"Run `decisions add` on the specific test transcript and show me the output."** Get a real output before guessing.
4. **"Let's `/rewind` and re-plan."** `/rewind` undoes Claude's last set of changes — restores files to where they were before `/implement`. Don't be sentimental about 20 lines Claude wrote two minutes ago.
5. **Pair with a working neighbour.** Don't take over their keyboard. Their hands, their lesson.

## Common build-block pitfalls

- **Editing the prompt instead of the file.** If Claude keeps getting something wrong, attendees instinctively want to type a longer message. Stop them. The correction belongs in CLAUDE.md, not the chat.
- **Implementing two stubs at once.** Some attendees will try to build Stub A and Stub C together. Don't let them. One stub, one plan, one implementation, one verification. Then the second.
- **Skipping the PRD edit.** Some attendees will jump straight to editing the CLAUDE.md without updating the PRD. Make them update the PRD first — the plan comes from the PRD, not from CLAUDE.md.
- **Treating Plan Mode as a formality.** If someone is rubber-stamping plans without reading them, slow them down. Ask them to read one step aloud and explain why it's in that order.

## Pre-workshop checklist

- [ ] Send the prerequisites sheet at T-5 days. Follow up at T-2 with anyone who hasn't confirmed install.
- [ ] Pre-test the install flow yourself on a fresh laptop. macOS and Windows.
- [ ] Run `decisions add inbox/` on all five sample transcripts and verify the output matches expectations.
- [ ] Write the Block 4 label table for sample-01 (or use the one in `resources/sample-transcripts.md`). Print it.
- [ ] Print 12 copies of: the PRD, the CLAUDE.md, the bad-vs-good prompts page, and the agenda.
- [ ] Pick the venue. Reservable room or corner, reliable Wi-Fi tested the day before, accessible power.
- [ ] Bring: power strip, USB-C and USB-A hubs.
- [ ] Charge your own laptop to 100%.

## Day-of staging

- **00:00:** Soft start. Late arrivals are guaranteed. Use 00:00–00:10 for tool check, not content.
- **The bad-prompt demo is non-negotiable.** It's the emotional hook. Don't shortcut it even if you're running behind.
- **The idempotency moment is the central beat.** If you're running short on time, cut Block 5 (track-pick) before cutting the idempotency and eval moments in Blocks 3 and 4.

## After the workshop

- Create a private group (Slack, WhatsApp, Telegram) for the cohort. Most learning happens between sessions.
- Two weeks later, ask: "Who processed a real transcript from their own meetings?" Those who did have the discipline. Those who didn't need a smaller, more specific prompt: "Pick one transcript from this week and run it."
- One month later, run a 60-minute "show your extension track" session. People who built something teach people who haven't started yet.

## Customising for your context {#customising}

**Different meeting types:** The five sample transcripts cover MCIT licensing, Aramco Digital pilot, SAMA partnership, annual ops planning, and career conversation. If your audience has different primary meeting types — investor rounds, board meetings, supplier negotiations — replace or supplement the samples. Update the Block 4 pre-label table to match.

**Different confidentiality rules:** The Stub C default is "career and performance conversations." Your organisation may have different categories — legal discussions, pre-announcement M&A meetings, board-only decisions. Edit the CLAUDE.md extraction rule in the seed repo to match.

**Different stub priorities:** If your audience is primarily in government relations, lead with Stub B (government tagging). If primarily in finance, lead with Stub E (pending decisions). The stub order in the PRD is a default recommendation, not a constraint.

**Arabic transcript support:** v0.1 is English-only. Arabic transcript processing works well with Claude but requires careful prompt design for mixed Arabic/English content. Don't attempt this in the 2-hour session — save it for Track B.

[← Back to home](../index.html)
