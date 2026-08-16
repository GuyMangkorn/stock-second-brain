---
type: source-batch
topic: ETF performance
accessed: 2026-08-17
input_source: Trello ETF child cards GSSC, XSMO, SSEUF
input_count: 3
workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS
annual_rows_as_of: "GSSC official 2018-2025; XSMO official 2016-2025; SSEUF canonical LSE:R2US official 2016-2025; current NAV/YTD fields through 2026-07-31"
tags:
  - source/etf
---

# ETF Performance Source Batch - 2026-08-17

## Scope and gate

Research-bearing lean run for GSSC, XSMO, and SSEUF. Source discovery, reading, reconciliation,
calculation, synthesis, and the complete pre-save checklist were performed
inline under `scheduled-inline`. No research worker, reviewer,
`source_verifier`, or other sub-agent was dispatched.

verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design

## Complete evidence register

| Input ticker | Status | Canonical entity key | Primary region | Current NAV YTD / as-of | Primary source | Gap / resolution note |
|---|---|---|---|---|---|---|
| GSSC | supported | NYSE Arca:GSSC | USA | 21.33% (2026-06-30) | https://am.gs.com/public-assets/documents/574deb07-24d6-11ef-870d-c7a1cb19e681 | passive/index-tracking U.S. small-cap multi-factor equity; 10-year history not yet available; daily NAV drawdown/recovery not disclosed |
| XSMO | supported | NYSE Arca:XSMO | USA | 30.50% (2026-06-30, secondary NAV) | https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/xsmo-invesco-s-p-smallcap-momentum-etf-fact-sheet.pdf | passive/index-tracking U.S. small-cap momentum equity; official current YTD not located; daily NAV drawdown/recovery not disclosed |
| SSEUF | supported | LSE:R2US | USA | 18.69% (2026-07-31) | https://www.ssga.com/uk/en_gb/institutional/etfs/state-street-spdr-russell-2000-us-small-cap-ucits-etf-acc-zprr-gy | OTC alias for official USD LSE line; passive/index-tracking U.S. small-cap equity; daily NAV drawdown/recovery not disclosed |

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

## SSEUF / R2US official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:R2US / SSEUF | https://www.ssga.com/uk/en_gb/institutional/etfs/state-street-spdr-russell-2000-us-small-cap-ucits-etf-acc-zprr-gy | Official State Street product page: fund identity, listing table, benchmark, official Fund Net/NAV performance, current NAV/YTD, standard deviation and tracking error | Annual rows 2016-2025 and rolling/current fields as of 2026-07-31; NAV quote as of 2026-07-17 |
| LSE:R2US / SSEUF | https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-zprr-gy.pdf | Official State Street factsheet: ISIN, USD LSE ticker R2US, inception, TER, accumulating share class, optimized replication, benchmark and performance | Factsheet dated 30 Jun 2026; performance table through 31 Jul 2026 |
| LSE:R2US / SSEUF | https://www.ssga.com/library-content/kids?country=ie&documentType=kid&isin=IE00BJ38QD84&language=en_gb&ticker=zprr-gy | Official KID: index-tracking/passive objective, optimization policy, accumulating income treatment and risk disclosures | Accurate as of 2026-02-19 |
| SSEUF alias | https://www.google.com/finance/beta/quote/SSEUF%3AOTCMKTS | Secondary OTC alias and USD quote cross-check; canonical exchange key remains LSE:R2US | Search snapshot accessed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused without a new search |

## SSEUF / R2US raw observations and calculations

| Year | R2US Fund Net / NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 20.97% | 11.96% |
| 2017 | 13.98% | 21.83% |
| 2018 | -11.34% | -4.38% |
| 2019 | 24.98% | 31.49% |
| 2020 | 19.36% | 18.40% |
| 2021 | 14.70% | 28.71% |
| 2022 | -20.78% | -18.11% |
| 2023 | 16.27% | 26.29% |
| 2024 | 11.19% | 25.02% |
| 2025 | 12.32% | 17.88% |
| 2026 YTD | 18.69% | not available from cached current-year benchmark |

