---
type: source-batch
topic: ETF performance
accessed: 2026-08-16
input_source: Trello ETF child cards DGS, DLS, CALF, FYC
input_count: 4
workflow: check-etf-performance
review_gate: PASS
reviewer: local checklist fallback after source_verifier timeout
annual_rows_as_of: "mixed: DGS/DLS 2026-03-31; CALF 2025-12-31; FYC 2026-06-30"
tags:
  - source/etf
---

# ETF Performance Source Batch - 2026-08-16

## Scope and gate

Research-bearing lean runs for DGS, DLS, CALF, and FYC. Fresh read-only research workers returned the evidence below. The project-scoped source_verifier timed out after multiple waits; the documented local checklist fallback returned PASS. No manager web research or durable writes were used to produce the evidence.

## Complete evidence register

| Input ticker | Status | Canonical entity key | Primary region | Current NAV YTD / as-of | Source URL | Gap / resolution note |
|---|---|---|---|---|---|---|
| DGS | supported | NYSE Arca:DGS | Emerging Markets | 8.86% (2026-07-31) | https://www.wisdomtree.com/us/products/equity/dgs | passive/index-tracking equity; issuer-reported 10-year average annual NAV TR 8.31%; annual NAV TR rows 2016-2025 from presentation dated 2026-03-31; official daily NAV drawdown/recovery not disclosed |
| DLS | supported | NYSE Arca:DLS | International | 8.54% (2026-07-31) | https://www.wisdomtree.com/us/products/equity/dls | passive/index-tracking equity; issuer-reported 10-year average annual NAV TR 7.69%; annual NAV TR rows 2016-2025 from presentation dated 2026-03-31; official daily NAV drawdown/recovery not disclosed |
| CALF | supported | Cboe BZX:CALF | USA | 10.60% (2026-06-22) | https://www.paceretfs.com/products/CALF | passive/index-tracking equity; expense ratio 0.59%; separate 12.78% NAV YTD snapshot as of 2026-06-16; no 2026-08-16 current figure located; annual 2025 field carries issuer 1 Year/YTD label; official daily NAV drawdown/recovery not disclosed |
| FYC | supported | NASDAQ:FYC | USA | 23.54% (2026-07-31) | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FYC | passive/rules-based index-tracking equity; expense ratio 0.70% as of 2025-12-01; annual NAV TR rows 2016-2025 from factsheet data as of 2026-06-30; stale factsheet YTD 32.59% as of 2026-06-30 is separate dated observation; daily NAV drawdown/recovery not disclosed |

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

## DLS official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:DLS | https://www.wisdomtree.com/us/products/equity/dls | Official product page: identity, net expense ratio, current NAV TR fields, NAV/market price, distribution yield and distributions | Page/current quote as of 2026-08-14; performance month-end as of 2026-07-31 |
| NYSE Arca:DLS | https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-dls-1050.ashx?la=en | Official factsheet: fund identity, inception, gross expense ratio and NAV total-return definition | Factsheet data as of 2026-03-31 |
| NYSE Arca:DLS | https://www.wisdomtree.com/us/media/dls-presentation | Official presentation: annual NAV TR observations and since-inception risk metrics | Presentation dated 2026-03-31; annual rows and risk metrics as of 2026-03-31; sole supplied full annual-row source, with SEC prospectus independently corroborating 2022 at -17.36% and no conflict established |
| NYSE Arca:DLS | https://www.sec.gov/Archives/edgar/data/1350487/000121465923010467/dls497k.htm | SEC summary prospectus: passive objective, issuer benchmark, NAV return definition and risk observations | Prospectus filed 2023; official risk observations and non-diversified status |
| NYSE Arca:DLS | https://www.wisdomtree.com/us/indexes/wtisdi | Official issuer index methodology/benchmark identity | Methodology page accessed 2026-08-16; index data as of 2026-07-29 |
| S&P 500 TR | cached official references listed in the DGS section above | Cached benchmark annual convention | USD total return with dividends reinvested; cache as of 2025-12-31 |

## DLS raw observations and calculations

| Year | DLS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.00% | 11.96% |
| 2017 | 30.95% | 21.83% |
| 2018 | -18.69% | -4.38% |
| 2019 | 22.11% | 31.49% |
| 2020 | -1.23% | 18.40% |
| 2021 | 11.66% | 28.71% |
| 2022 | -17.36% | -18.11% |
| 2023 | 15.40% | 26.29% |
| 2024 | 3.24% | 25.02% |
| 2025 | 33.49% | 17.88% |
| 2026 YTD | 8.54% | not available from cached current-year benchmark |

- Metric basis: DLS official NAV Total Return, USD, distributions reinvested and fund expenses reflected in NAV.
- Issuer benchmark: WisdomTree International SmallCap Dividend Index (WTISDI); it is retained as metadata and not silently substituted for the common S&P 500 reference.
- Net expense ratio: 0.58% as of 2026-08-14 from the official product page; gross expense ratio: 0.58% as of 2026-03-31 from the official factsheet.
- 2016-2025 DLS compound: 101.65% cumulative; rounded-input CAGR 7.27%.
- 2021-2025 DLS compound: 46.75% cumulative; rounded-input CAGR 7.97%.
- S&P 500 2016-2025 cached compound: 298.33% cumulative; rounded-input CAGR 14.82%.
- S&P 500 2021-2025 cached compound: 96.17% cumulative; rounded-input CAGR 14.43%.
- Formula: CAGR = product(1 + annual return)^(1 / number of years) - 1.
- Current NAV: 89.274 USD and market price: 88.940 USD, as of 2026-08-14; market-price discount -0.375% is separate from NAV TR.
- Distribution yield: 6.43% as of 2026-08-14 from the official product page; issuer annualized-distribution measure, not total return.
- Recent distributions: 1.43500 USD (ex/pay 2026-06-25/2026-06-29), 0.16500 USD (2026-03-26/2026-03-30), 0.83275 USD (2025-12-26/2025-12-30), and 0.59000 USD (2025-09-25/2025-09-29).

