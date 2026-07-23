---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DBJP
ticker: DBJP
exchange: NYSE Arca
fund: Xtrackers MSCI Japan Hedged Equity ETF
tracked_index: MSCI Japan US Dollar Hedged Index
benchmark: S&P 500 Total Return
updated: 2026-07-23
performance_as_of: 2026-06-30
current_ytd_as_of: not disclosed
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
primary_region: Japan
tags:
  - analysis/etf-performance
  - ticker/DBJP
  - geography/Japan
---

# DBJP Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

DBJP เป็น passive/index-tracking Japan equity ETF ที่ใช้ MSCI Japan US Dollar
Hedged Index เป็น issuer benchmark. Official Q2 2026 factsheet รายงาน rolling
10-year NAV Total Return CAGR `17.28%` ณ `2026-06-30` โดย NAV return รวมการ
reinvest distributions และหัก fund expenses แล้ว. Annual NAV TR ที่ยืนยันได้จาก
official summary prospectus ครอบคลุม `2016-2024`; ปี `2025` และ current YTD
ยังเป็น `ไม่พบข้อมูลที่ยืนยันได้` จาก issuer source ที่ตรวจสอบรอบนี้.

## Performance check

- entity_key: `NYSE Arca:DBJP`
- Inception: `2011-06-08`
- Classification: passive, index-tracking, single-country Japan equity ETF
- Metric: NAV Total Return รวม reinvested distributions และ fund expenses
- Tracked index: `MSCI Japan US Dollar Hedged Index`
- Expense ratio: `0.45%` ณ `2026-06-30`
- Distribution frequency: annual distribution schedule
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year window represented by issuer field: `2016-06-30` ถึง `2026-06-30`
- Actual elapsed years: `10.00`
- 10-year NAV TR CAGR: `17.28%`
- Normalized start/end TR values: `100.00` / `492.31` (derived from the issuer's
  rounded `17.28%` annualized return; raw NAV endpoint levels are not disclosed)
- Formula: `(492.31 / 100.00)^(1 / 10.00) - 1 ≈ 17.28%`
- Exact June-to-June S&P 500 TR comparison for this rolling window: `not disclosed`

| Year | DBJP NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -2.00% | 11.96% |
| 2017 | 20.83% | 21.83% |
| 2018 | -14.03% | -4.38% |
| 2019 | 20.78% | 31.49% |
| 2020 | 9.49% | 18.40% |
| 2021 | 12.89% | 28.71% |
| 2022 | -2.54% | -18.11% |
| 2023 | 34.97% | 26.29% |
| 2024 | 26.05% | 25.02% |
| 2025 | not disclosed | 17.88% |

Annual DBJP rows are official NAV total-return rows from the DWS summary
prospectus. The S&P 500 rows use the cached USD Total Return convention as of
`2025-12-31`; it is a common reference, not DBJP's tracked index.

## Up years / Down years

Among the complete official DBJP rows for `2016-2024`:

- Up years / Down years: `6 / 3`
- Best: `2023 +34.97%`
- Least positive: `2020 +9.49%`
- Worst: `2018 -14.03%`
- Least bad down year: `2022 -2.54%`
- 2016-2024 cumulative return: `+51.99%`
- 2016-2024 annualized return: `10.81%` over `9` complete calendar years
- Current YTD: `ไม่พบข้อมูลที่ยืนยันได้` from the issuer's latest factsheet

The `10.81%` calendar-row CAGR is not the same measurement as the official
rolling 10-year CAGR because the windows and endpoint conventions differ.

## Risk read-through

10-year NAV TR CAGR `17.28%` แสดงผลตอบแทนระยะยาวที่แข็งแรง แต่ DBJP ยังเป็น
single-country equity exposure จึงไวต่อ Japan macro cycle, sector concentration,
valuation และ FX. กองทุน hedge USD/JPY ด้วย forward contracts; hedge ลด currency
exposure แต่มี hedge cost และ basis risk. Issuer factsheet รายงาน beta `0.89`
และ expense ratio `0.45%` ณ `2026-06-30`. Daily NAV history ที่พอจะคำนวณ
max drawdown และ recovery อย่าง reproducible ยังไม่เปิดเผยใน source ที่ใช้รอบนี้.

## Sources

- [DWS Q2 2026 DBJP factsheet](https://www.dws.com/US/EN/resources/Xtrackers-MSCI-Japan-Hedged-Equity-ETF/DBJP_fact-sheet.pdf) — fund identity, exchange, index, inception, NAV TR and risk fields; as of `2026-06-30`
- [DWS DBJP summary prospectus](https://etf.dws.com/en-us/AssetDownload/Index/c7bca405-12a0-486d-8a66-5d3558c23fa0/DBJP-SUM.pdf) — passive/indexing approach and official calendar-year NAV TR rows `2015-2024`
- [DWS 2025 dividend schedule](https://etf.dws.com/en-us/AssetDownload/Index/6b4403da-1256-4e11-8e8a-14254534db91/Dividend-Schedule.pdf) — annual distribution schedule
- [DWS currency-hedged ETF explanation](https://etf.dws.com/en-us/etf-knowledge/focus-topics-etf-investment-strategies/currency-hedged-etfs-mitigating-currency-risks-from-international-equities/) — USD/JPY forward-hedging mechanism
- [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source-batch convention — common USD total-return reference
- ETF source batch: [[ETF_performance_sources_2026-07-23]] | [[ETF Performance Index]]
