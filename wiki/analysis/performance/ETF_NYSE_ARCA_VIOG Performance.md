---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VIOG
ticker: VIOG
exchange: NYSE Arca
fund: Vanguard S&P Small-Cap 600 Growth ETF
tracked_index: S&P SmallCap 600 Growth Index
benchmark: S&P 500 Total Return
updated: 2026-08-16
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-20
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/VIOG
  - geography/United-States
---

# VIOG Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

VIOG เป็น passive/index-tracking U.S. small-cap growth ETF ที่ติดตาม `S&P
SmallCap 600 Growth Index` ด้วย full replication. ใน comparison window
2016-2025 มี 8 ปีบวก / 2 ปีลบ; cumulative return ที่คำนวณจาก official 2016-2024
rows และ 2025 secondary row คือ `151.94%` หรือ rounded-input CAGR `9.68%`,
เทียบ S&P 500 TR `298.33%` / `14.82%`. ปีดีที่สุดคือ 2021 ที่ `+22.46%` และ
แย่ที่สุดคือ 2022 ที่ `-21.22%`. Current official NAV TR YTD ที่ยืนยันได้ล่าสุด
คือ `+22.11%` ณ 20 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:VIOG`
- Classification: supported passive/index-tracking equity ETF using a
  full-replication approach; exchange NYSE Arca
- Inception: 7 ก.ย. 2010; expense ratio `0.10%`; quarterly distribution
- Metric: `NAV Total Return` บนฐาน USD รวม reinvested dividends และ capital
  gains; figures เป็น pre-tax และ net of expenses ตาม issuer disclosure
- Tracked index (issuer benchmark): `S&P SmallCap 600 Growth Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ VIOG)
- Official rolling 10-year NAV TR: average annual `11.89%` และ cumulative
  `not disclosed` ณ 30 มิ.ย. 2026; raw rolling endpoints ไม่ได้เปิดเผย จึงไม่
  คำนวณซ้ำ
- Current official NAV TR YTD: `22.11%` ณ 20 ก.ค. 2026; current fact sheet
  month-end snapshot คือ `26.98%` ณ 30 มิ.ย. 2026 และเก็บเป็นคนละ as-of date
- Official annual NAV rows are available through 2024 from Vanguard's S&P ETF
  prospectus; the 2025 complete-year row `5.40%*` is a secondary standardized
  total-return observation used only to complete the comparison window

| Year | VIOG NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 22.01% | 11.96% |
| 2017 | 14.58% | 21.83% |
| 2018 | -4.18% | -4.38% |
| 2019 | 20.95% | 31.49% |
| 2020 | 19.48% | 18.40% |
| 2021 | 22.46% | 28.71% |
| 2022 | -21.22% | -18.11% |
| 2023 | 16.95% | 26.29% |
| 2024 | 9.44% | 25.02% |
| 2025 | 5.40%* | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2021, `+22.46%`; least positive: 2025, `+5.40%*`
- Worst: 2022, `-21.22%`; least bad down year: 2018, `-4.18%`
- 2016-2025 cumulative/CAGR: VIOG `151.94%` / `9.68%`; S&P 500 TR
  `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: VIOG `30.14%` / `5.41%`; S&P 500 TR
  `96.17%` / `14.43%`
- 2025 relative to S&P 500 TR: `5.40% - 17.88% = -12.48 pp` (secondary row)

`*` 2025 เป็น secondary standardized total-return observation; ไม่ใช่ annual
row ที่เปิดเผยใน official Vanguard prospectus ที่ตรวจสอบได้ จึงไม่ใช้เพื่ออ้างว่า
เป็น issuer-published NAV row.

## Risk read-through

VIOG มีหุ้น `348` รายการ, turnover `47.6%` และ standard deviation `19.41%`
ณ 30 มิ.ย. 2026. Exposure เป็น small-cap/growth และมีน้ำหนัก sector หลักใน
Industrials `21.3%`, Health Care `17.0%`, Information Technology `15.4%` และ
Financials `15.1%`; จึงไวต่อ growth-style rotation, valuation, cyclicality,
sector และ liquidity risk. Vanguard ระบุว่าราคาของ small-cap ETF อาจผันผวนมากกว่า
large-cap ETF. Official daily NAV history ที่เพียงพอสำหรับ maximum drawdown
และ recovery ยังไม่ถูกยืนยัน จึงไม่ใช้ตัวเลข secondary proxy.

## Sources

- [Official Vanguard VIOG product page](https://investor.vanguard.com/investment-products/etfs/profile/viog) — identity, tracked index and issuer performance fields
- [Official Vanguard S&P ETF prospectus](https://fund-docs.vanguard.com/p3340.pdf) — official VIOG annual NAV rows through 2024 and strategy/risk context
- [Official Vanguard VIOG fact sheet](https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3347.pdf) — current 10-year return, return basis, inception, expense ratio, exchange, holdings and risk snapshot as of 30 Jun 2026
- [Official Vanguard advisor VIOG page](https://advisors.vanguard.com/investments/products/viog/vanguard-sp-small-cap-600-growth-etf) — latest verified NAV TR YTD as of 20 Jul 2026
- Secondary [Yahoo Finance VIOG performance history](https://uk.finance.yahoo.com/quote/VIOG/performance/) and [ETFReplay VIOG return table](https://www.etfreplay.com/etf/viog) — corroborating 2025 complete-year total-return row `5.40%`
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-08-16]] | [[ETF Performance Index]]
