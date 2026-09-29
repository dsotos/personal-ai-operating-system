# Memory and knowledge

## Source of truth

Choose one human-readable knowledge base as the canonical source. Other stores may index or cache it, but they should not silently become a competing authority.

## Obsidian's role

Obsidian can serve as this persistent knowledge hub: a private vault for curated memories, project notes, research and source links, decisions, and reusable procedures. Hermes is the orchestrator that retrieves relevant vault context and coordinates specialist work; Obsidian is where durable knowledge is organized and linked.

Keep the vault selective and useful rather than copying every conversation into it. After work is verified, preserve durable outcomes with their source, date, and status. Keep the actual vault, attachments, personal notes, and local path outside the public repository; publish only sanitized examples and templates.

The specific folder structure is a deployment choice, not a universal requirement. Keep a single clear source of truth and make any indexes, caches, or agent-specific stores derivative.

## Capture pattern

Every durable note should preserve:

- title;
- source or provenance;
- capture date;
- status: `verified`, `provisional`, `opinion`, or `decision`;
- related project or topic;
- links to supporting or contradicting notes;
- optional review date or reviewer when the note is provisional.

Use the public [Obsidian note template](../templates/obsidian-note.md) as a starting point. The epistemic `status` of a note is different from the execution states in `docs/mental-model.md`.

## Inbox and weekly triage

Use an `inbox/` for short-lived captures only. During a weekly review, process every item:

1. Validate the source and preserve the access/capture date.
2. Merge it into an existing note, create a durable note, or discard it.
3. Assign a project or explicitly mark it as cross-project.
4. Set `status` to `verified`, `provisional`, `opinion`, or `decision`.
5. Add links to related or contradicting notes.
6. Add a reviewer/date when the note remains provisional.
7. Empty or archive the inbox item after the decision.

A note must have an owner and a next review rule. Do not use the inbox as an unbounded memory store.

## Note lifecycle

1. **Captured:** a source or idea enters the inbox.
2. **Triaged:** provenance, project, status, and links are assigned.
3. **Maintained:** the note is updated when evidence or decisions change.
4. **Reviewed:** provisional notes are checked before their review threshold.
5. **Archived or removed:** stale, superseded, or no-longer-useful notes leave active views with a reason recorded when appropriate.

The default provisional review threshold in this repository is **30 days from `captured`**. A private installation may change the value, but it must update the Dataview query and documentation together.

## Dataview radar

If the Dataview plugin is installed, save this query as a dashboard note or embed it in the weekly review:

```dataview
TABLE captured, reviewed, project, source
FROM ""
WHERE status = "provisional"
  AND captured <= date(today) - dur(30 days)
  AND !contains(file.path, "/templates/")
  AND !contains(file.path, "/inbox/")
SORT captured ASC
```

This radar lists provisional notes that have reached the 30-day review threshold, excludes the public template and inbox, and uses the existing `captured` field. To change the threshold, replace `30` in both this documentation and the private dashboard query. If Dataview is not installed, use a search for `status: provisional` and review notes whose `captured` date is at least 30 days old.

The public [inbox placeholder](../inbox/README.md) is intentionally empty; a private vault can use the same structure without publishing its contents.
## Retrieval pattern

Before drafting or deciding:

1. Search by project, topic, and entities.
2. Retrieve the smallest useful set of notes.
3. Check dates and status.
4. Prefer primary sources for factual claims.
5. State uncertainty when evidence is incomplete.

## Do not turn memory into a transcript dump

Memory should preserve durable context and reusable lessons, not every interaction. Raw conversations belong in a private, access-controlled session store when they need to be retained at all.
