---
type: source-batch
topic: ETF performance
accessed: 2026-08-16
input_source: Trello ETF child card DGS
input_count: 1
workflow: check-etf-performance
review_gate: PASS
reviewer: source_verifier
annual_rows_as_of: 2026-03-31
tags:
  - source/etf
---

# ETF Performance Source Batch - 2026-08-16

## Scope and gate

Research-bearing lean run for DGS. The fresh read-only research worker returned the evidence below, and the project-scoped source_verifier returned PASS after correction of the canonical links, as-of metadata, unsupported drawdown proxy, and metric labels.

## Complete evidence register

| Input ticker | Status | Canonical entity key | Primary region | Current NAV YTD / as-of | Source URL | Gap / resolution note |
|---|---|---|---|---|---|---|
| DGS | supported | NYSE Arca:DGS | Emerging Markets | 8.86% (2026-07-31) | https://www.wisdomtree.com/us/products/equity/dgs | passive/index-tracking equity; issuer-reported 10-year average annual NAV TR 8.31%; annual NAV TR rows 2016-2025 from presentation dated 2026-03-31; official daily NAV drawdown/recovery not disclosed |

## DGS official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:DGS | https://www.wisdomtree.com/us/products/equity/dgs | Official product page: identity, expense ratio, NAV/market price, YTD, 1-year/10-year fields and distributions | Page/current quote as of 2026-08-14; performance month-end as of 2026-07-31 |
| NYSE Arca:DGS | https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-dgs-1068.pdf | Official factsheet: fund identity, inception, NAV total-return definition, benchmark and supporting performance fields | Factsheet comparison fields as of 2026-06-30 |
| NYSE Arca:DGS | https://www.wisdomtree.com/us/media/dgs-presentation | Official presentation: annual NAV TR observations for complete calendar years 2016-2025 | Presentation dated 2026-03-31; values rounded as disclosed |
| NYSE Arca:DGS | https://www.sec.gov/Archives/edgar/data/1350487/000121465925011290/dgs73125497k.htm | SEC summary prospectus: passive objective, issuer benchmark, NAV return definition and quarterly risk observations | Prospectus filed 2025; risk observations include 1Q2020 and 2Q2020 |
| NYSE Arca:DGS | https://www.wisdomtree.com/us/indexes/WTEMSC | Official issuer index methodology/benchmark identity | Accessed in current research; benchmark metadata |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark identity; cached annual convention | USD total return with dividends reinvested; cache as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached source reference for 2016-2019 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached source reference for 2018-2022 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached source reference for 2021 row | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached source reference for 2022-2025 rows | Reference window as documented in skill |

## DGS raw observations and calculations

| Year | DGS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 14.91% | 11.96% |
| 2017 | 35.48% | 21.83% |
| 2018 | -15.39% | -4.38% |
| 2019 | 17.28% | 31.49% |
| 2020 | 4.14% | 18.40% |
| 2021 | 15.60% | 28.71% |
| 2022 | -12.15% | -18.11% |
| 2023 | 18.92% | 26.29% |
| 2024 | 2.13% | 25.02% |
| 2025 | 20.40% | 17.88% |
| 2026 YTD | 8.86% | not available from cached current-year benchmark |

- Metric basis: DGS official NAV Total Return, USD, distributions reinvested and fund expenses reflected in NAV.
- Issuer benchmark: WisdomTree Emerging Markets SmallCap Dividend Index (WTEMSC); it is retained as metadata and not silently substituted for the common S&P 500 reference.
- 2016-2025 DGS compound: 138.91% cumulative; rounded-input CAGR 9.10%.
- 2021-2025 DGS compound: 48.50% cumulative; rounded-input CAGR 8.23%.
- S&P 500 2016-2025 cached compound: 298.33% cumulative; rounded-input CAGR 14.82%.
- S&P 500 2021-2025 cached compound: 96.17% cumulative; rounded-input CAGR 14.43%.
- Formula: CAGR = product(1 + annual return)^(1 / number of years) - 1.
- Current NAV: 63.900 USD and market price: 63.570 USD, as of 2026-08-14; market-price discount -0.519% is separate from NAV TR.
- Recent distributions: 0.84000 USD (ex/pay 2026-06-25/2026-06-29), 0.20000 USD (2026-03-26/2026-03-30), 0.57891 USD (2025-12-26/2025-12-30), and 0.79500 USD (2025-09-25/2025-09-29).

## Gaps and conflicts

- Raw start/end TR values, exact endpoint dates, and elapsed years for the issuer-reported 10-year average annual NAV TR 8.31% are not disclosed; it is not relabelled as an independently calculated CAGR.
- Official daily NAV history sufficient for maximum drawdown and recovery is not verified; no numeric secondary proxy is saved.
- S&P 500 2026 current YTD was not used because the cached convention ends at 2025-12-31 and no fresh current benchmark evidence was supplied in this packet.
- The DGS annual observations are rounded source values, so cumulative/CAGR calculations are approximations from rounded inputs.
