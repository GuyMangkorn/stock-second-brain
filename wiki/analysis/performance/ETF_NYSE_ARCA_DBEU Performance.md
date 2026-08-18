---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DBEU
input_ticker: DBEU
ticker: DBEU
exchange: NYSE Arca
fund: Xtrackers MSCI Europe Hedged Equity ETF
tracked_index: MSCI Europe US Dollar Hedged Index
benchmark: S&P 500 Total Return
updated: 2026-08-19
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: not disclosed
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; secondary annual/YTD proxy where marked
return_currency: USD
primary_region: Europe
tags:
  - analysis/etf-performance
  - ticker/DBEU
  - geography/Europe
---

# DBEU Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`DBEU` เป็น `passive-index` Europe equity ETF ที่ hedge currency exposure เป็น
USD. Official DWS factsheet รายงาน rolling `10-year NAV Total Return CAGR`
`11.58%` ณ `2026-06-30`; annual calendar rows และ current YTD ในหน้านี้เป็น
secondary NAV-return capture ที่ทำเครื่องหมาย `*` เพราะ issuer capture ที่ตรวจ
ยังไม่แสดง annual/YTD table เดียวกัน. Secondary YTD ล่าสุดที่พบคือ `+11.50%*`
ณ `2026-06-30`.

## Performance check

- `entity_key: NYSE Arca:DBEU`
- Inception: `2013-09-30`
- Classification: `passive-index`; SEC summary prospectus ระบุ passive/indexing approach และ full replication เป็นหลัก
- Metric: `NAV Total Return` รวมผลกระทบจาก distributions และ fund expenses; market-price return แยกออกจากตารางนี้
- Tracked index: `MSCI Europe US Dollar Hedged Index`; index strategy hedge currencies to USD ด้วย one-month forward contracts
- Expense ratio: `0.45%` ณ `2026-06-30`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year window: issuer rolling field `2016-06-30` ถึง `2026-06-30`; raw endpoint values ไม่ได้เปิดเผย
- 10-year NAV TR CAGR: `11.58%` (issuer-reported; raw endpoint values not disclosed)
- Coverage/source note: DWS official factsheet supplies rolling NAV/benchmark fields; annual rows and YTD below are secondary NAV-return observations marked `*`. S&P rows reuse the cached USD convention as of `2025-12-31`.

| Year | DBEU NAV TR proxy* (USD) | S&P 500 TR (USD) |
|---|---:|---:|
| 2016 | 8.10%* | 11.96% |
| 2017 | 14.60%* | 21.83% |
| 2018 | -8.50%* | -4.38% |
| 2019 | 26.80%* | 31.49% |
| 2020 | -0.50%* | 18.40% |
| 2021 | 23.30%* | 28.71% |
| 2022 | -6.20%* | -18.11% |
| 2023 | 17.00%* | 26.29% |
| 2024 | 9.50%* | 25.02% |
| 2025 | 22.50%* | 17.88% |

`*` Annual and YTD rows are the secondary source's rounded NAV-return capture,
not issuer-published rows in the reviewed DWS factsheet. The S&P 500 column is
a common USD reference, not DBEU's tracked index.

## Up years / Down years

- Up years / Down years: `7 / 3` (2016-2025 complete calendar proxy rows)
- Best: `2019 +26.80%*`
- Least positive: `2016 +8.10%*`
- Worst: `2018 -8.50%*`
- Least bad down year: `2020 -0.50%*`
- 2016-2025 cumulative proxy return: `+159.58%*`; rounded-input CAGR: `10.01%*` over `10` complete calendar years
- 2021-2025 cumulative proxy return: `+81.51%*`; rounded-input CAGR: `12.66%*`
- Current YTD: `+11.50%*` as of `2026-06-30`; official issuer YTD was not disclosed in the reviewed capture

## Risk read-through

Official rolling `10-year NAV TR CAGR` is `11.58%` as of `2026-06-30`. The
secondary 2016-2025 return population has `11.83%*` standard deviation, while
DWS reports beta `0.73` against the hedged index. Daily NAV history sufficient
to reproduce maximum drawdown and recovery was not disclosed in the reviewed
sources, so `risk-adjusted evidence: not-verified` for those fields. DBEU held
410 securities across 15 developed European markets; the largest country
weights were UK `20.08%`, Switzerland `14.86%`, France `14.29%`, Germany
`13.10%`, and Netherlands `10.57%` as of `2026-06-30`. Financials `23.71%` and
Industrials `17.59%` were the largest sector weights. USD hedging reduces direct
non-USD currency exposure but adds forward-contract, basis and hedge-cost risk;
the expense ratio is `0.45%`.

## Sources

- [DWS Q2 2026 DBEU factsheet](https://etf.dws.com/download/asset/b2d0199b-0bfc-4ed0-866b-24f31967f463) — official identity, rolling NAV/benchmark returns, inception, fee, holdings and risk fields; as of `2026-06-30`
- [SEC DBEU summary prospectus](https://www.sec.gov/Archives/edgar/data/1503123/000008805325000878/k100125dbeu.htm) — official NYSE Arca identity, passive/indexing strategy, fee and risk disclosures; October 2025
- [AAII DBEU performance page](https://www.aaii.com/etf/ticker/DBEU) — secondary rounded annual NAV-return and YTD rows; as of `2026-06-30`
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached S&P 500 TR convention — common USD benchmark definition and `2016-2025` rows
- ETF source batch: [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
