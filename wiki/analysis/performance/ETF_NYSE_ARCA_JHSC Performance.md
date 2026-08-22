---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:JHSC
ticker: JHSC
exchange: NYSE Arca
fund: John Hancock Multifactor Small Cap ETF
tracked_index: John Hancock Dimensional Small Cap Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: "not disclosed"
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/JHSC
  - geography/United-States
---

# JHSC Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

JHSC เป็น passive/index-tracking U.S. small-cap multifactor equity ETF ที่
ติดตาม John Hancock Dimensional Small Cap Index โดยเน้น smaller cap, lower
relative price และ higher profitability. Official NAV Total Return ล่าสุดที่
ตรวจสอบได้คือ `16.34%` YTD ณ 2026-06-30; rolling 5-year NAV TR annualized คือ
`8.00%` และ since-inception annualized คือ `9.14%`. Issuer capture ที่ตรวจสอบ
ไม่เปิดเผย complete calendar-year NAV rows จึงคำนวณ 2021-2025 CAGR, up/down count
และ best/worst year ไม่ได้โดยไม่เติมข้อมูลที่ไม่ยืนยัน.

## Performance check

- entity_key: `NYSE Arca:JHSC`
- Inception: 2017-11-08
- Expense ratio: gross `0.46%`, net `0.42%` (contractual through 2026-08-31; factsheet as of 2026-06-30)
- Metric: `NAV Total Return` รวม distributions ที่ reinvested และ fund expenses ตาม issuer convention; USD
- Tracked index (issuer benchmark): John Hancock Dimensional Small Cap Index
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR CAGR: not applicable (<10-year fund history)
- Available rolling NAV TR: 1-year `25.93%`, 3-year annualized `14.42%`, 5-year annualized `8.00%`, and since-inception annualized `9.14%`; all as of 2026-06-30
- 2021-2025 CAGR: not disclosed because official calendar-year NAV TR rows were not available
- Current official NAV TR YTD: `16.34%` as of 2026-06-30; official market-price YTD `16.10%` on the same factsheet is kept separate
- Coverage/source note: the official factsheet provides rolling/period returns and a growth-of-$10,000 chart, but not a complete calendar-year NAV table. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; no synchronized current-year benchmark comparison is asserted.

| Year | JHSC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | 11.96% |
| 2017 | not disclosed | 21.83% |
| 2018 | not disclosed | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | not disclosed | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ JHSC;
annual rows ของฝั่ง JHSC ถูกระบุเป็น `not disclosed` ตามเอกสารทางการที่อ่านได้
และไม่มีการใช้ fiscal-year returns จาก annual report แทน calendar-year returns.

## Up years / Down years

- Up years / Down years: not disclosed because official calendar-year NAV rows are not disclosed
- Best: not disclosed
- Least positive: not disclosed
- Worst: not disclosed
- Least bad down year: not disclosed
- Current JHSC NAV TR YTD: +16.34% as of 2026-06-30
- Current NAV / market price: ไม่พบข้อมูลที่ยืนยันได้จาก official source batch ที่อ่านได้

## Risk read-through

JHSC ให้ broad U.S. small-cap exposure ผ่าน rules-based multifactor process ที่
เน้น size, relative price และ profitability. จึงยังมี small-cap, factor-regime,
valuation, cyclicality และ liquidity risk แม้จะกระจายประมาณ 496 holdings ณ
2026-06-30. Official daily NAV history และ complete calendar-year rows สำหรับ
คำนวณ annual-return volatility, max drawdown และ recovery ยังไม่พบข้อมูลที่
ยืนยันได้ จึงไม่สร้างตัวเลข proxy เพิ่ม. Fund expense ratio สุทธิ `0.42%` และ
index reconstitution/rebalance เป็น semiannual ตาม factsheet.

## Sources

- [Official JHSC investor factsheet, June 30 2026](https://www.jhinvestments.com/content/dam/jhi-investments/JHINV/public/ETFs/Documents/FactSheets/InvestorFactSheet/etf-multifactor-small-cap-investor-fact-sheet-jhi.pdf)
- [Official JHSC SEC summary prospectus, September 1 2025](https://www.sec.gov/Archives/edgar/data/1478482/000119312525191975/d942427d497k.htm)
- [Official JHSC statutory prospectus](https://www.jhinvestments.com/content/dam/jhi-investments/JHINV/public/ETFs/Documents/Prospectuses/StatutoryProspectus/etf-multifactor-small-cap-statutory-prospectus-jhi.pdf)
- [Official John Hancock ETF page](https://www.jhinvestments.com/etf)
- [S&P 500 index definition and cached historical reference](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
