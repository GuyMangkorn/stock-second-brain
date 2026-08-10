# Trello ETF Batch Size Design

**Status:** Approved by user on 2026-08-10

## Goal

Allow a Trello ETF batch parent to control how many ETF queue items one
automation invocation processes, while preserving the existing one-ticker
`check-etf-performance` worker contract and preventing concurrent durable
writes.

## Configuration contract

The parent card description may contain one exact one-line field:

```text
batch_size: 3
```

`batch_size` is a positive base-10 integer. If it is absent, the effective
value is `1` for backward compatibility. A duplicate, zero, negative,
fractional, non-numeric, or conflicting value is a pre-claim global
configuration error. The card value is authoritative; the scheduler must not
infer a size from the title, list, or generic automation wording.

The effective number of items is the smaller of `batch_size` and the number of
eligible queue items remaining in that invocation. Existing cards therefore
continue to process one ETF unless their description opts into a larger size.

## Execution design

The coordinator claims one parent once, keeps the claim while it processes up
to `batch_size` items, and calls `$check-etf-performance <TICKER> mode: lean`
sequentially for each selected ticker. Each downstream call retains its own
research delegation, reconciliation, pre-save review, and handoff envelope.
The coordinator updates the checklist immediately after each successful item
and maintains `attempted_this_run` so an item is not selected twice.

Item selection preserves the existing retry preference: eligible retries are
selected first when `retry_pending` is true; otherwise the first normal item is
selected. The selection is recomputed after every item so exception state and
checklist state remain current.

## Failure and finalization

- A global failure stops the batch immediately, creates no ticker exception,
  and blocks the owned parent.
- An explicit item-level failure leaves that checklist item unchecked, creates
  or updates its exception card, and continues to the next unattempted item
  while capacity remains.
- A confirmation-pending or terminal exception is never sent downstream.
- After the last attempted item, the parent is marked `done` only when every
  checklist item is checked. Otherwise an automation run releases a
  non-terminal parent to `Ready for AI` with the existing retry flag rules.

The completion response reports all tickers attempted in the invocation and
the aggregate checklist/exception counts. Successful ETFs do not create child
cards.

## Scope and compatibility

Only `.codex/skills/trello-etf-batch/SKILL.md` changes behavior. The
`check-etf-performance` skill remains single-ticker because each ETF owns a
separate performance page, source batch, review gate, and possible region/index
update. The scheduled invocation text must instruct the worker to respect the
parent card's `batch_size` rather than hard-code one ETF.

## Verification

Verify the skill text contains the complete config validation, sequential
multi-item execution, failure handling, finalization, and updated automation
contract. Run a focused static contract test with examples for the default,
valid multi-item, and invalid configuration cases before claiming completion.
