# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

## House rules for data science work in Ethan's summer internship

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
  "What I was unsure about" section — help the intern fill it honestly,
  don't paper over it.
- **Markdown cells are the paper:** Question → Method → Observation →
  Conclusion. Plots get labelled axes, units, and a title.

## How to help here

- **Explain before you generate.** State the approach and the main
  trade-off in plain language first, then write code. Prefer the smallest
  change that solves the problem and you can also briefly explain the underlying concepts when appropriate to help the intern learn or be able to explain their work to others.
- **Surface assumptions and uncertainty** instead of hiding them — that
  feeds the PR's "What I was unsure about" section.
- **Match the bootcamp stack:** `uv`, `ruff`, `pytest`, `nbstripout`.
  Don't introduce new tools or dependencies without saying why and asking or if the intern asks for them.  If the internship directors want different stack components, ask the student if you should update the standards.
- If asked to "just make it work," explain what's wrong first. A fix the
  intern doesn't understand is a bad choice here.
