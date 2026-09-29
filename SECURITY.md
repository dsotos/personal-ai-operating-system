# Security and privacy

This project separates the public operating model from private deployment data.

## Never commit

- API keys, access tokens, OAuth files, cookies, passwords, or private certificates.
- Personal memories, raw chat transcripts, voice samples, address books, or calendars.
- Real phone numbers, WhatsApp/Jabber/Telegram identifiers, email addresses, or contact IDs.
- Machine-specific home directories, production URLs, cron IDs, database files, or session stores.
- Client, employer, customer, medical, financial, or confidential business information.

## Before publishing

1. Run the repository checks in `scripts/`.
2. Inspect `git diff --cached` manually.
3. Search for secrets and personal identifiers.
4. Review links, screenshots, examples, and generated files.
5. Publish only synthetic or deliberately generalized data.

## Threat model

Assume that anything in a public repository will be copied, indexed, archived, and read without context. A value that is harmless locally may reveal identity, infrastructure, or access boundaries when combined with other public information.

## Automated controls

- `scripts/check_public_safety.py` is a conservative local complement. It looks for a small set of obvious paths, assignments, and identifiers; it is not an exhaustive secret detector.
- The GitHub Action in `.github/workflows/public-quality.yml` checks out full history and runs Gitleaks against the repository. It also checks Markdown links with Lychee.
- The tracked `.githooks/pre-commit` hook runs Gitleaks on staged changes. Install it with `bash scripts/install-hooks.sh` after installing Gitleaks.

A passing local check does not prove that a repository is safe. Review staged diffs and history manually before publishing.

## Reporting a vulnerability

When GitHub Private vulnerability reporting is enabled for this repository, use the repository's **Security** tab and choose **Report a vulnerability**. Do not put credentials or exploit details in a public issue.

Enabling that feature is a manual repository-owner step under GitHub Settings → Security / Code security and analysis. Until it is enabled, report suspected leaks privately to the maintainers through an authenticated private channel; do not publish details in an issue or discussion.

If a secret was exposed, remove the exposure and rotate the credential. Rewriting Git history does not guarantee that copies, forks, caches, or logs no longer contain the old value.
