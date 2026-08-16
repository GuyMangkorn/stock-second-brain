---
type: source-batch
topic: ETF performance
accessed: 2026-08-17
input_source: Trello ETF child card GSSC
input_count: 1
workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS
annual_rows_as_of: "2018-2025 official issuer; current NAV/YTD 2026-06-30"
tags:
  - source/etf
---

# ETF Performance Source Batch - 2026-08-17

## Scope and gate

Research-bearing lean run for GSSC. Source discovery, reading, reconciliation,
calculation, synthesis, and the complete pre-save checklist were performed
inline under `scheduled-inline`. No research worker, reviewer,
`source_verifier`, or other sub-agent was dispatched.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## Complete evidence register

| Input ticker | Status | Canonical entity key | Primary region | Current NAV YTD / as-of | Primary source | Gap / resolution note |
|---|---|---|---|---|---|---|
| GSSC | supported | NYSE Arca:GSSC | USA | 21.33% (2026-06-30) | https://am.gs.com/public-assets/documents/574deb07-24d6-11ef-870d-c7a1cb19e681 | passive/index-tracking U.S. small-cap multi-factor equity; 10-year history not yet available; daily NAV drawdown/recovery not disclosed |

## GSSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:GSSC | https://am.gs.com/public-assets/documents/574deb07-24d6-11ef-870d-c7a1cb19e681 | Official Goldman Sachs product/fact card: fund identity, exchange, inception, expense ratio, NAV return definition, annual NAV rows, current NAV/YTD | Annual rows 2018-2025 and performance fields as of 2026-06-30 |
| NYSE Arca:GSSC | https://www.sec.gov/Archives/edgar/data/1479026/000119312525334837/d72082d497k.htm | SEC summary prospectus: passive objective, issuer benchmark, inception, NAV return definition, and risk quarters | Filed 2025-12-29; performance period through 2024-12-31; best/worst quarter disclosures |
| NYSE Arca:GSSC | https://www.sec.gov/Archives/edgar/data/1479026/000119312526206736/d120512dncsrs.htm | SEC semi-annual report: current fund classification and expense observation | Period ended 2026-02-28; annualized fund cost 0.20% |
| NYSE Arca:GSSC | https://www.etfcentral.com/fund/GSSC | Secondary current price/NAV and YTD context | Snapshot updated 2026-07-27; return basis not used for NAV TR ranking |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused for eligible 2018-2019 rows |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused for 2018-2022 rows |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused for 2022-2025 rows |

## GSSC raw observations and calculations

| Year | GSSC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -8.72% | -4.38% |
| 2019 | 23.43% | 31.49% |
| 2020 | 15.80% | 18.40% |
| 2021 | 24.05% | 28.71% |
| 2022 | -16.87% | -18.11% |
| 2023 | 17.37% | 26.29% |
| 2024 | 10.94% | 25.02% |
| 2025 | 10.71% | 17.88% |
| 2026 YTD | 21.33% | not available from cached current-year benchmark |

- Metric basis: official GSSC NAV Total Return in USD; distributions are reinvested and fund expenses are reflected in NAV.
- Issuer benchmark: Goldman Sachs ActiveBeta U.S. Small Cap Equity Index; retained as metadata and not substituted for the common S&P 500 reference.
- 2018-2025 GSSC compound: `93.95%` cumulative; rounded-input CAGR `8.63%`.
- 2021-2025 GSSC compound: `48.66%` cumulative; rounded-input CAGR `8.25%`.
- S&P 500 cached 2018-2025 compound: `192.03%` cumulative; rounded-input CAGR `14.33%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official fact card also reports 5-year annualized NAV TR `8.46%` and since-inception annualized NAV TR `10.86%` as of 2026-06-30; these are not relabelled as a 10-year CAGR.
- Official prospectus risk observations: best quarter `+29.24%` in 4Q2020; worst quarter `-30.94%` in 1Q2020.

## GSSC gaps and conflicts

- Inception is 2017-06-28, so the 2017 partial year is excluded from complete-year ranking and the official history is under 10 years as of 2026-06-30.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- The latest official NAV TR YTD field located is 21.33% as of 2026-06-30. A later secondary snapshot reports a different YTD figure with an unclear return basis, so it is not mixed into the NAV table.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## Scheduled-inline local review

- Status: `PASS`
- Confirmed ticker/exchange, passive classification, inception, expense ratio, issuer benchmark, NAV TR definition, official annual rows, current YTD as-of, S&P cache window/basis, best/worst ranking, formulas, source links, graph breadcrumb, region ownership, and unresolved gaps.
- Planned durable files reviewed before save: `wiki/analysis/performance/ETF_NYSE_ARCA_GSSC Performance.md`, this source batch, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `wiki/analysis/comparisons/ETF Region Index.md`, and `log.md`.
