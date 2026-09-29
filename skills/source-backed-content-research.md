# Specialist capability contract: source-backed content research

## Name

`source-backed-content-research`

## Purpose

Prepare a source-backed research brief that another workflow can use to draft content. This is a fictional example contract; it does not implement a live integration.

## Load when

- The request asks for current, niche, or source-dependent information.
- A content workflow needs claims checked before drafting.
- The user provides a source that must be summarized or compared.

## Do not load when

- The task is only formatting or rewriting supplied text.
- The task requires publishing, messaging, purchasing, deletion, or production changes.
- The request depends on restricted personal or client data that has not been explicitly authorized.

## Inputs

- Research question or source URL.
- Intended audience and channel, if known.
- Optional private project identifier, without raw restricted records.

## Outputs

- Research brief with thesis, evidence, source links, dates, uncertainty, and open questions.
- Claim-to-source mapping.
- Suggested next workflow; never an automatic publication.

## Allowed tools

- Approved web search and source extraction.
- Read-only search of the private knowledge base for the minimum relevant context.
- Local text processing.

## Prohibited tools

- Publishing or posting tools.
- Messaging tools.
- Purchases, payments, deletion, or production administration.
- Reading credentials, raw session stores, address books, or unrelated private notes.

## Data access

- `Public`: yes, as required by the research question.
- `Private`: only the minimum relevant project context.
- `Sensitive`: no, unless a separately approved workflow provides an explicit redacted excerpt.
- `Restricted`: no by default; stop and escalate if required.

## Disclosure limits

- Preserve source URLs and access dates.
- Do not copy personal data that is not necessary for the claim.
- Label vendor claims, inference, and opinion separately from verified source facts.
- Do not invent quotes, metrics, experience, or source conclusions.

## Approval boundary

Preparing the brief does not require publication approval. Any external publication, message, or data sharing requires a separate explicit approval record naming the exact target and scope.

## Evidence required

- Source URL or file reference for each material factual claim.
- Capture/access date for current information.
- Explicit uncertainty when a source is inaccessible, partial, or contradictory.
- Run log using the five execution states when tools are used.

## Acceptance criteria

- The brief answers the stated question or identifies what remains unknown.
- Every material claim has provenance or is labeled interpretation.
- Restricted data was not accessed or disclosed.
- No external side effect occurred.
- A reviewer can reproduce the source trail.
