---
type: source-batch
topic: ETF performance
accessed: 2026-08-17
input_source: Trello ETF child cards GSSC, XSMO, SSEUF, FNDA, ZPRVF, NUSC, IMWSF, DES
input_count: 8
workflow: check-etf-performance
execution_profile: scheduled-inline
verification_mode: scheduled-local
reviewer_dispatch: not-attempted-by-design
review_gate: PASS
annual_rows_as_of: "GSSC official 2018-2025; XSMO official 2016-2025; SSEUF canonical LSE:R2US official 2016-2025; FNDA secondary 2016-2025; ZPRVF canonical LSE:USSC official 2016-2025; NUSC official 2017-2025; IMWSF canonical LSE:WSML official 2019-2025; DES official 2016-2025; current NAV/YTD fields through 2026-08-14; S&P current cross-check through 2026-08-10"
tags:
  - source/etf
---

# ETF Performance Source Batch - 2026-08-17

## Scope and gate

Research-bearing lean source batch for GSSC, XSMO, SSEUF, FNDA, ZPRVF, NUSC, IMWSF, and DES. Source discovery, reading, reconciliation,
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
| FNDA | supported | NYSE Arca:FNDA | USA | 21.18% (2026-06-30) | https://www.schwabassetmanagement.com/products/fnda | passive/index-tracking U.S. small-cap fundamental equity; annual calendar rows are secondary total-return proxy; daily NAV drawdown/recovery not disclosed |
| NUSC | supported | Cboe BZX:NUSC | USA | 16.76% (2026-06-30) | https://documents.nuveen.com/Documents/Nuveen/Viewer.aspx?uniqueId=8238272c-9326-4c32-93cb-40d80e4fc4a9 | passive/index-tracking U.S. small-cap ESG equity; history under 10 years; Nuveen HTML performance table rendered no records, official PDF factsheet used; daily NAV drawdown/recovery not disclosed |
| IMWSF | supported | LSE:WSML | International | 19.00% (2026-08-13) | https://www.ishares.com/uk/professionals/en/products/296576/ishares-msci-world-small-cap-ucits-etf-fund?siteEntryPassthrough=true&switchLocale=y | OTC alias resolved to official USD LSE line by ISIN `IE00BF4RFH31`; passive/global developed small-cap equity; history under 10 years; daily NAV drawdown/recovery not disclosed |

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

## DES official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:DES | https://www.wisdomtree.com/us/products/equity/des | Official product page: fund identity, passive/index-tracking description, NAV/market price, rolling and YTD performance, expense, and distributions | NAV/price and expense through 2026-08-14; rolling 10Y and YTD performance through 2026-07-31; distributions through 2026-07-28 |
| NYSE Arca:DES | https://www.wisdomtree.com/us/media/des-presentation | Official issuer presentation: calendar-year NAV total returns and methodology | 2016-2025 annual NAV rows; presentation data as of 2026-03-31 |
| NYSE Arca:DES | https://www.wisdomtree.com/us/media/wisdomtree-factsheet-des-1008 | Official quarterly factsheet: exchange, inception, index, expense, and return definition | Factsheet data as of 2026-03-31 |
| NYSE Arca:DES | https://www.sec.gov/Archives/edgar/data/1350487/000121465925011322/des73125497k.htm | SEC summary prospectus: passive indexing, listing, fees, and return treatment | Filing reviewed 2026-08-17 |
| WTSDI | https://www.wisdomtree.com/us/indexes/wtsdi | Official tracked-index methodology and identity | Index methodology page reviewed 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Common benchmark definition | USD total return convention; page reviewed 2026-08-17 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current cross-check | `14.04%` YTD displayed on page dated 2026-08-10; not synchronized with DES YTD 2026-07-31 |
| S&P 500 TR cached annual rows | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true; https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-2021/; https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached project convention for complete calendar years | 2016-2025 USD gross total return, dividends reinvested, as of 2025-12-31 |

## DES raw observations and calculations

| Year | DES NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.06% | 11.96% |
| 2017 | 8.66% | 21.83% |
| 2018 | -12.74% | -4.38% |
| 2019 | 20.30% | 31.49% |
| 2020 | -4.41% | 18.40% |
| 2021 | 26.71% | 28.71% |
| 2022 | -10.94% | -18.11% |
| 2023 | 16.40% | 26.29% |
| 2024 | 9.79% | 25.02% |
| 2025 | 0.26% | 17.88% |
| 2026 YTD | 22.93% (official NAV, 2026-07-31) | 14.04% (official current page dated 2026-08-10; not same date) |

