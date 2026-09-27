# How the system works

This guide explains the system without assuming prior knowledge of AI agents.

## 1. A personal AI system is a small operating system

A chatbot answers a message. A personal AI operating system maintains context, follows procedures, uses tools, and records what happened.

```mermaid
flowchart TD
    H[Human intent] --> C[Conversation and clarification]
    C --> R[Routing]
    R --> M[Memory retrieval]
    M --> W[Workflow and skills]
    W --> G[Generation or tool call]
    G --> V[Review and verification]
    V --> D[Durable record]
    V --> A[Approved external action]
```

The important shift is from *prompt in, answer out* to *intent in, governed result out*.

## 2. The public/private split

The public project contains reusable ideas. A real installation adds private identity, knowledge, accounts, and integrations.

```mermaid
flowchart LR
    P[Public core\nDocs, templates, skills] --> I[Private installation]
    I --> K[Private knowledge]
    I --> X[Private integrations]
    I --> T[Private preferences]
    K -. never sync automatically .-> P
    X -. never sync automatically .-> P
    T -. never sync automatically .-> P
```

This direction matters. The private layer may consume public improvements, but private data should never flow back into the public repository automatically.

## 3. What happens when a request arrives

Example: “Turn this article into a LinkedIn post.”

```mermaid
sequenceDiagram
    participant U as User
    participant A as Assistant
    participant K as Knowledge base
    participant S as Source/web
    participant R as Review gate

    U->>A: Request adaptation
    A->>K: Search related notes and style
    A->>S: Verify current claims
    S-->>A: Sources and limits
    A->>A: Draft canonical argument
    A->>A: Adapt to LinkedIn
    A->>R: Present draft and evidence
    R-->>A: Approve or revise
    A->>K: Store final draft, sources, lesson
```

The assistant should not publish simply because it can generate a good draft.

## 4. Four states of truth

A tool call is not the same as a verified outcome.

```mermaid
stateDiagram-v2
    [*] --> Proposed
    Proposed --> Accepted: human approval
    Accepted --> Executed: tool call
    Executed --> Observed: result returned
    Observed --> Verified: read-back/check passes
    Observed --> NeedsReview: result incomplete or ambiguous
    NeedsReview --> Proposed
    Verified --> [*]
```

Use these words in logs and reports. They prevent “the API returned 200” from being confused with “the intended change is visible in the target system.”

## 5. Why memory needs structure

Memory is more useful when it has an owner and status.

```mermaid
graph TD
    N[New information] --> P[Preserve provenance]
    P --> C[Classify]
    C --> F{What is it?}
    F -->|Preference| U[User profile]
    F -->|Decision| D[Decision record]
    F -->|Project context| J[Project note]
    F -->|Procedure| S[Skill or runbook]
    F -->|Temporary detail| T[Session only]
```

Do not turn the memory system into an unsearchable transcript archive.

## Rendering diagrams

GitHub renders Mermaid diagrams in Markdown. If a different renderer does not support Mermaid, the surrounding text should still explain the workflow in plain language.