- Input ticker `SSEUF` is an OTC alias; official State Street listing data maps the same ISIN/share class to USD `LSE:R2US`. The primary listing is Deutsche Börse `ZPRR`, but the durable key uses the USD London line matching the input currency.
- Metric basis: official R2US Fund Net performance is NAV-based and net of fees; the accumulating share class retains income in NAV.
- Issuer benchmark: Russell 2000 Index Net Total Return (`RU20N30U`); retained as metadata and not substituted for the common S&P 500 reference.
- Official 10-year rolling NAV TR: `163.53%` cumulative / `10.18%` annualized as of 2026-07-31; since-inception: `177.36%` cumulative / `8.81%` annualized.
- 2016-2025 R2US compound: `140.61%` cumulative; rounded-input CAGR `9.18%`.
- 2021-2025 R2US compound: `31.94%` cumulative; rounded-input CAGR `5.70%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk observations: 3-year standard deviation `19.67%` and tracking error `0.08%` as of 2026-07-31.

## SSEUF / R2US gaps and conflicts

- The input is an OTC alias (`SSEUF`) rather than the official USD London ticker; the canonical exchange-qualified key is `LSE:R2US` and the official primary listing is Deutsche Börse `ZPRR`. The alias, ISIN, share-class currency and index identity were reconciled before save.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## XSMO official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:XSMO | https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/xsmo-invesco-s-p-smallcap-momentum-etf-fact-sheet.pdf | Official Invesco fact sheet: fund identity, exchange, inception, expense ratio, index, annual NAV rows, issuer average annual returns, and benchmark continuity note | Annual rows 2016-2025 and standard performance as of 2025-12-31 |
| NYSE Arca:XSMO | https://www.invesco.com/us/en/financial-products/etfs/invesco-sp-smallcap-momentum-etf.html | Official Invesco product page and product identity cross-check | Current product page accessed 2026-08-17; current numeric YTD field not extractable |
| NYSE Arca:XSMO | https://www.sec.gov/Archives/edgar/data/1209466/000119312525190429/d56632d497k.htm | SEC summary prospectus: passive objective, ticker/exchange, fee breakdown, index exposure, inception, and risk quarters | Filed 2025; risk/performance table through 2024-12-31 |
| NYSE Arca:XSMO | https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=xsmo | Secondary NAV performance snapshot used only for current YTD context | NAV YTD +30.5% as of 2026-06-30 |
| NYSE Arca:XSMO | https://totalrealreturns.com/n/XSMO | Secondary total-return cross-check | Snapshot +18.10% YTD as of 2026-07-29; return basis/as-of conflict, not mixed into NAV ranking |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused without a new search |

## XSMO raw observations and calculations

| Year | XSMO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.17% | 11.96% |
| 2017 | 23.42% | 21.83% |
| 2018 | -2.88% | -4.38% |
| 2019 | 28.35% | 31.49% |
| 2020 | 21.84% | 18.40% |
| 2021 | 19.28% | 28.71% |
| 2022 | -15.48% | -18.11% |
| 2023 | 21.43% | 26.29% |
| 2024 | 17.57% | 25.02% |
| 2025 | 9.81% | 17.88% |
| 2026 YTD | 30.50% (secondary NAV) | not available from cached current-year benchmark |

- Metric basis: official XSMO NAV Total Return in USD; distributions are reinvested and fund expenses are reflected in NAV.
- Issuer benchmark: S&P SmallCap 600 Momentum Index; retained as metadata and not substituted for the common S&P 500 reference.
- 2016-2025 XSMO compound: `217.50%` cumulative; rounded-input CAGR `12.25%`.
- 2021-2025 XSMO compound: `58.05%` cumulative; rounded-input CAGR `9.59%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official fact sheet reports 10-year average annual NAV TR `12.25%` and inception average annual NAV TR `8.38%` as of 2025-12-31; the 10-year issuer field is not relabelled as a raw cumulative endpoint.
- SEC prospectus risk observations: best quarter `+23.72%` in 2Q2020; worst quarter `-25.15%` in 1Q2020.

## XSMO gaps and conflicts

- Official current XSMO NAV TR YTD was not located in the issuer materials read on 2026-08-17. The latest usable current snapshot is a secondary NAV return of `30.50%` as of 2026-06-30.
- Another secondary source reports `18.10%` YTD as of 2026-07-29, but its return basis and date convention are not reconciled with the Schwab NAV snapshot; it is retained as a conflict and excluded from the ranking table.
- The tracked-index history includes predecessor methodologies before 2019-06-21; calendar rows remain issuer fund NAV observations, not a synthetic backfilled index series.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## Scheduled-inline local review

- Status: `PASS`
- Confirmed GSSC, XSMO, and SSEUF ticker/exchange, passive classification, inception, expense ratio, issuer benchmark, NAV TR definition, official annual rows, current-YTD as-of/basis, S&P cache window/basis, best/worst ranking, formulas, source links, graph breadcrumb, region ownership, and unresolved gaps.
- XSMO-specific local checklist: verified the official 2016-2025 annual rows, issuer 10-year average annual field, secondary current NAV snapshot, separate return-basis treatment, predecessor-index continuity note, 8/2 up/down count, and no unsupported drawdown/recovery inference.
- SSEUF-specific local checklist: verified OTC-to-`LSE:R2US` alias mapping, ISIN/share-class currency, passive classification, official 2016-2025 rows, official 10-year/current NAV fields, S&P cache convention, 8/2 up/down count, risk metrics, graph breadcrumb, primary-region ownership, and no unsupported drawdown/recovery inference.
- Planned durable files reviewed before save: `wiki/analysis/performance/ETF_NYSE_ARCA_GSSC Performance.md`, `wiki/analysis/performance/ETF_NYSE_ARCA_XSMO Performance.md`, `wiki/analysis/performance/ETF_LSE_R2US Performance.md`, this source batch, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `wiki/analysis/comparisons/ETF Region Index.md`, and `log.md`.