- DES 2016-2025 compound: `106.62%` cumulative; rounded-input CAGR `7.53%`.
- DES 2021-2025 compound: `44.59%` cumulative; rounded-input CAGR `7.65%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- The official rolling 10-year DES NAV TR field is `8.04%` as of 2026-07-31; raw rolling endpoints were not disclosed in the reviewed issuer capture. The `7.53%` figure is the separate 2016-2025 calendar-window calculation from rounded annual rows.
- DES annual-row sample standard deviation is `15.30%`; this is calculated from the ten rounded annual NAV TR observations and is not a daily risk measure.
- Year-end cumulative-path drawdown approximation is `-12.74%` at the 2018 year-end observation, with recovery above the prior year-end high by 2019; no daily maximum drawdown is claimed.
- Latest four official cash distributions reviewed sum to `$0.305`; latest listed distribution is `$0.045` ex/pay 2026-07-28/30, and the product page shows distribution yield `1.30%` as of 2026-08-14. These are separate from total return.

## DES pre-save checklist

- `verification_mode: scheduled-local`
- `reviewer_dispatch: not-attempted-by-design`
- Entity and exchange reconciled as `NYSE Arca:DES`; passive/index-tracking classification confirmed from issuer and SEC sources.
- Return basis, USD currency, issuer benchmark, common benchmark, annual coverage, current-field as-of dates, and separate NAV/price/distribution fields were checked before write.
- Every durable number above maps to an official URL or the cached S&P convention; rounded-input calculations are labeled and no synchronized S&P current-YTD spread is asserted.
- Existing DES performance path and USA-region navigation were updated in place; no duplicate canonical page was created.
- Local pre-save result: `PASS`.

## DES gaps and conflicts

- DES official rolling 10-year performance is available, but raw endpoint values were not disclosed in the reviewed issuer capture; it is not substituted with the calendar-window CAGR.
- DES YTD is as of 2026-07-31 while the official S&P current cross-check is displayed for 2026-08-10; no same-date benchmark spread is claimed.
- Annual issuer rows are rounded; cumulative, CAGR, and annual-row volatility are rounded-input calculations.
- Official daily NAV history sufficient for a daily maximum-drawdown and recovery statistic was not verified; only the labeled year-end observation approximation is retained.

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

## FNDA official and secondary source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| NYSE Arca:FNDA | https://www.schwabassetmanagement.com/products/fnda | Official Schwab product page: objective, index, passive style, fee, current NAV/YTD, holdings, turnover, beta and standard deviation | Official NAV/YTD and risk fields as of 2026-06-30; quote/NAV profile as of 2026-07-30 |
| NYSE Arca:FNDA | https://www.schwabassetmanagement.com/resource/fnda-fact-sheet | Official Schwab factsheet entry | Last updated 2026-06-30; PDF viewer download was not text-extractable in the web session |
| NYSE Arca:FNDA | https://www.sec.gov/Archives/edgar/data/1454889/000110465925063127/tm2513735-8_497k.htm | SEC summary prospectus: passive objective, fee, index methodology, 2024 index change, risk quarters and official 2024 performance table | Filed 2025-06-27; performance table through 2024-12-31 |
| NYSE Arca:FNDA | https://www.etfreplay.com/etf/fnda | Secondary dividend-adjusted total-return annual rows used for 2016-2025 common-window calculations | Data as of 2026-08-03; complete annual rows through 2025 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official benchmark definition | USD total return, dividends reinvested; cached convention as of 2025-12-31 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/market-attributes-us-equities/ | Cached annual reference rows | 2022-2025; reused without a new search |

## FNDA raw observations and calculations

| Year | FNDA secondary total-return proxy | S&P 500 TR |
|---|---:|---:|
| 2016 | 23.54% | 11.96% |
| 2017 | 12.66% | 21.83% |
| 2018 | -12.10% | -4.38% |
| 2019 | 24.33% | 31.49% |
| 2020 | 8.46% | 18.40% |
| 2021 | 31.11% | 28.71% |
| 2022 | -14.82% | -18.11% |
| 2023 | 20.31% | 26.29% |
| 2024 | 8.99% | 25.02% |
| 2025 | 7.44% | 17.88% |
| 2026 YTD | 21.18% (official NAV) | not available from cached current-year benchmark |

- Metric basis for the current field: official Schwab NAV Total Return in USD; distributions are reinvested and fund expenses are reflected in NAV.
- Annual-row basis: ETFreplay dividend-adjusted total-return proxy; it is not relabelled as official issuer NAV return.
- Issuer benchmark: current RAFI Fundamental High Liquidity US Small Index; the fund changed from Russell RAFI US Small Company Index effective 2024-06-21.
- Official rolling 10-year NAV TR: annualized `11.53%` as of 2026-06-30; raw endpoints are not disclosed.
- 2016-2025 secondary proxy compound: `159.56%` cumulative; rounded-input CAGR `10.01%`.
- 2021-2025 secondary proxy compound: `57.34%` cumulative; rounded-input CAGR `9.49%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk observations: best quarter `+30.46%` in 4Q2020; worst quarter `-35.49%` in 1Q2020; 3-year standard deviation `18.38%` and beta `1.00` as of 2026-06-30.

