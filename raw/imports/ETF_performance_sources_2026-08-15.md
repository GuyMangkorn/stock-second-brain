---
type: etf-performance-source-batch
workflow: check-etf-performance
tickers:
  - ESML
mode: lean
run_date: 2026-08-15
return_basis: NAV total return
benchmark_basis: S&P 500 Total Return, USD, dividends reinvested
review_status: PASS; source_verifier timed out, local checklist fallback passed
---

# ESML Performance Sources — 2026-08-15

## Source map

| Source | Type | As-of / access date | Claims used |
|---|---|---|---|
| https://www.ishares.com/us/products/296644/ESML | Official issuer product page | current facts 2026-08-13 | identity, exchange, issuer benchmark, distributions, current cross-check |
| https://www.ishares.com/ch/professionals/en/products/296644/ishares-esg-aware-msci-usa-small-cap-etf-fund | Official issuer professional page | NAV/YTD 2026-08-13 | NAV 56.31 USD, NAV TR YTD 23.07%, current facts |
| https://www.ishares.com/us/literature/fact-sheet/esml-ishares-esg-aware-msci-usa-small-cap-etf-fund-fact-sheet-en-us.pdf | Official issuer factsheet | 2026-06-30 | expense ratio, 2025 return, fund facts, return basis |
| https://www.ishares.com/us/literature/summary-prospectus/sp-msci-usa-small-cap-esg-optimized-etf-8-31.pdf | Official issuer summary prospectus | dated 2025-12-30 | inception, 2019-2024 annual NAV TR, quarterly extremes, return definition |
| https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official S&P DJI index-return report | 2026-08-10 | nearest current S&P 500 Gross TR YTD |
| https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Official S&P DJI research | cached reference as of 2025-12-31 | S&P 500 TR annual rows 2019-2025 under project cache |
| https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Official S&P DJI market attributes | cached reference as of 2025-12-31 | S&P 500 TR annual rows 2022-2025 under project cache |
| https://www.trefis.com/data/companies/ESML | Secondary performance source | analysis through 2026-06-28 | price-based drawdown/recovery context only |

## Verified observations

- Canonical identity: Cboe BZX:ESML; iShares ESG Aware MSCI USA Small-Cap ETF; passive/index-tracking U.S. equity ETF; inception 2018-04-10; USD.
- Issuer benchmark: MSCI USA Small Cap Extended ESG Focus Index; expense ratio 0.17%.
- NAV Total Return includes reinvested distributions and fund expenses; it is kept separate from market-price return.
- Official ESML NAV TR complete rows: 2019 28.53%, 2020 19.77%, 2021 19.31%, 2022 -17.22%, 2023 17.31%, 2024 11.86%, 2025 10.62%.
- Official issuer benchmark rows: 2019 28.7%, 2020 20.0%, 2021 19.54%, 2022 -17.22%, 2023 17.26%, 2024 12.08%, 2025 10.83%; 2019-2020 are rounded to one decimal in the source.
- Current official NAV is 56.31 USD and current ESML NAV TR YTD is 23.07%, both as of 2026-08-13.
- Nearest official current S&P 500 Gross TR YTD is 14.04% for 2025-12-31 close to 2026-08-10 close; exact 2026-08-13 S&P TR was not located.
- Latest four official cash distributions are 0.142985, 0.132258, 0.112826, and 0.108366 USD per share; sum 0.496435 and average 0.124109; quarterly frequency; through 2026-06-15.
- Official quarterly extremes: worst quarter -30.78% in Q1 2020 and best quarter +29.31% in Q4 2020. Exact official daily NAV max drawdown and recovery date are not disclosed.

## Cached benchmark

- S&P 500 TR annual cache: 2019 31.49%, 2020 18.40%, 2021 28.71%, 2022 -18.11%, 2023 26.29%, 2024 25.02%, 2025 17.88%; USD, dividends reinvested, reference as of 2025-12-31.
- 2021-2025 S&P 500 TR compounds to 96.17% / CAGR 14.43%; 2019-2025 rows are used only as a common reference, not as ESML issuer benchmark.

## Calculations and gaps

- ESML 2019-2025 cumulative NAV TR: product(1 + annual TR) - 1 = 120.70%; rounded-input CAGR = 11.97%.
- ESML 2021-2025 cumulative NAV TR: 43.37%; rounded-input CAGR = 7.47%.
- Up/down years: 6 / 1; best 2019 +28.53%; worst 2022 -17.22%; least positive 2025 +10.62%.
- 10-year NAV TR is not applicable because inception is 2018; 2018 partial-year return was not verified.
- Annual path from 2021 year-end normalized to 100.00: 82.78 after 2022, 97.11 after 2023, 108.63 after 2024, 120.16 after 2025; this is a year-end recovery read, not a daily NAV drawdown/recovery calculation.
- Secondary Trefis price-based recovery figures are retained only as labelled context and are not mixed with NAV TR.

## Planned durable outputs

- Created `wiki/analysis/performance/ETF_CBOE_BZX_ESML Performance.md`.
- Created `raw/imports/ETF_performance_sources_2026-08-15.md`.
- Updated `wiki/analysis/comparisons/USA ETF.md`, `ETF Region Index.md`, and `ETF Performance Index.md`, and appended one `etf-performance` bullet to `log.md`.
- Assigned primary region USA; added breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]` and `geography/United-States` tag.

## Review record

- Project-scoped `source_verifier` was dispatched with the complete packet but timed out after bounded waits. The documented local checklist fallback passed: source/as-of mapping, return-basis separation, calculations, file paths, and graph/index links were checked before saving. No research was performed locally; both research lanes returned source-backed evidence.
