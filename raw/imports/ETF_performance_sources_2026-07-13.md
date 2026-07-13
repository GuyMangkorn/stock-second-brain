---
type: source-note
source_profile: etf-performance-delta
accessed: 2026-07-13
canonical_output: wiki/analysis/performance/ETF_AMEX_DGRO Performance.md
tags:
  - source/etf
  - source/performance
  - source/benchmark
---

# DGRO Benchmark Comparator Source - 2026-07-13

## Source Map

| Scope | Official source | Role | Data date |
|---|---|---|---|
| `AMEX:DGRO` | [iShares DGRO product page](https://www.ishares.com/us/products/264623/ishares-core-dividend-growth-etf), [DGRO factsheet](https://www.ishares.com/us/literature/fact-sheet/dgro-ishares-core-dividend-growth-etf-fund-fact-sheet-en-us.pdf) | Fund identity, NAV Total Return, and issuer benchmark metadata | 2026-06-30 for performance; see prior batch for full source map |
| `S&P 500 TR` | [iShares IVV factsheet](https://www.ishares.com/us/literature/fact-sheet/ivv-ishares-core-s-p-500-etf-fund-fact-sheet-en-us.pdf) | Official S&P 500 Index (USD) calendar-year benchmark returns | 2026-03-31 factsheet; calendar years 2021-2025 |
| `S&P 500` | [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Index definition and total-return series identity | accessed 2026-07-13 |

## Reporting Scope

- Comparator window: complete calendar years 2021-2025.
- Currency: USD.
- Return basis: S&P 500 Total Return with dividends reinvested; not price
  return and not net total return.
- DGRO series: official `NAV Total Return`, including reinvested distributions
  and fund expenses, as captured in the prior 2026-07-12 batch.
- The issuer-tracked DGRO index remains `Morningstar US Dividend Growth Index`.
  `S&P 500 Total Return` is the common reference benchmark requested for the
  performance comparison, not a substitute description of DGRO's index.

## Extracted Facts

| Year | DGRO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 26.56% | 28.71% |
| 2022 | -7.85% | -18.11% |
| 2023 | 10.43% | 26.29% |
| 2024 | 16.61% | 25.02% |
| 2025 | 15.74% | 17.88% |

The IVV factsheet identifies its benchmark as `S&P 500 Index (USD)` and reports
the S&P 500 benchmark rows above. The annual DGRO rows and the source-date
details remain in `raw/imports/ETF_performance_sources_2026-07-12.md`.

## Calculations

- S&P 500 cumulative return: `Π(1 + annual TR) - 1 = 96.17%`.
- S&P 500 CAGR: `(1 + 96.17%)^(1 / 5) - 1 = 14.43%`.
- DGRO cumulative return and CAGR retained from the official common window:
  `73.82%` and `11.69%`.
- DGRO minus S&P 500: `-22.35 percentage points` cumulative and `-2.74
  percentage points` annualized CAGR.
- DGRO beat S&P 500 in 2022 by `10.26 percentage points`; it lagged in 2021,
  2023, 2024, and 2025.

## Missing / Unverified Data

- S&P 500 comparator rows for 2014-2020 are not added to the DGRO page because
  those DGRO rows are marked `*` as secondary dividend-reinvested market-price
  proxies rather than official NAV Total Return.
- A same-date current YTD S&P 500 comparator is not added to the annual table;
  the existing DGRO YTD snapshot remains as of 2026-06-30.

## Handoff For Ingest

Update only `wiki/analysis/performance/ETF_AMEX_DGRO Performance.md` with the
S&P 500 comparator and retain the issuer benchmark as metadata. Do not change
the DGRO entity's tracked-index description or create a corporate valuation.
