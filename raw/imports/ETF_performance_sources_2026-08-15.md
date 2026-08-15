---
type: etf-performance-source-batch
workflow: check-etf-performance
tickers:
  - ESML
  - IJT
  - IJS
mode: lean
run_date: 2026-08-15
return_basis: NAV total return
benchmark_basis: S&P 500 Total Return, USD, dividends reinvested
review_status: PASS; ESML/IJT/IJS source_verifier timed out with documented local checklist fallback passed
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

# IJS Performance Sources — 2026-08-15

## Source map

| Source | Type | As-of / access date | Claims used |
|---|---|---|---|
| https://www.ishares.com/us/products/239775/ishares-sp-smallcap-600-value-etf | Official issuer product page | current fields 2026-08-14; YTD 2026-08-13 | identity, exchange, NAV, price, rolling return, current NAV TR YTD |
| https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-s-and-p-small-cap-600-value-etf-3-31.pdf | Official summary prospectus | accessed 2026-08-15; dated July 31, 2026 | annual NAV TR, benchmark/market-price cross-check, return definition, risk |
| https://www.ishares.com/us/literature/fact-sheet/ijs-ishares-s-p-small-cap-600-value-etf-fund-fact-sheet-en-us.pdf | Official factsheet | 2026-06-30 / 2026-07-31 fields | expense ratio, rolling return, risk, yields |
| https://www.ishares.com/us/literature/annual-report/ar-ijs-en.pdf | Official annual report | accessed 2026-08-15 | fallback source only |
| https://www.spglobal.com/spdji/en/indices/equity/sp-smallcap-600-value/ | Official index provider | accessed 2026-08-15 | tracked benchmark identity |
| https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization | Official S&P DJI returns page | page dated 2026-08-15 | current S&P 500 TR reference 14.54% |
| Project S&P 500 TR cache | Official cached convention | reference 2025-12-31 | common annual comparison rows |

## Verified observations

- Canonical identity: NYSE Arca:IJS; iShares S&P Small-Cap 600 Value ETF; passive/index-tracking U.S. equity ETF; inception 2000-07-24; USD; expense ratio 0.18%; quarterly distributions.
- Issuer benchmark: S&P SmallCap 600 Value Index (SPTRSV). NAV TR includes reinvested distributions and fund expenses; market-price TR is kept separate.
- Official annual IJS NAV TR rows: 2016 31.17%, 2017 11.36%, 2018 -12.80%, 2019 24.25%, 2020 2.56%, 2021 30.47%, 2022 -11.32%, 2023 14.64%, 2024 7.42%, 2025 6.55%.
- Official benchmark rows are 2021 30.95%, 2022 -11.04%, 2023 14.89%, 2024 7.56%, 2025 6.70%; 2016-2020 are not disclosed and were not backfilled.
- Official market-price TR rows are 2021 30.53%, 2022 -11.33%, 2023 14.69%, 2024 7.35%, 2025 6.54%; 2016-2020 are not disclosed.
- Official current NAV is $140.69 and closing market price $140.68 as of 2026-08-14; NAV TR YTD is +23.99% as of 2026-08-13.
- Official rolling 10-year NAV TR window is 2016-06-30 → 2026-06-30, 10.00 years; issuer-reported 173.99% cumulative / 10.60% annualized; normalized 100.00 → 273.99; raw endpoints are not disclosed.
- Official risk fields are 3-year standard deviation 19.74% and beta 1.07 as of 2026-07-31; best quarter +32.92% Q4 2020 and worst quarter -37.36% Q1 2020.
- Latest four official distributions are $0.539899, $0.204616, $0.544229, and $0.511064 on ex-dates 2026-06-15, 2026-03-17, 2025-12-16, and 2025-09-16; total $1.799808/share; zero capital gains/ROC. Issuer trailing yield is 1.32% as of 2026-07-31.
- Current S&P 500 TR reference is +14.54% as of 2026-08-15; it is not synchronized with IJS's 2026-08-13 YTD.

## Cached benchmark

- S&P 500 TR annual cache: 2016 11.96%, 2017 21.83%, 2018 -4.38%, 2019 31.49%, 2020 18.40%, 2021 28.71%, 2022 -18.11%, 2023 26.29%, 2024 25.02%, 2025 17.88%; USD, dividends reinvested, reference as-of 2025-12-31.
- S&P 500 cache 2021-2025 rounded-input approximation compounds to 96.17% / CAGR 14.43%; it is common reference only, not IJS's tracked benchmark.

## Calculations and gaps

- IJS 2016-2025 rounded-input approximation: product(1 + annual TR) - 1 = 146.41%; CAGR = 9.44%. Inputs: 31.17%, 11.36%, -12.80%, 24.25%, 2.56%, 30.47%, -11.32%, 14.64%, 7.42%, 6.55%.
- IJS 2021-2025 rounded-input approximation: product(1 + annual TR) - 1 = 51.81%; CAGR = 8.71%. Inputs: 30.47%, -11.32%, 14.64%, 7.42%, 6.55%.
- Up/down years in 2016-2025: 8 / 2; best 2016 +31.17%; worst 2018 -12.80%; least positive 2025 +6.55%; least-bad down year 2022 -11.32%.
- No official daily NAV TR series was used; exact maximum drawdown and recovery date remain not disclosed. Market-price and issuer-benchmark annual rows for 2016-2020 remain not disclosed.

## Planned durable outputs

- Create wiki/analysis/performance/ETF_NYSE_ARCA_IJS Performance.md.
- Update wiki/analysis/comparisons/USA ETF.md, ETF Region Index.md, and ETF Performance Index.md; append one etf-performance bullet to log.md.
- Assign primary region USA; add breadcrumb [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]] and geography/United-States tag.