## DLS gaps and conflicts

- Issuer-reported 10-year average annual NAV TR 7.69% uses rolling/issuer methodology distinct from the 2016-2025 calendar-row CAGR 7.27%; raw endpoints and elapsed years are not disclosed, so the 7.69% figure is labelled issuer average annual, not recomputed CAGR.
- DLS annual NAV TR rows are sourced from the official 2026-03-31 presentation as the sole supplied full annual-row source in this packet; the SEC prospectus independently corroborates 2022 at -17.36%; no independent full annual series was verified and no conflict was established.
- Official daily NAV history sufficient for maximum drawdown and recovery is not verified; no numeric secondary proxy is saved.
- S&P 500 2026 current YTD was not used because the cached convention ends at 2025-12-31 and no fresh current benchmark evidence was supplied in this packet.

## CALF official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| Cboe BZX:CALF | https://www.paceretfs.com/products/CALF | Official product page: identity, name change, expense ratio, NAV YTD, 1-year/10-year/since-inception fields and current product snapshot | Product-page performance fields as of 2026-06-22 and additional issuer fields as of 2026-03-31 |
| Cboe BZX:CALF | https://www.paceretfs.com/products | Official product listing snapshot: separate current-YTD observation | NAV TR YTD 12.78% as of 2026-06-16 |
| Cboe BZX:CALF | https://docs.paceretfs.com/assets/pdfs/Pacer_CALF_Summary.pdf | Official summary prospectus: passive objective, inception, total annual expenses, NAV return definition and risk disclosures | Prospectus dated 2025-08-31; annual rows through 2024 |
| Cboe BZX:CALF | https://www.paceretfs.com/media/why_calf.pdf | Official performance sheet: annual NAV TR observations and 2025 issuer 1 Year/YTD field | 2018-2024 complete calendar rows; 2025 field ending 2025-12-31 |
| Cboe BZX:CALF | https://www.spglobal.com/spdji/en/indices/strategy/pacer-us-small-cap-cash-cows-index/ | Official index methodology and administrator reference | Methodology accessed in current research; S&P DJI administration from 2024-11-18; V1/V2 launch metadata from 2025 |
| Cboe BZX:CALF | https://www.cboe.com/us/equities/market_statistics/listed_symbols/ | Exchange listing reference | Cboe BZX listing and ticker identity |
| Cboe BZX:CALF | https://cdn.cboe.com/resources/regulation/circulars/products/IC-2025-139.pdf | Exchange name-change reference | CALF listing/name-change evidence; fund-name change effective 2025-03-10 |
| Cboe BZX:CALF | https://www.paceretfs.com/resources/distributions | Official distribution schedule | Distribution observations through 2026-06-04 |
| S&P 500 TR | cached official references listed in the DGS section above | Cached benchmark annual convention | USD total return with dividends reinvested; cache as of 2025-12-31 |

## CALF raw observations and calculations

| Year | CALF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | 11.96% |
| 2017 | not disclosed | 21.83% |
| 2018 | -9.71% | -4.38% |
| 2019 | 18.54% | 31.49% |
| 2020 | 16.31% | 18.40% |
| 2021 | 40.50% | 28.71% |
| 2022 | -15.18% | -18.11% |
| 2023 | 35.54% | 26.29% |
| 2024 | -7.45% | 25.02% |
| 2025 | 2.34%† | 17.88% |

- Metric basis: CALF official NAV Total Return, USD, distributions reinvested and fund expenses reflected in NAV.
- Issuer benchmark: Pacer US Small Cap Cash Cows Index; the methodology and S&P DJI administration are retained as metadata and not silently substituted for the common S&P 500 reference.
- Expense ratio: 0.59%; confirmed by the Pacer product page and summary prospectus dated 2025-08-31.
- 2018-2025 CALF compound: 90.45% cumulative; rounded-input annualized return approximately 8.39%.
- 2021-2025 CALF compound: 52.99% cumulative; rounded-input CAGR approximately 8.88%; average positive year 26.13%.
- S&P 500 2018-2025 compound: 192.03% cumulative; rounded-input CAGR approximately 14.33%.
- S&P 500 2021-2025 cached compound: 96.17% cumulative; rounded-input CAGR 14.43%.
- Formula: CAGR = product(1 + annual return)^(1 / number of years) - 1.
- Current NAV YTD: 10.60% as of 2026-06-22; separate 12.78% snapshot as of 2026-06-16; no 2026-08-16 figure located. These are separate dated observations, not a same-date conflict.
- Current quote: NAV 50.50 USD and market price 50.51 USD as of 2026-06-12.
- Recent distributions: 0.0447590 USD (2026-06-04), 0.0709307 USD (2026-03-05), 0.3314134 USD (2025-12-30, payable 2026-01-05), and 0.1600544 USD (2025-09-04); sum 0.6071575 USD.
- Official daily NAV history sufficient for maximum drawdown and recovery is not verified; no numeric secondary proxy is saved.

## CALF gaps and conflicts

- Current NAV YTD values are separate stale snapshots with different as-of dates (10.60% on 2026-06-22 and 12.78% on 2026-06-16); no 2026-08-16 current field was located.
- The 2025 2.34% row is an issuer 1 Year/YTD field ending 2025-12-31 rather than a separately labelled complete calendar-year observation; 2018-2024 remain the complete calendar rows.
- Raw endpoint dates and elapsed years for the issuer since-inception NAV TR 8.44% and 1-year field 21.46% are not disclosed; these are not recomputed as CAGRs.
- Official daily NAV history sufficient for maximum drawdown and recovery is not verified; no numeric secondary proxy is saved.
- The CALF annual observations are rounded source values, so cumulative/annualized calculations are approximations from rounded inputs.

