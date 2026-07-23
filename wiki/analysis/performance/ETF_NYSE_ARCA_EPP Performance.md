---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EPP
ticker: EPP
exchange: NYSE Arca
fund: iShares MSCI Pacific ex Japan ETF
tracked_index: MSCI Pacific ex Japan Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-23
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/EPP
  - geography/Asia-Pacific
---

# EPP Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

EPP เป็น passive/index-tracking equity ETF ที่ติดตาม developed-market equities ใน
Pacific region โดยไม่รวม Japan. Official NAV Total Return ครบ rolling 10 ปี
2016-06-30 ถึง 2026-06-30 ให้ cumulative return 103.63% และ CAGR 7.37%;
complete calendar rows มีปีบวก 8 ปีและปีลบ 2 ปี. Current NAV YTD อยู่ที่
11.23% ณ 2026-07-21.

## Performance check

- entity_key: NYSE Arca:EPP
- Inception: 2001-10-25
- Metric: NAV Total Return รวม gross income ที่ reinvested where applicable และ fund expenses
- Tracked index (issuer benchmark): MSCI Pacific ex Japan Index (Net)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year window: 2016-06-30 to 2026-06-30
- 10-year NAV TR CAGR: 7.37%; start TR value 100.00 and end TR value 203.63 เป็น normalized levels จาก official cumulative return; actual years 10.00
- Formula: (End TR / Start TR)^(1 / Years) - 1 = (203.63 / 100.00)^(1 / 10.00) - 1 = 7.37%
- Calendar-row calculation: rounded official rows 2016-2025 compound to 94.42% and CAGR 6.87%; rows 2021-2025 compound to 29.35% and CAGR 5.28%
- Coverage/source note: official calendar table displays 2016-2020 at one decimal; 2021-2025 are available at two decimals in the current issuer rendering. Raw NAV endpoint levels are not disclosed.

| Year | EPP NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.40% | 11.96% |
| 2017 | 25.40% | 21.83% |
| 2018 | -10.70% | -4.38% |
| 2019 | 17.90% | 31.49% |
| 2020 | 6.00% | 18.40% |
| 2021 | 4.42% | 28.71% |
| 2022 | -6.45% | -18.11% |
| 2023 | 5.92% | 26.29% |
| 2024 | 4.04% | 25.02% |
| 2025 | 20.16% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ EPP;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31.

## Up years / Down years

- Up years / Down years: 8 / 2
- Best: 2017, +25.40%
- Least positive: 2024, +4.04%
- Worst: 2018, -10.70%
- Least bad down year: 2022, -6.45%
- Current YTD: +11.23% as of 2026-07-21

## Risk read-through

Rolling 10-year NAV TR CAGR อยู่ที่ 7.37% ต่ำกว่า S&P 500 common reference
อย่างชัดเจนในช่วงเดียวกัน. EPP มี 3-year standard deviation 14.53% ณ
2026-06-30 และ 93 holdings ณ 2026-07-22; exposure กระจุกใน Australia
63.05%, Hong Kong 17.59% และ Singapore 17.39%, โดย sector Financials
45.74% และ Materials 15.16%. Expense ratio 0.47%. Daily NAV history สำหรับ
การคำนวณ max drawdown และ recovery: not disclosed.

## Sources

- Official issuer product and performance page:
  https://www.ishares.com/us/products/239674/ishares-msci-pacific-ex-japan-etf
- Official S&P 500 index page:
  https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-23]]
