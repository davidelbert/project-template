# Runbook

The literal "from zero" procedure for this project. Commands, not prose.
If a step here is wrong, the runbook is the bug — fix it in the same PR.

## 0. Prerequisites

- `uv` installed (`uv --version`)
- `gh` authenticated (`gh auth status`)
- Repo cloned, you're in the repo root

## 1. Build the environment

```bash
uv venv
uv pip install -e ".[dev]"        # add ,data for the OSF fetcher: ".[dev,data]"
```

## 2. Get the data

See **DATA.md** for the source and license. Then:

```bash
uv run python scripts/fetch_data.py --project <OSF_PROJECT_ID>
```

Verify: `ls data/raw/` shows the expected files.

## 3. Run the analysis

Open the notebooks in numeric order and, for each one, use
**Kernel → Restart Kernel and Run All Cells**:

```bash
uv run jupyter lab
```

`01-explore` → `02-clean` → `03-summarize` → `04-analysis`. A notebook
that only works when run out of order is broken.

## 4. Check it

```bash
uv run pytest          # tests for code in src/
uv run ruff check .    # lint
```

Both must pass before you open a PR. CI runs the same two commands.

## 5. Where things land

- `data/raw/`       — fetched inputs (gitignored)
- `data/processed/` — cleaned/derived data (gitignored)
- `notebooks/`      — the narrative; outputs stripped by `nbstripout`
- `src/myproject/`  — reusable functions the notebooks import

## Common failures

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: myproject` | env not installed / wrong venv | re-run step 1; `uv run` prefixes the right venv |
| Notebook works only run top-to-bottom out of order | hidden cell-order state | Restart-and-run-all; fix the ordering |
| `scripts/fetch_data.py`: `osfclient` not found | `[data]` extra not installed | `uv pip install -e ".[dev,data]"` |
| CI red, green locally | uncommitted file or stripped-output diff | `git status`; ensure `nbstripout` is installed |
| Empty/garbled CSV | encoding or sentinel values | see DATA.md "Known quirks" |

## Who to ask

Reviewer: **Dad**. Open an issue describing what you tried and what you
expected before pinging — writing it up usually finds the bug.
