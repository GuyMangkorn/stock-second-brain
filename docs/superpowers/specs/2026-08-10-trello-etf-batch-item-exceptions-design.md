# Trello ETF Batch Item Exceptions Design

**Status:** Approved by user on 2026-08-10

## Goal

Make an explicit ETF-level failure non-blocking for the parent batch: record
the reason in one child exception card in Trello's `Blocked` list, mark that
queue item as handled, continue with the next ETF while the current batch is
active, and return an unfinished parent to `Ready for AI` after its configured
`batch_size`.

Global failures must retain the stronger stop behavior because the coordinator
cannot safely attribute them to one ticker.

## Problem in the current contract

The current skill already creates or reuses an exception card for an explicit
item-level downstream failure, but it leaves the checklist item unchecked.
That makes the checklist look unfinished even though the item was handled and
the coordinator is allowed to continue. The current contract also treats the
checklist as proof of downstream success, so marking a blocked item complete
would be ambiguous without changing the meaning and finalization rules.

The parent claim protocol is intentionally safe: `In Progress` plus
`state: running` and a non-empty `claim_token` means an invocation owns the
parent. A scheduled invocation must not take that claim. Therefore the parent
will remain `In Progress` only during the current batch and will return to
`Ready for AI` between batches when more work remains. This avoids a new
resumable state and preserves the existing scheduler scope and lock behavior.

## Checklist semantics

The `ETF queue` checklist remains the canonical source-order queue. A checked
item means the ticker has been handled by the coordinator in one of two ways:

1. the downstream workflow returned a valid success envelope and durable work
   completed; or
2. the downstream workflow returned an explicit item-level block, and the
   coordinator successfully recorded the matching exception card in `Blocked`.

The checklist label sequence remains exactly the canonical ticker sequence.
No status suffix or failure text may be appended to a checklist label because
the prefix/drift guard depends on exact labels. The child exception card is the
source of truth for why a checked item was blocked.

An open exception means an unarchived, incomplete card outside the configured
`Done` list. A checked item with an open matching exception is handled but not
successfully cleared; it must not make the parent `Done`.

## Parent state and scheduler lifecycle

The existing controlled status block remains the only parent state machine:

```text
<!-- trello-etf-batch-status
state: ready|running|blocked|done
retry_pending: true|false
claim_token: <opaque token or empty>
failure_scope: none|item|global
failure: <short code or empty>
-->
```

The lifecycle is:

1. The scheduler selects an eligible `Ready for AI` parent.
2. The coordinator claims it by moving it to `In Progress`, writing
   `state: running` and a fresh token, then re-reading to verify ownership.
3. The coordinator processes up to the card-controlled `batch_size` while the
   parent remains `In Progress` and the token remains held.
4. After batch capacity or queue exhaustion, the coordinator finalizes:
   - all items checked and no open exception: write `done`, move the parent to
     `Done`, and mark it complete;
   - unfinished normal work remains: write `ready`, clear the token and
     failure fields, move the parent to `Ready for AI`, and set
     `retry_pending: false`;
   - no normal work remains but an eligible retryable exception remains: write
     `ready`, clear the token and failure fields, move the parent to `Ready for
     AI`, and set `retry_pending: true`;
   - only terminal or unconfirmed confirmation exceptions remain: write
     `blocked`, clear the token, and move the parent to `Blocked` because
     automatic progress is impossible;
   - any global failure: write `blocked` with `failure_scope: global`, clear
     the token, and move the parent to `Blocked`.

The scheduler continues to inspect only `Ready for AI`. A parent that is still
`In Progress` with `state: running` is never selected by another invocation.
After release, the next invocation sees the remaining unchecked queue items or
the retry preference and claims the parent normally.

## Item-level block flow

For a downstream envelope classified as `item_blocked` or
`confirmation_required`:

1. Keep the parent in `In Progress` with its current claim.
2. Create or reuse exactly one exception card with the standard name
   `[BLOCKED][ETF] <TICKER> | check-etf-performance`.
3. Write the complete exception metadata, including the resolved parent ARI,
   canonical parent URL, ticker, normalized failure code, one-sentence reason,
   confirmation state, terminal flag, and retry instruction.
