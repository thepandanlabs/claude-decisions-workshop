# Track B — Google Drive / Notion Sync

**Goal:** The tool pulls meeting transcripts directly from a Google Drive folder or Notion database — no manual export, no drag-and-drop. You drop a transcript into Drive, run one command, and it lands in the ledger. An evening of work.

## What changes

Add a `decisions pull` command that fetches new transcripts from a configured source (Drive folder or Notion database) and runs `decisions add` on each one. Two parts: the connector (authenticates and downloads files) and the deduplication guard (don't re-import what's already in the ledger).

## Starting prompt

Paste into a fresh Claude Code session in your repo, with Plan Mode on (Shift+Tab twice):

```text
Read PRD.md and CLAUDE.md.

We're adding an automatic pull command to the decisions tool.

What to add:
1. A `decisions pull` command that:
   - Reads a source config from ~/.decisions/config.json
     (either "google_drive" or "notion" with connection details)
   - Downloads any new .txt or .md files added since the last pull
   - Runs `decisions add` on each downloaded file
   - Skips files already in the ledger (use the existing SHA-256 deduplication)
   - Logs how many files were checked, how many were new

2. A `decisions pull --setup` sub-command that:
   - Asks which source: Google Drive or Notion
   - Walks through the authentication steps for the chosen source
   - Writes credentials to ~/.decisions/config.json (not tracked by git)
   - Confirms the connection by listing the first 3 files found

Source option A — Google Drive:
- Use the Google Drive API v3 with OAuth2 (googled "google drive api python quickstart")
- Target a specific folder ID (user pastes it from the Drive URL)
- Filter: only files modified since last pull timestamp

Source option B — Notion:
- Use the Notion API (official Python SDK: notion-sdk-py)
- Target a specific database ID (user pastes it from Notion URL)
- Each row = one meeting; "Transcript" property = the text content

Config file (example):
{
  "source": "google_drive",
  "folder_id": "...",
  "last_pull": "2026-05-01T08:00:00Z",
  "credentials_path": "~/.decisions/gdrive-credentials.json"
}

Constraints:
- OAuth tokens and API keys must be in ~/.decisions/ — never in the repo.
- The pull command must be idempotent: running it twice imports nothing new.
- If Drive/Notion is unreachable, exit cleanly with a message — don't crash.
- Log each pull attempt to ~/.decisions/pull-log.jsonl (timestamp, source,
  files_checked, files_imported, error if any).

Plan first. Do not write code yet.
```

## Milestones

1. **`decisions pull --setup` completes without error.** Authentication succeeds. The config file is written. Three file names print to the terminal.
2. **`decisions pull` imports one new transcript.** Drop a new .txt file into the Drive folder (or Notion row), run the command, confirm the file is in the ledger.
3. **Idempotency holds.** Run `decisions pull` again immediately — zero new imports.

## Definition of done

- `decisions pull` runs without error on a folder/database that has new content.
- Running it a second time on the same state produces zero new imports.
- Credentials live in `~/.decisions/` and are not tracked by git (`.gitignore` covers them).
- `~/.decisions/pull-log.jsonl` contains a valid record after each run.

## Things to watch for

- **OAuth consent screen.** Google Drive API requires an OAuth app configured in Google Cloud Console. The setup takes 10–15 minutes before writing any code. Do this first.
- **Notion integration scope.** When creating a Notion integration, you must explicitly share the target database with it — it won't see your workspace by default.
- **Drive folder ID vs file ID.** The folder ID is in the URL when you open a Drive folder: `drive.google.com/drive/folders/<FOLDER-ID>`. Copy the right segment.
- **Large folders.** If the Drive folder has hundreds of files, add a `--since` date filter so the first pull doesn't try to import your entire meeting archive at once.

## Read next

- **Google Drive API Python quickstart** — search "Google Drive API Python quickstart" in Google's developer docs.
- **Notion SDK for Python** (`notion-sdk-py`) — search "notion-sdk-py" on PyPI for install instructions and examples.
- **`decisions add` deduplication** — review `src/decisions/ingest.py` in the seed repo. The SHA-256 check there is what prevents duplicates; `pull` relies on it.

[← Back to home](../index.html)
