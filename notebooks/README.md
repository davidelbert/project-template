# Notebooks

Conventions for this folder:

- **Numbered and verb-prefixed**: `01-explore-dataset.ipynb`, `02-clean-and-summarize.ipynb`. Order matters; topic matters; tense doesn't.
- **One narrative per notebook.** New analysis = new notebook.
- **Restart-and-run-all must succeed** before every commit.
- **Markdown cells are the paper.** Each section: Question → Method → Observation → Conclusion.
- **Code that's reused or longer than ~15 lines** moves to `src/myproject/`. Notebooks import from there.

Start a new notebook by copying `_TEMPLATE.ipynb` — it already has the
four-section structure and a parameters cell laid out for you.
