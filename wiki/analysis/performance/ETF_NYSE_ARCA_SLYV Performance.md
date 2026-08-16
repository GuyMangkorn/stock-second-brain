---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:SLYV
ticker: SLYV
exchange: NYSE Arca
fund: State Street SPDR S&P 600 Small Cap Value ETF
tracked_index: S&P SmallCap 600 Value Index
benchmark: S&P 500 Total Return
updated: 2026-08-16
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-10
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/SLYV
  - geography/United-States
---

# SLYV Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

SLYV เป็น passive/index-tracking U.S. small-cap value ETF ที่ติดตาม `S&P
SmallCap 600 Value Index` ด้วย sampling. ใน complete calendar window 2016-2025
มี 8 ปีบวก / 2 ปีลบ; cumulative NAV Total Return ที่คำนวณจาก annual rows คือ
`147.73%` หรือ rounded-input CAGR `9.50%`, เทียบ S&P 500 TR `298.33%` /
`14.82%`. ปีดีที่สุดคือ 2016 ที่ `+31.14%` และแย่ที่สุดคือ 2018 ที่ `-12.69%`.
Current official NAV TR YTD ที่ยืนยันได้ล่าสุดคือ `+20.17%` ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:SLYV`
- Classification: supported passive/index-tracking equity ETF using a
  representative-sampling approach; exchange NYSE Arca
- Inception: 25 ก.ย. 2000; expense ratio `0.15%`; quarterly distribution
- Metric: `NAV Total Return` บนฐาน USD รวม reinvested dividends และ capital
  gains; SSGA ระบุว่าเป็นผลตอบแทน net of fees และ market-price return แยกต่างหาก
- Tracked index (issuer benchmark): `S&P SmallCap 600 Value Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ SLYV)
- Official rolling 10-year NAV TR: average annual `10.06%` ณ 31 ก.ค. 2026;
  raw rolling endpoints ไม่ได้เปิดเผย จึงไม่คำนวณซ้ำ
- Current official NAV TR YTD: `20.17%` ณ 31 ก.ค. 2026; older factsheet
  snapshot คือ `20.85%` ณ 30 มิ.ย. 2026 และเก็บเป็นคนละ as-of date
- Latest NAV: `110.17` ณ 10 ส.ค. 2026

| Year | SLYV NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.14% | 11.96% |
| 2017 | 11.45% | 21.83% |
| 2018 | -12.69% | -4.38% |
| 2019 | 24.31% | 31.49% |
| 2020 | 2.60% | 18.40% |
| 2021 | 30.66% | 28.71% |
| 2022 | -11.13% | -18.11% |
| 2023 | 14.71% | 26.29% |
| 2024 | 7.28%* | 25.02% |
| 2025 | 6.52%* | 17.88% |

`*` ปี 2024–2025 ใช้ secondary standardized total-return rows จาก ETFReplay
และมี TotalRealReturns ช่วย corroborate; official SEC prospectus rows ที่ใช้ใน
ตารางครอบคลุมถึง 2023.

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2016, `+31.14%`; least positive: 2025, `+6.52%`
- Worst: 2018, `-12.69%`; least bad down year: 2022, `-11.13%`
- 2016-2025 cumulative/CAGR: SLYV `147.73%` / `9.50%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: SLYV `52.21%` / `8.77%`; S&P 500 TR
  `96.17%` / `14.43%`
- 2025 relative to S&P 500 TR: `6.52% - 17.88% = -11.36 pp`

## Risk read-through

SLYV มีหุ้น `462` รายการ ณ 30 มิ.ย. 2026 และ exposure หลักอยู่ใน Financials
`21.55%`, Consumer Discretionary `15.90%`, Industrials `13.03%`, Information
Technology `12.59%` และ Health Care `7.46%`. Small-cap/value factor, sector
rotation, liquidity และ valuation risk จึงมีความสำคัญ; SSGA ระบุว่าหุ้น value
อาจ underperform และ small-cap companies มีความผันผวน/สภาพคล่องสูงกว่า. Official
daily NAV history ที่เพียงพอสำหรับ maximum drawdown และ recovery ยังไม่ถูกยืนยัน
จึงไม่ใช้ตัวเลข secondary proxy.

## Sources

- [Official State Street SLYV product page](https://www.ssga.com/us/en/individual/etfs/state-street-sp-600-small-cap-value-etf-slyv) — identity, current performance, NAV, holdings and risk fields
- [Official State Street SLYV fact sheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-slyv.pdf) — return basis, benchmark, inception, expense ratio, exchange, holdings and sector snapshot as of 30 Jun 2026
- [SEC-hosted SLYV summary prospectus](https://www.sec.gov/Archives/edgar/data/1064642/000119312524242957/R25.htm) — strategy, risk and official annual rows through 2023
- [ETFReplay SLYV history](https://www.etfreplay.com/etf/slyv) — secondary 2024–2025 complete-year rows
- [TotalRealReturns SLYV history](https://totalrealreturns.com/n/SLYV) — secondary corroboration for annual total returns
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-16]] | [[ETF Performance Index]]
