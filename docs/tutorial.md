# Tutorial: build your first private installation

This tutorial creates a small, safe personal AI operating model. It does not require exposing any private data to this repository.

## Step 1: choose the source of truth

Pick one place for durable knowledge. Examples include an Obsidian vault, a Git repository, or a private document system. Other search indexes may mirror it, but they should not silently become the authority.

Write down:

- where durable notes live;
- how projects are organized;
- how decisions are recorded;
- how sources are cited;
- what must never leave the private system.

## Step 2: define identity separately from memory

Create a private identity file containing your name, language, timezone, preferences, and working style. Keep it outside this public repository.

Do not put your real identity into the public templates.

## Step 3: add one workflow

Start with `workflows/source-to-note.md` or `workflows/idea-to-content.md`. A single reliable workflow is more useful than a large catalogue that nobody trusts.

Test with a fictional article and fictional project before connecting real sources.

## Step 4: add review gates

Make drafts local and publishing explicit. The assistant may prepare a post, but it should not publish it until you approve the exact target and content.

## Step 5: measure usefulness

After a week, review:

- which notes were retrieved correctly;
- which workflows saved time;
- where the assistant guessed;
- which approvals were unclear;
- which procedures should become reusable skills.

Keep improving the workflow, not just the prompt.

## Regression evaluations

Run the synthetic routing fixtures and policy checks with:

```sh
python scripts/test_evaluations.py
```

The fixtures cover all seven routing categories, ambiguity, restricted data, missing authorization, tool failure, and post-publication discrepancy. They validate the declared contract mechanically; they do not simulate an AI router or replace human review. Add a synthetic case to `examples/routing-evaluations.json` when a new boundary or regression is discovered.

## Step 6: connect tools gradually

Add one integration at a time. For each integration document:

- required permissions;
- data sent to the service;
- approval boundary;
- verification method;
- rollback or disable path.