## FNDA gaps and conflicts

- Official current NAV/YTD and rolling 10-year fields are available only through 2026-06-30 in the product-page extract; the profile quote/NAV is newer at 2026-07-30 but is not a return metric.
- Schwab's SEC table reports 2024 before-tax return `8.96%`; the secondary annual proxy reports `8.99%`. The values are retained as a source conflict and not silently merged.
- Official annual NAV rows for 2016-2025 were not text-extractable from the issuer bar-chart/factsheet materials, so the common-window annual table remains explicitly secondary.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual proxy observations are rounded values; cumulative and CAGR outputs are rounded-input calculations.

## Scheduled-inline local review

- Status: `PASS`
- Confirmed GSSC, XSMO, SSEUF, and FNDA ticker/exchange, passive classification, inception, expense ratio, issuer benchmark, NAV TR definition, official annual/current fields, secondary annual proxy basis, S&P cache window/basis, best/worst ranking, formulas, source links, graph breadcrumb, region ownership, and unresolved gaps.
- XSMO-specific local checklist: verified the official 2016-2025 annual rows, issuer 10-year average annual field, secondary current NAV snapshot, separate return-basis treatment, predecessor-index continuity note, 8/2 up/down count, and no unsupported drawdown/recovery inference.
- SSEUF-specific local checklist: verified OTC-to-`LSE:R2US` alias mapping, ISIN/share-class currency, passive classification, official 2016-2025 rows, official 10-year/current NAV fields, S&P cache convention, 8/2 up/down count, risk metrics, graph breadcrumb, primary-region ownership, and no unsupported drawdown/recovery inference.
- FNDA-specific local checklist: verified passive/index classification, exchange, inception, fee, current tracked index, official NAV 10Y/YTD fields, secondary annual-row basis, 2024 benchmark splice, 8/2 up/down count, risk metrics, source conflict, graph breadcrumb, primary-region ownership, and no unsupported drawdown/recovery inference.
- ZPRVF-specific local checklist: resolved the OTC input alias to official USD `LSE:USSC` by ISIN `IE00BSPLC413`, verified passive/index-tracking equity classification, inception, TER, accumulation, issuer benchmark, official 2016-2025 Fund Net rows, rolling 10-year NAV TR, current YTD, S&P cache window/basis, current benchmark date mismatch, 8/2 up/down count, risk metrics, graph breadcrumb, USA primary-region ownership, and no unsupported drawdown/recovery inference.
- NUSC-specific local checklist: verified Cboe BZX identity, passive/index classification, inception, 0.31% fee, Nuveen ESG USA Small-Cap Index, official 2017-2025 NAV/index rows, official 2026 YTD NAV/index fields, under-10-year history, SEC best/worst-quarter corroboration, S&P cache window/basis, 7/2 up/down count, HTML/PDF performance-rendering conflict, graph breadcrumb, USA primary-region ownership, and no unsupported drawdown/recovery inference.
- IMWSF-specific local checklist: resolved OTC `IMWSF` to USD `LSE:WSML` by ISIN `IE00BF4RFH31`, verified passive/physical/optimised UCITS structure, inception, TER, accumulating treatment, official 2019-2025 NAV/index rows, current product-page NAV/YTD, factsheet July YTD, S&P cache/current date mismatch, 6/1 up/down count, 3-year standard deviation and beta, graph breadcrumb, International primary-region ownership, and no unsupported drawdown/recovery inference.
- Planned durable files reviewed before save: `wiki/analysis/performance/ETF_NYSE_ARCA_GSSC Performance.md`, `wiki/analysis/performance/ETF_NYSE_ARCA_XSMO Performance.md`, `wiki/analysis/performance/ETF_LSE_R2US Performance.md`, `wiki/analysis/performance/ETF_LSE_USSC Performance.md`, `wiki/analysis/performance/ETF_NYSE_ARCA_FNDA Performance.md`, `wiki/analysis/performance/ETF_CBOE_BZX_NUSC Performance.md`, `wiki/analysis/performance/ETF_LSE_WSML Performance.md`, this source batch, `wiki/analysis/comparisons/USA ETF.md`, `wiki/analysis/comparisons/International ETF.md`, `wiki/analysis/performance/ETF Performance Index.md`, `wiki/analysis/comparisons/ETF Region Index.md`, and `log.md`.

