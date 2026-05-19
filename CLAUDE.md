# Working agreement for this repo

This is a **learning project**. The goal is the student understanding the
code and the workflow — not finishing fast. If you're an AI assistant
(Claude Code, Cursor, etc.) working in this repo, optimize for that.

Per the bootcamp, the student uses AI to *explain* code through Step 6 and
to *help write* code from Step 7 on. Respect that staging.

## House rules

- **Notebooks are front-ends.** Reusable logic, anything reused, or any
  block longer than ~15 lines goes in `src/<package>/`; the notebook
  imports it. Don't pile logic into cells.
- **Restart-and-run-all is the contract.** Never produce a notebook that
  depends on out-of-order cell execution. Imports at the top; parameters
  in one cell near the top.
- **Data never goes in git.** It lives in `data/` (gitignored). Document
  provenance in `DATA.md`; fetch via `scripts/fetch_data.py`. Don't
  inline dataset contents or hard-code absolute paths.
- **Small commits, one issue per PR.** Every PR includes a
  "What I was unsure about" section — help the student fill it honestly,
  don't paper over it.
- **Markdown cells are the paper:** Question → Method → Observation →
  Conclusion. Plots get labelled axes, units, and a title.

## How to help here

- **Explain before you generate.** State the approach and the main
  trade-off in plain language first, then write code. Prefer the smallest
  change that teaches the concept.
- **Surface assumptions and uncertainty** instead of hiding them — that
  feeds the PR's "What I was unsure about" section.
- **Don't do the learning steps for the student.** Don't auto-run
  notebooks, don't `git commit`/`git push`/merge PRs, and don't refactor
  beyond what was asked. Suggest; let them drive.
- **Match the bootcamp stack:** `uv`, `ruff`, `pytest`, `nbstripout`.
  Don't introduce new tools or dependencies without saying why and asking.
- If asked to "just make it work," explain what's wrong first. A fix the
  student doesn't understand is a failure here.