## FYC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NASDAQ:FYC | https://www.ftportfolios.com/Retail/Etf/EtfSummary.aspx?Ticker=FYC | Official product page: identity, objective/index, expense ratio, NAV and market-price performance fields, current quote and risk statistics | Performance fields as of 2026-07-31; fund data/current quote as of 2026-08-10 |
| NASDAQ:FYC | https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=29c701a2-4b98-4006-99f0-71fd4ef8a9bc | Official factsheet: annual NAV TR rows, benchmark/methodology context, dated performance and risk snapshot | Data as of 2026-06-30 |
| NASDAQ:FYC | https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=d24d61fb-5be7-49f4-8363-d88a069a92a8 | Official prospectus: fund objective, enhanced-index structure, expense and risk disclosures | Prospectus source reviewed in current research |
| NASDAQ:FYC | https://www.sec.gov/Archives/edgar/data/1383496/000144554621001844/adex_ncsrs.htm | SEC fund report: fund/index disclosures and benchmark continuity context | SEC filing source reviewed in current research |
| NASDAQ:FYC | https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=b97b7535-edcd-43ec-8197-65d981643943 | Official distribution release | Release 2026-06-24; ex-date 2026-06-25; payable 2026-06-30 |
| NASDAQ:FYC | https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=865e45a8-c914-4704-bc74-7227c3cabaf5 | Official distribution release | Release 2025-09-24; ex-date 2025-09-25; payable 2025-09-30 |
| NASDAQ:FYC | https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=93a2ae96-a7c6-468c-b68b-8f516d1de5c4 | Official distribution release | Release 2024-12-12; ex-date 2024-12-13; payable 2024-12-31 |
| NASDAQ:FYC | https://www.ftportfolios.com/Common/ContentFileLoader.aspx?ContentGUID=5ee832a4-dafc-4226-8043-a2d58ea398b6 | Official distribution release | Release 2024-09-25; ex-date 2024-09-26; payable 2024-09-30 |
| NASDAQ:FYC | https://www.ftportfolios.com/Retail/Etf/Etffundnewsarchive.aspx?SubCategoryCode=PRESS_RELEASE_DISTRIBUTIONS&Ticker=FYC | Official distribution archive | Archive checked in current research; 2025 Q4 and 2026 Q1 entries not located |
| S&P 500 TR | cached official references listed in the DGS section above | Cached benchmark annual convention | USD total return with dividends reinvested; cache as of 2025-12-31 |

## FYC raw observations and calculations

| Year | FYC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 13.92% | 11.96% |
| 2017 | 23.19% | 21.83% |
| 2018 | -5.60% | -4.38% |
| 2019 | 16.80% | 31.49% |
| 2020 | 32.08% | 18.40% |
| 2021 | 21.75% | 28.71% |
| 2022 | -25.75% | -18.11% |
| 2023 | 14.15% | 26.29% |
| 2024 | 24.05% | 25.02% |
| 2025 | 24.34% | 17.88% |
| 2026 YTD | 23.54% | not available from cached current-year benchmark |

- Metric basis: FYC official NAV Total Return, USD, distributions reinvested and fund expenses reflected in NAV. The issuer's market-price total return fields are retained separately and are not substituted into the NAV table.
- Issuer benchmark: Nasdaq AlphaDEX Small Cap Growth Index (NQDXUSMCGT); the issuer benchmark and index methodology are retained as metadata and not silently substituted for the common S&P 500 reference.
- Index methodology: Nasdaq US 700 Small Cap Growth universe, growth/value factor screens, 262 securities, modified equal-dollar quintile weighting, quarterly rebalance.
- Expense ratio: 0.70% as of 2025-12-01.
- 2016-2025 FYC compound: 225.29% cumulative; rounded-input CAGR approximately 12.52%.
- 2021-2025 FYC compound: 59.17% cumulative; rounded-input CAGR approximately 9.74%; average positive year 21.07%.
- S&P 500 2016-2025 cached compound: 298.33% cumulative; rounded-input CAGR 14.82%.
- S&P 500 2021-2025 cached compound: 96.17% cumulative; rounded-input CAGR 14.43%.
- Formula: CAGR = product(1 + annual return)^(1 / number of years) - 1.
- Current product-page NAV TR YTD: 23.54% as of 2026-07-31; market-price YTD: 23.50% as of 2026-07-31.
- Current quote: NAV 122.42 USD and market price 122.52 USD as of 2026-08-10.
- Issuer 10-year NAV average annual field: 13.92% as of 2026-07-31; raw endpoints and elapsed years are not disclosed, so it is not relabelled as the 2016-2025 CAGR.
- Factsheet dated 2026-06-30 reports a stale NAV YTD 32.59%, 1-year 60.30%, 10-year 15.41%, and since-inception annualized 13.21%; the newer product-page fields are used for current claims.
- Recent distributions: 0.1297 USD (release/ex/pay 2026-06-24/2026-06-25/2026-06-30), 0.0776 USD (2025-09-24/2025-09-25/2025-09-30), 0.1473 USD (2024-12-12/2024-12-13/2024-12-31), and 0.3440 USD (2024-09-25/2024-09-26/2024-09-30); listed total 0.6986 USD, not treated as TTM because 2025 Q4 and 2026 Q1 entries were not located.
- Risk observations: 3-year standard deviation 21.59% as of 2026-07-31; factsheet snapshot 21.08% as of 2026-06-30; best quarter +30.65% in 4Q2020 and worst quarter -29.82% in 1Q2020.
- Benchmark continuity: issuer benchmark methodology changed on 2016-04-08; fund 2016 row is a full-year NAV observation and is retained with the caveat.
- Official daily NAV history sufficient for maximum drawdown and recovery is not verified; no numeric secondary proxy is saved.

