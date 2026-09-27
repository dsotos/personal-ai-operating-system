# Privacy model

A useful personal assistant needs context, but context does not mean everything should be exposed to every tool or model.

## Data classes

- **Public:** information safe to publish.
- **Private:** personal notes and preferences needed for the user's assistant.
- **Sensitive:** credentials, financial, health, client, legal, or access-control data.
- **Restricted:** information that should remain in a particular system or channel.

## Handling rules

- Minimize the context passed to each workflow.
- Prefer summaries and identifiers over raw records.
- Keep secrets in environment-specific secret stores.
- Redact personal identifiers before using examples or logs.
- Use synthetic data in tests and documentation.
- Separate drafting from publishing credentials.
- Keep channel allowlists explicit and fail closed when uncertain.

## Public documentation rule

If an example could identify a real person, company, account, machine, project, or private channel, replace it with a fictional equivalent or remove it.