## Review record

- Project-scoped source_verifier timed out after bounded waits. The documented local checklist fallback passed after the arithmetic correction and explicit rolling-window/as-of/rounded-input disclosure; no research was performed locally.

# IJT Performance Sources — 2026-08-15

## Source map

| Source | Type | As-of / access date | Claims used |
|---|---|---|---|
| https://www.ishares.com/us/products/239773/ishares-sp-smallcap-600-growth-etf | Official issuer product page | current facts through 2026-08-14 | identity, current exchange, benchmark, NAV, assets, current performance |
| https://www.ishares.com/us/literature/fact-sheet/ijt-ishares-sp-smallcap-600-growth-etf-fact-sheet-en-us.pdf | Official issuer factsheet | 2026-06-30 / 2026-07-31 fields | return basis, rolling 10-year return, risk, distributions, fund facts |
| https://www.sec.gov/Archives/edgar/data/1100663/000119312523190469/R67.htm | SEC filing, official prospectus performance table | accessed 2026-08-15 | annual NAV total-return rows 2013-2022 and benchmark comparison |
| https://www.sec.gov/Archives/edgar/data/1100663/000119312525171574/d921702d497k.htm | SEC filing, official summary prospectus | accessed 2026-08-15 | 2023-2024 annual return and benchmark rows; risk and return definitions |
| https://www.spglobal.com/spdji/en/indices/equity/sp-smallcap-600-growth-index/ | Official index provider | accessed 2026-08-15 | tracked benchmark identity and index context |
| https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot | Official S&P DJI index-return report | current page unavailable in research lane | current S&P 500 TR comparison target; no exact official value used |
| https://www.slickcharts.com/sp500/returns | Secondary benchmark source | 2026-08-14 | secondary S&P 500 total-return comparison only |
| https://koalagains.com/dimension-portfolio/etf/ijt | Secondary performance context | accessed 2026-08-15 | cross-check only; not used as primary annual return source |

## Verified observations

- Canonical identity: NASDAQ:IJT; iShares S&P Small-Cap 600 Growth ETF; passive/index-tracking U.S. equity ETF; inception 2000-07-24; USD; expense ratio 0.18%; quarterly distributions.
- Issuer benchmark: S&P SmallCap 600 Growth Index, index symbol SPTRSG. Current issuer materials identify NASDAQ as the exchange; older SEC text refers to NYSE Arca. The historical exchange discrepancy is disclosed rather than silently normalized.
- Official annual IJT NAV total-return rows: 2013 42.62%, 2014 3.71%, 2015 2.65%, 2016 22.00%, 2017 14.57%, 2018 -4.28%, 2019 20.82%, 2020 19.17%, 2021 22.40%, 2022 -21.24%, 2023 16.97%, 2024 9.42%, 2025 5.20%.
- Latest official NAV is 178.49 USD as of 2026-08-14; official IJT NAV total-return YTD is 26.03% as of 2026-08-13; net assets are 8.434 billion USD as of 2026-08-14.
- Official issuer rolling 10-year return as of 2026-06-30 is 205.63% cumulative / 11.82% annualized. The raw endpoints were not disclosed in the source.
- Official issuer risk fields as of 2026-07-31 include 3-year standard deviation 19.48% and beta 1.09. Official quarterly extremes are +29.74% in Q4 2020 and -28.21% in Q1 2020.
- Latest four official distributions total 1.211989 USD per share; trailing distribution yield is 0.70% as of 2026-07-31.
- Current S&P 500 total-return comparison uses a secondary +14.54% value as of 2026-08-14 because the official dynamic S&P DJI page was unavailable in the research lane. It is not presented as an official issuer benchmark figure.

## Cached benchmark

- S&P 500 TR annual cache: 2016 11.96%, 2017 21.83%, 2018 -4.38%, 2019 31.49%, 2020 18.40%, 2021 28.71%, 2022 -18.11%, 2023 26.29%, 2024 25.02%, 2025 17.88%; USD, dividends reinvested, reference as-of 2025-12-31.
- The cached rows are a common comparison convention and are kept separate from IJT's issuer benchmark.

## Calculations and gaps

- IJT 2016-2025 cumulative NAV TR: product(1 + annual TR) - 1 = 150.04%; rounded-input CAGR = 9.60%.
- IJT 2021-2025 cumulative NAV TR: 29.80%; rounded-input CAGR = 5.35%.
- Up/down years for 2016-2025: 8 / 2; best 2021 +22.40%; worst 2022 -21.24%; least positive 2025 +5.20%; least-bad down year 2018 -4.28%.
- Official annual rows before 2013 were not located in the checked source set. Exact official daily NAV maximum drawdown and recovery date were not disclosed. Raw endpoints for the issuer's rolling 10-year field were not disclosed.
- The historical exchange discrepancy and the secondary current S&P comparison are retained as explicit source-quality gaps.

## Planned durable outputs

- Created `wiki/analysis/performance/ETF_NASDAQ_IJT Performance.md`.
- Updated `wiki/analysis/comparisons/USA ETF.md`, `ETF Region Index.md`, and `ETF Performance Index.md`, and appended one `etf-performance` bullet to `log.md`.
- Assigned primary region USA; added breadcrumb `[[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]` and `geography/United-States` tag.

## Review record

- Project-scoped `source_verifier` was dispatched with the complete IJT packet but timed out after bounded waits. The documented local checklist fallback passed: source/as-of mapping, exchange conflict, return-basis separation, calculations, file paths, and graph/index links were checked before saving. No research was performed locally; the research worker returned source-backed evidence.
