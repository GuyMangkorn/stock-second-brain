---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:GMF
ticker: GMF
exchange: NYSE Arca
issuer: State Street Investment Management
fund: State Street SPDR S&P Emerging Asia Pacific ETF
tracked_index: S&P Emerging Asia Pacific BMI Index
benchmark: S&P 500 Total Return
inception: 2007-03-20
expense_ratio: 0.49% gross
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/GMF
  - geography/Asia-Pacific
---

# GMF Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

GMF เป็น passive/index-sampling equity ETF ที่ให้ broad exposure ต่อ emerging Asia-Pacific และติดตาม `S&P Emerging Asia Pacific BMI Index`. Official standardized NAV Total Return รวม reinvested distributions และหัก fund expenses ให้ 10-year average annual return `9.94%` ณ 2026-06-30; จาก official daily NAV และ distribution workbooks คำนวณเป็น cumulative `158.00%`. ช่วง 2021-2025 ให้ CAGR `4.20%` เทียบกับ S&P 500 Total Return `14.43%`; latest official YTD คือ `12.56%` ณ 2026-06-30.

## Performance check

- `entity_key`: `NYSE Arca:GMF`; State Street ยืนยัน listing เป็น NYSE Arca, ticker `GMF`, asset class Equity, inception `2007-03-20` และ benchmark `S&P Emerging Asia Pacific BMI Index`.
- `Metric`: official NAV Total Return in USD; State Street ระบุว่า results assume reinvestment of dividends/capital gains และ performance แสดง net of fees. ไม่ผสมกับ market-price return.
- `Expense ratio`: gross `0.49%`; net expense ratio/waiver `ไม่พบข้อมูลที่ยืนยันได้`.
- `Current NAV`: `US$152.77` ณ 2026-07-22; latest standardized NAV TR YTD `12.56%` ณ 2026-06-30.
- `10-year NAV TR`: issuer-published NAV average annual return `9.94%` ณ 2026-06-30; raw workbooks reproduce `9.94%` after distribution reinvestment.

### 10-year NAV TR window

| Field | Value |
|---|---:|
| Start date | 2016-06-30 |
| End date | 2026-06-30 |
| Start NAV input | 74.630855 |
| End NAV input | 156.481539 |
| Start TR value | 100.00 (normalized index) |
| End TR value | 258.0033 (normalized NAV TR index) |
| Actual years | 10.00 calendar years / 3,652 days |
| Cumulative NAV TR | 158.00% (calculated from official workbooks) |
| CAGR | 9.94% |

Calculation: start with one share at the 2016-06-30 NAV, reinvest each official distribution using the payable-date NAV, then value the accumulated shares at the 2026-06-30 NAV. Formula: `(258.0033 / 100.00)^(1 / 10.00) - 1 = 9.94%`. This calculation convention reproduces State Street's published 10-year NAV return and June 2026 YTD to two decimals; the normalized TR index is not a separate issuer-published NAV series.

### Calendar-year NAV TR vs S&P 500 Total Return

Annual GMF rows are calculated from State Street's official daily NAV history and official distribution workbook; they are not a secondary price proxy. S&P 500 rows reuse the cached USD Total Return convention for complete calendar years 2021-2025.

| Year | GMF NAV TR (USD) | S&P 500 TR (USD) |
|---|---:|---:|
| 2021 | -1.49% | 28.71% |
| 2022 | -19.00% | -18.11% |
| 2023 | 7.88% | 26.29% |
| 2024 | 17.01% | 25.02% |
| 2025 | 21.94% | 17.88% |

จาก unrounded official inputs GMF มี cumulative `22.83%` และ CAGR `4.20%` ใน 2021-2025 เทียบกับ S&P 500 TR cumulative `96.17%` และ CAGR `14.43%`; GMF ต่ำกว่าประมาณ `10.23 pp` ต่อปีในช่วง common window นี้. ตารางแสดง annual rows ที่ปัดเป็นสองทศนิยม จึงอาจ compound ได้ `22.82%` เมื่อคำนวณจากค่าที่ปัดแล้ว.

## Up years / Down years

- Up years / Down years: `3 / 2`
- Best: `2025`, `21.94%`
- Least positive: `2023`, `7.88%`
- Worst: `2022`, `-19.00%`
- Least bad down year: `2021`, `-1.49%`
- Latest official YTD: `12.56%` as of 2026-06-30; current NAV `US$152.77` as of 2026-07-22.

## Risk read-through

GMF กระจายหลายประเทศแต่ยังมี emerging-market และ FX risk: country weights ณ 2026-06-30 คือ Taiwan `40.81%`, China `32.12%`, India `20.15%`; sector weights หลักคือ Information Technology `40.49%`, Financials `16.65%` และ Consumer Discretionary `9.81%`. มี 1,281 holdings ณ 2026-07-21. Official volatility/beta metrics ใน compact State Street capture เป็น `ไม่พบข้อมูลที่ยืนยันได้`; ความเสี่ยงหลักจึงอยู่ที่ประเทศ/ค่าเงิน/technology และ liquidity ของ emerging markets.

## Sources

- [State Street GMF product and performance page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-emerging-asia-pacific-etf-gmf) — identity, NYSE Arca listing, benchmark, inception, NAV, fee, standardized NAV TR and portfolio snapshot; accessed 2026-07-24.
- [State Street GMF factsheet, June 2026](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-gmf.pdf) — NAV TR definition, fee, holdings and country/sector weights; as of 2026-06-30.
- [Official GMF NAV history workbook](https://www.ssga.com/library-content/products/fund-data/etfs/us/navhist-us-en-gmf.xlsx) and [official historical distributions workbook](https://www.ssga.com/library-content/products/fund-data/etfs/us/spdr-etf-historical-distributions.xlsx) — daily NAV and distribution inputs for the calculated annual/10-year NAV TR rows; downloaded 2026-07-24.
- [S&P 500 Total Return reference](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common USD total-return benchmark convention.
- [[ETF_performance_sources_2026-07-23]] | [[ETF Performance Index]]
