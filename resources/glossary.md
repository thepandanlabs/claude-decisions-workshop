# Glossary

Every term used in the workshop, defined in plain language. If something in a block runbook or resource page is unclear, look here first.

---

## Workshop-specific terms

**PRD (Product Requirements Document)**
A one-page spec that describes what you're building, what it must do, and what's explicitly out of scope. Claude reads the PRD before planning anything. The PRD is not permanent — edit it when what you want changes. In this workshop, the PRD ships with five "stub" sections: gaps you fill in during Block 3.

**Stub (in the PRD)**
A clearly marked incomplete section of the PRD. The seed repo ships with v0.1 working and five stubs describing what v0.1 doesn't do yet. In Block 3, you pick one stub, write its spec, and build it.

**CLAUDE.md**
A text file in the project root that Claude reads at the start of every turn. It tells Claude the project's rules — what stack to use, how to extract decisions, what to ask before making structural changes. Unlike the chat prompt, the CLAUDE.md persists across sessions. Edit it when you want to change Claude's behaviour permanently.

**Extraction rules**
The section of `CLAUDE.md` that defines how the tool recognises decisions, action items, pending decisions, and their fields. Written in plain English — not code. These are the rules you own and can edit.

**Eval (evaluation)**
A saved input, the known-right answer, and a check that they match. For the decisions tool: one transcript (input), a hand-labelled table of what decisions and actions were in it (known-right answer), and the comparison between tool output and the label (check). No code required to run one.

**Golden file**
A saved correct output that future runs are compared against automatically. Developers use these in automated test suites. In the manager workshop, the facilitator's pre-labelled table for sample-01 is the equivalent.

**Idempotent / Idempotency**
Safe to run multiple times with the same result. `decisions add inbox/` is idempotent: running it twice on the same folder adds zero new records the second time. No double-counting, no duplicates.

**Recall**
One of the three verification questions: did the tool catch everything that was actually in the transcript? A recall failure means something was missed.

**Precision**
One of the three verification questions: did the tool invent anything that wasn't actually in the transcript? A precision failure means something was hallucinated (made up).

**Determinism**
One of the three verification questions: does the tool produce identical output when run twice on the same input? A deterministic tool is trustworthy; a non-deterministic one is not.

**Acceptance criteria**
The five or six specific, testable statements that define when the tool is "done." For this workshop: `decisions add inbox/` produces records, re-running produces zero new records, `decisions query --owner` filters correctly, etc.

---

## Claude Code concepts

**Claude Code**
Anthropic's command-line tool for software development using Claude. Unlike the chat interface, Claude Code has persistent context (via files), can run commands, reads and edits files, and maintains state across sessions.

**Plan Mode**
A mode where Claude can only read and plan — it cannot edit files or run commands. Activated by pressing Shift+Tab twice in a Claude Code session. The goal: you read and approve a numbered plan before a single line of code is written.

**Auto-Accept mode**
A mode (one Shift+Tab in Claude Code) where Claude edits files without asking for permission on each change. Faster than default, but you should still read the diffs.

**Agentic loop**
The cycle Claude Code runs through on each turn: read context (CLAUDE.md, open files, your message) → act via tools (read files, edit files, run commands) → wait for your review. Claude re-reads CLAUDE.md every turn — so editing the file changes Claude's behaviour immediately.

**Tool (in Claude Code)**
A capability Claude uses during the agentic loop. Examples: Read (reads a file), Edit (edits a file), Bash (runs a shell command). In Plan Mode, the Edit and Bash tools are disabled.

**Context window**
The amount of information Claude can hold in working memory at one time. Files on disk are not in the context window — Claude must read them explicitly. The CLAUDE.md is read every turn; other files are read when Claude opens them.

**Slash command**
A reusable prompt stored as a text file in `.claude/commands/`. Triggered by typing `/command-name` in the Claude Code session. The seed repo ships with four: `/prime`, `/plan`, `/implement`, `/verify`.

**Subagent**
A separate Claude Code session with its own context window, spawned by the main session to handle an independent task in parallel. Not used in the workshop but relevant for the extension tracks.

---

## Software terms

**CLI (Command-Line Interface)**
A program you interact with by typing commands in a terminal window, rather than clicking buttons in a graphical application. The `decisions` tool is a CLI: you type `decisions add inbox/` and it processes your transcripts.

**Terminal**
The text-based window where you type commands. On macOS: Terminal app or iTerm2. On Windows: PowerShell or Windows Terminal. On Linux: any terminal emulator.

**SQLite**
A lightweight database that lives as a single file (here: `decisions.db`) on your machine. No server needed, no cloud sync. The decisions tool uses SQLite to store every extracted record persistently across sessions.

**Ledger**
The SQLite database file (`decisions.db`) that accumulates all extracted decisions and action items across every transcript you process. Unlike a chat session, the ledger persists between sessions and can be queried at any time.

**SHA-256 hash**
A short fingerprint that uniquely identifies a file's contents. The decisions tool computes a SHA-256 hash for each transcript file and uses it to detect duplicates — same file processed twice produces the same hash, so the second run produces zero new records.

**MCP (Model Context Protocol)**
An open standard that lets AI assistants call external tools. Track D connects the decisions tool to Claude Desktop via MCP — so you can ask Claude a question and it queries your live ledger to answer, rather than guessing.

**API (Application Programming Interface)**
A defined way for one program to talk to another. The decisions tool calls the Anthropic Claude API to extract structured information from transcripts — it sends the transcript text and receives back structured JSON (a common data format).

**Deduplication**
The process of ensuring the same item is only stored once. `decisions add` deduplicates by file hash: if you add the same transcript twice, the second run recognises the hash is already in the ledger and skips it.

**Exit code**
A number a command reports when it finishes — 0 means success, anything else means failure. Used by automation tools to decide whether to proceed to the next step.

[← Back to home](../index.html)
