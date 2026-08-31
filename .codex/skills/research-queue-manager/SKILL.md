---
name: research-queue-manager
description: Process Ready ETF Research Cards sequentially through the project Markdown Research Queue.
---

# Research Queue Manager

Use this project-scoped skill for a scheduled or explicit bounded processing
run. The manager owns selection, claim confirmation, handoff validation, result
routing, and the scoped Git commit. It does not infer a workflow from a ticker
or title. V1 selects only Ready cards whose explicit workflow is
`check-etf-performance`.

## Execution contract

Require exactly one positive base-10 `count` and an execution profile of
`interactive-delegated` or `scheduled-inline`. Select oldest-first with a
stable timestamp/card-ID tie-break and process sequentially in the same saved
project checkout. Acquire the project lease before selection. Under
`scheduled-inline`, all ETF research and the pre-save verification checklist
remain inline in the top-level context; no worker or reviewer is dispatched.

The command surface exposes the claim boundary and lets the caller invoke the
downstream workflow before routing its result:

```text
python3 scripts/research_queue.py claim-next --count 1 --owner research-queue-manager
python3 scripts/research_queue.py renew --card-id <ID> --owner <OWNER> --fencing-token <TOKEN> --phase pre-write
python3 scripts/research_queue.py route --card-id <ID> --owner <OWNER> --fencing-token <TOKEN> --handoff-json '<SEVEN-FIELD JSON>' --commit
```

For deterministic integration tests, `process` accepts one handoff fixture and
uses the same claim/route/commit path. A production caller must invoke
`check-etf-performance` with `mode: lean`, the explicit execution profile, and
the queue caller boundary, then pass only its complete structured handoff to
`route`.

## Lease and fencing

Each claim records owner, acquisition time, execution phase, fencing token, and
a renewable two-hour `lease_expires_at`. `updated_at` is business activity and
does not keep a dead worker alive. Renew only at safe phase boundaries. Every
mutation and downstream pre-save boundary revalidates the token. Run recovery
when a claim is expired:

```text
python3 scripts/research_queue.py recover
```

An expired pre-write claim with no scoped output returns to Ready. A writing or
finalizing claim, or ambiguous partial output, becomes Blocked with
`partial-write-recovery`. Never retry that case automatically.

## Result boundary

Accept exactly these seven handoff fields:

```text
status, scope, durable_write, exhausted, confirmation, code, reason
```

Only `PASS + item + completed + false + none + success|durable-write-complete`
routes to Done. Accepted item-scoped warnings, unsupported types, data gaps,
and downstream errors route to Blocked and allow the next card. Missing,
malformed, contradictory, or global results persist `unknown-result` on the
known card, report a global stop, and leave unstarted cards unchanged. Never
infer success from prose, exit status, links, or file presence.

## Git boundary and human controls

On successful completion, commit the card and explicitly supplied scoped
outputs together; unrelated user changes remain unstaged. Done and Cancelled
cards retain stable paths. Humans may use `hold`, `unblock`, and `cancel` for
manual control; In Progress and Done are automation-owned.
