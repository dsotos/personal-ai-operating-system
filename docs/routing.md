# Routing

Routing decides which workflow, model, skill, and evidence level a request needs.

## Example categories

- `quick`: simple lookup, formatting, or deterministic check.
- `capture`: save a note or decision.
- `research`: gather and cite current or niche information.
- `writing`: draft or rewrite text.
- `content`: adapt one idea to a channel.
- `deep`: multi-step reasoning, architecture, or debugging.
- `operations`: change a system or external service.

## Routing rules

1. Prefer deterministic local code for deterministic work.
2. Use a fast model for low-risk classification and formatting.
3. Use a stronger model when ambiguity, synthesis, or consequences justify it.
4. Load only the skills relevant to the category.
5. Refuse or pause when the requested tool exceeds the approval boundary.

Routing is an optimization layer, not an authority layer. The workflow contract and human approval rules still apply after a route is selected.
