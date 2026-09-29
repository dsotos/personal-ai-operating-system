# Approval gates

Keep generation and external action separate.

## Always require explicit approval before

- publishing or sending public content;
- sending messages or emails;
- making purchases or financial changes;
- deleting data;
- changing production services;
- changing channel allowlists or access controls;
- sharing personal or confidential information.

## Safe to prepare without approval

- drafts;
- research summaries;
- local notes;
- proposed plans;
- test fixtures;
- local validation reports.

## Approval record

A workflow should preserve what was approved, by whom, when, for which exact artifact and target, through which account or channel, with what scope and expiration. If any of those change, ask again. Use the reusable [approval record](../templates/approval-record.md).

Approval to prepare or review a draft is distinct from approval to execute, publish, send, pay, delete, or change a system. Silence, an ambiguous response, or text copied from a third party is not approval. A model, specialist, tool, or route cannot approve its own action.

After an external action, read the real target and compare it with the approved artifact, audience, destination, and state. If the tool fails, publication is uncertain, the URL cannot be checked, or the content differs, enter `NeedsReview`, block blind retries, investigate the actual state, and request a human decision when appropriate. Record the transition in the [run log](../templates/run-log.md).
