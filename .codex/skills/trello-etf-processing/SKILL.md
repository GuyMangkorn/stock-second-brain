---
name: trello-etf-processing
description: "Use when a Trello ETF child card in Ready for AI must be processed by check-etf-performance."
---

# Trello ETF Performance Processor

This skill owns only the claim of one exact ETF child card and the handoff of
its processing result. It must not perform source discovery, research
delegation, reviewer work or vault writes locally. No local research and no
local vault writes are permitted.

## Required target and identity

Consume one exact child card in Ready for AI. Do not search by title, ticker,
or workflow key. Resolve the exact target directly and require these identity
fields:

```text
workflow: trello-etf-item
parent_ari: <parent card ARI>
ticker: <canonical uppercase ticker>
```

validate workflow trello-etf-item, parent_ari and ticker. match the child identity parent_ari + ticker, require the canonical uppercase ticker, and
require the title equal to ticker. Do not touch cards in In Progress, Blocked
or Done.

## Claim and direct reread

1. Require the exact child to be in `Ready for AI`.
2. Read and validate its canonical uppercase ticker.
3. move to In Progress for that same card.
4. directly reread the same card and confirm that its lane is `In Progress`.

If the lane does not confirm In Progress, return global claim-state-error and do not invoke downstream. Do not claim a mutation that was not confirmed.

## Single-ticker processing handoff

After a confirmed claim, invoke exactly one ticker performance check:

```text
$check-etf-performance <TICKER>
mode: lean
```

Wait for research delegation, reconciliation, pre-save review and durable-write
result. Require the complete result envelope with all seven fields:

```text
status: PASS|WARNING|CHANGES_REQUIRED|BLOCKED|ERROR
scope: item|global|unknown
durable_write: completed|not_completed|unknown
exhausted: true|false
confirmation: none|required|confirmed
code: <normalized-stable-code>
reason: <concise-one-sentence-reason>
```

Missing, contradictory, or malformed output is normalized to:

```text
status: ERROR
scope: global
durable_write: unknown
exhausted: false
confirmation: none
code: unknown-result
reason: Downstream result was missing, malformed, or contradictory.
```

Forward it to trello-etf-result as this complete normalized envelope together with any downstream output links. never move the child to Done/Blocked directly. This
skill does not decide the final child lane; `trello-etf-result` owns that
transition.
