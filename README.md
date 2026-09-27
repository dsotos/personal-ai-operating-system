# Personal AI Operating System

A privacy-first, documented operating model for building a personal AI assistant around memory, reusable workflows, specialist skills, human approval, and verifiable execution.

This repository is a public reference implementation. It is intentionally generic: it contains no personal memories, credentials, private conversations, contact data, production identifiers, or user-specific configuration.

## What this is

A practical blueprint for an assistant that can:

- capture and organize knowledge;
- retrieve relevant context before acting;
- classify requests and route them to the right workflow;
- brainstorm and research with source discipline;
- turn ideas into content for different channels;
- preserve decisions and reusable procedures;
- ask for approval before external side effects;
- report what was planned, executed, and actually verified.

## What this is not

- a dump of a private assistant's memory;
- a replacement for Hermes Agent, Obsidian, or any model provider;
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

## Repository map

- `docs/` — architecture, memory, routing, privacy, approvals, and content workflows.
- `templates/` — safe starting points for a personal installation.
- `skills/` — reusable capability contracts.
- `workflows/` — end-to-end procedures.
- `examples/` — fictional data only.
- `scripts/` — validation and secret-safety checks.

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
