# TODO: SQLite read/write operations.
# - Apply migrations/0001_init.sql on first run
# - write_record(record: dict) -> None — insert or skip (SHA-256 dedup)
# - read_records(filters: dict) -> list[dict] — query with optional filters
# See CLAUDE.md Conventions section for deduplication rules.
# No network calls in this file.
