---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:SFLO
ticker: SFLO
exchange: NASDAQ
fund: VictoryShares Small Cap Free Cash Flow ETF
tracked_index: Victory U.S. Small Cap Free Cash Flow Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: "not disclosed"
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/SFLO
  - geography/United-States
---

# SFLO Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

SFLO เป็น passive/index-tracking U.S. small-cap free-cash-flow/value-factor
equity ETF ที่ติดตาม Victory U.S. Small Cap Free Cash Flow Index. Official NAV
Total Return ล่าสุดที่ตรวจสอบได้คือ `16.54%` YTD และ `31.73%` สำหรับ 1-year ณ
2026-06-30; issuer factsheet รายงาน since-inception annualized NAV TR `14.48%`.
กองทุนเริ่มปลายปี 2023 จึงยังไม่มี 10-year หรือ 2021-2025 CAGR และ issuer
materials ที่ตรวจสอบเปิดเผย calendar-year NAV row เพียงปี 2024 ที่ `6.49%`.

## Performance check

- entity_key: `NASDAQ:SFLO`
- Inception: `2023-12-20` ใน official factsheet; SEC summary prospectus และ Victory ETF lineup ระบุ `2023-12-21` — conflict นี้เก็บไว้แยกตาม source
- Primary listing: Nasdaq Stock Market LLC
- Expense ratio: gross `0.56%`, net `0.49%` (contractual waiver through 2026-10-31; factsheet as of 2026-06-30)
- Metric: `NAV Total Return` รวม dividends/capital gains ที่ reinvested และ fund expenses ตาม issuer convention; USD
- Tracked index (issuer benchmark): Victory U.S. Small Cap Free Cash Flow Index
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR CAGR: not applicable (<10-year fund history)
- Available official calendar row: 2024 NAV TR `6.49%` (SEC summary prospectus, period ended 2024-12-31); 2023 inception-year partial is excluded and 2025 calendar row is not disclosed in the reviewed official capture
- Available rolling/period NAV TR: QTD `14.24%`, YTD `16.54%`, 1-year `31.73%`, and since-inception annualized `14.48%`, all as of 2026-06-30
- 2021-2025 CAGR: not applicable because the fund started in December 2023 and complete calendar rows are unavailable
- Current official NAV TR YTD: `16.54%` as of 2026-06-30; official closing market-price return `16.47%` and issuer-index return `16.95%` on the same factsheet are kept separate
- Coverage/source note: S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; no synchronized current-year benchmark comparison is asserted against SFLO's 2026-06-30 YTD.

| Year | SFLO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | 11.96% |
| 2017 | not disclosed | 21.83% |
| 2018 | not disclosed | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | not disclosed | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | 6.49% | 25.02% |
| 2025 | not disclosed | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ SFLO;
2023 เป็น inception-year partial และไม่ถูกนำไปจัดอันดับ. ไม่ได้ใช้ index
return `16.95%` แทน fund NAV TR `16.54%`.

## Up years / Down years

- Up years / Down years: not disclosed because only one complete official calendar-year NAV row was available
- Best: not disclosed
- Least positive: not disclosed
- Worst: not disclosed
- Least bad down year: not disclosed
- Current SFLO NAV TR YTD: +16.54% as of 2026-06-30
- Current NAV / market price: ไม่พบข้อมูลที่ยืนยันได้จาก official source batch ที่อ่านได้

## Risk read-through

SFLO คัดเลือก U.S. small-cap companies ที่มี profitability, high free-cash-flow
yield และ favorable growth ผ่าน rules-based index ที่ rebalances/reconstitutes
quarterly; factsheet ระบุ 202 holdings ณ 2026-06-30. ความเสี่ยงหลักคือ
small-cap volatility, value/FCF factor regime, sector concentration, liquidity
และความไม่แน่นอนของ forward cash-flow estimates. Official factsheet ไม่ได้
เปิดเผย standard deviation, Sharpe ratio, beta หรือ daily NAV history ใน
capture ที่ตรวจสอบ จึงยังไม่สร้างตัวเลข volatility, max drawdown หรือ recovery
proxy เพิ่ม.

## Sources

- [Official Victory SFLO product page](https://advisor.vcm.com/products/victoryshares-etfs/victoryshares-etfs-list/victoryshares-small-cap-free-cash-flow-etf)
- [Official Victory SFLO factsheet, June 30 2026](https://www.vcm.com/assets/etf/factsheet-pdf/VS%20SFLO%20FS.pdf)
- [Official SEC SFLO summary prospectus, November 1 2025](https://www.sec.gov/Archives/edgar/data/1547580/000119312525260722/f43139d1.htm)
- [Official Victory Capital SFLO launch announcement](https://ir.vcm.com/news/news-details/2023/Victory-Capital-Adds-VictoryShares-Small-Cap-Free-Cash-Flow-ETF-to-its-ETF-Lineup/default.aspx)
- [Official Victory U.S. Small Cap Free Cash Flow Index page](https://www.vettafi.com/indexing/index/sflo)
- [S&P 500 index definition and cached historical reference](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
