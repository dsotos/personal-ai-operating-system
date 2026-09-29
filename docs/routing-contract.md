# Routing contract

Routing maps the seven categories below to an operational lane, evidence level, and tool boundary. A lane describes a workflow posture, not a model name. Routing never grants permission by itself.

| Category | Lane | Evidence level | Allowed tools by default | Approval default |
|---|---|---|---|---|
| `quick` | `fast-local` | none or supplied context | local file read, deterministic scripts | no external effect; escalate if scope changes |
| `capture` | `knowledge-capture` | provenance required | private knowledge-base read/write, local validation | approval only if the note contains restricted data or changes a controlled record |
| `research` | `source-backed` | source-backed and dated | web search/extraction, read-only knowledge-base search, local text processing | no publication or messaging; escalate for restricted sources |
| `writing` | `drafting` | supplied context or cited sources | local drafting, style checks, read-only knowledge search | draft approval is separate from publication approval |
| `content` | `channel-adaptation` | canonical thesis plus relevant sources | local drafting, source lookup, read-only knowledge search | explicit approval before publishing or sending |
| `deep` | `deep-reasoning` | explicit assumptions, evidence, and review | specialist skills, code/read-only tools, delegation when configured | approval for external or irreversible effects |
| `operations` | `controlled-operation` | pre/post state and read-back | only the named operational tool and verification read-back | explicit approval before external, destructive, access, or production changes |

## Ambiguity and escalation

- If multiple categories fit, select the most restrictive evidence and approval posture until clarified.
- If the request changes from drafting to sending or publishing, re-route to `operations` for the side effect.
- If restricted data is required, pause and request an explicit scope rather than widening access implicitly.
- If a tool fails, do not infer success; record `NeedsReview` with the failure and next check.
- A model, specialist, or route cannot approve its own action.

## Lane semantics

- `fast-local`: cheap, deterministic, no network by default.
- `knowledge-capture`: preserve provenance and durable state.
- `source-backed`: verify current or niche claims.
- `drafting`: produce a reviewable draft without external effects.
- `channel-adaptation`: change format while preserving the canonical thesis.
- `deep-reasoning`: spend more context and review on ambiguity or consequence.
- `controlled-operation`: execute a named side effect only after approval and verify it afterward.

The lane can be implemented with different models or tools. The contract remains valid when providers change.
