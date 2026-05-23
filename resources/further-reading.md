# Further Reading

Curated. Current as of May 2026. Each link is something worth an evening, not a comprehensive index.

## The official sources

- **Claude Code documentation** — `code.claude.com/docs`
- **Claude Code Quickstart** — `code.claude.com/docs/en/quickstart`
- **Claude Code Best Practices** — `code.claude.com/docs/en/best-practices`
- **Anthropic engineering blog** — `anthropic.com/engineering`
- **Claude Code 101 free course** — `anthropic.skilljar.com/claude-code-101`
- **Pricing (Pro $20/month, verified May 2026)** — `claude.com/pricing`
- **Supported countries (Saudi Arabia listed)** — `anthropic.com/supported-countries`

## On the workflow

- **"A conversation on Claude Code"** — Boris Cherny (the creator) and Alex Albert. YouTube, June 2025, ~21 minutes. Watch this. He describes the Plan Mode workflow in his own words: *"If my goal is to write a Pull Request, I will use Plan mode, and go back and forth with Claude until I like its plan. From there, I switch into auto-accept edits mode and Claude can usually 1-shot it. A good plan is really important."*
- **"Best practices for Claude Code"** — Anthropic. Read it once. Then read it again after you've built two projects — different sentences land the second time.

## On evals and verification

The canonical reading is Hamel Husain. Don't read everything — read these two, in order:

- **"Your AI Product Needs Evals"** — `hamel.dev/blog/posts/evals/`. Thirty minutes. Read first. Read once a quarter.
- **"Using LLM-as-a-Judge For Evaluation"** — `hamel.dev/blog/posts/llm-judge/`. Read second, when you want to add an AI-powered check on top of hand-labelling.

For a longer treatment: **"A Field Guide to Rapidly Improving AI Products"** (Hamel Husain, O'Reilly, July 2025). Two hours. Read when you're past your second project.

## On agents and automation

- **"Building effective agents"** (Schluntz and Zhang, Anthropic, December 2024) — `anthropic.com/engineering/building-effective-agents`. Required reading before building Track C (Slack watch). The prompt chaining and evaluator-optimiser patterns apply directly to an agent that watches a folder and escalates uncertain extractions.
- **Claude Agent SDK overview** — `code.claude.com/docs/en/agent-sdk/overview`. The current source of truth for building autonomous agents on top of Claude Code.

## On MCP

- **MCP spec home** — `modelcontextprotocol.io`. Read "Concepts" first.
- **MCP TypeScript SDK** — `github.com/modelcontextprotocol/typescript-sdk`. v1.x is current stable as of May 2026. Use v1 for Track D.
- **Claude Desktop config docs** — search for `claude_desktop_config.json` in the Anthropic docs.

## Community resources

- **"A Complete Guide to Claude Code"** by Cole Medin. YouTube, August 2025, ~50 minutes. Slash commands, MCP, PRP framework (Plan-Review-Prompt: a structured prompting workflow), subagents. Best single overview if you're past the first project.
- **The Claude Code Handbook** — freeCodeCamp. Comprehensive intro, free.

## The reading order if you have one weekend

1. Watch **Cherny + Albert "A conversation on Claude Code"** (21 min).
2. Read **Hamel's "Your AI Product Needs Evals"** (30 min).
3. Read **Anthropic's "Best practices for Claude Code"** (20 min).
4. Pick one extension track. Build it.

That's a Saturday. By Sunday, you have a real tool.

[← Back to home](../index.html)
