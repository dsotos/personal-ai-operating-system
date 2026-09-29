# Generic specialist ficha

## Name

`SPECIALIST_NAME`

## Scope

What this specialist owns and what it explicitly does not own.

## Trigger

Requests that should load this specialist. Include non-trigger examples.

## Inputs

- Required context.
- Optional context.
- Provenance and freshness requirements.

## Outputs

- Expected artifact or result.
- Evidence and uncertainty.
- Handoff destination, if any.

## Allowed tools

List tools by capability, not by secret or machine-specific identifier.

## Data access

State whether the specialist may access `Public`, `Private`, `Sensitive`, and `Restricted` data. Follow `docs/privacy.md`; a handoff does not widen access.

## Approval boundary

State what can be prepared locally and which actions require explicit human approval.

## Acceptance criteria

Use observable checks: required fields, source trail, destination, read-back, or test result.
