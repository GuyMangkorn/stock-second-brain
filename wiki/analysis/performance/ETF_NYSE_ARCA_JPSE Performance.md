---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:JPSE
ticker: JPSE
exchange: NYSE Arca
fund: JPMorgan Diversified Return U.S. Small Cap Equity ETF
tracked_index: JP Morgan Diversified Factor US Small Cap Equity Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
price_nav_as_of: "not disclosed"
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/JPSE
  - geography/United-States
---

# JPSE Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

JPSE เป็น passive/index-tracking U.S. small-cap ETF ที่ติดตาม JP Morgan
Diversified Factor US Small Cap Equity Index ผ่าน rules-based risk allocation
และ value/quality/momentum factors. Official NAV Total Return สำหรับ complete
calendar years 2017-2025 ให้ cumulative `118.79%` และ rounded-input CAGR `9.09%`;
ใน common 2021-2025 window ให้ CAGR `8.55%` ต่ำกว่า S&P 500 Total Return `14.43%`.
Current NAV TR YTD อยู่ที่ `20.41%` ณ 2026-06-30. ปี 2016 ไม่ถูกนำมาคำนวณเพราะ
กองทุนเริ่ม 2016-11-15 และ issuer แสดงเพียง partial inception-year history.

## Performance check

- entity_key: `NYSE Arca:JPSE`
- Inception: 2016-11-15
- Expense ratio: 0.29% (gross and net, as of 2026-06-30; prospectus dated 2026-03-01 also states 0.29%)
- Metric: `NAV Total Return` รวม dividends/capital gains ตาม issuer convention และ fund expenses; USD
- Tracked index (issuer benchmark): JP Morgan Diversified Factor US Small Cap Equity Index
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- Available calendar window: 2017-01-01 to 2025-12-31 (nine complete calendar years); 2016 partial inception-year row excluded
- Available-window NAV TR: cumulative `118.79%`; rounded-input CAGR `9.09%`; normalized start TR value `100.00`, end TR value `218.79`, years `9.00`
- Issuer launch-to-date average annual NAV TR: `11.09%` as of 2026-06-30; this is kept separate from the 2017-2025 calendar CAGR
- Common calendar window: 2021-2025 cumulative `50.73%` / CAGR `8.55%`; S&P 500 cached cumulative `96.17%` / CAGR `14.43%`
- Current official NAV TR YTD: `20.41%` as of 2026-06-30; market-price return `20.71%` on the same factsheet

| Year | JPSE NAV TR | S&P 500 TR |
|---|---:|---:|
| 2017 | 14.38% | 21.83% |
| 2018 | -8.14% | -4.38% |
| 2019 | 22.67% | 31.49% |
| 2020 | 12.62% | 18.40% |
| 2021 | 29.14% | 28.71% |
| 2022 | -14.42% | -18.11% |
| 2023 | 15.77% | 26.29% |
| 2024 | 8.13% | 25.02% |
| 2025 | 8.95% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ JPSE;
annual rows ใช้ cached USD Total Return convention ณ 2025-12-31. Cumulative
returns และ CAGRs เป็น rounded-input calculations จาก official JPMorgan annual
NAV observations. ไม่มีการเติม 2016 partial return เพื่อสร้างหน้าต่าง 10 ปี.

## Up years / Down years

- Up years / Down years: 7 / 2 in the complete 2017-2025 window
- Best: 2021, +29.14%
- Least positive: 2024, +8.13%
- Worst: 2022, -14.42%
- Least bad down year: 2018, -8.14%
- Current JPSE NAV TR YTD: +20.41% as of 2026-06-30
- Current NAV / market price: ไม่พบข้อมูลที่ยืนยันได้จาก official source batch ที่อ่านได้

## Risk read-through

JPSE มี annual-return volatility แบบ population standard deviation `12.98%`
จาก official 2017-2025 rows ที่ปัดเศษ. Rules-based value/quality/momentum
selection และ sector-risk balancing ทำให้ exposure ต่างจาก Russell 2000 แบบ
market-cap-weighted แต่ยังมี small-cap, factor-regime, cyclicality, liquidity
และ valuation risk. Factsheet รายงาน 3-year monthly standard deviation `17.63%`
ณ 2026-06-30. Official daily NAV history สำหรับคำนวณ max drawdown และ recovery
ยังไม่พบข้อมูลที่ยืนยันได้ จึงไม่สร้างตัวเลข proxy เพิ่ม.

## Sources

- [Official JPMorgan JPSE factsheet, June 30 2026](https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-JPSE.PDF)
- [Official SEC JPSE summary prospectus, March 1 2026](https://www.sec.gov/Archives/edgar/data/1485894/000119312526071849/d58277d497k.htm)
- [Official SEC JPSE annual shareholder report, October 31 2025](https://www.sec.gov/Archives/edgar/data/1485894/000119312525336832/d43117dncsr.htm)
- [S&P 500 index definition and cached historical reference](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
