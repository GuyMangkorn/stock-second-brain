# Normalized ETF Fund Facts

This folder owns normalized, source-backed facts for passive,
index-tracking equity ETFs.

Use `ETF_EXCHANGE_TICKER_fund_facts.md` so listings with the same ticker do not
collide. Each file must use `entity_key: EXCHANGE:TICKER`, retain separate
as-of dates for holdings, NAV/price, AUM, distributions, performance, and
methodology, and link back to its source note under `raw/imports/`.

Required sections are `Identity & Structure`, `Cost & Tradability`, `Portfolio
Exposure`, `Index Methodology`, `Performance & Income`, and `Risks & Gaps`.
Store facts once here; ETF entities, comparisons, and decisions should link to
this file rather than copy full tables.

Do not place company financial statements here. Do not normalize unsupported
bond, commodity, multi-asset, active, leveraged, inverse, or derivative-heavy
ETFs under the v1 contract.
