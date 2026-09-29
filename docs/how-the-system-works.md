# How the system works

This guide explains the system without assuming prior knowledge of AI agents.

## 1. A personal AI system is a small operating system

A chatbot answers a message. A personal AI operating system maintains context, follows procedures, uses tools, and records what happened.

```mermaid
flowchart TD
    H[Human intent] --> C[Conversation and clarification]
    C --> O[Hermes orchestrator]
    O <--> K[Obsidian private knowledge vault]
    O --> R[Routing and specialist selection]
    R --> S[Focused agent or workflow]
    S --> O
    O --> V[Review and verification]
    V --> D[Curated durable note back to Obsidian]
    V --> A[Approved external action]
```

The important shift is from *prompt in, answer out* to *intent in, governed result out*.

The persistent knowledge layer in this architecture is **Obsidian**: a private, linked vault for curated memory, projects, sources, decisions, and procedures. Hermes retrieves relevant context from it and coordinates specialists; verified durable results can be recorded back into it. The vault is not a transcript dump and never flows into the public repository.

![Full system diagram: Hermes, Obsidian, specialist agents, tools, and approval gates](architecture.svg)

## 1a. Hermes coordinates specialist agents

Hermes is the orchestrator, not the only worker. It routes each request to a bounded specialist and remains responsible for coordinating, applying approval rules, and checking the outcome.

```mermaid
flowchart LR
    U[Human] --> H[Hermes\nOrchestrator]
    H -->|monitor and document| M[Media and LinkedIn agent]
    H -->|track upcoming trips| T[Travel agent]
    H -->|research and draft| C[Content agent]
    H -->|prepare private billing files| I[Invoicing agent]
    M --> H
    T --> H
    C --> H
    I --> H
    H --> G{External action?}
    G -->|yes: request approval| A[Human review]
    G -->|no| V[Verify and record]
    A --> V
```

The specialists are examples of focused roles, not universal defaults. A deployment can implement them as separate agents or as narrowly scoped workflows. Either way, give each only the data and tools its task requires; drafts and preparations do not automatically authorize publishing, sending, or payment.

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
    participant H as Hermes orchestrator
    participant K as Obsidian vault
    participant S as Source/web
    participant W as Content specialist
    participant R as Review gate

    U->>H: Request adaptation
    H->>K: Retrieve relevant context and style
    H->>S: Verify current claims
    S-->>H: Sources and limits
    H->>W: Ask for a channel-ready draft
    W-->>H: Draft and rationale
    H->>R: Present draft and evidence
    R-->>H: Approve or revise
    H->>K: Store verified draft, sources, and lesson
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
