# Track D — MCP + Claude Desktop

**Goal:** Ask Claude Desktop natural-language questions about your decisions ledger and get real answers — not summaries of a document you pasted, but live queries against your actual database. "What's open from the Aramco meeting?" → real results, instantly. A weekend project.

## What changes

Build an MCP server (a small program that runs locally and gives Claude Desktop structured access to tools) that exposes the decisions ledger as a set of queryable tools. Claude Desktop calls these tools when you ask questions about your meetings. Three tools: `query_decisions` (search by owner, status, tag, date range), `get_open_items` (all unresolved action items), and `summarise_week` (decisions and actions from a given week).

## What MCP is

MCP stands for Model Context Protocol — an open standard that lets Claude (and other AI assistants) call tools you define on your local machine. Instead of pasting data into the chat, Claude queries your data source directly through a secure local connection. No data leaves your machine.

When Claude Desktop has an MCP server configured, you see it listed under "Available Tools" in the interface. When you ask a question that seems to need that tool, Claude calls it automatically — you don't have to invoke it manually.

## Starting prompt

Paste into a fresh Claude Code session in your repo, with Plan Mode on (Shift+Tab twice):

```text
Read PRD.md and CLAUDE.md.

We're building an MCP server that gives Claude Desktop access to the
decisions ledger.

What to build:
1. An MCP server in src/decisions_mcp/ that:
   - Uses the Python MCP SDK (pip install mcp)
   - Connects to ~/.decisions/decisions.db (the SQLite ledger)
   - Exposes three tools:

   Tool 1: query_decisions
   - Parameters: owner (optional), status (optional: open/closed/pending),
     tag (optional: GOV/CONFIDENTIAL), week (optional: ISO week string)
   - Returns: list of matching decisions and action items, formatted as
     structured text Claude can read

   Tool 2: get_open_items
   - Parameters: owner (optional)
   - Returns: all action items with no completed_date, sorted by deadline
     ascending (nulls last)

   Tool 3: summarise_week
   - Parameters: week (ISO week string, e.g. "2026-W21")
   - Returns: decisions made, action items assigned, pending decisions
     awaiting approval — grouped by meeting

2. A Claude Desktop config snippet (claude_desktop_config.json format)
   that the user can paste to register the server.

MCP server config block (example):
{
  "mcpServers": {
    "decisions": {
      "command": "python",
      "args": ["-m", "decisions_mcp"],
      "cwd": "/path/to/decisions-repo"
    }
  }
}

Constraints:
- The server reads the database — no writes. Read-only.
- If the database doesn't exist yet, return a clear message:
  "No ledger found. Run `decisions add inbox/` first."
- Tools must return results within 2 seconds on a ledger of up to
  1000 records.
- Server must start and stop cleanly — no zombie processes.

Plan first. Do not write code yet.
```

## Milestones

1. **MCP server starts without error.** Run `python -m decisions_mcp` — no errors, process stays alive.
2. **Claude Desktop lists the server under Available Tools.** After pasting the config snippet, restart Claude Desktop, open the tool list, confirm "decisions" appears.
3. **One real query works.** Ask Claude Desktop: "What action items does Ahmed have open?" — Claude calls `query_decisions`, returns results from your actual ledger.
4. **Natural-language question, live data.** Ask: "Summarise what was decided in week 21 of 2026." Results come from the database, not from anything you pasted.

## Definition of done

- Claude Desktop can answer questions about the ledger without any copy-paste.
- All three tools return results for a ledger with at least 10 records.
- The server exits cleanly when Claude Desktop is closed.
- No database writes happen through the MCP interface.

## Things to watch for

- **Claude Desktop subscription.** MCP tools require Claude Desktop (free download), but using them requires a Claude Pro subscription. The same $20/month subscription covers both the workshop and this track.
- **Config file location.** `claude_desktop_config.json` lives in a platform-specific location: `~/Library/Application Support/Claude/` on macOS, `%APPDATA%\Claude\` on Windows. Paste the server block inside the `"mcpServers"` key — don't replace the whole file.
- **Absolute paths in config.** The `"cwd"` value in the config must be an absolute path to your repo. A relative path will silently fail.
- **MCP SDK version.** Use v1.x of the Python MCP SDK (`pip install mcp>=1.0`). The API changed significantly between v0 and v1 — examples you find online may be for the older version.
- **Read-only discipline.** This tool should never write to the ledger. If a user asks Claude to "delete that action item," Claude will try — if your MCP server has write access, it will succeed. Enforce read-only at the connection level: open the SQLite connection with `check_same_thread=False` and don't expose any write tools.

## Going further

Once the three core tools work, natural extensions are:

- **`add_note` tool** — attach a follow-up note to an existing decision without re-running the full extraction
- **`mark_complete` tool** — mark an action item resolved directly from the chat (carefully — this is a write operation)
- **Multi-ledger support** — point the server at multiple `decisions.db` files (one per project) and route queries by project name

## Read next

- **MCP spec home** — `modelcontextprotocol.io`. Read "Concepts" first, then "Python SDK".
- **Python MCP SDK** — `github.com/modelcontextprotocol/python-sdk`. v1.x is current stable as of May 2026.
- **Claude Desktop config docs** — search for `claude_desktop_config.json` in the Anthropic docs for the exact file location and format.
- **"Building effective agents"** (Anthropic) — the tool-use patterns in this guide describe exactly what happens when Claude Desktop calls your MCP tools.

[← Back to home](../index.html)
