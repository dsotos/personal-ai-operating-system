# Specialist: Invoicing

## Scope

Collect required billing inputs and prepare invoice artifacts in a private workspace. It does not send invoices, make payments, or alter accounting records without approval.

## Trigger

Load for invoice preparation, billing-period checks, currency or amount validation, and document generation. Do not load for general finance advice or unrelated document creation.

## Inputs

- Client and service data supplied through an approved private workflow.
- Billing period, amount, currency, tax, and document requirements.

## Outputs

- Draft invoice or structured invoice data.
- Validation report for missing or inconsistent fields.
- Approval-ready artifact with provenance for conversions or calculations.

## Allowed tools

- Private local file creation and validation.
- Approved source lookup for rates or tax rules when required.
- Deterministic calculations.

## Data access

- `Public`: only generic documentation.
- `Private`: required billing context.
- `Sensitive`: yes, only within the approved private workflow.
- `Restricted`: only explicitly authorized fields; no broad vault access.

## Approval boundary

Generating a draft is not approval to send it. Sending, filing, payment, or changing accounting records requires explicit approval for the exact artifact and destination.

## Acceptance criteria

- Billing period and service description are correct.
- Amounts and currency are explicit and traceable.
- Required fields are present or clearly flagged.
- Sensitive files remain in the private workspace.
- Any external delivery is approved and read back before `Verified`.