## FYC gaps and conflicts

- The issuer's rolling/average annual NAV 10-year field is 13.92% as of 2026-07-31, while the rounded complete calendar rows calculate to 12.52% for 2016-2025; the issuer does not disclose comparable endpoints and elapsed-year convention, so both are retained with distinct labels.
- The factsheet's 32.59% NAV YTD as of 2026-06-30 is a stale dated snapshot; the product page's 23.54% as of 2026-07-31 is the newer current-YTD observation and the two are not treated as a same-date conflict.
- The issuer benchmark methodology change on 2016-04-08 falls inside the calendar window; the full-year 2016 fund row is official, but the period is flagged as a benchmark-continuity caveat.
- Original listing date was not verified in the reviewed official sources.
- Distribution archive review did not locate 2025 Q4 or 2026 Q1 entries; the 0.6986 USD sum is not labelled TTM.
- Official daily NAV history sufficient for maximum drawdown and recovery is not verified; no secondary numeric proxy is saved.

## Scheduled-inline run - VTWG

workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

### VTWG official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NASDAQ:VTWG | https://investor.vanguard.com/investment-products/etfs/profile/vtwg | Official Vanguard product page: fund identity, index objective, annual NAV/market-price returns, current YTD and distributions | Annual rows as of 2025-12-31; current product/YTD snapshots include 2026-07-02 and 2026-07-17 |
| NASDAQ:VTWG | https://advisors.vanguard.com/investments/products/vtwg/vanguard-russell-2000-growth-etf | Official Vanguard advisor page: current NAV YTD observation | NAV YTD 16.85% as of 2026-07-17 |
| NASDAQ:VTWG | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3353.pdf | Official factsheet: passive full-replication classification, benchmark, inception, exchange, expense ratio, NAV-return definition and risk statistic | Factsheet as of 2026-06-30 |
| NASDAQ:VTWG | https://institutional.vanguard.com/content/dam/inst/iig-transformation/pdf/total_return_chart.pdf | Official Vanguard total-return chart: rolling 10-year and since-inception NAV total returns | Performance periods ended 2026-06-30 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition; cached common reference convention | USD total return with dividends reinvested; cache as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached source reference for 2016-2019 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached source reference for 2018-2022 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached source reference for 2021 row | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached source reference for 2022-2025 rows | Reference window as documented in skill |

### VTWG raw observations and calculations

| Year | VTWG NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 11.40% | 11.96% |
| 2017 | 22.13% | 21.83% |
| 2018 | -9.31% | -4.38% |
| 2019 | 28.59% | 31.49% |
| 2020 | 34.70% | 18.40% |
| 2021 | 2.82% | 28.71% |
| 2022 | -26.35% | -18.11% |
| 2023 | 18.73% | 26.29% |
| 2024 | 15.17% | 25.02% |
| 2025 | 13.07% | 17.88% |
| 2026 YTD | 16.85% | not available from cached current-year benchmark |

- Metric basis: official VTWG NAV Total Return, USD, dividends and capital-gain distributions reinvested, pre-tax and net of expenses.
- Issuer benchmark: Russell 2000 Growth Index; it is retained as metadata and not silently substituted for the common S&P 500 reference.
- Classification: passive/index-tracking equity ETF using full replication; exchange NASDAQ; inception 2010-09-20; quarterly distribution schedule; expense ratio 0.06%.
- 2016-2025 VTWG compound: 150.23% cumulative; rounded-input CAGR 9.61%.
- 2021-2025 VTWG compound: 17.08% cumulative; rounded-input CAGR 3.20%.
- S&P 500 2016-2025 cached compound: 298.33% cumulative; rounded-input CAGR 14.82%.
- S&P 500 2021-2025 cached compound: 96.17% cumulative; rounded-input CAGR 14.43%.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official rolling 10-year NAV TR: 210.66% cumulative / 12.00% annualized as of 2026-06-30. Raw endpoints are not disclosed; normalized index representation is 100.00 at 2016-06-30 and 310.66 at 2026-06-30 over 10.00 years.
- Official factsheet 3-year monthly standard deviation: 21.30% as of 2026-06-30.
- Current official NAV TR YTD: 16.85% as of 2026-07-17. Earlier official snapshots were 20.04% as of 2026-07-02 and 22.23% as of 2026-06-30; these are dated observations, not a same-date conflict.

### VTWG gaps and conflicts

- The rolling 10-year issuer field supplies cumulative and annualized returns but not raw TR endpoint values; the normalized 100.00 → 310.66 representation is explicitly derived from the disclosed cumulative return and is not presented as raw NAV history.
- Current-YTD fields are not synchronized: the newer official advisor-page observation as of 2026-07-17 is used for the current claim; earlier 2026-07-02 and 2026-06-30 values remain provenance only.
- Official daily NAV history sufficient to verify maximum drawdown and recovery was not located; no numeric secondary proxy is saved.
- S&P 500 current-year YTD is not supplied because the cached benchmark convention ends at 2025-12-31; the annual comparison therefore uses the common 2016-2025 window only.

## Scheduled-inline run - VTWV

workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

