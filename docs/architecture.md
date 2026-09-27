# Architecture

## Public core and private overlay

The public core contains generic procedures and templates. The private overlay contains the identity, data, integrations, and deployment decisions of one person.

```text
public-core/
├── docs/
├── templates/
├── skills/
└── workflows/

private-overlay/
├── identity/
├── memory/
├── writing-samples/
├── integrations/
└── local-config/
```

The safe flow is from public core into a private installation. Do not automatically publish from the private overlay back to the public repository.

## Recommended components

- **Conversation layer:** the assistant and its channel adapters.
- **Memory layer:** a human-readable knowledge base with stable paths and links.
- **Skill layer:** reusable procedures loaded when relevant.
- **Routing layer:** deterministic rules plus model selection for complex cases.
- **Tool layer:** filesystem, web, code, browser, messaging, and scheduling capabilities.
- **Review layer:** approval gates for publishing, messaging, payments, and destructive changes.
- **Verification layer:** read-back checks, tests, and evidence records.

## Integration rule

Integrations should be replaceable. Keep provider-specific credentials and adapters in the private overlay; keep the workflow contract provider-neutral.
