# ADR: Decompose the Trello ETF Workflow into Focused Skills

**Date:** 2026-08-15  
**Status:** Proposed  
**Deciders:** Stock Second Brain maintainers

## Context

`trello-etf-batch` currently combines backlog interpretation, ETF queue
construction, lane claiming, downstream invocation, result classification and
exception-card management. This makes a scheduled workflow difficult to route
and makes each responsibility hard to test independently.

The requested workflow has three distinct operations: split a user-created
master card into ticker cards, process a Ready-for-AI ticker card, and route
the result to Done or Blocked. A fourth manager must choose the operation from
the scheduler prompt and honor its requested count.

## Decision

Keep `$trello-etf-batch` as the public manager/router entry point and create
three focused skills:

- `trello-etf-backlog`
- `trello-etf-processing`
- `trello-etf-result`

Use `parent_ari + ticker` as the child identity. Child cards carry the ticker
for processing and the parent ARI for batch isolation. A child begins in
`Ready for AI`; processing claims it into `In Progress`; result routing moves
it to `Done` on a strict successful durable-write envelope or to `Blocked`
with a recorded reason for every other result.

## Consequences

Positive:

- Each state mutation and downstream handoff has one owner.
- Multiple master cards may contain the same ticker without identity collision.
- The scheduler can bound work with an explicit positive `count`.
- The child card is both the work item and the failure record, so exception
  cards are unnecessary for this workflow.

Costs and constraints:

- Existing monolithic checklist/exception behavior is replaced for new runs.
- The manager must prevent overlapping scheduled workers.
- Partial backlog creation leaves the master in `Backlog` and relies on
  idempotent retry by `parent_ari + ticker`.
- Trello lane changes remain operational claims rather than atomic locks.

## Rejected alternatives

1. Keep the monolith and add internal sections: lower file churn, but the
   responsibilities remain coupled and cannot be invoked independently.
2. Build a persistent event/saga layer: stronger orchestration semantics, but
   it adds storage and state machinery not required for the requested Trello
   card workflow.
