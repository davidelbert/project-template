# Common tasks, one word each. Run `make <target>`.
# This is the RUNBOOK as runnable commands — keep the two in sync.

.PHONY: help setup data test lint nb clean

help:                ## Show this help
	@grep -E '^[a-z]+:.*##' $(MAKEFILE_LIST) | sed 's/:.*##/\t/'

setup:               ## Create the venv and install the project
	uv venv
	uv pip install -e ".[dev,data]"

data:                ## Fetch raw data into data/raw/ (see DATA.md)
	uv run python scripts/fetch_data.py

test:                ## Run the test suite
	uv run pytest

lint:                ## Run the linter
	uv run ruff check .

nb:                  ## Launch Jupyter Lab
	uv run jupyter lab

clean:               ## Remove caches and the venv (not your data)
	rm -rf .venv .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
