# Contributing

Contributions should improve the reusable operating model without adding private deployment assumptions.

## Before opening a change

- Use synthetic data.
- Check for secrets and personal identifiers.
- Keep provider-specific details in examples or separate integration notes.
- Explain the problem the change solves.
- Add or update documentation and acceptance criteria.

## Local checks

Run these commands before opening a pull request:

```sh
python scripts/check_public_safety.py
bash scripts/install-hooks.sh
bash .githooks/pre-commit
```

For a full-history secret scan, install Gitleaks and run it from the repository root:

```sh
brew install gitleaks
gitleaks git --redact --verbose
```

The GitHub Action uses full history (`fetch-depth: 0`) and a pinned Gitleaks action/tool version. Dependabot checks GitHub Action updates monthly. Update the action SHA and `GITLEAKS_VERSION` together, run the local checks, and document the version change.

For Markdown links, the CI-equivalent tool is Lychee. Install it using the method documented by Lychee for your platform, then run:

```sh
lychee --verbose --no-progress --exclude 'https://example.org/synthetic-source' './**/*.md'
```

A real broken link should fail CI. The synthetic example URL is excluded deliberately; replace it with a real source only in a private installation. External sites can be temporarily unavailable, so investigate a link-check failure before changing the exclusion list.

## Pull request checklist

- [ ] No credentials, private data, or machine-specific identifiers.
- [ ] Public/private boundary remains clear.
- [ ] Examples are fictional or generalized.
- [ ] Documentation explains the trade-off, not only the command.
- [ ] Validation scripts pass.
- [ ] `python scripts/test_evaluations.py` passes when routing or workflow contracts change.
- [ ] `gitleaks git --redact --verbose` passes for the full history.
- [ ] Lychee passes for Markdown links, with only documented synthetic exclusions.

## Style

Prefer plain Markdown, small focused workflows, explicit assumptions, and evidence-based claims.
