---
type: etf-performance
instrument_type: ETF
entity_key: LSE:CPXJ
ticker: ISMJF
exchange: LSE
fund: iShares Core MSCI Pacific ex-Japan UCITS ETF
tracked_index: MSCI Pacific ex Japan Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-08
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/ISMJF
  - geography/Asia-Pacific
---

# ISMJF Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

ISMJF เป็น OTC alias ของ iShares Core MSCI Pacific ex-Japan UCITS ETF ซึ่งมี
canonical listing เป็น `LSE:CPXJ`. กองเป็น passive, physically replicated,
index-tracking equity ETF ที่ติดตาม MSCI Pacific ex Japan Index (Net). Official
rolling NAV Total Return 10 ปี ณ 2026-06-30 อยู่ที่ cumulative `108.94%` และ
CAGR `7.65%` จาก normalized TR 100.00 เป็น 208.94 ใน 10.00 ปี. Official
calendar NAV TR rows 2016-2025 compound ได้ `100.75%` หรือ CAGR `7.22%`;
common window 2021-2025 ได้ CAGR `5.63%` เทียบกับ S&P 500 TR `14.43%`.
Current NAV TR YTD ล่าสุดที่ยืนยันได้คือ `8.15%` ณ 2026-07-08.

## Performance check

- input ticker: ISMJF
- entity_key: LSE:CPXJ
- Inception: 2010-01-12
- Metric: NAV Total Return with gross income reinvested where applicable; NAV performance is kept separate from market price
- Tracked index (issuer benchmark): MSCI Pacific ex Japan Index (Net)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year window: 2016-06-30 to 2026-06-30
- 10-year NAV TR CAGR: 7.65%; start TR value 100.00 and end TR value 208.94 เป็น normalized levels จาก official cumulative return; actual years 10.00
- Formula: (208.94 / 100.00)^(1 / 10.00) - 1 = 7.65%
- Calendar-row calculation: official rows 2016-2025 compound to 100.75% and CAGR 7.22%; rows 2021-2025 compound to 31.49% and CAGR 5.63%
- Coverage/source note: rolling return is as of 2026-06-30; annual rows are as of 2025-12-31; current YTD is as of 2026-07-08. Raw NAV endpoint levels are not disclosed.

| Year | ISMJF / CPXJ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.70% | 11.96% |
| 2017 | 25.80% | 21.83% |
| 2018 | -10.40% | -4.38% |
| 2019 | 18.20% | 31.49% |
| 2020 | 6.40% | 18.40% |
| 2021 | 4.70% | 28.71% |
| 2022 | -6.10% | -18.11% |
| 2023 | 6.30% | 26.29% |
| 2024 | 4.50% | 25.02% |
| 2025 | 20.40% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ CPXJ;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31.

## Up years / Down years

- Up years / Down years: 8 / 2
- Best: 2017, +25.80%
- Least positive: 2021, +4.70%
- Worst: 2018, -10.40%
- Least bad down year: 2022, -6.10%
- Current YTD: +8.15% as of 2026-07-08

## Risk read-through

CPXJ กระจาย developed Pacific ex-Japan แต่ยังมี Australia, Hong Kong,
Singapore, New Zealand, country, currency และ financials/materials
concentration. Expense ratio อยู่ที่ 0.20%, 93 holdings และ 3-year standard
deviation 15.02% ณ 2026-06-30. Daily NAV history สำหรับ max drawdown และ
recovery: ไม่พบข้อมูลที่ยืนยันได้ใน lean capture.

## Sources

- Official issuer product and performance page:
  https://www.ishares.com/uk/professional/en/products/253735/ishares-core-msci-pacific-ex-japan-ucits-etf?siteEntryPassthrough=true&switchLocale=y
- Official issuer factsheet:
  https://www.ishares.com/nl/professionele-belegger/nl/literature/fact-sheet/cspxj-ishares-core-msci-pacific-ex-japan-ucits-etf-fund-fact-sheet-en-nl.pdf?siteEntryPassthrough=true&switchLocale=y
- Official S&P 500 index page:
  https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
