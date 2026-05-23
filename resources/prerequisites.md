# Prerequisites

**Read this before you arrive. Plan 30 minutes of setup at home.**

Two hours in a coffee shop is not enough time to debug a broken install. Everyone needs the four things below working *before* walking in.

## 1. A paid Claude subscription

The $20/month Claude Pro plan is enough for this workshop. Monthly billing is fully supported as of May 2026 — annual is optional ($17/month if you prefer to pre-pay).

- Subscribe at `claude.com/pricing` → pick **Pro**.
- Claude Code is included with Pro at no extra cost.
- The free plan will **not** work — Claude Code requires a paid subscription.

For Saudi Arabia specifically: Anthropic officially supports Saudi Arabia for both Claude.ai and the API. No VPN needed. See the [KSA payment notes](ksa-payments.md) page if your card is declined.

## 2. Claude Code installed

Two install paths. Pick one. The native installer is the current recommendation.

**Native installer (no Node.js needed):**

```bash
# macOS / Linux / WSL (Windows Subsystem for Linux)
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```

The `curl` / `irm` commands download and run the installer automatically — same idea as a web-based setup wizard, just in the terminal.

**npm fallback (if you prefer Node.js):**

```bash
npm install -g @anthropic-ai/claude-code
```

`npm` is the package manager that comes with Node.js — a way to install command-line tools with one command.

If you hit `EACCES` errors on npm (a permission error meaning "this installer doesn't have write access to the system folder"), **do not use `sudo`**. Set up a user-local prefix instead:

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc   # or ~/.zshrc
source ~/.bashrc
```

Then retry.

**Verify it works:**

```bash
claude --version    # should print a version number
claude doctor       # should show green checkmarks
```

Run `claude` once in any folder. You'll be prompted to log in via browser. Use your paid Claude account.

## 3. Python 3.11 or higher

The workshop tool is built in Python. Check:

```bash
python --version   # or: python3 --version
```

If you're below 3.11, install via [python.org](https://www.python.org/downloads/), Homebrew (`brew install python@3.12` — Homebrew is a popular tool installer for macOS), or your operating system's package manager.

## 4. The seed repo cloned

Don't try to clone at the coffee shop on shared Wi-Fi — do this at home.

The seed lives inside the workshop repo, in the `seed/` subfolder. Clone the workshop repo and navigate into it:

```bash
git clone https://github.com/thepandanlabs/claude-decisions-workshop.git
cd claude-decisions-workshop/seed
```

Then install the tool and verify it runs:

```bash
uv tool install --editable .   # or: pip install -e .
decisions --help
decisions add inbox/
```

The last command should process the five sample transcripts without error. v0.1 extracts decisions only — you will see 0 action items. That's expected. The stubs add the rest.

The seed folder ships with:

- `PRD.md` — the one-page spec for the decisions CLI, with five stub sections.
- `CLAUDE.md` — the extraction rules.
- `.claude/commands/` — the four slash commands (`/prime`, `/plan`, `/implement`, `/verify`).
- `inbox/` — five sample KSA meeting transcripts.
- `src/decisions/` — stub source files (Claude builds the implementation during the workshop).
- `tests/` — a minimal automated test suite (one idempotency test, one schema test).

## Also helpful

- **Git installed.** Windows: install [Git for Windows](https://git-scm.com/download/win) so Claude Code's Bash tool works correctly.
- **A code editor.** VS Code, Cursor, or whatever you already use. Not strictly required — Claude Code edits files for you — but useful for reading the diffs (the change summaries Claude shows as it builds).
- **A meeting transcript of your own** (anonymised, as a `.txt` file) if you want to test the tool on something beyond the supplied samples. Optional.

## Day-of setup

Arrive at 100% battery. Coffee-shop power outlets are unreliable. A 2-hour workshop running Claude Code on Sonnet will drain a laptop to ~30%.

Bring your phone with mobile hotspot ready. Coffee-shop Wi-Fi is the single most common failure mode.

## If something is broken the morning of the workshop

Run `claude doctor` and read the output. If it doesn't fix itself, message the facilitator with the **exact** error text — not a paraphrase. Don't show up with nothing installed; the room has 6–12 people and one facilitator, and one broken laptop can swallow ten minutes.

[← Back to home](../index.html)