### VTWV official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NASDAQ:VTWV | https://investor.vanguard.com/investment-products/etfs/profile/vtwv | Official Vanguard product page: fund identity, index objective, annual NAV/market-price returns and performance navigation | Product page accessed 2026-08-16; dynamic annual table was corroborated with official Vanguard materials below |
| NASDAQ:VTWV | https://advisors.vanguard.com/investments/products/vtwv/vanguard-russell-2000-value-etf | Official Vanguard advisor page: current NAV YTD and expense ratio | NAV YTD 23.63% as of 2026-07-17; expense ratio 0.06% as of 2026-02-02 |
| NASDAQ:VTWV | https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3352.pdf | Official factsheet: passive full-replication classification, benchmark, inception, exchange, expense ratio, NAV-return definition and risk statistic | Factsheet as of 2026-06-30; NAV YTD 22.99%, 10-year average annual NAV TR 10.86%, standard deviation 19.42% |
| NASDAQ:VTWV | https://fund-docs.vanguard.com/p3348.pdf | Official Vanguard prospectus chart: calendar NAV total-return observations for 2015-2024 | 2016-2024 rows used; latest prospectus chart ending 2024 |
| NASDAQ:VTWV | https://www.sec.gov/Archives/edgar/data/1021882/000119312525325212/f43593d1.htm | SEC-hosted official summary prospectus: passive objective, index, fund identity and historical-return chart context | Summary prospectus dated 2025-12-19; 2025 YTD field through 2025-09-30 and risk disclosures |
| NASDAQ:VTWV | https://institutional.vanguard.com/content/dam/inst/iig-transformation/pdf/total_return_chart.pdf | Official Vanguard Total Returns snapshot: 2025 calendar return and rolling 10-year average annual NAV TR | 2025 NAV TR 12.61% at 2025-12-31 snapshot; 10-year NAV TR 10.86% as of 2026-06-30 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition; cached common reference convention | USD total return with dividends reinvested; cache as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached source reference for 2016-2019 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached source reference for 2018-2022 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached source reference for 2021 row | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached source reference for 2022-2025 rows | Reference window as documented in skill |

### VTWV raw observations and calculations

| Year | VTWV NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.55% | 11.96% |
| 2017 | 7.78% | 21.83% |
| 2018 | -12.92% | -4.38% |
| 2019 | 22.33% | 31.49% |
| 2020 | 4.74% | 18.40% |
| 2021 | 28.13% | 28.71% |
| 2022 | -14.56% | -18.11% |
| 2023 | 14.66% | 26.29% |
| 2024 | 7.98% | 25.02% |
| 2025 | 12.61% | 17.88% |
| 2026 YTD | 23.63% | not available from cached current-year benchmark |

- Metric basis: official VTWV NAV Total Return, USD, dividends and capital-gain distributions reinvested, pre-tax and net of expenses.
- Issuer benchmark: Russell 2000 Value Index; it is retained as metadata and not silently substituted for the common S&P 500 reference.
- Classification: passive/index-tracking equity ETF using full replication; exchange NASDAQ; inception 2010-09-20; quarterly distribution schedule; expense ratio 0.06%.
- 2016-2025 VTWV compound: 141.46% cumulative; rounded-input CAGR 9.22%.
- 2021-2025 VTWV compound: 52.63% cumulative; rounded-input CAGR 8.83%.
- S&P 500 2016-2025 cached compound: 298.33% cumulative; rounded-input CAGR 14.82%.
- S&P 500 2021-2025 cached compound: 96.17% cumulative; rounded-input CAGR 14.43%.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official rolling 10-year NAV TR: average annual 10.86% as of 2026-06-30. Raw endpoints and cumulative return are not disclosed, so no normalized endpoint is calculated.
- Official factsheet 3-year monthly standard deviation: 19.42% as of 2026-06-30.
- Current official NAV TR YTD: 23.63% as of 2026-07-17. Earlier official factsheet snapshot was 22.99% as of 2026-06-30; these are dated observations, not a same-date conflict.

### VTWV gaps and conflicts

- The issuer's rolling 10-year field supplies average annual NAV TR 10.86% but not raw endpoints or cumulative total return; it is not recomputed as a CAGR.
- Annual rows 2016-2024 are from the official prospectus chart and 2025 is from the official December 31, 2025 Total Returns snapshot; the annual series is retained as a mixed-source official series with provenance above.
- The official advisor page exposes an inception metadata value of 2026-07-21 that conflicts with the official factsheet and fund materials. The verified inception used here is 2010-09-20; the conflicting metadata is not used in calculations.
- Official daily NAV history sufficient to verify maximum drawdown and recovery was not located; no numeric secondary proxy is saved.
- S&P 500 current-year YTD is not supplied because the cached benchmark convention ends at 2025-12-31; the annual comparison therefore uses the common 2016-2025 window only.

### VTWV scheduled-local pre-save checklist

- PASS — source identity, ETF type, exchange, benchmark, return basis, periods, units/currency, as-of dates, annual observations, calculations, reconciliation, source conflicts, unresolved gaps, planned file contents, region links, and exact scheduled-inline verification lines reviewed locally before write.

## Scheduled-inline run - SCHC

workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

### SCHC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:SCHC | https://www.schwabassetmanagement.com/products/schc | Official Schwab product page: objective, fund identity, current NAV/quote, expense ratio, holdings, turnover, standard deviation and current performance | Product profile and quote as of 2026-08-14; holdings as of 2026-08-13; profile risk fields as of 2026-07-31 |
| NYSE Arca:SCHC | https://www.schwabassetmanagement.com/resource/etf-investment-performance-summary | Official Schwab ETF Investment Performance Summary | Monthly returns ended 2026-07-31; quarterly average annual returns ended 2026-06-30 |
| NYSE Arca:SCHC | https://www.schwabassetmanagement.com/resource/schc-fact-sheet | Official Schwab fact sheet: objective, inception, exchange, expense ratio, annual NAV/market-price chart, return definition and risk statistic | All information as of 2026-06-30; complete calendar rows 2016-2025 |
| NYSE Arca:SCHC | https://www.sec.gov/Archives/edgar/data/1454889/000110465926020712/tm266454-8_497k.htm | SEC-hosted official summary prospectus: index objective, representative sampling and risk disclosures | Summary prospectus dated 2026-02-27 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition; cached common reference convention | USD total return with dividends reinvested; cache as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached source reference for 2016-2019 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached source reference for 2018-2022 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached source reference for 2021 row | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached source reference for 2022-2025 rows | Reference window as documented in skill |

