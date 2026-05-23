# From Meetings to Decisions — Workshop Kit

A 2-hour workshop for managers (tech or non-tech) in KSA/Riyadh. Attendees build a `decisions` CLI that processes meeting transcripts into a queryable SQLite ledger — something a chat interface structurally cannot produce.

**Workshop site:** [thepandanlabs.github.io/claude-decisions-workshop](https://thepandanlabs.github.io/claude-decisions-workshop)

**Seed repo** (attendees clone this): [thepandanlabs/decisions-seed-repo](https://github.com/thepandanlabs/decisions-seed-repo)

## What attendees build

A `decisions` CLI that:
- Processes a folder of meeting transcripts in one command
- Extracts decisions, action items, owners, and deadlines via Claude
- Stores everything in a persistent SQLite ledger with SHA-256 deduplication
- Answers cross-meeting queries like `decisions query --owner "Ahmed" --open`

The key insight: a chat interface can summarise one meeting. This tool accumulates across weeks and queries across meetings — something fundamentally different.

## Structure

```
claude-decisions-workshop/
├── index.html              # Landing page
├── viewer.html             # Generic markdown renderer (no build step)
├── days/                   # 6 workshop block files
├── resources/              # Prerequisites, CLAUDE.md template, glossary, etc.
├── tracks/                 # 4 manager extension tracks
└── scripts/
    └── verify-links.sh     # Link checker
```

## Running locally

```bash
python3 -m http.server 8080
# Open http://localhost:8080
```

No build step. No dependencies. Works from the filesystem.

## Deploying

See `DEPLOY.md`. GitHub Pages from `main` / root. The `.nojekyll` file is required.

## By Pandan Labs

Built for the Riyadh manager community. Same workflow discipline as the developer workshop — different tool, different audience.
