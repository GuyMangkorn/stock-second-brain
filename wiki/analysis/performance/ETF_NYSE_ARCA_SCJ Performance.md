---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:SCJ
ticker: SCJ
exchange: NYSE Arca
fund: iShares MSCI Japan Small-Cap ETF
tracked_index: MSCI Japan Small Cap Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-21
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/SCJ
  - geography/Japan
---

# SCJ Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

SCJ เป็น passive/index-tracking Japan small-cap equity ETF ของ iShares ที่
ติดตาม MSCI Japan Small Cap Index (Net). Official rolling NAV Total Return
10 ปี ณ 2026-06-30 อยู่ที่ cumulative `119.60%` และ CAGR `8.18%` จาก
normalized TR 100.00 เป็น 219.60 ใน 10.00 ปี. Official calendar NAV TR rows
2016-2025 compound ได้ `92.14%` หรือ CAGR `6.75%`; common window 2021-2025
ได้ CAGR `5.20%` เทียบกับ S&P 500 TR `14.43%`. Current NAV TR YTD ล่าสุดที่
ยืนยันได้จาก iShares คือ `16.10%` ณ 2026-07-21.

## Performance check

- entity_key: NYSE Arca:SCJ
- Inception: 2007-12-20
- Metric: NAV Total Return รวม reinvested dividends/capital-gains distributions และ fund expenses
- Tracked index (issuer benchmark): MSCI Japan Small Cap Index (Net)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year window: 2016-06-30 to 2026-06-30
- 10-year NAV TR CAGR: 8.18%; start TR value 100.00 and end TR value 219.60 เป็น normalized levels จาก official cumulative return; actual years 10.00
- Formula: (219.60 / 100.00)^(1 / 10.00) - 1 = 8.18%
- Calendar-row calculation: official rows 2016-2025 compound to 92.14% and CAGR 6.75%; precise official 2021-2025 rows compound to 28.85% and CAGR 5.20%
- Coverage/source note: rolling return is as of 2026-06-30; annual rows are as of 2025-12-31; current YTD is as of 2026-07-21. Raw NAV endpoint levels are not disclosed.

| Year | SCJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.60% | 11.96% |
| 2017 | 30.90% | 21.83% |
| 2018 | -16.40% | -4.38% |
| 2019 | 19.00% | 31.49% |
| 2020 | 6.30% | 18.40% |
| 2021 | -2.40% | 28.71% |
| 2022 | -12.70% | -18.11% |
| 2023 | 12.95% | 26.29% |
| 2024 | 3.26% | 25.02% |
| 2025 | 29.66% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ SCJ;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31.

## Up years / Down years

- Up years / Down years: 7 / 3
- Best: 2017, +30.90%
- Least positive: 2024, +3.26%
- Worst: 2018, -16.40%
- Least bad down year: 2021, -2.40%
- Current YTD: +16.10% as of 2026-07-21

## Risk read-through

SCJ เป็น small-cap Japan equity exposure จึงมีความเสี่ยงด้าน liquidity,
country, currency และ small-cap volatility. Expense ratio อยู่ที่ 0.50%,
787 holdings และ 3-year standard deviation 14.09% ณ 2026-06-30. Daily NAV
history สำหรับการคำนวณ max drawdown และ recovery: ไม่พบข้อมูลที่ยืนยันได้ใน
lean capture.

## Sources

- Official issuer U.S. product and performance page:
  https://www.ishares.com/us/products/239666/ishares-msci-japan-smallcap-etf
- Official issuer performance view with 2016-2025 rows and current observations:
  https://www.ishares.com/uk/professional/en/products/239666/ishares-msci-japan-smallcap-etf?siteEntryPassthrough=true&switchLocale=y
- Official issuer factsheet:
  https://www.ishares.com/us/literature/fact-sheet/scj-ishares-msci-japan-small-cap-etf-fund-fact-sheet-en-us.pdf
- Official S&P 500 index page:
  https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
