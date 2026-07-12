---
type: source-note
instrument_type: ETF
entity_key: AMEX:DGRO
ticker: DGRO
source_profile: performance-history
accessed: 2026-07-12
normalized_output: raw/funds/ETF_AMEX_DGRO_performance.md
tags:
  - source/etf
  - source/performance
  - ticker/DGRO
---

# DGRO Performance Source Note - 2026-07-12

## Source Map

| Priority | Source | Data date / access | Use |
|---|---|---|---|
| 1 | [iShares DGRO product page](https://www.ishares.com/us/products/264623/ishares-core-dividend-growth-etf) | official performance through 2026-06-30; accessed 2026-07-12 | NAV total return, market-price return, benchmark, YTD and rolling returns |
| 1 | [iShares DGRO factsheet](https://www.ishares.com/us/literature/fact-sheet/dgro-ishares-core-dividend-growth-etf-fund-fact-sheet-en-us.pdf) | factsheet 2026-03-31 | calendar-year 2021-2025, 3-year standard deviation, benchmark |
| 4 | [PortfoliosLab DGRO](https://portfolioslab.com/symbol/DGRO) | dividend-adjusted daily data; last updated 2026-07-11 | monthly behavior and drawdown context only; secondary source |
| 4 | [Total Real Returns DGRO](https://totalrealreturns.com/n/DGRO%2CSPY) | dividend-reinvested series through 2026-07-09 | extended pre-2021 market-price-adjusted proxy only; secondary source |

## Reporting Scope

Canonical ranking uses official issuer NAV total returns for the common complete
window 2021-2025. The issuer page exposes 2026 YTD as a partial period and it is
not ranked with complete calendar years. The 2014-2020 extension is retained as
secondary context because the current issuer calendar table exposes only
2021-2025.

## Currency / Units

- Returns are percentages in USD terms.
- NAV total return assumes reinvested distributions and includes fund expenses.
- Secondary monthly and drawdown data are dividend-adjusted market-data context,
  not a replacement for official NAV performance.

## Extracted Facts

| Field | Value | Source |
|---|---:|---|
| Fund inception | 2014-06-10 | iShares product page / factsheet |
| Benchmark | Morningstar US Dividend Growth Index | iShares product page |
| Expense ratio | 0.08% | iShares product page / factsheet |
| 2026 YTD NAV total return | 10.22% as of 2026-06-30 | iShares product page |
| 1-year NAV total return | 21.00% as of 2026-06-30 | iShares product page |
| 3-year average annual NAV return | 16.38% as of 2026-06-30 | iShares product page |
| 5-year average annual NAV return | 11.02% as of 2026-06-30 | iShares product page |
| 3-year standard deviation | 11.11% as of 2026-03-31 | iShares factsheet |

## Missing / Unverified Data

- `ไม่พบข้อมูลที่ยืนยันได้` for an issuer-exposed full calendar-year NAV table
  before 2021 in the captured page surface.
- The secondary extension is not mixed into the canonical issuer ranking.
- A reproducible monthly NAV series is not yet normalized; monthly behavior is
  retained as secondary dividend-adjusted context.

## Handoff For Ingest

- Normalize official 2021-2025 calendar-year NAV returns and the 2026 partial
  snapshot into `raw/funds/ETF_AMEX_DGRO_performance.md`.
- Keep secondary monthly and drawdown metrics visibly labelled.
- Use the common 2021-2025 window for the first cross-ETF matrix.