### SCHC raw observations and calculations

| Year | SCHC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 3.17% | 11.96% |
| 2017 | 29.33% | 21.83% |
| 2018 | -18.65% | -4.38% |
| 2019 | 22.96% | 31.49% |
| 2020 | 10.69% | 18.40% |
| 2021 | 12.14% | 28.71% |
| 2022 | -21.92% | -18.11% |
| 2023 | 14.69% | 26.29% |
| 2024 | 1.90% | 25.02% |
| 2025 | 37.73% | 17.88% |
| 2026 YTD | 6.15% | not available from cached current-year benchmark |

- Metric basis: official SCHC NAV Total Return, USD, with dividends and distributions reinvested; the issuer's total-return disclosure is kept separate from market-price return.
- Issuer benchmark: FTSE Developed Small Cap ex US Liquid Index (Net); S&P 500 TR is a common reference benchmark and is not silently substituted for SCHC's tracked index.
- Classification: passive/index-tracking equity ETF using representative sampling; exchange NYSE Arca; inception 2010-01-14; semi-annual distribution; expense ratio 0.06% effective 2026-06-11.
- 2016-2025 SCHC compound: 108.21% cumulative; rounded-input CAGR 7.61%.
- 2021-2025 SCHC compound: 40.94% cumulative; rounded-input CAGR 7.10%.
- S&P 500 2016-2025 cached compound: 298.33% cumulative; rounded-input CAGR 14.82%.
- S&P 500 2021-2025 cached compound: 96.17% cumulative; rounded-input CAGR 14.43%.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official rolling 10-year NAV TR: average annual 8.23% as of 2026-06-30. Raw rolling endpoints and cumulative return are not disclosed, so no normalized endpoint is calculated.
- Official three-year standard deviation: 16.73% as of 2026-06-30 from the fact sheet; the newer product page shows 16.57% as of 2026-07-31.
- Current official NAV TR YTD: 6.15% as of 2026-07-31. The earlier official factsheet observation was 5.25% as of 2026-06-30; these are dated observations, not a same-date conflict.
- Current product-page NAV: US$51.24 as of 2026-08-14; bid/ask midpoint US$51.06 and premium/discount 0.24% were shown for the same date.

### SCHC gaps and conflicts

- The issuer's rolling 10-year field supplies average annual NAV TR 8.23% but not raw endpoints or cumulative total return; it is not recomputed as a CAGR.
- Annual rows are official Schwab NAV total-return observations from the June 30, 2026 fact sheet; market-price rows are retained only as a separate source observation and are not mixed into the NAV calculations.
- The February 2026 SEC summary prospectus states 0.08% operating expenses, while Schwab's current product page states the expense ratio became 0.06% effective 2026-06-11. The current 0.06% figure is used and the dated prior disclosure is preserved as a source conflict.
- Official daily NAV history sufficient to verify maximum drawdown and recovery was not located; no numeric secondary proxy is saved.
- S&P 500 current-year YTD is not supplied because the cached benchmark convention ends at 2025-12-31; the annual comparison uses the common 2016-2025 window only.

### SCHC scheduled-local pre-save checklist

- PASS — source identity, ETF type, exchange, benchmark, return basis, periods, units/currency, as-of dates, annual observations, calculations, reconciliation, source conflicts, unresolved gaps, planned contents of the SCHC performance page/source batch/International ETF/ETF Region Index/ETF Performance Index/log, region links, and exact scheduled-inline verification lines reviewed locally before write.

## Scheduled-inline run - ISCG

workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

### ISCG official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:ISCG | https://www.ishares.com/us/products/239587/ishares-morningstar-smallcap-growth-etf | Official iShares product page: objective, current NAV/price, calendar rows, current YTD, holdings, beta and standard deviation | Current NAV/price as of 2026-08-14; NAV TR YTD as of 2026-08-13; holdings as of 2026-08-13; risk fields as of 2026-07-31 |
| NYSE Arca:ISCG | https://www.ishares.com/us/literature/fact-sheet/iscg-ishares-morningstar-small-cap-growth-etf-fund-fact-sheet-en-us.pdf | Official iShares fact sheet: return basis, 2021-2025 calendar NAV rows, rolling annualized return, benchmark and fund facts | All information as of 2026-06-30 |
| NYSE Arca:ISCG | https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-morningstar-small-cap-growth-etf-4-30.pdf | Official iShares summary prospectus: 2016-2024 calendar NAV rows, representative sampling and risk disclosures | Summary prospectus dated 2025-08-29; performance chart through 2024-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition; cached common reference convention | USD total return with dividends reinvested; cache as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached source reference for 2016-2019 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached source reference for 2018-2022 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached source reference for 2021 row | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached source reference for 2022-2025 rows | Reference window as documented in skill |

### ISCG raw observations and calculations

| Year | ISCG NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 9.48% | 11.96% |
| 2017 | 23.48% | 21.83% |
| 2018 | -5.79% | -4.38% |
| 2019 | 27.41% | 31.49% |
| 2020 | 43.28% | 18.40% |
| 2021 | -1.32% | 28.71% |
| 2022 | -26.65% | -18.11% |
| 2023 | 22.84% | 26.29% |
| 2024 | 13.44% | 25.02% |
| 2025 | 13.09% | 17.88% |
| 2026 YTD | 19.39% | not available from cached current-year benchmark |

