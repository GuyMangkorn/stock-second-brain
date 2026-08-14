---
name: trello-etf-backlog
description: "Use when a Trello master card in Backlog must be split into idempotent ETF ticker cards in Ready for AI."
---

# Trello ETF Backlog Splitter

This skill owns input parsing and child-card creation for a Trello ETF master card. It does not call check-etf-performance, browse sources, create performance pages, or manage child result state.

## Eligibility and input

Require exactly one resolved master card in the `Backlog` list. Its description must contain an input block with `workflow: trello-etf-backlog`. Accept legacy workflow: trello-etf-batch only when the card is in Backlog and has input. Resolve project-relative paths from the `stock-second-brain` root.

Read the referenced local Markdown ETF list before any Trello mutation; the parser must resolve exactly one Markdown table column named Symbol or Ticker and normalize each nonempty value to uppercase after trimming whitespace/backticks, preserve source order, and deduplicate by first occurrence. Missing or unreadable files, both aliases, neither alias, empty rows, or zero canonical symbols return `input-malformed` without mutation.

## Split and reconcile

For each canonical ticker, use `parent_ari + ticker is the idempotency key`. Look up children by parent ARI and ticker; an unarchived matching child in any lane counts as already created. Require creation in Ready for AI: otherwise create a child with title equal to ticker in `Ready for AI` and this exact description:

```text
workflow: trello-etf-item
parent_ari: <resolved master card ARI>
ticker: <CANONICAL_UPPERCASE_TICKER>
```

If an item-specific create error occurs, record it and provide continuation through remaining missing tickers after an item-specific create error. Keep the master in Backlog if any identity is missing. When every identity exists, move master to Done and complete it. A child in Blocked or Done counts as created.

Return the created, already-present, and failed ticker identities, plus the final master-card state. Never mutate child result state.
