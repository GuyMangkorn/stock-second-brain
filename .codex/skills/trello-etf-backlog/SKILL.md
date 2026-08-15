---
name: trello-etf-backlog
description: "Use when a Trello master card in Backlog must be split into idempotent ETF ticker cards in Ready for AI."
---

# Trello ETF Backlog Splitter

This skill owns input parsing and child-card creation for a Trello ETF master card. It does not call check-etf-performance, browse sources, create performance pages, or manage child result state.

## Eligibility and input

Require exactly one resolved master card in the `Backlog` list. Its
description must contain exactly one accepted workflow line and exactly one
nonempty `input:` path/config line. Accept only
`workflow: trello-etf-backlog`, or the legacy `workflow: trello-etf-batch` when
the card is in `Backlog`. Duplicate, missing, blank, unknown, or conflicting
workflow/input lines are `input-malformed`/`workflow-config-mismatch`; stop
before reading a file or mutating Trello. Accept workflow matching
case-insensitively, then normalize it to the canonical workflow internally.
Resolve project-relative paths from the `stock-second-brain` root.

Read the referenced local Markdown ETF list before any Trello mutation; the parser must resolve exactly one Markdown table column named Symbol or Ticker, with the header named Symbol or Ticker matched case-insensitively, and normalize each nonempty value to uppercase after trimming whitespace/backticks, preserve source order, and deduplicate by first occurrence. Both aliases or neither alias are `input-malformed`; missing or unreadable files, empty rows, or zero canonical symbols also return `input-malformed` without mutation.

## Split and reconcile

For each canonical ticker, use `parent_ari + ticker is the idempotency key`. Look up children by parent ARI and ticker; an unarchived matching child in any lane counts as already created. Require creation in Ready for AI: otherwise create a child with title equal to ticker in `Ready for AI` and this exact description:

```text
workflow: trello-etf-item
parent_ari: <resolved master card ARI>
ticker: <CANONICAL_UPPERCASE_TICKER>
```

If an item-specific create error occurs, record it and provide continuation through remaining missing tickers after an item-specific create error. Keep the master in Backlog if any identity is missing. When every identity exists, move master to Done and complete it. A child in Blocked or Done counts as created.

An authentication, Trello, board, list, lookup, mutation, or configuration failure that is not an item-specific child-create error is a global failure. Stop without continuing mutations, leave every not-yet-confirmed ticker unclaimed, and report only confirmed master and child state. Do not claim that a failed master move or completion succeeded.

Return the created, already-present, and failed ticker identities, plus the final master-card state. Never mutate child result state.
