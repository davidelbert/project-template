# makeaproject

<!-- Once CI is set up (Step 7), uncomment and update OWNER/REPO:
[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)
-->

Write one paragraph here to say: what this project is and what question it answers. Write it for someone who has never seen the project before. This repo is going to be the first deliverable you bring to the pod team meeting and then it can get filled out as you understand the project and develop things.

## Quickstart

```bash
git clone git@github.com:OWNER/REPO.git
cd REPO
uv venv
uv pip install -e ".[dev]"
uv run jupyter lab
```

Then open `notebooks/01-explore.ipynb` and run all cells.

New to this repo? Read **RUNBOOK.md** for the literal step-by-step, and
**DATA.md** for where the data comes from and how to fetch it.

## Layout

```
.
├── data/                 # not in git — see DATA.md
├── notebooks/            # numbered, narrative analyses
├── scripts/              # fetch_data.py and other one-off utilities
├── src/myproject/        # reusable functions; notebooks import from here
└── tests/                # pytest tests for src/
```

## Data

See **DATA.md** for the source, citation, license, and the exact command
to fetch the raw data. Raw data is never committed to this repo.

## Findings

(Filled in as the project progresses. Step 5's last issue is to write this section.)

## Status

Pre-alpha / in progress / archived — pick one.
