---
name: trello-etf-batch
description: "Use when the user supplies an exact Trello parent card URL or ARI and asks to run or resume workflow: trello-etf-batch for a local Markdown ETF list; maintain the parent checklist and exception cards, and invoke check-etf-performance in lean mode. A list file or board search alone must not trigger execution."
---

# Trello ETF Batch

## Purpose and boundary

Use this skill as a Trello workflow coordinator for ETF performance batches.
Keep Trello state management here and delegate every ETF analysis to
`check-etf-performance`.

- Do not browse issuer, regulator, exchange, benchmark, or secondary sources
  from this coordinator.
- Do not duplicate the research worker or pre-save reviewer required by
  `check-etf-performance`.
- Do not write ETF performance pages, source batches, entities, or logs here.
  The downstream skill remains the sole writer of those durable vault outputs.
- Do not treat the input list's price, AUM, displayed return, or expense-ratio
  snapshot as evidence.
- Do not depend on Trello attachments. Read the local path in the card
  description.
- Do not start merely because a card exists. Require an explicit invocation
  that names the exact parent card URL or ARI.

## Trigger and card contract

Use for prompts such as:

- `[$trello-etf-batch] https://trello.com/c/<card>`
- `Run trello-etf-batch on https://trello.com/c/<card>`
- An automation prompt that names the exact parent card URL or ARI and sets
  `run_mode: automation`.

The parent-card target is required. Do not discover or select a parent by
board-wide search, title, or workflow key alone. If the prompt has no exact
card URL or ARI, stop with `parent card target required`. Resolve one target
card directly; zero or multiple resolutions are a global pre-claim error.

After reading the target card, require these exact configuration keys:

`workflow: trello-etf-batch`
`input: /absolute/or/project-relative/path/to/etf-list.md`

Use `mode: lean` by default and reject `mode: chat` for this durable batch
workflow. Resolve project-relative paths from the stock-second-brain root.

The optional `run_mode: manual|automation` may be in the card description or
the invocation. An invocation value overrides the card value only when the
card has no conflicting value. If neither supplies it, default to `manual`.
`automation` must be explicit; never infer automation from a generic schedule
or from a card list. An invalid or conflicting value is a global pre-claim
configuration error.

The optional one-line `batch_size: <positive integer>` may appear in the
parent description. If it is absent, default to `1`. Parse it as one positive
base-10 integer matching `[1-9][0-9]*`. A duplicate or conflicting
`batch_size`, or a zero, negative, fractional, or non-numeric value, is a
pre-claim `workflow-config-mismatch`. The card value is authoritative: an
invocation or scheduler must not override it or infer a different count from
the title, list, queue length, or generic automation wording. For
`run_mode: automation`, process up to `batch_size` items in one claimed run;
the effective count is smaller when fewer eligible queue items remain. Manual
mode retains its existing behavior of processing all unattempted work in the
same claim.

Use these defaults unless the card supplies an override:

- Expected board: `stock-analysis-task`
- Ready list: `Ready for AI`
- Active list: `In Progress`
- Blocked list: `Blocked`
- Done list: `Done`

Accept optional one-line overrides: `board:`, `ready_list:`,
`active_list:`, `blocked_list:`, and `done_list:`. The resolved parent board,
card ARI, and canonical card URL are the source of truth after the target is
read.

## Token-efficient Trello access

1. Read the supplied parent card URL or ARI directly and verify its exact
   workflow key, board, list, and configuration.
2. Never use board-wide workflow-key search to select a parent. After the
   parent is known, search only for the current ticker's exception card or
   known open retries.
3. After resolving the parent, read only that card and its `ETF queue`
   checklist. Do not list the entire board on every loop.
4. Use checklist-item updates for normal progress. Do not create a child card
   for a successful ETF.

## Queue input and checklist

Read the Markdown input file and resolve exactly one table column named `Symbol`
or `Ticker`, case-insensitively; treat the two aliases as equivalent. Both
aliases are ambiguous and neither alias is malformed: reject either state as a
global `input-malformed` result before any claim, checklist, or Trello mutation;
trim whitespace and backticks, normalize each symbol to uppercase,
preserve source order, and deduplicate repeated symbols by keeping the first
canonical occurrence. The canonical source sequence is `S`.

- Fail globally when the file is missing, unreadable, has both aliases or
  neither alias, has a malformed/empty ticker row, or produces no canonical
  symbols; the invalid alias states return `input-malformed`.
- Ignore every other column for queue construction and evidence.
- Create one checklist named `ETF queue` with the full canonical sequence when
  it does not exist.
- If exactly one `ETF queue` checklist exists, let its normalized item-label
  sequence be `C`. Accept it only when `C` equals the exact prefix `S[0:len(C)]`
  and `len(C) <= len(S)`. The checked/unchecked boolean is state attached to
  each matched label and is preserved; it is not part of the prefix test.
  Append only `S[len(C):]` in source order.
- If more than one `ETF queue` checklist exists, or if `C` has an unknown,
  duplicate, out-of-order, removed, or otherwise non-prefix item, stop with a
  checklist mismatch. Do not silently delete, uncheck, reorder, or merge work.

The checklist is the normal progress source of truth. A checked item means the ticker has been handled by the coordinator, either through downstream
success or through a successful item-level exception-card mutation. The
child exception card is the source of truth for why a handled item was
blocked. A checked item with an open matching exception is handled but not
successfully cleared, so it must not make the parent eligible for `Done`. A
disclosed `not disclosed` or `ไม่พบข้อมูลที่ยืนยันได้` field is not by itself a
failure.

## Lane-only parent state and claim protocol

The parent card's Trello lane is the sole runtime state:

- `Ready for AI` is the only eligible parent lane.
- `In Progress` means a worker may be active; do not mutate the parent,
  checklist, or exception cards from a new invocation.
- `Blocked` means user action is required; the user must move the parent to
  `Ready for AI` to retry.
- `Done` is a validated no-op only when the queue is complete and no exception is open.

Do not read, validate, write, or delete legacy `trello-etf-batch-status` blocks.
They are inert text retained only for backward compatibility. Preserve all
other user configuration text in the parent description.

Validate the exact parent target, board/list IDs, configuration, input file,
and canonical source sequence before claiming. To claim an eligible parent:

1. Confirm that its current lane is `Ready for AI`, then move it to `In Progress`.
2. Immediately read the exact parent directly again.
3. Continue only when that direct read still shows `In Progress`.

If the lane does not match after the move, stop without any further Trello
mutation or downstream call. If the parent is already in `In Progress`, return `batch already claimed` without mutating it. A parent in `Blocked` is never
retried in place.

Trello does not expose an atomic compare-and-set operation, so the lane is not
an exactly-once distributed lock. This workflow requires at most one automation worker per parent. If a worker is abandoned, the user must confirm it is
inactive before moving the parent to `Ready for AI`; the skill must not reset
the lane automatically.

## Exception cards

For an explicit downstream item-level failure, create or reuse exactly one
exception card in the blocked list. Use this name:

`[BLOCKED][ETF] <TICKER> | check-etf-performance`

Its description must contain these metadata lines:

- `workflow: trello-etf-batch-exception`
- `parent_ari: <resolved parent card ARI>`
- `parent_url: <resolved canonical parent card URL>`
- `ticker: <canonical uppercase TICKER>`
- `failure: <stable failure code>`
- `reason: <one concise sentence>`
- `confirmation: none|required|confirmed`
- `terminal: true|false`
- `retry: move parent to Ready for AI`

Use the resolved parent ARI as the primary identity and the canonical parent
URL as a compatibility key. Treat the exception card as the Trello child
record linked by `parent_ari` and `parent_url`; do not create child cards for
successful ETFs. Define `open` as unarchived, not completed, and not in the
configured Done list. For retry classification, consider only open cards. A
card with a nonempty `parent_ari` is a candidate only when it equals the
resolved parent ARI; a conflicting ARI is never a fallback. A legacy card
with an absent `parent_ari` may be reused only when its canonical parent URL
and ticker match exactly; backfill the canonical parent ARI. A renamed
matching card is still the same card; rename it to the standard name. If
multiple open matching cards exist, stop with a global ambiguity error. When
an item failure needs an exception and no open match exists, reuse at most
one historical closed match with the same canonical identity and reopen it;
multiple historical matches are a global ambiguity. If no match exists, the
fallback is exactly one standard-name card with an absent parent ARI whose
canonical parent URL and ticker match, otherwise create one. Never accept a
card with a conflicting nonempty parent ARI or create duplicate exception
cards.

When backfilling a legacy match, default missing `confirmation` to `none` and
missing `terminal` to `true` only when its normalized failure is
`unsupported-etf-type`; otherwise default `terminal` to `false`. Always write
the complete metadata set before using the card for retry or finalization.

When retrying, only an open exception with `terminal: false` and no
unconfirmed `confirmation` is eligible. Move it to the active list before the
downstream call. After any item-level retry failure, update its metadata and
move it back to the configured Blocked list; if that move/update fails, treat
the result as a global state failure. On downstream success, move it to Done
and mark it complete. An exception card is not a child card for normal
successful work.

`unsupported-etf-type` is terminal for the current queue entry: write
`terminal: true` and `retry: correct the input or create a corrected parent;
do not retry automatically`. Exclude terminal exceptions from the computed
`retry_pending` set. To requeue after correcting the input, the user must make an
explicit operator correction and set the exception to `terminal: false` (or
create a corrected parent); the prefix/checklist drift guard still rejects
silent removal or replacement of a queue item.

## Blocker routing contract

The word “blocker” is not by itself an item-level result. Route each ticker
only after validating the complete downstream handoff envelope:

- `item-level`: an accepted `WARNING` with `scope: item` and
  `confirmation: required`, an accepted `CHANGES_REQUIRED`/`BLOCKED` with
  `scope: item` and an accepted item code, or an accepted item-level error.
  A known ticker-scoped downstream `ERROR` is an item-level error when the
  selected single-ticker call reports `research-sub-agent-unavailable` or
  `item-downstream-error`, has `durable_write: not_completed`,
  `exhausted: false`, `confirmation: none`, and `scope: item` or
  `scope: global`.
  Accepted scope values for this item-error branch are `scope: item` or `scope: global`.
  The coordinator owns the selected ticker, so it normalizes a reported
  `scope: global` for these two downstream-only codes to item-level. An
  item-level error is `status: ERROR` with `scope: item` and
  `durable_write: not_completed`, `exhausted: false`, `confirmation: none`,
  and `research-sub-agent-unavailable` or `item-downstream-error`.
  `research-sub-agent-unavailable` may be item-level even when the selected
  single-ticker handoff reports `scope: global`. These results are
  ticker-specific: create or reuse exactly one exception card, write its
  complete metadata, move the child to `Blocked`, then check only the matching
  `ETF queue` item and continue to the next eligible ticker while `batch_size`
  capacity remains.
  The item-level error sequence is exactly `create or reuse exactly one exception card` → `check only the matching `ETF queue` item` → `continue to the next eligible ticker`; `Trello/tool/auth failures remain global`.
- `terminal item-level`: `unsupported-etf-type` still follows the child-card
  and checklist flow above, but its child is not retryable. If terminal or
  unconfirmed-confirmation exceptions are the only remaining work, the parent
  ends in `Blocked`.
- `global-level`: `scope: unknown`, any accepted global code, a missing or
  contradictory envelope, or a Trello/board/input/claim failure. An `ERROR`
  with a reported `scope: global` is global unless it passes the explicit
  known ticker-scoped downstream error envelope above. Do not create a ticker
  exception, do not check the affected queue item, do not continue to another
  ticker, and block the owned parent. A global failure has no safe ticker
  identity and must not be represented as an item child.

Therefore, “create child → move child to `Blocked` → check queue item →
continue” applies only after the item-level branch succeeds. The coordinator
must respect the parent card’s `batch_size`. The parent card’s `batch_size` does not override a global stop.

## Execution loop

1. Read and validate the exact parent target, board/list IDs, configuration,
   effective `run_mode`, optional `batch_size`, and local input file. Build the
   nonempty canonical source sequence `S` before claiming or making any queue
   or exception mutation. Resolve the parent before mutating Trello.
   For automation, resolve `batch_limit` from the card's `batch_size` or the
   default `1`; manual mode keeps its existing unbounded per-claim behavior.
2. Inspect the parent lane only after configuration and input validation.
   `Ready for AI` is the only lane eligible for selection. If the parent is in
   `Done`, read its single `ETF queue` checklist and matching exception cards;
   accept a no-op only when the labels equal `S` exactly, every item is
   checked, and no exception is open. A missing, duplicate, mismatched, or
   incomplete checklist or any open exception is a global state error; never
   accept an empty or unvalidated input as Done. If the parent is already in `In Progress`, return `batch already claimed` without mutating it. If it is in
   `Blocked`, require the user to move it to `Ready for AI` without mutating it.
3. Claim the Ready parent using the lane-only protocol above. A pre-claim error
   does not seize or block a parent. After moving it to `In Progress`, perform
   the required direct re-read and stop without further mutation if the lane
   differs.
4. Build or reconcile the ETF queue checklist. Read only the exception cards
   needed to classify unchecked tickers as normal-pending and handled checked
   tickers as open-retry, confirmation-pending, or terminal-pending.
5. Keep an in-memory `attempted_this_run` set so an item is not selected
   repeatedly in the same invocation, plus `processed_count` for downstream
   item attempts. In automation, select up to `batch_size` items sequentially
   and stop selecting when `processed_count` reaches `batch_limit`. Compute:
   - `normal_pending`: unchecked tickers with no open exception and not already
     attempted in this run;
   - `retryable_open`: all open non-terminal item exceptions with `confirmation: none` or `confirmation: confirmed`;
   - `selectable_retries`: entries from `retryable_open` whose ticker is not in `attempted_this_run`;
   - `confirmation_pending`: checked tickers with an open exception whose
     `confirmation` is `required` but not yet `confirmed`.
   - `terminal_pending`: checked tickers with an open exception whose
     `terminal` is `true`.
6. At the start of each selection pass, if automation has reached
   `batch_limit`, finalize using step 12. Always select normal items before eligible retries: choose the first unattempted normal item when one exists,
   otherwise choose the first entry in `selectable_retries`. Use `selectable_retries` for selection and `retryable_open` for finalization. If no unattempted
   work remains, finalize using step 12.
7. For each selected retry, move/reuse its exception card in the active list.
   For each selected ticker, invoke `$check-etf-performance <TICKER>` with
   `mode: lean` one ticker at a time. Wait for its research delegation,
   reconciliation, pre-save review, and durable-write result. Do not perform
   those steps locally. Require the downstream handoff envelope defined in
   `Failure classification`; missing or ambiguous fields are a global result.
   A valid item-level `ERROR` is handled through the item exception flow and
   does not stop the batch. Never invoke downstream for a
   `confirmation_pending` item; it becomes eligible only after the user
   changes that exception line to `confirmation: confirmed` and moves the
   parent to Ready for AI.
8. For a successful item, mark the checklist item checked only for
   `status: PASS`, `scope: item`, and `durable_write: completed` in that
   envelope. On success, close any matching exception by moving it to Done and
   marking it complete, then increment `processed_count` once for the successful item. An accepted item-level blocker or item-level error may
   check the item only after its child exception mutation succeeds.
9. On a downstream handoff that passes the explicit item-level routing
   contract, keep the parent in `In Progress`,
   create or reuse exactly one exception card, write its complete metadata including `reason`, set `confirmation: required` only for
   `confirmation_required` and otherwise `confirmation: none`, set
   `terminal: true` only for `unsupported-etf-type` and otherwise `false`,
   Move the exception card to the configured `Blocked` list, and only after
   those mutations leave the matching `ETF queue` checklist item checked.
   If that exception state change fails, classify the run as global and leave
   the affected checklist item unchanged. After the exception mutation
   succeeds, add the ticker to `attempted_this_run`, increment
   `processed_count`, and continue to the next unattempted eligible ticker
   while batch capacity remains. Manual mode continues while unattempted work
   remains.
10. On a global failure after this invocation moved the parent to `In Progress`
    and the direct re-read confirmed that lane, move the parent to `Blocked`.
    Do not create a ticker exception card. A global failure before exact parent
    resolution or before a confirmed lane claim returns without pretending to
    update Trello. If a required lane move fails, report `claim-state-error`
    and stop. A global failure leaves the affected checklist item unchanged.
11. Keep the parent in `In Progress` while processing. In manual mode, repeat
    steps 5–10 while unattempted work remains.
12. After an item, when automation reaches its batch capacity, or after the
    final queue inspection, use these mutually exclusive branches:
    - If every queue item is checked and no exception is open, move the parent to `Done` and mark it complete; this is the `all items checked and no open exception` branch;
    - else if unfinished normal work remains, manual mode continues with the
      parent in `In Progress`; automation moves the parent to `Ready for AI`;
    - else if `retryable_open` is nonempty, an eligible retryable exception remains; move the parent to `Ready for AI`. Manual mode reaches this branch only after every retryable entry is in `attempted_this_run`, so it does not retry a ticker twice in one invocation; a later invocation may select it again;
    - else if only terminal or unconfirmed confirmation exceptions remain,
      move the parent to `Blocked` and do not mark it complete;
    - otherwise report a global checklist/state inconsistency and, because the
      invocation moved the parent to `In Progress`, move the parent to
      `Blocked` without creating an exception card.

When a user moves a Blocked parent to Ready for AI, derive retry eligibility from the checklist and open exception cards. Do not infer retry work from the
parent description. A terminal or confirmation-pending exception still keeps
the parent blocked when no normal work remains. Manual mode processes all
unattempted normal and retry work in the same invocation, while each ticker is
attempted at most once per invocation. The scheduler continues to inspect only `Ready for AI`.

## Failure classification

Treat these as global failures: missing/ambiguous exact parent target,
workflow/configuration/run-mode/batch-size mismatch, Trello authentication/tool failure,
board/list resolution failure, unreadable/malformed input, checklist mismatch,
an owned lane/ownership transition failure, or a downstream handoff with `scope: unknown`, a
global code, or an unrecognized/invalid error envelope. A known ticker-scoped
downstream `ERROR` with code `research-sub-agent-unavailable` or
`item-downstream-error` may be item-level when the complete accepted item
envelope is present, even when the downstream reports `scope: global`; this
normalization is limited to the selected single-ticker call.
`claim-state-error` remains an accepted global failure code for a lane or
ownership transition failure after this invocation moved the parent. A
pre-claim configuration/Trello failure is reported without seizing or
blocking a parent; a post-claim global failure moves the parent to `Blocked`
when the required Trello lane mutation succeeds.

The downstream handoff must be normalized to this explicit envelope for each
single-ticker invocation within the batch:

`status: PASS|WARNING|CHANGES_REQUIRED|BLOCKED|ERROR`
`scope: item|global|unknown`
`durable_write: completed|not_completed|unknown`
`exhausted: true|false`
`confirmation: none|required|confirmed`
`code: <stable code>`
`reason: <concise reason>`

All fields are required. Normalize `code` by trimming, lowercasing, and
replacing spaces/underscores with hyphens. Thus both `unsupported ETF type`
and `unsupported_etf_type` become `unsupported-etf-type`. The only accepted
codes are:

- success: `success`, `durable-write-complete`;
- warning: `review-warning`, `confirmation-required`;
- item: `unsupported-etf-type`, `item-pre-save-non-pass`,
  `item-hard-data-gap`, `research-sub-agent-unavailable`,
  `item-downstream-error`;
- global: `trello-tool-failure`,
  `trello-auth-failure`, `board-list-resolution-failure`,
  `workflow-config-mismatch`, `input-malformed`, `checklist-mismatch`,
  `claim-state-error`, `global-error`, `unknown-result`.

Apply precedence before mapping: any global code or `scope: unknown` is always
`global_blocked`, even if other fields incorrectly say PASS. For a selected
single-ticker call, a known ticker-scoped `ERROR` code may override a reported
`scope: global` only when the complete item-level error envelope passes.
Any other `status: ERROR`, including an invalid or contradictory envelope, is
global. A global code also overrides a contradictory item scope. Reject unknown
codes, missing fields, and contradictory combinations as global; never let a
contradictory PASS reach the checklist.

After that precedence check, apply this closed mapping:

- `PASS` + `scope: item` + `durable_write: completed` is `success`; the
  downstream durable workflow has completed its required research,
  reconciliation, pre-save gate, and vault writes. It also requires
  `exhausted: false`, `confirmation: none`, and a success code. A disclosed
  gap remains a successful result when downstream says so.
- `WARNING` + `scope: item` + `durable_write: not_completed` is
  `confirmation_required`: treat it as the same safe item-level exception
  flow used for other explicit item blocks. Create or update the one
  exception card, write the required user confirmation plus full metadata
  including `reason`, move it to the configured Blocked list, and only then
  mark the matching `ETF queue` item checked. The exception remains open, the
  item stays handled but not successfully cleared, `Done` remains blocked
  while that open confirmation exception exists, and the current run may
  continue while capacity remains. This preserves the project rule that a
  reviewer warning pauses a save without falling out of the handled-item
  model. It also requires `exhausted: false`, `confirmation: required`, and
  a warning code. A scope-free or `scope: unknown` warning is global because
  the coordinator cannot safely assign ownership.
- `CHANGES_REQUIRED` or `BLOCKED` with explicit `scope: item` is
  `item_blocked` only with `durable_write: not_completed`,
  `exhausted: true`, `confirmation: none`, and an item code; this includes the
  normalized code `unsupported-etf-type` and a final item gate that remains
  non-PASS after downstream's correction/re-review policy. Create or reuse the
  exception card. `unsupported-etf-type` must set `terminal: true` and is not
  eligible for retry; other accepted item codes set `terminal: false`.
- `ERROR` with `scope: item` or reported `scope: global` is `item_blocked` only
  for the selected single-ticker call, with
  `durable_write: not_completed`, `exhausted: false`, `confirmation: none`,
  and `research-sub-agent-unavailable` or `item-downstream-error`. Use the
  same child-card metadata, `Blocked` move, matching queue-item check, and
  continue flow as other item-level blockers; set `terminal: false` so the
  child can be retried.
- A known global code, `scope: unknown`, an invalid `ERROR` envelope, or a
  Trello/tool/auth failure is `global_blocked`; block the parent and create no
  ticker exception. A reported `scope: global` is also global when its code is
  not one of the two explicitly accepted ticker-scoped downstream error codes.
- Any unknown status, missing required field, contradictory combination (for
  example PASS without completed durable writes), or scope-free non-warning
  failure is global. Do not infer item failure from a disclosed data gap or
  from a field marked `not disclosed`/`ไม่พบข้อมูลที่ยืนยันได้`, and do not
  override the downstream quality gate.

## Automation contract

The skill does not create automations. A recurring automation must explicitly
invoke this skill with the exact parent card URL or ARI and
`run_mode: automation`, and say:

```text
Process up to the parent card’s `batch_size` eligible ETFs sequentially
(default 1); update the Trello parent/checklist state after each ticker,
classify each downstream handoff before mutating Trello; for an accepted
item-level `WARNING`/`CHANGES_REQUIRED`/`BLOCKED` result, create or reuse
exactly one exception card named `[BLOCKED][ETF] <TICKER> |
check-etf-performance`, write complete metadata, move only that child to
`Blocked`, check only that ticker's queue item after the child mutation
succeeds (this flow checks that queue item only after the child state update),
and continue to the next ticker while capacity remains. This allows the current batch to continue. After capacity, release a non-terminal parent back to Ready for AI. For a selected single-ticker call, a complete `ERROR` envelope with `research-sub-agent-unavailable` or `item-downstream-error` may be handled as item-level even when it reports `scope: global`; use the child/check/continue sequence above. For `ERROR` with `scope: unknown`, a global code, or any ambiguous/invalid envelope, create no child, leave the affected queue item unchecked, block the parent, and stop the run. Trello/tool/auth failures remain global. After batch capacity or queue exhaustion, release a non-terminal parent back to `Ready for AI`; keep terminal or unconfirmed-confirmation item exceptions in `Blocked`. Generic scheduler text must respect the parent card’s `batch_size`.
```

Never schedule overlapping automation workers for the same parent.

## Completion response

Return a compact status containing:

- parent card and current list;
- tickers processed in this invocation, if any;
- counts of checked, normal-pending, retry-pending, and blocked items; derive
  any reported retry-pending count from `retryable_open`;
- any exception card URL/name;
- downstream output links only when the downstream skill returned them.

Do not paste the full ETF performance report into Trello or the chat when a
durable output link is available.
