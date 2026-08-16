---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:XSMO
ticker: XSMO
exchange: NYSE Arca
fund: Invesco S&P SmallCap Momentum ETF
tracked_index: S&P SmallCap 600 Momentum Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-07-27
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/XSMO
  - geography/United-States
---

# XSMO Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

XSMO เป็น Invesco S&P SmallCap Momentum ETF แบบ passive/index-tracking ที่
ติดตาม S&P SmallCap 600 Momentum Index บน NYSE Arca. Official 2016-2025 NAV
Total Return ให้ cumulative `217.50%` และ rounded-input CAGR `12.25%`; ใน
common 2021-2025 window ให้ CAGR `9.59%` ต่ำกว่า S&P 500 Total Return `14.43%`.
Current YTD ที่พบเป็น secondary NAV return `30.50%` ณ 2026-06-30; official
current YTD ที่ใหม่กว่านี้ไม่พบในเอกสาร issuer ที่อ่านได้ จึงไม่ผสมกับ annual
table.

## Performance check

- entity_key: `NYSE Arca:XSMO`
- Inception: 2005-03-03
- Expense ratio: 0.36% (management fee 0.29% + other expenses 0.07%)
- Metric: `NAV Total Return` รวม reinvested dividends/distributions และ fund expenses; USD
- Tracked index (issuer benchmark): S&P SmallCap 600 Momentum Index
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR: issuer-reported average annual `12.25%` ณ 2025-12-31; raw rolling endpoints ไม่ได้เปิดเผย
- Common calendar window: official complete 2016-2025; cumulative `217.50%` / rounded-input CAGR `12.25%`
- 2021-2025 cumulative `58.05%` / CAGR `9.59%`; S&P 500 cached 2021-2025 cumulative `96.17%` / CAGR `14.43%`
- Coverage/source note: official issuer annual NAV rows cover 2016-2025. Current YTD `30.50%` เป็น secondary NAV return ณ 2026-06-30; อีกแหล่ง secondary ให้ตัวเลขและ as-of ต่างกัน จึงไม่ใช้ปนในตารางหลัก.

| Year | XSMO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.17% | 11.96% |
| 2017 | 23.42% | 21.83% |
| 2018 | -2.88% | -4.38% |
| 2019 | 28.35% | 31.49% |
| 2020 | 21.84% | 18.40% |
| 2021 | 19.28% | 28.71% |
| 2022 | -15.48% | -18.11% |
| 2023 | 21.43% | 26.29% |
| 2024 | 17.57% | 25.02% |
| 2025 | 9.81% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ XSMO;
annual rows ใช้ cached USD Total Return convention ณ 2025-12-31. ตัวเลข
cumulative/CAGR เป็น rounded-input calculations จาก annual observations.

## Up years / Down years

- Up years / Down years: 8 / 2 in the complete 2016-2025 window
- Best: 2019, +28.35%
- Least positive: 2016, +7.17%
- Worst: 2022, -15.48%
- Least bad down year: 2018, -2.88%
- Current XSMO NAV TR YTD: +30.50% as of 2026-06-30, secondary source

## Risk read-through

XSMO มี small-cap และ momentum exposure จึงมี momentum-cycle, valuation,
turnover, volatility และ liquidity risk. SEC summary prospectus ระบุ best
quarter `+23.72%` ใน 2Q2020 และ worst quarter `-25.15%` ใน 1Q2020. ประวัติ
tracked index มี methodology/benchmark predecessor หลายช่วงก่อน 2019; ตั้งแต่
2019-06-21 จึงเป็น S&P SmallCap 600 Momentum Index ตามเอกสาร issuer. Official
daily NAV history สำหรับคำนวณ max drawdown และ recovery ยังไม่พบข้อมูลที่ยืนยันได้.

## Sources

- [Official Invesco XSMO fact sheet](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/xsmo-invesco-s-p-smallcap-momentum-etf-fact-sheet.pdf)
- [Official Invesco XSMO product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-sp-smallcap-momentum-etf.html)
- [SEC XSMO summary prospectus](https://www.sec.gov/Archives/edgar/data/1209466/000119312525190429/d56632d497k.htm)
- [Schwab XSMO performance snapshot](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=xsmo) (secondary current NAV/YTD context)
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- [S&P 500 historical reference](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true)
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
