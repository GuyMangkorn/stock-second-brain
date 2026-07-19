---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DTD
input_alias: AMEX:DTD
ticker: DTD
exchange: NYSE Arca
fund: WisdomTree U.S. Total Dividend Fund
tracked_index: WisdomTree U.S. Dividend Index (WTDI)
issuer_broad_benchmark: MSCI USA IMI Total Return
benchmark: S&P 500 Total Return
updated: 2026-07-13
performance_as_of: 2026-06-30
price_nav_as_of: 2026-07-10
source_batch: raw/imports/ETF_performance_sources_2026-07-13.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - geography/United-States
  - ticker/DTD
---

# DTD Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

DTD ให้ cumulative NAV Total Return `+206.16%` ในช่วง complete calendar years
2016-2025 หรือ CAGR `11.84%`; official rolling 10-year NAV CAGR ล่าสุดอยู่ที่
`12.06%` ณ 30 มิ.ย. 2026. เป็นบวก 8 ปีและลบ 2 ปี. ปีดีที่สุดคือ 2019 ที่ `+28.28%`
และแย่ที่สุดคือ 2018 ที่ `-6.35%`. ฐานปีล่าสุดที่ใช้คือ 2025 ที่ `+14.22%` ซึ่งเป็น
NAV return หลัง expense ratio แล้ว. เทียบกับ S&P 500 TR cache ในช่วงเดียวกันที่
`298.33%` หรือ CAGR `14.82%`. 2026 YTD ล่าสุดคือ `+10.80%` ณ 30 มิ.ย. 2026.

## Performance check

- `entity_key: NYSE Arca:DTD` (`AMEX:DTD` เป็น input alias ที่ผู้ใช้ส่งมา)
- Inception: 16 มิ.ย. 2006
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Expense treatment: NAV Total Return เป็นผลตอบแทนของกองทุนหลังค่าใช้จ่ายดำเนินงาน
  ที่สะท้อนใน NAV; net expense ratio คือ `0.28%` ณ 10 ก.ค. 2026. ตัวเลขของ
  benchmark/index ไม่ได้หักค่าธรรมเนียมของ DTD
- Tracked index: `WisdomTree U.S. Dividend Index (WTDI)`; issuer broad-based
  benchmark คือ `MSCI USA IMI Total Return`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference,
  not DTD's tracked index or issuer broad-based benchmark)
- Annual coverage: official complete years 2016-2025; ไม่มี partial-year marker
- Performance as-of: 30 มิ.ย. 2026. NAV/market price as-of: 10 ก.ค. 2026

- Annual NAV TR coverage: official 2016-2025 NAV TR

| ปี | DTD NAV Total Return | S&P 500 TR |
|---|---:|---:|
| 2016 | +16.59% | +11.96% |
| 2017 | +17.25% | +21.83% |
| 2018 | -6.35% | -4.38% |
| 2019 | +28.28% | +31.49% |
| 2020 | +2.57% | +18.40% |
| 2021 | +26.14% | +28.71% |
| 2022 | -3.81% | -18.11% |
| 2023 | +10.44% | +26.29% |
| 2024 | +18.75% | +25.02% |
| 2025 | +14.22% | +17.88% |

**Up years / Down years**

- Best: 2019, `+28.28%`
- Least positive: 2020, `+2.57%`
- Worst: 2018, `-6.35%`
- Least bad down year: 2022, `-3.81%`
- Current YTD: `+10.80%` NAV; underlying WTDI `+10.95%`, both as of 30 มิ.ย. 2026
- Latest completed-year base: 2025 NAV Total Return `+14.22%`

## Risk read-through

2016-2025 CAGR คำนวณจาก official annual returns อยู่ที่ `11.84%`; S&P 500 TR
cache อยู่ที่ `14.82%` ในช่วงเดียวกัน. Issuer-reported MSCI USA IMI comparison
ยังเก็บไว้ใน source batch เดิม. **10-year NAV CAGR:** `12.06%` และ
since-inception annualized NAV return `9.68%` ณ 30 มิ.ย. 2026 ตาม issuer.
Official since-inception standard deviation อยู่ที่ `14.71%` เทียบกับ MSCI USA IMI
`15.71%` ณ 31 มี.ค. 2026. Secondary total-return series รายงาน maximum drawdown
`-58.19%` เมื่อ 9 มี.ค. 2009 และ recovery `855` trading sessions; ใช้เป็น risk
context ไม่ใช่ issuer NAV series.

**Classification:** Structural = U.S. all-cap dividend-weighted equity. Behavioral
= broad dividend/value tilt ที่มี downside ระยะสั้น แต่ยังเป็น equity risk และไม่ใช่
crisis hedge.

## Sources

- [WisdomTree DTD product page](https://www.wisdomtree.com/us/products/equity/dtd) — fund identity, exchange, fee, NAV/price as of 2026-07-10, current YTD and WTDI rolling returns as of 2026-06-30
- [WisdomTree DTD Q1-2026 presentation](https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/presentations/equity/dtd_presentation.pdf) — official calendar returns 2016-2025 and risk statistics as of 2026-03-31
- [WisdomTree DTD factsheet](https://www.wisdomtree.com/us/media/wisdomtree-factsheet-dtd-1005) — inception, expense ratio, NAV return definition, and benchmark disclosures
- [WisdomTree U.S. Dividend Index](https://www.wisdomtree.com/us/indexes/wtdi) — tracked-index methodology and current index facts
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference identity
- [PortfoliosLab](https://portfolioslab.com/symbol/DTD) — secondary maximum-drawdown and recovery context
- [[ETF_performance_sources_2026-07-13]] | [[ETF_performance_sources_2026-07-12]] | [[ETF Performance Index]]
