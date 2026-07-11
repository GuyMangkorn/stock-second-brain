---
name: explain-market-move
description: Use when the user asks why a stock, ETF, sector, index, commodity, or currency moved today, in a recent session, after an event, or over a short dated window.
---

# Explain Market Move

## Core Principle

Explain the observed move without claiming more causality than the evidence
supports. Establish the price window first, then rank at most three drivers.

## Default Mode

Use `chat` unless the user explicitly asks to save, update, refresh, or create a
memo. Keep chat output at or below 400 words and do not write files.

Promote to `lean` only when verified evidence materially changes an existing
thesis, risk, catalyst, or valuation watch item. In that case, create a compact
`wiki/analysis/catalysts/TICKER Market Move YYYY-MM-DD.md`, update the entity by
delta, and append one workflow bullet to `log.md`.

This skill may explain any ETF move in `chat`. Durable ETF output is limited to
passive, index-tracking equity ETFs. For bond, commodity, multi-asset, active,
leveraged, inverse, or derivative-heavy ETFs, stay in chat and do not create or
update ETF artifacts under the v1 contract.

## Workflow

1. Define the asset, exchange, session, timezone, and comparison window.
   For an ETF, resolve `entity_key: EXCHANGE:TICKER` and use the
   `ETF_EXCHANGE_TICKER` filename prefix for durable outputs.
2. Freshly verify price, percentage move, and timestamp. Correct a false premise
   before explaining it.
3. Compare the move with a relevant broad index and sector or peer basket.
   For an ETF, also distinguish fund-specific flows, premium/discount or
   tracking effects from benchmark and underlying-holdings moves.
4. Build a dated event timeline from official company or regulatory sources,
   market data, and reputable reporting.
5. Rank no more than three candidate drivers and assign one evidence label:
   - `confirmed event`: the event and timing are verified; causality may remain
     uncertain.
   - `probable driver`: timing, relative performance, and credible reporting
     support the attribution.
   - `speculative narrative`: plausible but not sufficiently evidenced.
6. State confidence and the observation that would weaken the explanation.

## Chat Output Recipe

1. `Bottom line`: one or two sentences, including a premise correction if needed.
2. `Move check`: asset return, benchmark return, window, and checked timestamp.
3. `Drivers`: up to three bullets with evidence label and confidence.
4. `What to watch`: one or two falsifiers or next confirmations.

Link sources beside the claims they support. Keep current price facts separate
from company-filed fundamentals or normalized ETF fund facts.

## Durable Output

The catalyst note contains only:

- move and relative-performance check
- ranked drivers with evidence labels
- for ETFs, separate fund-, index-, and underlying-holdings-level drivers
- thesis impact
- falsifiers / follow-up
- compact source links

Reference existing source, fundamentals, valuation, and decision notes. Do not
copy their financial tables, source maps, bull/bear cases, or missing-data lists.

## Common Mistakes

- Explaining a different session than the one the user meant.
- Treating a nearby headline as proven causality.
- Ignoring a market-wide or sector-wide move.
- Mixing stale quote data with current-event attribution.
- Saving routine price noise as durable company or ETF knowledge.
