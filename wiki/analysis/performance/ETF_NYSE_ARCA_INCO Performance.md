---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:INCO
ticker: INCO
exchange: NYSE Arca
fund: Columbia India Consumer ETF
tracked_index: Indxx India Consumer Index
benchmark: S&P 500 Total Return
updated: 2026-07-23
performance_as_of: 2026-05-31
current_ytd_as_of: 2026-05-31
price_nav_as_of: 2026-06-23
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/INCO
  - geography/India
---

# INCO Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

INCO เป็น indexed/passive equity ETF ที่ติดตาม Indxx India Consumer Index และ
จดทะเบียนบน NYSE Arca. Official issuer data แสดง 10-year average annual NAV
Total Return 8.72% ณ 2026-05-31; normalized end value 230.72 จาก start 100.00
เป็นค่าที่คำนวณจากตัวเลข annualized ที่ issuer ปัดเศษ ไม่ใช่ raw endpoint.
Current official NAV YTD อยู่ที่ -9.92% ณ 2026-05-31 และ latest verified NAV
อยู่ที่ US$59.45 ณ 2026-06-23.

## Performance check

- entity_key: NYSE Arca:INCO
- Inception: 2011-08-10
- Metric: NAV Total Return รวม reinvested dividends/capital gains และ fund expenses; official page calculates NAV return from daily 4:00pm NAV
- Tracked index (issuer benchmark): Indxx India Consumer Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year coverage: issuer 10-year average annual NAV return as of 2026-05-31; implied start date 2016-05-31 and end date 2026-05-31; actual years 10.00
- Start TR value: 100.00 normalized; End TR value: 230.72 normalized, derived from issuer 10-year annualized return 8.72%; raw NAV endpoints are not disclosed
- 10-year NAV TR CAGR: 8.72% issuer-reported average annual NAV return
- Formula: (End TR / Start TR)^(1 / Years) - 1 = (230.72 / 100.00)^(1 / 10.00) - 1 = approximately 8.72%
- Coverage/source note: official page provides 2021-2025 calendar rows; 2016-2020 calendar rows are not disclosed in the selected current source. The normalized 10-year endpoint is derived from the rounded issuer annualized metric, not a proxy or market-price return.

| Year | INCO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 19.70% | 28.71% |
| 2022 | -7.40% | -18.11% |
| 2023 | 34.12% | 26.29% |
| 2024 | 13.78% | 25.02% |
| 2025 | 0.35% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ INCO;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31. ช่วง annual
comparison ที่เปิดเผยตรงกันคือ 2021-2025.

## Up years / Down years

- Up years / Down years: 4 / 1 ใน complete rows ที่ issuer เปิดเผย
- Best: 2023, +34.12%
- Least positive: 2025, +0.35%
- Worst: 2022, -7.40%
- Least bad down year: 2022, -7.40%
- 2021-2025 cumulative / CAGR: 69.74% / 11.16%; S&P 500 TR: 96.17% / 14.43%
- Current YTD: -9.92% NAV as of 2026-05-31

## Risk read-through

10-year issuer-reported NAV TR annualized return อยู่ที่ 8.72%, ขณะที่
2021-2025 complete disclosed rows ให้ CAGR 11.16%. INCO กระจุกใน India
consumer theme; issuerระบุว่า Indxx India Consumer Index เป็น maximum
30-stock, free-float-adjusted, market-cap-weighted index. Net expense ratio
0.75%, gross expense ratio 0.76%, waiver expiration 2026-07-31. Annual-return
population standard deviation จาก rounded 2021-2025 rows อยู่ที่ 14.59% เป็น
calculation ไม่ใช่ issuer 3-year volatility. Daily NAV history สำหรับ
max drawdown และ recovery: ไม่พบข้อมูลที่ยืนยันได้.

## Sources

- Official Columbia Threadneedle product/performance page:
  https://www.columbiathreadneedleus.com/investment-products/mutual-funds/columbia-india-consumer-etf/class-/details?cusip=19762B707
- Official Columbia India Consumer ETF factsheet:
  https://www.columbiathreadneedleus.com/binaries/content/assets/cti/public/columbia_india_consumer_etf_fs.pdf
- Official S&P 500 index page:
  https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-23]]
