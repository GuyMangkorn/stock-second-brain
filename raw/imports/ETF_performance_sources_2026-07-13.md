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
| `S&P 500 TR cache` | `check-etf-performance` cached convention; [S&P 500 Low Volatility historical comparison](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) | Reusable complete-year S&P 500 TR reference | 2025-12-31; calendar years 2016-2025 |
| `S&P 500` | [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Index definition and total-return series identity | accessed 2026-07-13 |

## Reporting Scope

- Cached comparator window: complete calendar years 2016-2025.
- Official DGRO NAV common window: complete calendar years 2021-2025.
- Currency: USD.
- Return basis: S&P 500 Total Return with dividends reinvested; not price
  return and not net total return.
- DGRO series: official `NAV Total Return`, including reinvested distributions
  and fund expenses, as captured in the prior 2026-07-12 batch.
- The issuer-tracked DGRO index remains `Morningstar US Dividend Growth Index`.
  `S&P 500 Total Return` is the common reference benchmark requested for the
  performance comparison, not a substitute description of DGRO's index.

## Extracted Facts

| Year | DGRO TR | S&P 500 TR |
|---|---:|---:|
| 2016* | 15.20% | 11.96% |
| 2017* | 23.00% | 21.83% |
| 2018* | -2.38% | -4.38% |
| 2019* | 29.87% | 31.49% |
| 2020* | 9.50% | 18.40% |
| 2021 | 26.56% | 28.71% |
| 2022 | -7.85% | -18.11% |
| 2023 | 10.43% | 26.29% |
| 2024 | 16.61% | 25.02% |
| 2025 | 15.74% | 17.88% |

The IVV factsheet identifies its benchmark as `S&P 500 Index (USD)` and reports
the 2021-2025 rows above. The 2016-2025 cache uses the source references listed
in the `check-etf-performance` convention. The annual DGRO rows and the
source-date details remain in `raw/imports/ETF_performance_sources_2026-07-12.md`.

## Calculations

- Official 2021-2025 S&P 500 common-window cumulative return:
  `Π(1 + annual TR) - 1 = 96.17%`.
- Official 2021-2025 S&P 500 common-window CAGR:
  `(1 + 96.17%)^(1 / 5) - 1 = 14.43%`.
- Cached S&P 500 2016-2025 cumulative return: `298.33%`.
- Cached S&P 500 2016-2025 CAGR: `14.82%` from rounded annual inputs.
- DGRO cumulative return and CAGR retained from the official common window:
  `73.82%` and `11.69%`.
- DGRO blended 2016-2025 `10-year TR CAGR*`: `13.08%`, cumulative `241.91%`;
  2016-2020 are secondary proxy rows and 2021-2025 are official NAV TR rows.
- Blended proxy gap versus S&P 500 cache: `-56.42 percentage points` cumulative
  and approximately `-1.74 percentage points` annualized.
- DGRO minus S&P 500: `-22.35 percentage points` cumulative and `-2.74
  percentage points` annualized CAGR.
- DGRO beat S&P 500 in 2022 by `10.26 percentage points`; it lagged in 2021,
  2023, 2024, and 2025.

## Missing / Unverified Data

- DGRO's 2016-2020 rows remain marked `*` as secondary dividend-reinvested
  market-price proxies rather than official NAV Total Return. The resulting
  2016-2025 DGRO figure is explicitly `10-year TR CAGR*`, not official NAV TR.
- A same-date current YTD S&P 500 comparator is not added to the annual table;
  the existing DGRO YTD snapshot remains as of 2026-06-30.

## Handoff For Ingest

Update only `wiki/analysis/performance/ETF_AMEX_DGRO Performance.md` with the
S&P 500 comparator and retain the issuer benchmark as metadata. Do not change
the DGRO entity's tracked-index description or create a corporate valuation.
