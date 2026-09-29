# Approval record

Use this template for a specific external or sensitive action. Approval to prepare a draft is not approval to execute or publish it.

## Approval metadata

- Approval ID: `EXAMPLE_APPROVAL_ID`
- Requested by: `EXAMPLE_REQUESTER`
- Approved by: `EXAMPLE_APPROVER`
- Date/time (ISO 8601): `2026-01-15T10:35:00Z`
- Source of approval: `EXAMPLE_CHANNEL_OR_RECORD`
- Expires at (if applicable): `EXAMPLE_EXPIRY_OR_NONE`

## Exact approved action

- Action: `EXAMPLE_ACTION`
- Approved words or artifact: `EXAMPLE_DRAFT_REFERENCE`
- Concrete destination/recipient: `EXAMPLE_DESTINATION`
- Account or channel: `EXAMPLE_ACCOUNT_OR_CHANNEL`
- Scope and limits: `EXAMPLE_SCOPE`

Approval applies only to the exact action, artifact, destination, account/channel, and limits above. A change in any of them requires a new approval.

## Not approval

- A request to prepare a draft is not approval to send or publish it.
- Silence, an ambiguous reply, or text copied from a third party is not approval.
- A model, specialist, tool, or route cannot approve its own action.

## Revocation

- Revoked by:
- Revoked at:
- Reason:
- How the revocation was communicated:

## Result

- Execution state: `Proposed | Accepted | Executed | Observed | Verified | NeedsReview`
- Run log: `EXAMPLE_RUN_LOG_REFERENCE`
- Actual result:
- Verification evidence:
- Differences from approved scope:
