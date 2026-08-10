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

Read the Markdown input file and parse the table column named `Symbol`,
case-insensitively. Trim whitespace and backticks, normalize each symbol to
uppercase, preserve source order, and deduplicate repeated symbols by keeping
the first canonical occurrence. The canonical source sequence is `S`.

- Fail globally when the file is missing, unreadable, has no `Symbol` column,
  has a malformed/empty ticker row, or produces no canonical symbols.
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

The checklist is the normal progress source of truth. A checked item means
the downstream performance workflow explicitly returned success for that
ticker. A disclosed `not disclosed` or `ไม่พบข้อมูลที่ยืนยันได้` field is not
by itself a failure.

## Controlled parent status and claim protocol

Preserve all user configuration text and maintain one replaceable status block
at the end of the parent description:

`<!-- trello-etf-batch-status
state: ready|running|blocked|done
retry_pending: true|false
claim_token: <opaque token or empty>
failure_scope: none|item|global
failure: <short code or empty>
-->`

Parent states must match both the list and the status block:

- `Ready for AI` + `ready` + empty token: unclaimed and eligible.
- `In Progress` + `running` + nonempty token: claimed by one invocation.
- `Blocked` + `blocked` + empty token: unresolved blocker; retry requires a
  user move back to `Ready for AI`.
- `Done` + `done` + empty token: all queue items checked; mark complete.

There must be exactly one complete status block. If it is absent on a Ready
parent, initialize all fields as `state: ready`, `retry_pending: false`,
empty `claim_token`, `failure_scope: none`, and empty `failure`. If a user
moves a Blocked parent to Ready for AI, accept that one explicit reset
transition: clear the token and old failure fields, set `state: ready`, and
derive `retry_pending` from retryable open exceptions. Any other list/block
disagreement is a global state error before downstream work. An In Progress
parent is never eligible for a new invocation; return `batch already claimed`.
A Blocked parent is never retried in place. A Done parent is a no-op only
after the input and exact complete checklist validation in the execution loop.

Every parent transition writes all status fields, not a partial patch:

- claim: `running`, current token, `failure_scope: none`, empty `failure`,
  and the derived retry flag;
- item result while a manual or bounded automation claim continues: `running`,
  current token,
  `failure_scope: item`, the normalized item code (or `none` after success),
  and the derived retry flag;
- automation release: `ready`, empty token, `failure_scope: none`, empty
  `failure`, and `retry_pending` set by the finalization rule;
- item-blocked stop: `blocked`, empty token, `failure_scope: item`, the
  normalized blocker code, and `retry_pending: true` only when a retryable
  open exception remains;
- global stop: `blocked`, empty token, `failure_scope: global`, the global
  code, and the derived retry flag;
- done: `done`, `retry_pending: false`, empty token, `failure_scope: none`,
  and empty `failure`.

Validate the block's keys, enum values, and uniqueness before any downstream
call. Do not leave a stale claim or failure value in a Ready or Done state.

To claim a Ready parent:

1. Move it to `In Progress`.
2. Write a fresh opaque `claim_token` and `state: running`; clear the old
   failure fields while preserving the configuration text.
3. Read the exact parent directly again. The invocation owns the claim only if
   the list is `In Progress` and the token exactly matches its token.

If the token is missing or different, this invocation lost the claim. It must
make no further Trello mutation: no status update, move, checklist edit,
exception card, or downstream call. Return the non-mutating result
`claim lost; another invocation owns the parent`.

Trello does not expose an atomic compare-and-set operation. This workflow
therefore requires at most one automation worker per parent and treats the
claim token plus second read as an operational ownership check, not an
exactly-once distributed lock. A second invocation must never process an
`In Progress` parent. If a worker is abandoned, the user must confirm it is
inactive and move the parent to `Ready for AI`; the skill must not auto-reset a
stale claim. A claim-collision/lost-claim result is not a global blocker for
the parent because the losing invocation does not own it.

## Exception cards

