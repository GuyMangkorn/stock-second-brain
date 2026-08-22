---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EES
ticker: EES
exchange: NYSE Arca
fund: WisdomTree U.S. SmallCap Fund
tracked_index: WisdomTree U.S. SmallCap Index (WTSEI)
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EES
  - geography/United-States
---

# EES Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

EES เป็น passive/index-tracking U.S. small-cap ETF ที่ใช้ earnings-weighted
WisdomTree U.S. SmallCap Index เป็น issuer benchmark. Official NAV Total Return
ช่วง 2016-2025 ให้ cumulative `158.70%` และ rounded-input CAGR `9.97%`; ใน
common 2021-2025 window ให้ CAGR `9.40%` ต่ำกว่า S&P 500 Total Return `14.43%`.
Current NAV TR YTD อยู่ที่ `19.57%` ณ 2026-07-31; S&P 500 TR cross-check ล่าสุด
ที่พบจากรายงาน official อยู่ที่ `9.00%` ณ 2026-07-28 จึงไม่ใช่ same-date pair.

## Performance check

- entity_key: `NYSE Arca:EES`
- Inception: 2007-02-23
- Expense ratio: 0.38% (net and gross, as of 2026-08-14)
- Metric: `NAV Total Return` รวม distributions ตาม issuer total-return convention และ fund expenses; USD
- Tracked index (issuer benchmark): WisdomTree U.S. SmallCap Index (`WTSEI`), formerly WisdomTree U.S. SmallCap Earnings Index
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year window: 2016-01-01 to 2025-12-31 (ten complete calendar years)
- 10-year NAV TR CAGR: `9.97%` rounded-input approximation; normalized start TR value `100.00`, end TR value `258.70`, years `10.00`. Issuer rolling 10-year average annual NAV TR is `10.85%` as of 2026-07-31; raw rolling endpoints are not disclosed.
- Common calendar window: 2016-2025 cumulative `158.70%`; 2021-2025 cumulative `56.73%` / CAGR `9.40%`; S&P 500 cached 2021-2025 cumulative `96.17%` / CAGR `14.43%`
- Coverage/source note: official WisdomTree annual NAV rows cover 2016-2025; annual inputs are rounded. No inception-year partial or secondary proxy is used.

| Year | EES NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 29.96% | 11.96% |
| 2017 | 12.56% | 21.83% |
| 2018 | -9.96% | -4.38% |
| 2019 | 21.92% | 31.49% |
| 2020 | 2.79% | 18.40% |
| 2021 | 34.34% | 28.71% |
| 2022 | -16.16% | -18.11% |
| 2023 | 18.42% | 26.29% |
| 2024 | 9.89% | 25.02% |
| 2025 | 6.93% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ EES;
annual rows ใช้ cached USD Total Return convention ณ 2025-12-31. Cumulative
returns และ CAGRs เป็น rounded-input calculations จาก annual observations.

## Up years / Down years

- Up years / Down years: 8 / 2 in the complete 2016-2025 window
- Best: 2021, +34.34%
- Least positive: 2020, +2.79%
- Worst: 2022, -16.16%
- Least bad down year: 2018, -9.96%
- Current EES NAV TR YTD: +19.57% as of 2026-07-31
- Current NAV / market price: $69.712 / $69.666 as of 2026-08-14

## Risk read-through

EES มี annual-return volatility แบบ population standard deviation `15.31%`
จาก official 2016-2025 rows. Earnings-weighted small-cap exposure ช่วยคัด
บริษัทที่มี positive cumulative earnings ตาม methodology แต่ยังมี small-cap,
cyclicality, liquidity, valuation และ factor-regime risk. Official daily NAV
history สำหรับคำนวณ max drawdown และ recovery ยังไม่พบข้อมูลที่ยืนยันได้ จึงไม่
สร้างตัวเลข proxy เพิ่ม.

## Sources

- [Official WisdomTree EES product page](https://www.wisdomtree.com/us/products/equity/ees)
- [Official WisdomTree EES factsheet](https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/us-equity/wisdomtree-factsheet-ees-1012.pdf)
- [Official WisdomTree EES Q1-2026 presentation](https://www.wisdomtree.com/us/media/ees-presentation)
- [Official WisdomTree U.S. SmallCap Index page](https://www.wisdomtree.com/us/indexes/WTSEI?index=WTSEI)
- [Official S&P 500 current index returns report](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page)
- [S&P 500 index definition and cached historical reference](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