## ZPRVF / USSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:USSC / input ZPRVF | https://www.ssga.com/ie/en_gb/institutional/etfs/state-street-spdr-msci-usa-small-cap-value-weighted-ucits-etf-zprv-gy | Official State Street product page: fund identity, listings, inception, TER context, official NAV, Fund Net/NAV performance, annual rows, standard deviation and tracking error | Fund performance through 2026-07-31; NAV 2026-08-14; characteristics 2026-08-13 |
| LSE:USSC / input ZPRVF | https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-zprv-gy.pdf | Official State Street factsheet: ISIN, USD LSE ticker, index, inception, TER, accumulation, optimized replication and performance | Factsheet dated 2026-06-30; performance table through 2026-07-31 |
| Input ZPRVF alias | https://stockanalysis.com/quote/otc/ZPRVF/ | Secondary OTC identity/exchange cross-check; not used for NAV TR ranking | OTC ticker identity checked 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current S&P 500 (TR) YTD cross-check | 14.04% as of 2026-08-16; not synchronized with ETF 2026-07-31 YTD and not used in annual table |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true | Cached annual reference rows | 2016-2019; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf | Cached annual reference rows | 2018-2022; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/ | Cached annual reference row | 2021; reused without a new search |
| S&P 500 TR | https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/ | Cached annual reference rows | 2022-2025; reused without a new search |

## ZPRVF / USSC raw observations and calculations

| Year | USSC Fund Net / NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 25.83% | 11.96% |
| 2017 | 9.37% | 21.83% |
| 2018 | -14.31% | -4.38% |
| 2019 | 23.80% | 31.49% |
| 2020 | 8.46% | 18.40% |
| 2021 | 35.40% | 28.71% |
| 2022 | -10.23% | -18.11% |
| 2023 | 21.18% | 26.29% |
| 2024 | 9.67% | 25.02% |
| 2025 | 13.89% | 17.88% |
| 2026 YTD | 20.29% (official Fund Net/NAV) | 14.04% (official current page, as of 2026-08-16; not same date) |

