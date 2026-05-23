# Track A — Scheduled Weekly Briefing

**Goal:** The tool emails you a structured weekly briefing every Monday at 8am — open decisions, action items by owner, upcoming deadlines, items needing follow-up. Set it once. Never compile a week-in-review manually again. An evening of work.

## What changes

Add a scheduled job that runs `decisions report --week` and sends the output as a formatted email. Two parts: the email formatter (converts markdown to readable HTML) and the scheduler (runs at a set time, no manual trigger).

## Starting prompt

Paste into a fresh Claude Code session in your repo, with Plan Mode on (Shift+Tab twice):

```text
Read PRD.md and CLAUDE.md.

We're adding a scheduled weekly briefing to the decisions tool.

What to add:
1. A `decisions send-report` command that:
   - Runs `decisions report --week <current week>` internally
   - Formats the output as a clean HTML email (readable in any email client)
   - Sends it via SMTP (Simple Mail Transfer Protocol — the standard
     email-sending protocol) using credentials from environment variables
   - Logs whether the send succeeded or failed, with timestamp

2. A cron job (a scheduled task that runs automatically at set times)
   that runs `decisions send-report` every Monday at 08:00 local time.
   Use system cron on macOS/Linux, or Task Scheduler on Windows.

Email config (from environment variables — never hardcoded):
- DECISIONS_SMTP_HOST — your mail server address
- DECISIONS_SMTP_PORT — port number (usually 587 for secure sending)
- DECISIONS_SMTP_USER — your email address
- DECISIONS_SMTP_PASS — your email password or app password
- DECISIONS_REPORT_TO — recipient address(es), comma-separated

Report content:
- Subject: "Weekly Decisions Briefing — [week of date]"
- Section 1: Open action items, grouped by owner, sorted by deadline
- Section 2: Decisions made this week
- Section 3: Pending decisions (awaiting approval)
- Section 4: Items with no deadline — flag for follow-up

Constraints:
- Credentials must come from environment variables. No hardcoding.
- If the ledger is empty for the week, still send — "No new decisions
  this week." Don't silently skip.
- Log every send attempt to ~/.decisions/send-log.jsonl (one JSON
  record per line) with: timestamp, week, success boolean, error if any.

Plan first. Do not write code yet.
```

## Milestones

1. **`decisions send-report` sends one email manually.** Run it. Receive the email. Check the formatting.
2. **Cron job is registered.** Verify with `crontab -l` (on macOS/Linux) — the job appears with the correct schedule.
3. **Send log is written.** After a successful send, `~/.decisions/send-log.jsonl` contains a valid record.

## Definition of done

- `decisions send-report` sends a formatted email without error.
- The email is readable on mobile (not a wall of plain text).
- The cron job runs on the correct schedule — verify by setting it to run in 2 minutes, confirming the email arrives, then resetting to weekly.
- Credentials never appear in any file tracked by git.
- Failed sends are logged and don't crash the tool.

## Things to watch for

- **App passwords, not account passwords.** Gmail, Outlook, and most enterprise mail require an "app password" (a separate password generated specifically for third-party apps) rather than your main account password. Generate one before starting.
- **Cron timezone.** System cron uses the system timezone. Confirm your machine's timezone is set correctly before trusting the schedule.
- **Empty weeks.** If you've processed no new transcripts this week, the report will be short — that's fine. An empty report is better than a missing one: it confirms the tool is running.

## Read next

- **crontab syntax guide** — search "crontab.guru" for an interactive editor that explains cron schedule syntax.
- **Gmail app passwords** — search "Gmail app password" in Google's support docs if you use Gmail.
- **Python `smtplib` docs** — `docs.python.org/3/library/smtplib.html`. The standard library module for sending email from Python.

[← Back to home](../index.html)
