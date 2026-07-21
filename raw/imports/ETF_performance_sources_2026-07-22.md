---
type: source-batch
topic: ETF performance
accessed: 2026-07-22
canonical_outputs:
  - wiki/analysis/performance/ETF_LSE_DXJ Performance.md
  - raw/imports/ETF_performance_sources_2026-07-22.md
  - wiki/analysis/comparisons/Japan ETF.md
  - wiki/analysis/performance/ETF Performance Index.md
  - wiki/analysis/comparisons/ETF Region Index.md
  - log.md
tags:
  - source/etf
  - ticker/DXJ
  - ticker/DXJJF
  - geography/Japan
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