- Metric basis: official ISCG NAV Total Return, USD, with dividends and capital gains reinvested; market-price return is kept separate.
- Issuer benchmark: Morningstar US Small Cap Broad Growth Extended Index; S&P 500 TR is a common reference benchmark and is not silently substituted for ISCG's tracked index.
- Classification: passive/index-tracking equity ETF using representative sampling; exchange NYSE Arca; inception 2004-06-28; quarterly distribution; expense ratio 0.06%.
- Official annual rows 2016-2024 are from the SEC-hosted summary prospectus; 2025 is from the current iShares product page/fact sheet. The published precision is retained by source.
- 2016-2025 ISCG compound: 165.20% cumulative; published-input CAGR 10.24%.
- 2021-2025 ISCG compound: 14.07% cumulative; published-input CAGR 2.67%.
- S&P 500 2016-2025 cached compound: 298.33% cumulative; rounded-input CAGR 14.82%.
- S&P 500 2021-2025 cached compound: 96.17% cumulative; rounded-input CAGR 14.43%.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official rolling 10-year NAV TR: 211.14% cumulative / 12.02% annualized as of 2026-06-30. Raw endpoints are not disclosed.
- Official standard deviation and beta: 18.69% and 1.24 as of 2026-07-31; holdings 929 as of 2026-08-13.
- Current official NAV TR YTD: 19.39% as of 2026-08-13; current NAV 66.33 USD and closing price 66.36 USD as of 2026-08-14.
- Official quarter extremes from the reviewed summary prospectus: best quarter +32.85% ended 2020-06-30; worst quarter -21.51% ended 2020-03-31.

### ISCG gaps and conflicts

- The rolling 10-year issuer field supplies cumulative and average annual NAV TR but not raw endpoints; no normalized endpoint is calculated.
- Annual rows use two official sources with different as-of windows: 2016-2024 from the 2025-08-29 summary prospectus and 2025 from the current product page/fact sheet. The source dates and published precision are retained rather than silently backfilled.
- Official daily NAV history sufficient to verify maximum drawdown and recovery was not located; no numeric secondary proxy is saved.
- S&P 500 current-year YTD is not supplied because the cached benchmark convention ends at 2025-12-31; the annual comparison uses the common 2016-2025 window only.

### ISCG scheduled-local pre-save checklist

- PASS — source identity, ETF type, exchange, benchmark, return basis, periods, units/currency, as-of dates, annual observations, calculations, reconciliation, source conflicts, unresolved gaps, planned contents of the ISCG performance page/source batch/USA ETF/ETF Region Index/ETF Performance Index/log, region links, and exact scheduled-inline verification lines reviewed locally before write.

## Scheduled-inline run - VIOO

workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

### VIOO official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:VIOO | https://investor.vanguard.com/investment-products/etfs/profile/vioo | Official Vanguard product page: fund identity, tracked index, annual NAV rows, benchmark rows, rolling and cumulative return fields | Annual rows through 2025-12-31; rolling/cumulative fields as of 2026-06-30 |
| NYSE Arca:VIOO | https://fund-docs.vanguard.com/F3345.pdf | Official Vanguard fact sheet: passive/full-replication approach, return basis, inception, expense ratio, exchange, holdings, standard deviation and sector snapshot | As of 2026-06-30 |
| NYSE Arca:VIOO | https://advisors.vanguard.com/investments/products/vioo/vanguard-sp-small-cap-600-etf | Official Vanguard advisor page: latest current NAV TR YTD and expense ratio | NAV TR YTD 22.03% as of 2026-07-17; expense ratio 0.07% as of 2025-12-19 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition; cached common reference convention | USD total return with dividends reinvested; cache as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached source reference for 2016-2019 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached source reference for 2018-2022 rows | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached source reference for 2021 row | Reference window as documented in skill |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached source reference for 2022-2025 rows | Reference window as documented in skill |

### VIOO raw observations and calculations

| Year | VIOO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 26.44% | 11.96% |
| 2017 | 13.31% | 21.83% |
| 2018 | -8.57% | -4.38% |
| 2019 | 22.72% | 31.49% |
| 2020 | 11.43% | 18.40% |
| 2021 | 26.67% | 28.71% |
| 2022 | -16.20% | -18.11% |
| 2023 | 16.00% | 26.29% |
| 2024 | 8.62% | 25.02% |
| 2025 | 5.99% | 17.88% |
| 2026 YTD | 22.03% | not available from cached current-year benchmark |

- Metric basis: official VIOO NAV Total Return, USD, with dividends and capital gains reinvested; market-price return is kept separate.
- Issuer benchmark: S&P SmallCap 600 Index; S&P 500 TR is a common reference benchmark and is not silently substituted for VIOO's tracked index.
- Classification: passive/index-tracking equity ETF using full replication; exchange NYSE Arca; inception 2010-09-07; annual distribution; expense ratio 0.07%.
- 2016-2025 annual NAV rows are the official Vanguard total-return table; the published precision is retained.
- 2016-2025 VIOO compound: 153.93% cumulative; published-input CAGR 9.77%.
- 2021-2025 VIOO compound: 41.76% cumulative; published-input CAGR 7.23%.
- S&P 500 2016-2025 cached compound: 298.33% cumulative; rounded-input CAGR 14.82%.
- S&P 500 2021-2025 cached compound: 96.17% cumulative; rounded-input CAGR 14.43%.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official rolling 10-year NAV TR: average annual 11.47% as of 2026-06-30. Raw rolling endpoints and cumulative return are not disclosed, so no normalized endpoint is calculated.
- Official current NAV TR YTD: 22.03% as of 2026-07-17. The fact sheet also reports 23.89% as of 2026-06-30; these are dated observations, not a same-date conflict, and the newer dated field is used for the current snapshot.
- Official fact-sheet snapshot: 607 holdings, turnover 21.8%, and three-year standard deviation 19.44% as of 2026-06-30.
- Latest NAV/market-price quote was not available in the reviewed text extracts; no quote is used in the return calculations.

### VIOO gaps and conflicts

