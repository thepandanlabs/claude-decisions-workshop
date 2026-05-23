# Track C — Slack Channel Watch

**Goal:** An agent monitors a Slack channel for meeting summaries. When someone drops a summary into the channel, the agent extracts decisions and action items automatically — no manual `decisions add`, no copy-paste. A weekend project.

## What changes

Add a `decisions watch` command that runs an agent loop: poll a Slack channel, detect new messages containing meeting content, extract decisions via the existing pipeline, post a structured reply to the thread. Three parts: the Slack connector (reads messages), the detection filter (is this a meeting summary?), and the reply formatter (posts extraction results back to the thread).

## Starting prompt

Paste into a fresh Claude Code session in your repo, with Plan Mode on (Shift+Tab twice):

```text
Read PRD.md and CLAUDE.md.

We're adding a Slack watch agent to the decisions tool.

What to add:
1. A `decisions watch` command that:
   - Polls a configured Slack channel every 60 seconds
   - Detects messages that look like meeting summaries (heuristic: length
     > 300 characters, or contains keywords like "decided", "action item",
     "follow up", "owner", "deadline")
   - For each matching message: runs the extraction pipeline on the text
   - Posts a structured reply in the message thread with the extracted
     decisions and action items (formatted as a Slack block message)
   - Adds the extraction to the ledger (same as `decisions add`)
   - Marks messages it has already processed so it doesn't re-extract on
     the next poll cycle

2. A `decisions watch --setup` sub-command that:
   - Prompts for a Slack bot token and channel ID
   - Writes them to ~/.decisions/slack-config.json (not tracked by git)
   - Posts a test message to confirm the connection works

Slack reply format (block message):
- Header: "Decisions extracted from this meeting"
- Section: decisions (if any), each as a bullet
- Section: action items (if any), each as a bullet with owner and deadline
- Footer: "Added to ledger · run `decisions query` to search"
- If nothing found: "No formal decisions or action items detected."

Detection heuristic:
- Don't extract from every message — only from messages that look like
  summaries. False negatives (missing a summary) are better than false
  positives (replying to someone's quick question). Tune the heuristic.

Slack config (from ~/.decisions/slack-config.json):
- bot_token — Slack bot token (starts with xoxb-)
- channel_id — the channel to watch
- processed_message_ids — list of already-handled message timestamps

Constraints:
- Bot token must not appear in any file tracked by git.
- If Slack is unreachable, log the error and retry on next poll — don't crash.
- `decisions watch` is a long-running process. Ctrl+C should exit cleanly.
- Log each extraction event to ~/.decisions/watch-log.jsonl (timestamp,
  message_ts, decisions_found, action_items_found, error if any).

Plan first. Do not write code yet.
```

## Milestones

1. **`decisions watch --setup` connects successfully.** Bot posts a test message to the channel. You see it in Slack.
2. **Agent detects and replies to one meeting summary.** Post a meeting summary (you can use one of the seed repo sample transcripts) in the channel. Within 60 seconds, the bot replies in the thread with extracted decisions and action items.
3. **Ledger is updated.** After the reply, `decisions query --open` shows the new items.
4. **Idempotency holds.** The bot does not reply a second time to a message it has already processed.

## Definition of done

- `decisions watch` runs without error and polls the channel on schedule.
- A meeting summary posted to the channel produces a structured thread reply within 90 seconds.
- The bot does not re-process messages already handled.
- Ctrl+C exits cleanly with no traceback.
- `~/.decisions/watch-log.jsonl` contains a valid record for each extraction event.

## Things to watch for

- **Slack bot scopes.** Your bot needs `channels:history` (to read messages), `chat:write` (to post replies), and `channels:join` (or be explicitly added to the channel). Missing scopes produce opaque 403 errors.
- **Socket Mode vs polling.** Slack's Events API (push-based) is more efficient but requires a public URL. Polling via the Web API is simpler for a local setup — the starting prompt uses polling. If you want real-time response, look into Socket Mode (no public URL needed, requires `connections:write` scope).
- **Rate limits.** The Slack Web API has tiered rate limits. Polling every 60 seconds on a single channel is well within free-tier limits, but don't drop it below 10 seconds.
- **Detection false positives.** The keyword heuristic will occasionally catch messages that are not meeting summaries. Review the first 10 detections manually before trusting it.
- **Subagent pattern.** This track is a good introduction to the evaluator-optimiser agent pattern described in Anthropic's "Building effective agents" guide (see Further Reading). The agent evaluates each message (is this a meeting summary?) then optimises the extraction (what decisions were made?).

## Read next

- **Slack Bolt for Python** — the official Slack SDK for Python. Search "Slack Bolt Python" in Slack's developer documentation. Much simpler than the raw Web API.
- **"Building effective agents"** (Anthropic) — the prompt-chaining and evaluator-optimiser patterns apply directly to this track. Link in Further Reading.
- **Socket Mode guide** — search "Slack Socket Mode Python" if you want push-based events instead of polling.

[← Back to home](../index.html)
