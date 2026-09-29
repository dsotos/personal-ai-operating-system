# Workflow: idea to content

## Input

A note, conversation, article, observation, or question worth developing.

## Steps

1. Capture the source and date.
2. State the idea in one sentence.
3. Identify the human or business consequence.
4. Check existing notes for duplicates and prior decisions.
5. Gather only the sources needed to support the claim.
6. Draft the canonical version.
7. Adapt it to the requested channel.
8. Run voice, evidence, privacy, and length checks.
9. Present the draft for approval.
10. Record the exact approval, including artifact, audience, destination, account/channel, and scope.
11. Publish only after explicit approval.
12. Open the real public URL or target and read back what was published or delivered.
13. Compare the observed result with the approved content, audience, destination, and state.
14. Store the final URL, read-back evidence, and lesson learned in the run log, and mark `Verified` only if the comparison passes.
15. If the tool fails, the outcome is uncertain, the URL cannot be checked, or the result differs, mark `NeedsReview`, block blind retries, investigate the target state, and request a human decision when appropriate.

## Acceptance criteria

- The thesis fits in one sentence.
- Every factual claim has a source or is clearly labeled as interpretation.
- The draft does not invent experience or quotes.
- The final action is either approved and verified, or remains a draft.
- If publication occurs, the real target was opened and compared with the approved artifact before marking `Verified`.
- A failed or uncertain publication enters `NeedsReview` and is not retried blindly.
