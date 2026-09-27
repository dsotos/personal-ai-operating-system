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

## Reporting

Do not open a public issue for a suspected secret or privacy leak. Remove local exposure, rotate the credential if applicable, and report privately to the repository maintainers.