- The issuer's rolling 10-year field supplies average annual NAV TR 11.47% but not raw endpoints or elapsed-year convention; it is not recomputed as the 2016-2025 calendar-row CAGR.
- Current YTD observations are dated 2026-06-30 (23.89%) and 2026-07-17 (22.03%); the newer 2026-07-17 value is used, and the difference is not treated as a same-date conflict.
- Official daily NAV history sufficient to verify maximum drawdown and recovery was not located; no numeric secondary proxy is saved.
- S&P 500 current-year YTD is not supplied because the cached benchmark convention ends at 2025-12-31; the annual comparison uses the common 2016-2025 window only.

### VIOO scheduled-local pre-save checklist

- PASS — source identity, ETF type, exchange, benchmark, return basis, periods, units/currency, as-of dates, annual observations, calculations, reconciliation, source conflicts, unresolved gaps, planned contents of the VIOO performance page/source batch/USA ETF/ETF Region Index/ETF Performance Index/log, region links, and exact scheduled-inline verification lines reviewed locally before write.

## Scheduled-inline run - RSSL

workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS

### RSSL official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:RSSL | https://www.globalxetfs.com/funds/RSSL | Official Global X product page: fund identity, objective, exchange, NAV/market price, expense ratio, risk fields, holdings, and performance history | NAV/price, risk and fund facts as of 2026-07-31; performance history and YTD fields through 2026-06-30 |
| NYSE Arca:RSSL | https://assets.globalxetfs.com/funds/documents/rssl/Fact-Sheet_RSSL.pdf | Official Global X fact sheet: inception, exchange, expense ratio, distribution frequency, return basis and NAV/market-price/index performance | All performance fields as of 2026-06-30; fact sheet dated/current capture 2026-08-16 |
| NYSE Arca:RSSL | https://www.sec.gov/Archives/edgar/data/1432353/000143235326000232/a497krussell2000.htm | SEC-hosted official summary prospectus: passive strategy, index construction, expenses and calendar-year performance | Prospectus dated 2026-03-01; calendar-year return table through 2025-12-31 |
| NYSE Arca:RSSL | https://assets.globalxetfs.com/funds/documents/rssl/prospectus-regulatory/Annual-Shareholder-Report.pdf | Official Global X annual shareholder report: 2025 performance context and inception history | Report period ended 2025-10-31; corroborating source, not used for the 2025 calendar row |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition; cached common reference convention | USD total return with dividends reinvested; cache as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached source reference for 2016-2019 rows | Reference window as documented in skill; only 2025 row used here from the cache |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached source reference for 2018-2022 rows | Reference window as documented in skill; only 2025 row used here from the cache |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached source reference for 2021 row | Reference window as documented in skill; only 2025 row used here from the cache |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached source reference for 2022-2025 rows | Reference window as documented in skill; 2025 row `17.88%` used here |

### RSSL raw observations and calculations

| Period | RSSL NAV TR | S&P 500 TR |
|---|---:|---:|
| 2025 complete calendar year | 12.76% | 17.88% |
| 2026 YTD | 22.52% as of 2026-06-30 | not available from cached current-year benchmark |

- Metric basis: official RSSL NAV Total Return, USD, with gross income/dividends and capital gains reinvested where applicable; fund expenses are reflected in the fund return. Market-price return is kept separate.
- Issuer benchmark: Russell 2000 RIC Capped Index; S&P 500 TR is a common reference benchmark and is not substituted for the issuer benchmark.
- Classification: passive/index-tracking equity ETF using an indexing approach and representative sampling; exchange NYSE Arca; inception 2024-06-04; quarterly distribution; total expense ratio 0.08%.
- 2025 RSSL return `12.76%` is the official one-year return before taxes ended 2025-12-31; 2025 S&P 500 TR is the cached official common reference `17.88%`.
- Relative calculation: `12.76% - 17.88% = -5.12 pp`.
- Complete-year count: `1` up / `0` down; best and least positive are 2025 `+12.76%`; no worst or least-bad down year is applicable.
- Official since-inception annualized NAV TR is `22.65%` as of 2026-06-30; raw TR endpoints and elapsed-year input are not disclosed, so no independent CAGR is calculated. A separate `14.97%` since-inception field in the 2026 prospectus is as of 2025-12-31 and is retained as a dated prior observation, not a same-date conflict.
- Current official NAV TR YTD is `22.52%` as of 2026-06-30. The product page provides a later NAV level `US$114.01` and risk fields as of 2026-07-31 but does not expose a later numeric YTD field; no YTD is inferred from price.
- Official risk snapshot: standard deviation `19.00%`, beta `1.22` versus S&P 500, and `1,960` holdings as of 2026-07-31.

### RSSL gaps and conflicts

- The fund commenced operations on 2024-06-04, so 10-year NAV TR is not applicable; the reviewed official sources do not disclose a year-end 2024 NAV TR row for the inception-year partial period. It is excluded from rankings rather than backfilled.
- The issuer's 2025-12-31 prospectus since-inception annualized field (`14.97%`) and the product-page 2026-06-30 field (`22.65%`) have different as-of dates; the newer field is used for the current snapshot.
- Official daily NAV history sufficient to verify maximum drawdown and recovery was not located; no numeric secondary proxy is saved.
- S&P 500 current-year YTD is not supplied because the cached benchmark convention ends at 2025-12-31; only the 2025 common annual comparison is shown.

### RSSL scheduled-local pre-save checklist

- PASS — source identity, ETF type, exchange, benchmark, return basis, distributions, periods, units/currency, as-of dates, annual observation, calculations, reconciliation, dated source differences, unresolved gaps, planned contents of the RSSL performance page/source batch/USA ETF/ETF Region Index/ETF Performance Index/log, region links, canonical tag, and exact scheduled-inline verification lines reviewed locally before write.
