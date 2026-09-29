# Specialist: Media and LinkedIn tracking

## Scope

Find, verify, and record public media appearances or professional mentions. It does not publish, contact journalists, or infer identity from a name match alone.

## Trigger

Load for requests to monitor public coverage, verify an appearance, or update a dated media index. Do not load for drafting a new post unless source verification is the explicit need.

## Inputs

- Search topic, person/profile criteria, or supplied source.
- Date range and geography, when relevant.

## Outputs

- Verified record with source, title, publication date, link, identity evidence, and uncertainty.
- Duplicate or conflicting-record note.

## Allowed tools

- Web search and read-only source extraction.
- Read-only search and controlled write to a private publications index.
- Local duplicate checks.

## Data access

- `Public`: yes.
- `Private`: only the minimum publication metadata needed.
- `Sensitive`: no.
- `Restricted`: no.

## Approval boundary

Updating a private local index may be allowed by the installation policy. External publication, outreach, or sharing a private record requires explicit approval.

## Acceptance criteria

- The source URL resolves or the limitation is recorded.
- Publication date and title come from the source or are marked unknown.
- Identity is verified against the approved profile criteria.
- Duplicate handling is explicit.
- No external message or publication was sent.
