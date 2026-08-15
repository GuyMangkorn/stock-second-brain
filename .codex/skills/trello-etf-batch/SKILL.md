---
name: trello-etf-batch
description: "Use for Trello ETF workflow prompts that explicitly provide task: backlog|etf-performance and a positive count; route bounded work to the focused Trello ETF skills. Do not use for unrelated Trello actions."
---

# Trello ETF Workflow Manager

## Purpose and boundary

`trello-etf-batch` is Skill 4, the manager/router for the Trello ETF workflow.
It parses the scheduler or user task, selects eligible cards, limits the run,
and delegates the selected work. It does not own ETF research, source
discovery, review gates, durable vault writes, or the state machine of a
backlog, processing, or result skill.

- Do not browse issuer, regulator, exchange, benchmark, or secondary sources.
- Do not write `raw/`, `wiki/`, `index.md`, or `log.md`.
- Do not create automations or schedule workers.
- Do not select or mutate cards outside the lane required by the selected task.
- Historical `ETF queue`, `batch_size`, and exception-card text may remain on
  old cards as inert history; this manager never reads, validates, writes, or
  resumes that former monolith runtime protocol.

The focused skills own their respective mutations: `$trello-etf-backlog`
splits masters, `trello-etf-processing` claims and processes children, and
`trello-etf-result` routes each processing result. The downstream
`check-etf-performance` skill remains the sole owner of research and durable
ETF performance outputs.

## Invocation contract

Every invocation must provide both fields, exactly once:

```text
task: backlog|etf-performance
count: <positive base-10 integer>
```

`count` must be a positive base-10 integer. count must be a positive base-10 integer matching `[1-9][0-9]*`.
Reject missing, duplicate, zero, negative, fractional or nonnumeric values
as
`workflow-config-mismatch` before any Trello mutation. Never infer `count`
from a card, title, queue length, available work, scheduler defaults, or a
previous run. Reject an unknown task before selection or mutation as the same
configuration error.

The manager resolves the configured board and required list names before
selection. Trello authentication, board/list resolution, malformed card
metadata, and other configuration failures are global failures: stop without
claiming additional work and do not report an unconfirmed mutation.

## Selection and routing

Maintain an in-memory `attempted_this_run` set. Selection is oldest-first by
card last activity, is bounded to at most `count`, and is sequential. Process
at most count selected cards. Add an
identity to the set before delegation so a card cannot be selected twice in
one run, even when it remains eligible after a delegated failure. Never touch
cards in `In Progress`, `Blocked`, `Done`, archived cards, malformed cards, or
cards without the identity required by the selected route.

### `task: backlog`

For task backlog, select masters only from `Backlog` and route them to the
focused backlog skill.

Select at most `count` open master cards in `Backlog` with valid backlog
configuration. Invoke `$trello-etf-backlog` for one master at a time, wait for
its result, then select the next oldest unattempted master. Track
`attempted_this_run` by master ARI. A master that remains in `Backlog` after
the focused skill returns is not eligible for a second selection in this run.

An item-specific child-creation failure belongs to the focused backlog skill;
continue to the next selected master when it reports that item-level outcome.
Stop globally for Trello, authentication, board/list, or configuration
failures.

### `task: etf-performance`

For task etf-performance, select children only from `Ready for AI`.

Select at most `count` valid, open child cards in `Ready for AI`, oldest-first
by last activity. A valid child has the required `workflow: trello-etf-item`,
`parent_ari`, and canonical `ticker` identity. Track `attempted_this_run` by
child ARI and never select a child from another lane. Never touch other lanes.

For each selected child, run the focused skills sequentially:

```text
trello-etf-processing(child card)
→ trello-etf-result(child card, processing result)
```

The processing skill must claim the child before invoking
`$check-etf-performance <TICKER>` with `mode: lean`; the result skill owns the
final `Done` or `Blocked` transition. If the result skill blocks the child
for an accepted ticker-specific failure, continue to the next selected child.
Stop the global run on Trello, authentication, board/list, configuration,
claim-state, or contradictory-result failures. Do not retry the failed child
or select it twice in this run.

## Overlap and completion

The manager must not overlap manager workers and must not schedule overlapping
workers for the same board.
The scheduler and any manual caller must provide one explicit task and count;
the manager processes only the requested number sequentially. A lane claim by
the processing skill is the concurrency boundary for a child. Return a
compact run result listing the task, requested count, attempted card IDs,
completed/blocked outcomes, and any global failure code. Do not claim that a
Trello transition or downstream durable write succeeded unless the delegated
skill confirmed it.