For an explicit downstream item-level failure, create or reuse one exception
card in the blocked list. Use this name:

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
URL as a compatibility key. Define `open` as unarchived, not completed, and
not in the configured Done list. For retry classification, consider only
open cards. A card with a nonempty `parent_ari` is a candidate only when it
equals the resolved parent ARI; a conflicting ARI is never a fallback. A
legacy card with an absent `parent_ari` may be reused only when its canonical
parent URL and ticker match exactly; backfill the canonical parent ARI. A
renamed matching card is still the same card; rename it to the standard name.
If multiple open matching cards exist, stop with a global ambiguity error.
When an item failure needs an exception and no open match exists, reuse at most
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
do not retry automatically`. Exclude terminal exceptions from
`retry_pending`. To requeue after correcting the input, the user must make an
explicit operator correction and set the exception to `terminal: false` (or
create a corrected parent); the prefix/checklist drift guard still rejects
silent removal or replacement of a queue item.

## Execution loop

1. Read and validate the exact parent target, board/list IDs, configuration,
   effective `run_mode`, optional `batch_size`, controlled status block, and
   local input file. Build the nonempty canonical source sequence `S` before
   any queue or exception mutation. Resolve the parent before mutating Trello.
   For automation, resolve `batch_limit` from the card's `batch_size` or the
   default `1`; manual mode keeps its existing unbounded per-claim behavior.
2. If the parent is Done, read its single `ETF queue` checklist and accept a
   no-op only when its labels equal `S` exactly and every item is checked. A
   missing, duplicate, mismatched, or incomplete checklist is a global state
   error; never accept an empty or unvalidated input as Done. If the parent is
   In Progress, stop with `batch already claimed`. If it is Blocked, require
   the user to move it to Ready for AI.
3. Claim the Ready parent using the claim protocol above. A pre-claim error
   does not seize or block a parent; a post-claim global failure must block it.
4. Build or reconcile the ETF queue checklist. Read only the exception cards
   needed to classify unchecked tickers as open-retry or normal-pending.
5. Keep an in-memory `attempted_this_run` set so an item is not selected
   repeatedly in the same invocation, plus `processed_count` for downstream
   item attempts. In automation, select up to `batch_size` items sequentially
   and stop selecting when `processed_count` reaches `batch_limit`. Compute:
   - `normal_pending`: unchecked tickers with no open exception and not already
     attempted in this run;
   - `retry_pending`: unchecked tickers with an open exception whose
     `terminal` is `false`, whose `confirmation` is `none` or `confirmed`, and
     not already attempted in this run;
   - `confirmation_pending`: unchecked open exceptions whose
     `confirmation` is `required` but not yet `confirmed`.
   - `terminal_pending`: unchecked open exceptions with `terminal: true`.
6. At the start of each selection pass, if automation has reached
   `batch_limit`, finalize using step 12. The status flag `retry_pending: true`
   is a scheduling preference, not proof
   that a retry exists. If it is true but the actual retry set is empty, clear
   it while keeping `state: running` and the current claim, then recompute.
   Select the first unattempted retry when the flag is true and one exists;
   otherwise select the first unattempted normal item. If manual work remains
   only in the other set, select its first item. If no unattempted work
   remains, finalize using step 12.
7. For each selected retry, move/reuse its exception card in the active list.
   For each selected ticker, invoke `$check-etf-performance <TICKER>` with
   `mode: lean` one ticker at a time. Wait for its research delegation,
   reconciliation, pre-save review, and durable-write result. Do not perform
   those steps locally. Require the downstream handoff envelope defined in
   `Failure classification`; missing or ambiguous fields are a global result.
   Never invoke downstream for a `confirmation_pending` item; it becomes
   eligible only after the user changes that exception line to
   `confirmation: confirmed` and moves the parent to Ready for AI.
8. Mark the checklist item checked only for `status: PASS`, `scope: item`,
   and `durable_write: completed` in that envelope. On success, close any
   matching exception by moving it to Done and marking it complete, then
   increment `processed_count` once for the successful item.
9. On an explicit downstream item-level failure, leave the item unchecked,
   create/update the one exception card, set `confirmation: required` only
   for `confirmation_required` and otherwise `confirmation: none`, set
   `terminal: true` only for `unsupported-etf-type` and otherwise `false`,
   add the ticker to `attempted_this_run`, increment `processed_count`, and
   move/update the exception in the configured Blocked list after the failure.
   If that exception state change fails, classify the run as global. In
   automation, continue to another unattempted item while batch capacity remains;
   otherwise finalize after this bounded batch. Manual mode continues while
   unattempted work remains.
10. On a global failure after this invocation owns the claim, update only the
    controlled parent status block with `state: blocked`, empty
    `claim_token`, `retry_pending: true` only when any retryable open item
    exception exists,
    `failure_scope: global`, and the short failure code; move the parent to
    Blocked. Do not create a ticker exception card. A global failure before
    exact parent resolution, or a lost claim, returns without pretending to
    update Trello. If a required state update/move fails, report that state
    change failure and stop.
11. For manual mode, retain `state: running` and the claim while unattempted
    work remains and repeat steps 5–10. Do not write `state: ready` while the
    parent stays In Progress.
12. After an item, when automation reaches its batch capacity, or after the
    final queue inspection, use these mutually exclusive branches:
    - if every checklist item is checked, write `state: done`,
      `retry_pending: false`, empty token and failure fields, move the parent
      to Done, and mark it complete;
    - else if any unattempted normal or retry item remains, manual mode
      continues with the running claim; automation writes `state: ready`,
      clears the token, moves the parent to Ready for AI, and sets
      `retry_pending: true` only when no unattempted normal item remains but
      an unattempted retry item does remain, otherwise `false`;
    - else if an unchecked item has a retryable open exception, write
      `state: blocked`, `retry_pending: true`, `failure_scope: item`, the
      exception code, clear the token, move the parent to Blocked, and do not
      mark it complete;
    - else if an unchecked item has `terminal_pending` or
      `confirmation_pending`, write `state: blocked`, `retry_pending: false`,
      `failure_scope: item`, the terminal/confirmation code, clear the token,
      move the parent to Blocked, and do not mark it complete;
    - otherwise report a global checklist/state inconsistency and, because the
      claim is owned, block the parent without creating an exception card.

When a user moves a Blocked parent to Ready for AI, its status block may keep
`retry_pending: true`; the next invocation prioritizes non-terminal open
exception tickers that do not require unconfirmed user confirmation. If no
eligible open retry exists, the flag is cleared before selection; a terminal
or confirmation-pending exception still keeps the parent blocked when no
normal work remains. When an
automation run releases a non-terminal parent with normal work after its
configured batch capacity, it writes `retry_pending: false`, so open
exceptions are skipped until normal work is exhausted. Manual mode processes
all unattempted normal and retry work in the same invocation, while each
ticker is attempted at most once per invocation.

## Failure classification

Treat these as global failures: missing/ambiguous exact parent target,
workflow/configuration/run-mode/batch-size mismatch, Trello authentication/tool failure,
board/list resolution failure, unreadable/malformed input, checklist mismatch,
an owned claim state error, or `research sub-agent unavailable` from the
downstream workflow. A lost claim is a non-mutating abort, not a global
failure to write to the parent. A pre-claim configuration/Trello failure is
reported without seizing or blocking a parent; a post-claim global failure
blocks the owned parent when the required Trello writes succeed.

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
  `item-hard-data-gap`;
- global: `research-sub-agent-unavailable`, `trello-tool-failure`,
  `trello-auth-failure`, `board-list-resolution-failure`,
  `workflow-config-mismatch`, `input-malformed`, `checklist-mismatch`,
  `claim-state-error`, `global-error`, `unknown-result`.

Apply precedence before mapping: any global code, `status: ERROR`, or
`scope: global|unknown` is always `global_blocked`, even if other fields
incorrectly say PASS. A global code also overrides a contradictory item scope.
Reject unknown codes, missing fields, and contradictory combinations as global;
never let a contradictory PASS reach the checklist.

After that precedence check, apply this closed mapping:

- `PASS` + `scope: item` + `durable_write: completed` is `success`; the
  downstream durable workflow has completed its required research,
  reconciliation, pre-save gate, and vault writes. It also requires
  `exhausted: false`, `confirmation: none`, and a success code. A disclosed
  gap remains a successful result when downstream says so.
- `WARNING` + `scope: item` + `durable_write: not_completed` is
  `confirmation_required`: keep the item unchecked and record the required
  user confirmation in its exception card. This preserves the project rule
  that a reviewer warning pauses a save. It also requires
  `exhausted: false`, `confirmation: required`, and a warning code. A
  scope-free or `scope: unknown` warning is global because the coordinator
  cannot safely assign ownership.
- `CHANGES_REQUIRED` or `BLOCKED` with explicit `scope: item` is
  `item_blocked` only with `durable_write: not_completed`,
  `exhausted: true`, `confirmation: none`, and an item code; this includes the
  normalized code `unsupported-etf-type` and a final item gate that remains
  non-PASS after downstream's correction/re-review policy. Create or reuse the
  exception card. `unsupported-etf-type` must set `terminal: true` and is not
  eligible for retry; other accepted item codes set `terminal: false`.
- A known global code, `scope: global|unknown`, `status: ERROR`, or a
  Trello/tool/auth failure is `global_blocked`; block the parent and create no
  ticker exception.
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
release a non-terminal parent back to Ready for AI, create an exception card
only for an explicit item-level block, and stop after that capacity or queue
exhaustion. Generic scheduler text must respect the parent card’s `batch_size`.
```

Never schedule overlapping automation workers for the same parent.

## Completion response

Return a compact status containing:

- parent card and current list;
- tickers processed in this invocation, if any;
- counts of checked, normal-pending, retry-pending, and blocked items;
- any exception card URL/name;
- downstream output links only when the downstream skill returned them.

Do not paste the full ETF performance report into Trello or the chat when a
durable output link is available.
