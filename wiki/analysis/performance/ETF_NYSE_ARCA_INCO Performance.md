---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:INCO
ticker: INCO
exchange: NYSE Arca
fund: Columbia India Consumer ETF
tracked_index: Indxx India Consumer Index
benchmark: S&P 500 Total Return
updated: 2026-08-29
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-07-28
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
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
จดทะเบียนบน NYSE Arca. Latest official Columbia ETF finder snapshot รายงาน
2026 YTD NAV TR `-4.67%` และ 10-year average annual NAV TR `8.38%` ณ
2026-07-31; ส่วน full product performance table ณ 2026-06-30 รายงาน 10-year
NAV TR `8.50%`, จึงเก็บสอง as-of dates แยกกัน. Latest verified NAV คือ
`US$60.84` และ market price `US$61.37` ณ 2026-07-28.

## Performance check

- entity_key: NYSE Arca:INCO
- Inception: 2011-08-10
- Metric: NAV Total Return รวม reinvested dividends/capital gains และ fund expenses; official page calculates NAV return from daily 4:00pm NAV
- Tracked index (issuer benchmark): Indxx India Consumer Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year coverage: issuer ETF finder 10-year average annual NAV return `8.38%` as of 2026-07-31; the detailed product table reported `8.50%` as of 2026-06-30. The 7/31 figure is used as the latest current field; raw 10-year NAV endpoints are not disclosed.
- Optional normalized comparison: start TR value `100.00`; end value `223.61`, derived as `100 × (1 + 0.0838)^10`; this is a rounded-input calculation, not a raw endpoint or market-price return.
- 10-year NAV TR CAGR: `8.38%` issuer-reported average annual NAV return as of 2026-07-31.
- Coverage/source note: official product/factsheet pages provide 2021-2025 calendar rows; 2016-2020 calendar rows are not disclosed in the reviewed capture. The ETF finder and detailed product page have different as-of dates; both are retained with explicit labels.

| Year | INCO NAV TR | Indxx India Consumer Index | S&P 500 TR |
|---|---:|---:|---:|
| 2021 | 19.70% | 22.76% | 28.71% |
| 2022 | -7.40% | -6.28% | -18.11% |
| 2023 | 34.12% | 40.74% | 26.29% |
| 2024 | 13.78% | 17.70% | 25.02% |
| 2025 | 0.35% | 2.45% | 17.88% |

INCO NAV 2021-2025 compound ได้ `69.74%` หรือ rounded-input CAGR `11.16%`;
issuer Indxx rows compound ได้ `95.25%` หรือ `14.32%`. S&P 500 เป็น common
reference benchmark ไม่ใช่ issuer benchmark ของ INCO; ตาราง S&P ใช้ cached USD
Total Return convention ณ 2025-12-31. ช่วง annual comparison ที่เปิดเผยตรงกัน
คือ 2021-2025.

## Up years / Down years

- Up years / Down years: 4 / 1 ใน complete rows ที่ issuer เปิดเผย
- Best: 2023, +34.12%
- Least positive: 2025, +0.35%
- Worst: 2022, -7.40%
- Least bad down year: 2022, -7.40%
- 2021-2025 cumulative / CAGR: 69.74% / 11.16%; issuer-index cumulative / CAGR: 95.25% / 14.32%; S&P 500 TR: 96.17% / 14.43%
- Latest current YTD: -4.67% NAV as of 2026-07-31; detailed product table YTD: -8.68% as of 2026-06-30

## Risk read-through

Latest issuer ETF finder 10-year average annual NAV TR อยู่ที่ `8.38%` ณ
2026-07-31; detailed product table ณ 2026-06-30 แสดง `8.50%`. INCO กระจุกใน
India consumer theme; issuerระบุว่า Indxx India Consumer Index เป็น maximum
30-stock, free-float-adjusted, market-cap-weighted index. Latest verified NAV
`US$60.84`, market price `US$61.37`, premium `+0.87%`, และ median bid-ask
spread `0.18%` ณ 2026-07-28. Portfolio characteristics ณ 2026-06-30 มี
P/E `19.68x`, P/B `6.44x`, และ sector weights Consumer Discretionary `64.28%`
กับ Consumer Staples `35.72%`. Net expense ratio `0.75%`, gross expense ratio
`0.76%` จาก Q2 factsheet; fee-waiver terms are kept as a dated source caveat.
Annual-return population standard deviation จาก rounded 2021-2025 rows อยู่ที่
14.59% เป็น calculation ไม่ใช่ issuer 3-year volatility. Daily NAV history
สำหรับ max drawdown และ recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official Columbia Threadneedle product/performance page:
  https://www.columbiathreadneedleus.com/investment-products/mutual-funds/columbia-india-consumer-etf/class-/details?cusip=19762B707
- Official Columbia India Consumer ETF factsheet:
  https://www.columbiathreadneedleus.com/binaries/content/assets/cti/public/columbia_india_consumer_etf_fs.pdf
- Official S&P 500 index page:
  https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-29]]
