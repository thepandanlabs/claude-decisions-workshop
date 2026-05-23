# TODO: Claude API call and structured extraction.
# - extract(transcript_text: str, source_file: str) -> list[dict]
# - Prompt Claude with the transcript text
# - Parse and validate the JSON response against the schema in PRD.md
# - Return a list of record dicts matching the schema
# See CLAUDE.md Extraction rules section for what Claude should return.
# Never call this function from tests — use recorded fixtures instead.
