# Data

Raw data is **never committed to this repo**. This file is the contract:
it says exactly where the data came from and how to get it back, so a
collaborator (or you, in six months) can reproduce the project from zero.

Fill every field in. "I'll remember" is how data provenance gets lost.

## Source

- **Project / dataset name:**
- **OSF project URL:**            (e.g. https://osf.io/abcde/)
- **OSF project ID:**             (the 5-char code, e.g. `abcde` — used by `scripts/fetch_data.py`)
- **DOI (if minted):**
- **Contact / depositor:**        (who at UVM Open Science owns this)
- **Date downloaded:**            (YYYY-MM-DD — data on OSF can change)

## License & usage terms

- **Data license:**               (e.g. CC-BY-4.0, CC0, "restricted — see below")
- **Citation (required form):**
- **Restrictions:**               (embargo, attribution, no-redistribution, IRB conditions)
- **Sensitive / PII:**            (yes/no — if yes, what, and what handling is required)

> The data license is separate from this repo's code LICENSE. OSF deposits
> are often CC-BY (cite to use) and sometimes restricted. If you're unsure,
> ask before sharing results outside the team.

## How to fetch it

```bash
# Public OSF project — no credentials needed:
uv run python scripts/fetch_data.py --project <OSF_PROJECT_ID>

# Or set it once:
export OSF_PROJECT=<OSF_PROJECT_ID>
uv run python scripts/fetch_data.py
```

Files land in `data/raw/`. If the data is **not** on OSF, replace the
command above with the exact steps (URL, login, manual export) someone
would follow — be literal.

## Schema / data dictionary

One row per column (or per file). Fill this in while you explore — it is
half of Step 5's first issue.

| Column | Type | Units | Description | Notes / quirks |
|--------|------|-------|-------------|----------------|
|        |      |       |             |                |

## Known quirks

Anything that bit you: weird encodings, sentinel values for missing data
(`-999`, `"N/A"`, blanks), duplicated rows, timezone assumptions, column
names that lie. Future-you will thank present-you.
