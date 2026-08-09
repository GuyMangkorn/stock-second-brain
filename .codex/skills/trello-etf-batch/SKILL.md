---
name: trello-etf-batch
description: "Orchestrate sequential ETF performance batches from a specific Trello parent card whose description contains workflow: trello-etf-batch, maintaining checklists, exception cards, resume/retry state, and invoking check-etf-performance in lean mode. Use when the user asks to run or resume a Trello ETF batch from that parent card; a Markdown list file alone must not trigger execution."
---

# Trello ETF Batch

## Purpose and boundary

Use this skill as a Trello workflow coordinator for ETF performance batches.
Keep Trello state management here and delegate every ETF analysis to
check-etf-performance.

- Do not browse issuer, regulator, exchange, benchmark, or secondary sources
  from this coordinator.
- Do not duplicate the research worker or pre-save reviewer required by
  check-etf-performance.
- Do not write ETF performance pages, source batches, entities, or logs here.
  The downstream skill remains the sole writer of those durable vault outputs.
- Do not treat the input list's price, AUM, displayed return, or expense-ratio
  snapshot as evidence.
- Do not depend on Trello attachments. Read the local path in the card
  description.
- Do not start merely because a card exists. Require an explicit skill
  invocation or an automation prompt.

## Trigger and card contract

Use for prompts such as:

- `[$trello-etf-batch] https://trello.com/c/<card>`
- `Run trello-etf-batch on the filtered ETF batch card`
- An automation prompt that names this skill and the specific parent card.

Do not start from a list file alone. Require a specific parent card URL or
ARI, or a prompt that otherwise points to one exact parent card.

The parent card must contain the exact configuration key:

`workflow: trello-etf-batch`

The required input key is:

`input: /absolute/or/project-relative/path/to/etf-list.md`

Use `mode: lean` by default and reject `mode: chat` for this durable batch
workflow. Resolve project-relative paths from the stock-second-brain root.

Use these defaults unless the card supplies an override:

- Board: `stock-analysis-task`
- Ready list: `Ready for AI`
- Active list: `In Progress`
- Blocked list: `Blocked`
- Done list: `Done`

Accept optional one-line overrides: `board:`, `ready_list:`,
`active_list:`, `blocked_list:`, and `done_list:`.

## Token-efficient Trello access

1. If the prompt supplies a card URL or ARI, read that card directly and verify
   its exact workflow key.
2. Otherwise resolve the configured board, search cards within that board for
   the workflow key, then read only the candidate cards and verify the exact
   description line.
3. Stop with an ambiguity error when more than one eligible open parent card
   remains and the prompt does not identify one.
4. After resolving the parent, read only that card and its `ETF queue`
   checklist. Do not list the entire board on every loop.
5. Search/read exception cards only for the current ticker or for open retries.
6. Use checklist-item updates for normal progress. Do not create a child card
   for a successful ETF.

## Queue input and checklist

Read the Markdown input file and parse the table column named `Symbol`,
case-insensitively. Preserve source order, trim whitespace/backticks, convert
to uppercase, and deduplicate repeated symbols by keeping the first canonical
occurrence.

- Fail globally when the file is missing, unreadable, has no Symbol column, or
  has a malformed/empty ticker row.
- Ignore every other column for queue construction and evidence.
- Create one checklist named `ETF queue` when it does not exist.
- When the checklist exists, preserve checked states and match items by exact
  canonical uppercase ticker name.
- Add only missing source tickers. If the existing checklist contains unknown,
  duplicate, or checked items no longer present in the source, stop with a
  checklist mismatch instead of silently deleting or unchecking work.

The checklist is the normal progress source of truth. A checked item means the
downstream performance workflow completed successfully for that ticker.

## Parent and exception state

Parent card states:

- `Ready for AI`: eligible to be claimed or explicitly retried.
- `In Progress`: claimed batch; treat as an execution lock.
- `Blocked`: unresolved exception or global failure; do not retry until the
  user moves the parent back to `Ready for AI`.
- `Done`: all queue items are checked; mark the card complete.

For an item-level failure, create or reuse one exception card in the blocked
list. Use this name:

`[BLOCKED][ETF] <TICKER> | check-etf-performance`

Its short description must contain:

```text
workflow: trello-etf-batch-exception
parent: <parent card URL>
ticker: <TICKER>
failure: <stable failure code>
reason: <one concise sentence>
retry: move parent to Ready for AI
```

Reuse an existing exception card only when both its name and parent URL match.
Move a retried exception to the active list while it is running; move it to
Done/complete after the ticker succeeds. Never create duplicate exception
cards for the same parent/ticker.

## Execution loop

1. Resolve and validate the parent card and its configuration.
2. Resolve board/list IDs by exact name and claim a Ready parent by moving it to
   the active list. If a parent is already In Progress, treat it as claimed and
   continue only when the invocation explicitly targets that batch.
3. Build or reconcile the ETF queue checklist.
4. Select the first unchecked ticker in source order:
   - while the parent is In Progress, skip unchecked tickers with an open
     exception card so independent work can continue;
   - when the parent was moved from Blocked to Ready, retry the first open
     exception before selecting ordinary unchecked work.
5. Invoke `$check-etf-performance <TICKER>` with `mode: lean`. Wait for its
   research delegation, reconciliation, pre-save review, and durable-write
   result. Do not perform those steps locally.
6. On success, mark the checklist item checked. If an old exception card exists,
   move it to Done and mark it complete.
7. On an item-level failure, create/update the exception card and leave the
   checklist item unchecked. Continue with the next unblocked ticker.
8. On a global failure, stop immediately, preserve the current item unchecked,
   record the concise batch failure/status reason on the parent card, and move
   the parent to Blocked. Do not create a ticker exception card for a global
   failure.
9. For an interactive/manual invocation, repeat steps 4–8 until no eligible
   ticker remains. For an automation invocation, process exactly one ticker and
   return the updated state.
10. When no unchecked ticker remains, move the parent to Done and mark it
    complete if no open exception remains. If only open exceptions remain,
    move the parent to Blocked and do not mark it complete.

## Failure classification

Treat these as global failures: Trello authentication/tool failure, ambiguous
parent or board/list resolution, unreadable/malformed input, checklist
mismatch, or `research sub-agent unavailable` from the downstream workflow.

Treat these as item-level failures: `unsupported ETF type`, an unresolved
ETF-specific source/data gap, or a downstream pre-save review that remains
non-PASS after its own correction/re-review policy. Do not override the
downstream quality gate.

## Automation contract

The skill does not create automations. A recurring automation should explicitly
invoke this skill, identify the exact parent card URL or ARI, and say:

`Process exactly one unchecked ETF, update the Trello parent/checklist state,
create an exception card only if needed, and stop after that ETF.`

If the parent is left In Progress after an automation run, the next run may
continue that claimed batch only when it targets that same explicit parent
card. If a run is abandoned, move the parent to Ready for AI before retrying.

## Completion response

Return a compact status containing:

- parent card and current list;
- ticker processed in this invocation;
- counts of checked, pending, and blocked items;
- any exception card URL/name;
- downstream output links only when the downstream skill returned them.

Do not paste the full ETF performance report into Trello or the chat when a
durable output link is available.

## End of complete candidate durable file: .codex/skills/trello-etf-batch/SKILL.md
