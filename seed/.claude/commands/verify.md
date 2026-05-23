Run the verification checklist in this order. Fix any failures before moving to the next step.

1. `pytest tests/ -v` — all tests must pass
2. `decisions add inbox/` — must process 5 transcripts without error
3. `decisions add inbox/` (again) — must report "5 files skipped (already processed)" and add zero records
4. `decisions query --open` — must return results without error
5. `decisions report --week 2026-W21` — must print a structured markdown briefing without error

If any step fails: read the error, fix the underlying cause, re-run from step 1.
Do not move on while any step is failing.
