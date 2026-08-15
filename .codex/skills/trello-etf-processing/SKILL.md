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

After a confirmed claim, invoke exactly one ticker performance check and ask it
for the caller-owned machine-readable handoff block:

```text
$check-etf-performance <TICKER>
mode: lean
caller: trello-etf-processing
handoff: trello_handoff
```

The downstream skill still owns research delegation, reconciliation, pre-save
review, durable writes, and its normal human-facing result. After that work it
must return exactly one structured `trello_handoff` block with the complete
seven-field envelope:

```text
status: PASS|WARNING|CHANGES_REQUIRED|BLOCKED|ERROR
scope: item|global|unknown
durable_write: completed|not_completed|unknown
exhausted: true|false
confirmation: none|required|confirmed
code: <normalized-stable-code>
reason: <concise-one-sentence-reason>
```

Skill 3 is the deterministic adapter at this boundary. Accept only the
complete structured block; never infer success or failure from prose, links,
file existence, or a human-facing report. Normalize `code` by trimming,
lowercasing, and replacing spaces and underscores with hyphens before forwarding.

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

This complete normalized envelope is the `invalid-envelope global-stop
sentinel` for Skill 2; it must not be treated as an ordinary item-level error.
Forward it to trello-etf-result as this complete envelope together with any
downstream output links. Forward it to trello-etf-result exactly once; never
move the child to Done/Blocked directly. This skill does not decide the final
child lane; `trello-etf-result` owns that transition.