- Metric basis: official State Street Fund Net performance is NAV-based and net of fees; the accumulating USD share class retains income in NAV.
- Issuer benchmark: `MSCI USA Small Cap Value Weighted Index` (Net Total Return); retained as metadata and not substituted for the common S&P 500 reference.
- Official rolling 10-year NAV TR: `213.35%` cumulative / `12.10%` annualized as of 2026-07-31. Because raw NAV endpoints are not disclosed, the performance page uses a normalized index calculation `100.00 → 313.35` over `10.00` years; this is not presented as a raw provider index level.
- 2016-2025 USSC compound: `191.31%` cumulative; rounded-input CAGR `11.28%`.
- 2021-2025 USSC compound: `83.97%` cumulative; rounded-input CAGR `12.97%`.
- S&P 500 cached 2016-2025 compound: `298.33%` cumulative; rounded-input CAGR `14.82%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk fields: 3-year standard deviation `18.28%` and annualized tracking error `0.07%` as of 2026-07-31; official NAV `US$96.48` as of 2026-08-14.

## ZPRVF / USSC gaps and conflicts

- The input ticker `ZPRVF` is an OTC alias. State Street's official listings for ISIN `IE00BSPLC413` identify the USD line as `LSE:USSC` and the primary EUR line as `Deutsche Börse:ZPRV`; the durable key uses `LSE:USSC` to match the USD share class while preserving the input alias in metadata.
- The latest official ETF YTD field is `20.29%` as of 2026-07-31. The latest official S&P 500 TR page reviewed shows `14.04%` as of 2026-08-16; the as-of dates differ, so the current benchmark figure is disclosed but not used as a same-date annual-table comparator.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations. Market-price observations from different currency listings are not mixed into the NAV Total Return ranking.

## NUSC official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| Cboe BZX:NUSC | https://documents.nuveen.com/Documents/Nuveen/Viewer.aspx?uniqueId=8238272c-9326-4c32-93cb-40d80e4fc4a9 | Official Nuveen factsheet: identity, passive/indexing approach, exchange, fee, NAV/index calendar returns, current YTD, holdings and risk context | Factsheet as of 2026-06-30; calendar rows 2017-2025; current NAV/index YTD 2026-06-30 |
| Cboe BZX:NUSC | https://www.nuveen.com/en-us/exchange-traded-funds/nusc-nuveen-esg-small-cap-etf | Official product page: identity, methodology, primary exchange, fee, inception, quote/NAV snapshot and current page-rendering check | Product-page quote/NAV as of 2026-06-26; performance component rendered no records in the reviewed capture |
| Cboe BZX:NUSC | https://www.sec.gov/Archives/edgar/data/1635073/000119312526080215/d91437d497k.htm | SEC summary prospectus: listing, objective, fees, index strategy, annual return chart and best/worst quarters | Filed 2026-02-27; annual rows through 2025; best/worst quarter history through 2025-12-31 |
| MSCI Nuveen ESG USA Small-Cap Index | https://www.msci.com/indexes/index/711741/nuveen-esg-usa-small-cap-index | Issuer benchmark identity and index-provider cross-check | Index identity checked 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |

## NUSC raw observations and calculations

| Year | NUSC NAV TR | Nuveen ESG USA Small-Cap Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2017 | 16.62% | 17.13% | 21.83% |
| 2018 | -9.28% | -8.88% | -4.38% |
| 2019 | 26.82% | 27.37% | 31.49% |
| 2020 | 23.48% | 23.97% | 18.40% |
| 2021 | 17.83% | 18.26% | 28.71% |
| 2022 | -17.68% | -17.55% | -18.11% |
| 2023 | 15.50% | 15.80% | 26.29% |
| 2024 | 8.48% | 8.79% | 25.02% |
| 2025 | 7.60% | 7.85% | 17.88% |
| 2026 YTD | 16.76% (official NAV) | 16.94% (official issuer index) | not available from cached current-year benchmark |

- Metric basis: official Nuveen NAV total return includes reinvested distributions and fund expenses; the issuer index excludes fund expenses.
- Issuer benchmark: `Nuveen ESG USA Small-Cap Index`, calculated by MSCI; retained as metadata and not substituted for the common S&P 500 reference.
- NUSC 2017-2025 compound: `116.65%` cumulative; rounded-input CAGR `8.97%`.
- NUSC 2021-2025 compound: `30.77%` cumulative; rounded-input CAGR `5.51%`.
- Issuer index 2017-2025 compound: `123.26%` cumulative; rounded-input CAGR `9.33%`; 2021-2025 CAGR `5.79%`.
- S&P 500 cached 2017-2025 compound: `255.78%` cumulative; rounded-input CAGR `15.14%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk observations: best quarter `+29.98%` in 4Q2020 and worst quarter `-30.76%` in 1Q2020 from the SEC summary prospectus; official daily NAV history for maximum drawdown/recovery was not verified.

## NUSC gaps and conflicts

- Inception was 13 Dec 2016, so 2016 is a partial inception period and the fund has not reached a full 10-year history as of 2026-06-30; no 10-year NAV CAGR is claimed.
- Nuveen's HTML product page rendered `No Records Available` for the performance component in the reviewed capture, while the official PDF factsheet dated 2026-06-30 supplied numeric calendar/YTD fields; the factsheet is used for performance and the rendering conflict is preserved here.
- The latest official NUSC performance field reviewed is `16.76%` NAV TR YTD as of 2026-06-30; the common S&P cache has no synchronized 2026 current-year row, so no current S&P YTD comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.

## IMWSF / WSML official source map

