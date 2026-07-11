# Equity Index ETF Reference

## Source Priority

1. Official issuer prospectus, product page, factsheet, and annual/semiannual report
2. Official daily or periodic holdings file and official NAV data
3. Official index-provider methodology, constituent, and rebalance documents
4. Regulator and listing-exchange filings or product pages
5. Reputable market data for dated price, volume, spread, and comparison context

Prefer the underlying document or downloadable table over a marketing summary.
Record a separate as-of date for holdings, NAV/price, distributions, AUM,
performance, and index methodology. Do not treat page access date as data date.

Preserve the vault's existing `entity_key` when a data vendor uses an exchange
alias such as `AMEX` while the issuer names the official venue differently.
Record both labels with sources and flag an unresolved identity conflict; never
create a second entity through silent alias normalization.

## Normalized Fund Facts

Use these sections in `raw/funds/ETF_EXCHANGE_TICKER_fund_facts.md`:

### Identity & Structure

- `entity_key`, ticker, exchange, fund, sponsor, domicile, listing currency
- benchmark index, passive/index-tracking evidence, inception date
- physical/full/sampling replication, distribution or accumulation policy
- securities-lending policy when decision-relevant and disclosed

### Cost & Tradability

- expense ratio and effective date
- AUM with currency and as-of date
- market price, NAV, premium/discount, volume, and spread with timestamps
- keep issuer operational facts separate from third-party market observations

### Portfolio Exposure

- holdings count and holdings as-of date
- top holdings, top-10 weight, sector, country, and currency exposure
- concentration calculations only when all included weights share one snapshot
- preserve cash, futures, swaps, and index positions disclosed in holdings

### Index Methodology

- eligible universe, selection screens, weighting, caps, buffers
- rebalance and reconstitution schedule
- dividend, quality, factor, ESG, or thematic rules that drive exposure
- methodology version or publication date

### Performance & Income

- NAV total return and market-price return with named periods
- benchmark return and sourced tracking difference/error definitions
- distribution yield, frequency, and history; do not mix trailing and indicated yield
- look-through multiples only with source, coverage, weighting basis, and as-of date

### Risks & Gaps

- concentration, factor, country, sector, FX, liquidity, closure, tax/withholding
- methodology, rebalance, sampling, tracking, and securities-lending risks
- missing/stale fields and source conflicts in their owning section

## Comparison Rules

Compare funds only across compatible mandate, benchmark exposure, currency,
distribution treatment, and periods. Explain when a lower fee is offset by
worse tracking, liquidity, tax treatment, or exposure mismatch. Holdings
overlap requires two compatible holdings snapshots; portfolio-fit claims also
require user-provided portfolio holdings.

## Decision Contract

Use this order:

1. `Portfolio Role`: core, satellite, income, factor tilt, or unsuitable
2. `Action Read`: `BUY`, `WATCH`, or `AVOID`, with conditions
3. `Current Price / NAV Check`
4. `Peer-Relative Read`
5. `Valuation / Cost / Tracking Read`
6. `Key Falsifier`
7. `Action-Relevant Gaps`
8. `Reports / Sources`

`BUY` requires current decision-grade market and fund data. Use `WATCH` when a
plausible role exists but evidence, price, freshness, or portfolio inputs are
incomplete. Use `AVOID` only when verified structure, exposure, cost, tracking,
or mandate mismatch supports it.
