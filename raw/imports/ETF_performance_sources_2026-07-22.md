---
type: source-batch
topic: ETF performance
accessed: 2026-07-22
canonical_outputs:
  - wiki/analysis/performance/ETF_LSE_DXJ Performance.md
  - wiki/analysis/performance/ETF_NYSE_ARCA_FLAU Performance.md
  - raw/imports/ETF_performance_sources_2026-07-22.md
  - wiki/analysis/comparisons/Japan ETF.md
  - wiki/analysis/comparisons/Australia ETF.md
  - wiki/analysis/performance/ETF Performance Index.md
  - wiki/analysis/comparisons/ETF Region Index.md
  - log.md
tags:
  - source/etf
  - ticker/DXJ
  - ticker/DXJJF
  - ticker/FLAU
  - geography/Japan
  - geography/Australia
---

# ETF Performance Source Batch - 2026-07-22

## DXJJF / DXJ Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `LSE:DXJ` / ISIN `IE00BVXC4854` | [WisdomTree product page](https://www.wisdomtree.com/gb/products/equities/wisdomtree-japan-equity-ucits-etf---usd-hedged) | Fund identity, official listings, inception, TER, current NAV, structure, index, holdings and distributions | Page accessed 2026-07-22; facts/NAV/holdings mostly as of 2026-07-20 |
| `LSE:DXJ` / ISIN `IE00BVXC4854` | [Official WisdomTree factsheet](https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BVXC4854/) | Official annual NAV Total Return rows, YTD, net-of-fees basis, index benchmark and product facts | Document/data as of 2026-06-30 |
| `LSE:DXJ` / ISIN `IE00BVXC4854` | [WisdomTree performance definition](https://www.wisdomtree.eu/de-de/etfs/export-tilted/wisdomtree-japan-equity-ucits-etf-usd-hedged) | Total-return convention: hypothetical 10K, daily NAV, net of fees, dividends reinvested on ex-date | Page accessed 2026-07-22 |
| `OTC Markets:DXJJF` | [ChartExchange OTC history](https://chartexchange.com/symbol/otc-dxjjf/historical/) | Secondary mapping/liquidity context; OTC last reported US$54.7274 and volume 455 | Quote date 2026-06-30; accessed 2026-07-22 |
| `S&P 500 TR` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Common reference benchmark identity and methodology | Page accessed 2026-07-22 |
| `S&P 500 TR` | [Cached S&P 500 Low Volatility history](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true); [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf); [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/); [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) | Reused cached 2016-2025 USD S&P 500 Total Return rows with dividends reinvested | Benchmark reference as of 2025-12-31 |

## Identity And Classification

- User ticker `DXJJF` resolves by ISIN `IE00BVXC4854` to WisdomTree Japan Equity UCITS ETF - USD Hedged.
- Canonical key: `LSE:DXJ`, because the issuer explicitly lists LSE:DXJ; Borsa Italiana and SIX also use `DXJ`, while Xetra uses `WTDX`.
- `DXJJF` is a secondary OTC alias; issuer and LSE pages do not explicitly list it. It is retained as an alias and not used as the canonical displayed key.
- Classification: supported passive, physical/full-replication, single-country Japan equity UCITS ETF; domicile Ireland; issuer WisdomTree Issuer ICAV.
- Inception: 18 May 2015; TER: 0.48%; base/NAV currency: USD; distributing semi-annually.
- Issuer benchmark: WisdomTree Japan Hedged Equity UCITS Index, USD, Bloomberg `WTIDJHUT`; rules-based, fundamentally weighted, dividend-paying Japanese companies with quality/momentum and ESG screens, with a USD/JPY hedge methodology.

## Return Basis And Current Observations

- Official NAV Total Return is net of fees and uses daily NAV with distributions reinvested at NAV on the ex-dividend date.
- Latest verified official NAV: US$53.244 as of 2026-07-20; daily return -0.003%.
- Latest verified official YTD NAV Total Return: +21.90% as of 2026-06-30. A current official performance table beyond 2026-06-30 was not verified.
- Latest verified issuer distributions: US$0.44390 ex-date 2026-07-02, record 2026-07-03, payable 2026-07-17; US$0.36790 ex-date 2026-01-02, record 2026-01-05, payable 2026-01-16. 2026 cash distributions observed total US$0.81180/share; this is not a forecast.
- OTC price history is sparse and is not used to calculate or rank NAV Total Return, YTD or drawdown.

## Official Annual NAV Total Return Inputs

| Year | DXJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 0.73% | 11.96% |
| 2017 | 22.17% | 21.83% |
| 2018 | -18.71% | -4.38% |
| 2019 | 18.53% | 31.49% |
| 2020 | 2.82% | 18.40% |
| 2021 | 18.07% | 28.71% |
| 2022 | 6.48% | -18.11% |
| 2023 | 40.46% | 26.29% |
| 2024 | 30.55% | 25.02% |
| 2025 | 31.19% | 17.88% |

All ETF annual rows are official complete calendar-year NAV Total Return, net of fees, in USD. S&P rows reuse the cached convention defined by `check-etf-performance`, not the issuer benchmark.

## Calculations And Gaps

- 2016-2025 ETF cumulative: `Π(1 + annual TR) - 1 = 268.73%`; CAGR: `(3.6872645)^(1 / 10) - 1 = 13.94%`. Start TR value is normalized to 100.00 and end TR value to 368.73. The CAGR is approximate because the published annual inputs are rounded.
- 2021-2025 ETF cumulative/CAGR: `202.44%` / `24.77%`; S&P 500 TR cumulative/CAGR: `96.17%` / `14.43%`.
- Up/down years: `9 / 1`; best 2023 `+40.46%`; least positive 2016 `+0.73%`; worst and least bad down year 2018 `-18.71%`.
- Annual-return population standard deviation from rounded 2016-2025 inputs: `16.69%`; this is a calculation, not an issuer 3-year volatility statistic.
- Official daily NAV Total Return series sufficient for official max drawdown and recovery: `ไม่พบข้อมูลที่ยืนยันได้`.
- Official performance beyond YTD 2026-06-30: `ไม่พบข้อมูลที่ยืนยันได้`.
- Official OTC price-return YTD/drawdown: `ไม่พบข้อมูลที่ยืนยันได้` because quote history is sparse and not the NAV Total Return basis.

## Pre-save Review Note

- An independent reviewer was dispatched with the complete evidence packet but did not return a verdict after bounded waits; the agent was stopped. The main agent applied the same local checklist before saving. No durable file was written before this local gate.

## Source-Quality Notes

- Do not substitute WisdomTree's US-listed NYSE Arca:DXJ (WisdomTree Japan Hedged Equity Fund, different fund/inception/ISIN) for this UCITS share class.
- Do not use OTC quote price as NAV Total Return; keep OTC alias/liquidity context separate.
- Local pre-save checklist passed after the independent reviewer dispatch did not return a verdict; the fallback is disclosed above.

## FLAU Source Map

| Scope | Source | Role | Data date |
|---|---|---|---|
| `NYSE Arca:FLAU` | [Franklin Templeton FLAU product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26365/SINGLCLASS/franklin-ftse-australia-etf) | Fund identity, exchange, inception, passive/indexed classification, issuer benchmark, expense ratio, distribution frequency, current YTD/NAV and sector snapshot | Page accessed 2026-07-22; issuer YTD 2026-07-02; latest pricing-history NAV 2026-07-17; sector/holdings snapshot 2026-07-02 |
| `NYSE Arca:FLAU` | [Franklin Templeton FLAU factsheet](https://www.franklintempleton.com/forms-literature/download/FLAU-FF) | Official NAV Total Return definition, annual calendar returns, benchmark, expense ratio, inception and risk statistics | Factsheet as of 2026-03-31; publication March 2026 |
| `NYSE Arca:FLAU` | [Franklin annual shareholder report](https://www.franklintempleton.com/forms-literature/download-preview/FLAU-ATSR) | Corroborating performance narrative and fund-cost disclosure | Period ended 2026-03-31; accessed 2026-07-22 |
| `FLAU` secondary proxy | [FinanceCharts FLAU performance](https://www.financecharts.com/etfs/FLAU/performance) | Current total-return proxy including price appreciation and reinvested dividends; used only to fill issuer's newer YTD gap, not mixed into NAV rankings | Last updated 2026-07-15; YTD `+10.91%*` |
| `S&P 500 TR` | [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | Common-reference benchmark identity and methodology | Page accessed 2026-07-22 |
| `S&P 500 TR` | [Cached S&P 500 Low Volatility history](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true); [S&P U.S. Equities Market Attributes July 2023](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf); [S&P U.S. Equities Market Attributes December 2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/); [S&P U.S. Equities Market Attributes December 2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) | Reused cached USD S&P 500 Total Return calendar rows with dividends reinvested | Benchmark reference as of 2025-12-31 |

## FLAU Identity And Classification

- Canonical key: `NYSE Arca:FLAU`; issuer lists the exchange as NYSE Arca and ticker as FLAU. No AMEX/provider slug is used as the displayed key.
- Fund: Franklin FTSE Australia ETF; inception 2 Nov 2017; base/NAV currency USD; passive/indexed equity ETF; issuer benchmark `FTSE Australia Capped Index-NR`.
- Objective: track, before fees and expenses, a market-capitalization-weighted index of Australian large- and mid-capitalization stocks.
- Expense ratio: `0.09%` gross and net, as of the most recent issuer prospectus/factsheet.
- Distribution frequency: semi-annual. Issuer distribution table lists record-date rows of `$0.450407/share` on 2026-06-20 and `$0.582120/share` on 2025-12-19; these are observed distributions, not forecasts.

## FLAU Return Basis And Current Observations

- Official NAV Total Return is based on ETF NAV, assumes reinvestment of distributions and deduction of fund expenses; the factsheet distinguishes NAV return from market-price return.
- Latest issuer YTD NAV Total Return verified: `+7.34%` as of 2026-07-02. A newer same-capture official YTD figure was not verified.
- Latest issuer pricing-history NAV verified: `US$34.04` as of 2026-07-17; this is a NAV observation, not itself a total-return YTD figure.
- Issuer since-inception NAV annualized return: `7.88%` as of 2026-05-31; it is a rolling since-inception metric and is kept separate from the 2018-2025 year-end-row CAGR.
- FinanceCharts secondary total-return proxy: `+10.91%*` YTD as of 2026-07-15; it includes price appreciation plus reinvested dividends and is not an official NAV series.

## FLAU Official Annual NAV Total Return Inputs

| Year | FLAU NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -12.25% | -4.38% |
| 2019 | 23.20% | 31.49% |
| 2020 | 11.04% | 18.40% |
| 2021 | 9.93% | 28.71% |
| 2022 | -5.42% | -18.11% |
| 2023 | 13.38% | 26.29% |
| 2024 | 0.92% | 25.02% |
| 2025 | 16.47% | 17.88% |

All FLAU annual rows are official complete calendar-year NAV Total Return, net of fees, in USD, from the March 2026 factsheet. The 2017 inception-year partial is not shown as a return and is excluded from rankings. S&P rows reuse the cached `2016-2025` convention, subset here to 2018-2025; they are a common reference, not the issuer benchmark.

## FLAU Calculations And Gaps

- 2018-2025 FLAU cumulative: `Π(1 + annual TR) - 1 = 66.33%`; CAGR: `(1.6633383)^(1 / 8) - 1 = 6.57%`. Normalized start/end TR values are `100.00` and `166.33`; rounded published inputs make the CAGR approximate.
- 2021-2025 FLAU cumulative/CAGR: `38.56%` / `6.74%`; S&P 500 TR cumulative/CAGR: `96.17%` / `14.43%`.
- 2018-2025 S&P 500 TR cumulative/CAGR: `192.03%` / `14.33%`.
- Up/down years: `6 / 2`; best 2019 `+23.20%`; least positive 2024 `+0.92%`; worst 2018 `-12.25%`; least bad down year 2022 `-5.42%`.
- Annual-return population standard deviation from rounded 2018-2025 inputs: `11.06%`; this is a calculation, not the issuer's 3-year NAV standard deviation of `16.99%`.
- Official daily NAV Total Return series sufficient for reproducible maximum drawdown and recovery: `ไม่พบข้อมูลที่ยืนยันได้`; annual rows are not used to infer intra-year drawdown.
- Official 10-year NAV TR CAGR: `ไม่พบข้อมูลที่ยืนยันได้` because the fund has not yet covered a complete 10-year period.
- Official YTD beyond 2026-07-02 in the same current performance capture: `ไม่พบข้อมูลที่ยืนยันได้`; retain the 2026-07-15 secondary proxy separately with `*`.

## FLAU Pre-save Review Note

- No independent reviewer tool was available in this thread. The main agent performed the same local checklist from `check-etf-performance/workflow.md` against the complete evidence packet before writing: ticker/exchange, fund classification, return basis, distributions, annual markers, calculations, benchmark cache, as-of dates, source links, filenames, region assignment, breadcrumbs, tags and planned log bullet.
- Local verdict: `PASS`; no critical or high-severity finding remained. The reviewer-availability fallback is disclosed here as required by the durable `lean` workflow.

## FLAU Source-Quality Notes

- Do not use the FinanceCharts `+10.91%*` proxy as official NAV YTD or mix it into annual NAV rankings; it is retained only because the issuer's latest verified YTD capture is dated 2026-07-02.
- Do not calculate a 10-year CAGR from the eight complete calendar-year rows; the official period is shorter than 10 years.
- FLAU is assigned to primary region `Australia` based on underlying exposure, not the NYSE Arca listing venue.