| Scope | Source | Role | Data / as-of date |
|---|---|---|---|
| LSE:WSML / input IMWSF | https://www.ishares.com/uk/professionals/en/products/296576/ishares-msci-world-small-cap-ucits-etf-fund?siteEntryPassthrough=true&switchLocale=y | Official iShares product page: USD share-class identity, listings, benchmark, TER, structure, current NAV/YTD, holdings and risk metrics | Current page observations: NAV 2026-08-14; NAV TR YTD 2026-08-13; portfolio/risk fields through 2026-07-31 |
| LSE:WSML / input IMWSF | https://www.ishares.com/gls-download/literature/fact-sheet/wsml-ishares-msci-world-small-cap-ucits-etf-fund-fact-sheet-en-gb.pdf | Official iShares factsheet: ISIN, launch, USD accumulating share class, physical/optimised structure, annual NAV/index rows, July YTD and listings | Factsheet dated July 2026; performance and NAV data as of 2026-07-31; other data as of 2026-08-07 |
| Input IMWSF alias | https://digital.fidelity.com/prgw/digital/research/quote/dashboard/summary?symbol=IMWSF | Secondary OTC alias / ISIN cross-check; not used for NAV Total Return ranking | OTC identity checked 2026-08-17 |
| S&P 500 TR | https://www.spglobal.com/spdji/en/indices/equity/sp-500/ | Official common benchmark definition | USD total return, dividends reinvested; cached annual convention as of 2025-12-31 |
| S&P 500 TR current | https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page | Official current S&P 500 TR YTD cross-check | 14.04% as of 2026-08-16; not synchronized with WSML 2026-08-13 YTD |

## IMWSF / WSML raw observations and calculations

| Year | WSML NAV TR | MSCI World Small Cap Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2019 | 25.73% | 26.19% | 31.49% |
| 2020 | 15.83% | 15.96% | 18.40% |
| 2021 | 15.81% | 15.75% | 28.71% |
| 2022 | -18.64% | -18.75% | -18.11% |
| 2023 | 16.02% | 15.76% | 26.29% |
| 2024 | 7.93% | 8.15% | 25.02% |
| 2025 | 19.84% | 19.88% | 17.88% |
| 2026 YTD | 19.00% (official NAV) | not available from same-date official product-page field | 14.04% (official current page, as of 2026-08-16; not same date) |

- Metric basis: official iShares NAV total return is shown on NAV basis with gross income reinvested where applicable; the accumulating USD share class retains income in NAV.
- Issuer benchmark: `MSCI World Small Cap Index (Net)`; retained as metadata and not substituted for the common S&P 500 reference.
- WSML 2019-2025 compound: `105.92%` cumulative; rounded-input CAGR `10.87%`.
- WSML 2021-2025 compound: `41.39%` cumulative; rounded-input CAGR `7.17%`.
- Issuer index 2019-2025 compound: `106.54%` cumulative; rounded-input CAGR `10.92%`; 2021-2025 CAGR `7.14%`.
- S&P 500 cached 2019-2025 compound: `205.41%` cumulative; rounded-input CAGR `17.29%`.
- S&P 500 cached 2021-2025 compound: `96.17%` cumulative; rounded-input CAGR `14.43%`.
- Formula: `CAGR = product(1 + annual return)^(1 / number of years) - 1`.
- Official risk fields: 3-year standard deviation `16.16%` and beta `1.000` as of 2026-06-30; holdings `3,558` as of 2026-07-30; official daily NAV history for maximum drawdown/recovery was not verified.

## IMWSF / WSML gaps and conflicts

- The OTC input `IMWSF` is not the canonical issuer listing. Official iShares listings for ISIN `IE00BF4RFH31` identify the USD line as `LSE:WSML`, with additional GBP/CHF/EUR listings; the durable key uses `LSE:WSML` while preserving the input alias.
- Inception was 27 Mar 2018; 2018 is a partial/inception period whose annual return is not disclosed in the reviewed official materials, and no 10-year NAV CAGR is claimed.
- The July factsheet reports NAV YTD `13.88%` as of 2026-07-31 while the newer product page reports `19.00%` as of 2026-08-13; these are separate as-of dates, so the newer product-page field is used as current and both observations are preserved.
- The current official S&P 500 TR page reports `14.04%` as of 2026-08-16, one date after the ETF current YTD; no synchronized current benchmark comparison is asserted.
- Official daily NAV history sufficient to calculate maximum drawdown and recovery was not verified; no numeric secondary drawdown proxy is saved.
- Annual observations are rounded issuer values; cumulative and CAGR outputs are rounded-input calculations.
