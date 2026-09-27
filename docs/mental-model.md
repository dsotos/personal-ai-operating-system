# Mental model

A personal AI operating system is not one prompt. It is a set of cooperating layers.

```text
Human intent
    ↓
Conversation and clarification
    ↓
Routing and workflow selection
    ↓
Memory retrieval and source gathering
    ↓
Reasoning and generation
    ↓
Review and approval
    ↓
Tool execution
    ↓
Verification and durable record
```

## The five questions every workflow should answer

1. What is the user trying to achieve?
2. What context is required, and where does it come from?
3. Which tools or skills are allowed?
4. What would count as a successful result?
5. What must be verified before reporting completion?

## State vocabulary

- **Proposed:** a possible plan or draft exists.
- **Accepted:** the human approved the plan or side effect.
- **Executed:** a tool or external system was called.
- **Observed:** the tool returned a result.
- **Verified:** a read-back or independent check confirms the intended state.

Do not collapse these states into a single claim such as “done.”

## Three memory types

- **Identity and preferences:** stable facts about the person and their working style.
- **Knowledge base:** notes, sources, decisions, projects, and reusable context.
- **Procedures:** repeatable workflows, checklists, and lessons learned.

Keep secrets and live credentials outside all three public layers.
