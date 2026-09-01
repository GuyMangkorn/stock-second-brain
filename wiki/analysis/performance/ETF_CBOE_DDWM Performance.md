---
type: etf-performance
entity_key: Cboe BZX:DDWM
updated: 2026-09-01
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - geography/International
---

# DDWM Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DDWM ให้ผลตอบแทน NAV Total Return `9.70%` ตั้งแต่ต้นปีถึง 31 ก.ค. 2026 และให้ rolling 10-year annualized NAV TR `10.41%` ถึงวันเดียวกัน. ช่วง 2016-2025 มี 8 ปีบวกและ 2 ปีลบ; CAGR จาก annual rows อยู่ที่ `10.10%` เทียบ S&P 500 TR `14.82%`.

## Performance check

- `entity_key: Cboe BZX:DDWM`
- Fund: WisdomTree Dynamic International Equity Fund
- Inception: `2016-01-07`; expense ratio: `0.40%` (official product page as of 2026-08-31)
- Metric: `NAV Total Return` รวม distributions reinvested และ fund expenses
- Issuer benchmark: WisdomTree Dynamic International Equity Index
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested)
- 10-year NAV TR CAGR: `10.41%` as of `2026-07-31` (official rolling issuer figure; raw endpoints not disclosed)
- Latest official NAV: `$47.511` as of `2026-08-31`; closing market price: `$47.534` as of `2026-08-28` (market price kept separate)
- Current YTD: `9.70%` as of `2026-07-31`; latest month-end official NAV TR field available in the reviewed issuer capture
- Coverage/source note: official annual NAV TR rows 2016-2025; calculated CAGRs use displayed rounded rows. Source batch: [[ETF_performance_sources_2026-09-01_run-4]]

- Annual NAV TR coverage: official 2016-2025 NAV TR

| ปี | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 14.18% | 11.96% |
| 2017 | 18.52% | 21.83% |
| 2018 | -11.05% | -4.38% |
| 2019 | 21.03% | 31.49% |
| 2020 | -4.20% | 18.40% |
| 2021 | 14.33% | 28.71% |
| 2022 | -1.27% | -18.11% |
| 2023 | 15.44% | 26.29% |
| 2024 | 10.65% | 25.02% |
| 2025 | 30.10% | 17.88% |

**Up years / Down years**

- Best: `2025 +30.10%`; least positive: `2024 +10.65%`
- Worst: `2018 -11.05%`; least bad down year: `2022 -1.27%`
- Current YTD: `9.70%` as of `2026-07-31`

## Risk read-through

Annual-path population standard deviationอยู่ที่ `11.96%` จากแถว 2016-2025; official 10-year annualized volatility อยู่ที่ `12.41%` as of `2026-03-31`. DDWM เป็น `passive-index` แบบ rules-based international dividend equity ที่มี dynamic FX hedge; aggregate hedge ratio อยู่ที่ `83.67%` as of `2026-08-31`. การกระจายประเทศและ sector ยังคงทำให้ผลลัพธ์ไวต่อ FX, financials และ international equity risk; daily NAV max drawdown และ exact recovery date ไม่ได้เปิดเผยในข้อมูลที่ตรวจสอบ. ตัวเลขเป็น index construction และ tracking หลังหัก fund expenses ไม่ใช่หลักฐานของ discretionary stock-picking skill.

## Sources

- [Official WisdomTree product/performance source](https://www.wisdomtree.com/us/products/equity/ddwm)
- [Official WisdomTree DDWM presentation](https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/presentations/equity/ddwm_presentation.pdf)
- [Official WisdomTree Dynamic International Equity Index](https://www.wisdomtree.com/us/indexes/WTDFAHD)
- S&P 500 TR cached 2016-2025 convention and full source map: [[ETF_performance_sources_2026-09-01_run-4]]