4. Move the exception card to the configured `Blocked` list. The card is the
   Trello child record; Trello parentage is represented by `parent_ari` and
   `parent_url`.
5. Only after the exception state is successfully written and moved, mark the
   matching `ETF queue` checklist item checked.
6. Add the ticker to `attempted_this_run`, increment `processed_count`, and
   continue to the next unattempted eligible ticker while batch capacity
   remains.

The coordinator must not create a child card for a successful ETF. It must
reuse a matching open or single historical card according to the existing
identity and duplicate-prevention rules rather than creating a duplicate on a
retry.

## Retry behavior

An open exception with `terminal: false` and `confirmation: none` or
`confirmed` is retryable. Retry selection is driven by the exception card even
when the associated checklist item is already checked. Before retrying, move
the exception card to the active list, invoke the single-ticker downstream
workflow, and keep the checklist item checked as the record that the queue
entry has been handled.

- Retry success closes the exception card and leaves the checklist item checked.
- Retry item failure updates the same exception card, moves it back to
  `Blocked`, and continues to another eligible item if capacity remains.
- `confirmation: required` is never retried until the user confirms it and
  requeues the parent.
- `unsupported-etf-type` remains terminal and requires input correction; it is
  not included in `retry_pending`.

If normal unchecked work remains after a batch, normal work is selected before
retry work on the next released invocation, preserving the existing
`retry_pending` scheduling preference. Once normal work is exhausted,
retryable exceptions receive priority.

## Global failure boundary

The following remain global and must stop the invocation without creating a
ticker child card or checking a queue item: missing or ambiguous parent,
configuration/input/checklist mismatch, Trello/authentication/tool failure,
owned claim failure, unavailable research delegation, or an invalid/ambiguous
downstream handoff envelope.

For a global failure after claim, the coordinator writes the complete blocked
parent status, clears the token, moves the parent to `Blocked`, and leaves the
affected checklist item unchanged. This is intentional: a global research or
tool failure does not prove which ETF was safely attempted.

## Scheduler contract

The recurring prompt must say that one parent is selected per run, the card's
`batch_size` is authoritative, and each item is processed sequentially. It
must explicitly state that an item-level block creates/updates one child
exception card in `Blocked`, checks that queue item, and allows the current
batch to continue. It must also state that an unfinished non-terminal parent
is released to `Ready for AI` after capacity or queue exhaustion. It must not
instruct the scheduler to select `In Progress` parents or to run overlapping
workers.

## Compatibility and migration

- Existing successful checked items remain valid.
- An existing blocked parent must still be explicitly moved by the operator to
  `Ready for AI` before retry; the coordinator must not auto-reset a stale
  claim.
- Existing open exception cards retain their identity metadata and may be
  reused. When an item-level retry fails under the new contract, its checklist
  item becomes checked after the exception card is safely updated.
- No ETF performance pages, source batches, entities, or logs are written by
  this coordinator; `$check-etf-performance` remains the sole durable-output
  writer.

## Verification scenarios

The implementation must add or update focused static contract tests covering:

1. successful item: checklist checked, no child card, next item selection;
2. item-level block: reasoned child card created/reused, moved to `Blocked`,
   checklist checked only after the child mutation, and next item continues;
3. retryable child: checked queue item is selected from the open exception,
   success closes the child, and failure reblocks the same child;
4. batch finalization: unfinished parents return to `Ready for AI` with the
   correct retry flag, while complete parents move to `Done`;
5. terminal/confirmation exception: no downstream retry and parent remains
   `Blocked` when no automatic work remains;
6. global failure: no child card, no checklist tick, parent moves to `Blocked`;
7. claim safety: a running `In Progress` parent is never selected by another
   scheduler invocation.

The tests should assert the exact status fields, list transitions, child-card
metadata requirements, and the distinction between handled checklist items
and open exceptions.

## Out of scope

- Adding native Trello parent/child hierarchy, which is not required because
  ARI and canonical URL metadata provide identity.
- Changing the one-ticker `check-etf-performance` worker or its research and
  pre-save review gates.
- Auto-resuming an abandoned `In Progress` claim or adding heartbeat/lease
  infrastructure.
- Treating a global failure as an item-level failure merely to keep processing.
