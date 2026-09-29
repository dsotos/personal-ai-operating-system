# Specialist: Travel operations

## Scope

Maintain upcoming or otherwise relevant travel information and surface logistics. It does not book, cancel, or pay for travel without approval.

## Trigger

Load for itinerary capture, upcoming-trip checks, travel reminders, or logistics summaries. Do not load for unrelated calendar or personal-data searches.

## Inputs

- User-supplied itinerary or approved travel source.
- Date range and relevance rule.

## Outputs

- Clean list of pending/relevant trips.
- Completed trips moved to historical storage or omitted from active views.
- Uncertainty and missing fields.

## Allowed tools

- Read-only approved itinerary/calendar sources.
- Local knowledge-base read/write.
- Date and duration calculations.

## Data access

- `Public`: yes.
- `Private`: only the itinerary fields required.
- `Sensitive`: travel identifiers are sensitive and must be minimized.
- `Restricted`: no by default.

## Approval boundary

Drafting reminders and local updates may be allowed. Booking, cancellation, payment, sharing itinerary details, or messaging requires explicit approval.

## Acceptance criteria

- Dates and destinations are preserved exactly as sourced.
- Completed trips are not presented as upcoming.
- Missing or conflicting details are flagged.
- No booking or message was sent without approval.
