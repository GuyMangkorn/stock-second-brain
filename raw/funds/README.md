# ETF Fund Facts

This folder owns normalized, source-backed structure facts for passive,
index-tracking equity ETFs: holdings, methodology, cost, income and identity.

Use `ETF_EXCHANGE_TICKER_fund_facts.md` so listings with the same ticker do not
collide. Each file must use `entity_key: EXCHANGE:TICKER`, retain separate
as-of dates for holdings, NAV/price, AUM, distributions, performance, and
methodology, and link back to its source note under `raw/imports/`.

Required sections are `Identity & Structure`, `Cost & Tradability`, `Portfolio
Exposure`, `Index Methodology`, `Performance & Income`, and `Risks & Gaps`.
Historical performance belongs to the single page under
`wiki/analysis/performance/ETF_EXCHANGE_TICKER Performance.md`; do not create a
second `raw/funds/*_performance.md` table.

Do not place company financial statements here. Do not normalize unsupported
bond, commodity, multi-asset, active, leveraged, inverse, or derivative-heavy
ETFs under the v1 contract.
