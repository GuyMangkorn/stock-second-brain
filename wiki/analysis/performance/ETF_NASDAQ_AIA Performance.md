---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:AIA
ticker: AIA
exchange: NASDAQ
fund: iShares Asia 50 ETF
tracked_index: S&P Asia 50 Capped Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-21
price_nav_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/AIA
  - geography/Asia-ex-Japan
---

# AIA Performance

> Navigation: [[ETF Region Index]] → [[Asia ex Japan ETF]] → [[ETF Performance Index]]

## Bottom line

AIA เป็น passive/index-tracking equity ETF ของ iShares ที่ติดตาม S&P Asia 50
Capped Index (Net) และจดทะเบียนบน NASDAQ. Official rolling 10-year NAV Total
Return ณ 2026-06-30 อยู่ที่ cumulative 298.99% และ CAGR 14.84%; latest current
date-to-date NAV Total Return YTD อยู่ที่ 40.47% ณ 2026-07-21. ตัวเลขหลักเป็น
NAV Total Return ที่รวมการ reinvest distributions และหัก fund expenses ตาม
วิธีคำนวณของ issuer.

## Performance check

- entity_key: NASDAQ:AIA
- Inception: 2007-11-13
- Expense ratio: 0.50%
- Metric: NAV Total Return รวม reinvested distributions และ fund expenses
- Tracked index (issuer benchmark): S&P Asia 50 Capped Index (Net)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year coverage: official rolling performance from 2016-06-30 to 2026-06-30; actual years 10.00
- Start TR value: 100.00 normalized; End TR value: 398.99 normalized, derived from official cumulative return 298.99%; raw NAV endpoints are not disclosed
- 10-year NAV TR CAGR: 14.84% issuer-reported average annual NAV Total Return
- Formula: (End TR / Start TR)^(1 / Years) - 1 = (398.99 / 100.00)^(1 / 10.00) - 1 = approximately 14.84%
- Coverage/source note: official page provides rolling 10-year cumulative/average annual returns as of 2026-06-30 and calendar rows 2021-2025. The normalized endpoint is derived from the rounded official cumulative metric, not a proxy or market-price return.

| Year | AIA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | -10.75% | 28.71% |
| 2022 | -24.07% | -18.11% |
| 2023 | 4.84% | 26.29% |
| 2024 | 20.42% | 25.02% |
| 2025 | 47.01% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ AIA;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31. ช่วง annual
comparison ที่เปิดเผยตรงกันคือ 2021-2025.

## Up years / Down years

- Up years / Down years: 3 / 2 ใน complete rows ที่ issuer เปิดเผย
- Best: 2025, +47.01%
- Least positive: 2023, +4.84%
- Worst: 2022, -24.07%
- Least bad down year: 2021, -10.75%
- 2021-2025 cumulative / CAGR: 25.77% / 4.69%; S&P 500 TR: 96.17% / 14.43%
- Current date-to-date YTD: 40.47% NAV as of 2026-07-21
- Standardized month-end YTD: 46.79% NAV as of 2026-06-30; kept separate from the later date-to-date observation

## Risk read-through

AIA กระจุกตัวใน Asia ex Japan large-cap equity โดย official exposure ณ
2026-07-21 อยู่ที่ Taiwan 37.23%, South Korea 26.21% และ China 25.48%;
Information Technology เป็น sector ใหญ่สุดที่ 56.39%. ความเสี่ยงหลักจึงเป็น
country, semiconductor/technology concentration และ FX. Daily NAV history
สำหรับคำนวณ max drawdown และ recovery: ไม่พบข้อมูลที่ยืนยันได้.

## Sources

- Official iShares product and performance page: https://www.ishares.com/us/products/239730/ishares-asia-50-etf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-23]] | [[ETF Performance Index]]
