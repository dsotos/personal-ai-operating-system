# Run log

Use one copy of this template for each meaningful execution. Replace every `EXAMPLE_*` marker in a private workspace; do not place real secrets or personal data in a public repository.

## Run metadata

- Run ID: `EXAMPLE_RUN_ID`
- Date/time (ISO 8601): `2026-01-15T10:30:00Z`
- Actor: `EXAMPLE_HUMAN_OR_AGENT`
- Request: `EXAMPLE_REQUEST`
- Route/category: `EXAMPLE_CATEGORY`
- Data classes accessed: `Public | Private | Sensitive | Restricted`
- Intended target/destination: `EXAMPLE_TARGET`

## State transitions

Record the five states exactly as defined in `docs/mental-model.md`. A tool attempt is not proof of execution, and a returned result is not proof of verification.

### Proposed

- Date/time:
- Actor:
- Decision or plan:
- Tools proposed:
- Evidence references:
- Result/notes:

### Accepted

- Date/time:
- Actor approving:
- Exact scope accepted:
- Approval record link:
- Tools allowed:
- Evidence references:
- Result/notes:

### Executed

- Date/time:
- Actor/tool:
- Exact operation attempted:
- Target:
- Tool invocation reference:
- Evidence references:
- Result/notes:

### Observed

- Date/time:
- Actor/tool:
- Returned status or visible effect:
- Raw result location (private if needed):
- Evidence references:
- Result/notes:

### Verified

- Date/time:
- Verifier:
- Read-back or independent check:
- Compared against:
- Evidence references:
- Result/notes:

## NeedsReview (optional)

Use this state when a tool fails, the outcome is uncertain, the target cannot be read back, or the observed result differs from the approved scope.

- Reason:
- Responsible reviewer:
- Next verification step:
- Additional approval required:
- External effects blocked until resolution: `yes | no`
- Resolution and date:

## Completion rule

Do not mark `Verified` until the intended target has been read back or independently checked. If publication or delivery is uncertain, do not retry blindly; investigate the target state first.
