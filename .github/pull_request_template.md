## What

Brief description of what this PR changes. One or two sentences.

## Why

Why this change is needed — link the issue with `Closes #N`.

Closes #

## What I was unsure about

The single most important section. List the choices you weren't sure about, the trade-offs you considered, or the things you'd like a reviewer to look at twice. If you can't think of anything, look harder — there is always something.

## Checklist

- [ ] Restart-and-run-all succeeds on every notebook touched by this PR
- [ ] Notebook outputs are stripped (`nbstripout` is installed) or the diff is intentional
- [ ] New code in `src/` has at least a smoke test
- [ ] `uv run pytest` passes locally
- [ ] `uv run ruff check .` passes locally
- [ ] README is up to date if behavior or setup changed
