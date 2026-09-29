# Personal AI Operating System

A privacy-first, documented operating model for building a personal AI assistant around memory, reusable workflows, specialist skills, human approval, and verifiable execution.

This repository is a public reference implementation. It is intentionally generic: it contains no personal memories, credentials, private conversations, contact data, production identifiers, or user-specific configuration.

## What this is

A practical blueprint for a **personal AI operating system coordinated by Hermes**. Hermes is the orchestrator: it receives requests, chooses the right specialist agent or workflow, gives it only the context and tools it needs, combines the result, and checks whether the work was actually completed.

Specialists focus on bounded areas such as:

- **Media and LinkedIn tracking:** find relevant appearances, verify sources, and keep a dated record with links.
- **Travel operations:** maintain upcoming trips, surface relevant logistics, and retire trips once completed.
- **Content creation:** research, draft, and adapt material for different channels; publishing remains a separate approval step.
- **Invoicing:** collect the required period and billing details, prepare the agreed documents, and handle the resulting files through a private workflow.

The exact implementation can use separate agents, profiles, skills, and scheduled workflows. The key is the operating model: Hermes coordinates; specialists have clear scopes; sensitive actions stay behind human approval.

**Obsidian is the persistent knowledge layer.** It is the private, human-readable source of truth for curated memory, project context, research sources, decisions, and reusable procedures. Hermes retrieves the relevant notes to guide work and preserves verified, durable outcomes there. Obsidian stores and connects knowledge; it does not replace Hermes as orchestrator, and it should not become a raw transcript dump.

![Architecture diagram: Hermes orchestrates specialist agents and uses Obsidian as its private knowledge hub](docs/architecture.svg)

## What this is not

- a dump of a private assistant's memory;
- a replacement for Hermes Agent, Obsidian, or any model provider; it documents how these layers can work together;
- an autonomous publishing system with credentials included;
- a universal configuration that can be copied without review.

## Design principles

1. **Private by default.** Personal data stays in a private overlay.
2. **Human approval for external effects.** Drafting is separate from publishing.
3. **Evidence over claims.** Planned, executed, observed, and verified are different states.
4. **Memory has an owner.** The knowledge base has a clear source of truth.
5. **Workflows before prompts.** Reusable procedures beat one-off instructions.
6. **Least privilege.** Tools and channels are enabled only when needed.
7. **Model-agnostic where possible.** The operating model should survive provider changes.

## Quick start

1. Read [the mental model](docs/mental-model.md).
2. Copy the templates into your own private workspace.
3. Define your source of truth for memory.
4. Add one workflow, such as `idea-to-content`.
5. Test it with synthetic data before connecting real accounts.
6. Keep the private overlay outside this repository.
7. Use the [routing contract](docs/routing-contract.md) and [specialist fichas](docs/architecture.md#hermes-as-orchestrator) before adding new capabilities.
8. Use the [Obsidian note template](templates/obsidian-note.md), keep captures in the [inbox placeholder](inbox/README.md), and review provisional notes with the [memory lifecycle](docs/memory.md).

## Repository map

- `docs/` — architecture, mental model, diagrams, tutorial, memory, routing, privacy, approvals, and content workflows.
- `templates/` — safe starting points for a personal installation.
- `skills/` — reusable capability contracts and bounded specialist fichas.
- `workflows/` — end-to-end procedures.

Key contracts:

- [Routing contract](docs/routing-contract.md)
- [Example capability](skills/source-backed-content-research.md)
- [Specialist ficha template](templates/specialist-card.md)
- `examples/` — fictional data and regression fixtures only.
- `scripts/` — validation, secret-safety, hook-installation, and evaluation scripts.
- `.github/workflows/` — full-history secret scan and Markdown link checks.

Start with [How the system works](docs/how-the-system-works.md) for the visual explanation, then follow the [first-installation tutorial](docs/tutorial.md).

## Public/private boundary

The public repository is the reusable core. A private installation may add:

- identity and preferences;
- private memories and conversations;
- personal writing samples;
- contacts and calendars;
- API keys and OAuth state;
- channel allowlists;
- real projects and publication records;
- machine-specific paths and service identifiers.

Never commit those files here. Use the examples and templates as a separate starting point.

## Status

Early public foundation. The structure is usable, but workflows and examples should be expanded through small, reviewed changes.

## License

The original documentation, templates, examples, and scripts in this repository are offered under the MIT License. Third-party software, models, and integrations retain their own licenses.
