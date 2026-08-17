---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IWO
ticker: IWO
exchange: NYSE Arca
fund: iShares Russell 2000 Growth ETF
tracked_index: Russell 2000 Growth Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-08-13
rolling_10y_as_of: 2026-06-30
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IWO
  - geography/United-States
---

# IWO Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

IWO เป็น passive/index-tracking U.S. small-cap growth equity ETF ที่ติดตาม
Russell 2000 Growth Index. Official complete 2016-2025 NAV Total Return table ที่
เผยแพร่ละเอียด `0.1%` ให้ cumulative `148.84%` หรือ rounded-input CAGR `9.54%`;
เทียบกับ S&P 500 TR `298.33%` / CAGR `14.82%`. ช่วง 2021-2025 IWO compound
`16.56%` หรือ CAGR `3.11%`. Issuer-reported rolling 10-year NAV TR annualized
คือ `11.92%` และ current NAV YTD คือ `21.61%` ณ 13 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:IWO`
- Inception: 24 ก.ค. 2000; expense ratio: `0.24%`
- Metric: `NAV Total Return` รวม reinvested dividends/distributions หลัง fund expenses; currency: USD
- Issuer benchmark: `Russell 2000 Growth Index` (`RU20GRTR`)
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference)
- 10-year calendar-window calculation: official complete-year NAV TR rows from
  2016-2025; cumulative `148.84%`, rounded-input CAGR `9.54%` using
  `(Π(1 + annual TR))^(1 / 10) - 1`.
- Issuer 10-year NAV TR annualized field: `11.92%` ณ 30 มิ.ย. 2026; raw endpoints
  ไม่ได้เปิดเผย จึงแยกจาก calendar-window calculation `9.54%`.
- Current quote: market price `US$395.65`, NAV `US$395.51`, calculated premium
  `0.04%` ณ 14 ส.ค. 2026
- Annual coverage: official complete years 2016-2025, published at `0.1%`
  precision; ไม่มี `*` หรือ `†`.

| ปี | IWO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 11.47% | 11.96% |
| 2017 | 22.24% | 21.83% |
| 2018 | -9.33% | -4.38% |
| 2019 | 28.46% | 31.49% |
| 2020 | 34.52% | 18.40% |
| 2021 | 2.71% | 28.71% |
| 2022 | -26.33% | -18.11% |
| 2023 | 18.58% | 26.29% |
| 2024 | 15.04% | 25.02% |
| 2025 | 12.92% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2020, `+34.52%`; least positive: 2021, `+2.71%`
- Worst: 2022, `-26.33%`; least bad down year: 2018, `-9.33%`
- 2016-2025 cumulative / CAGR: `148.84%` / `9.54%`
- 2021-2025 cumulative / CAGR: `16.56%` / `3.11%`
- Current YTD: IWO NAV `+21.61%` ณ 13 ส.ค. 2026

## Risk read-through

IWO เป็น passive U.S. small-cap growth equity จึงมี growth-valuation, healthcare,
technology, cyclicality และ liquidity sensitivity สูง. Official three-year standard
deviation คือ `21.62%` และ equity beta `1.45` ณ 31 ก.ค. 2026; factsheet ณ 30 มิ.ย.
2026 แสดง standard deviation `21.28%` และ beta `1.43`. Best quarter คือ `+30.58%`
(ไตรมาสสิ้นสุด 30 มิ.ย. 2020) และ worst quarter คือ `-25.79%` (ไตรมาสสิ้นสุด
31 มี.ค. 2020). Expense ratio อยู่ที่ `0.24%`, fund จ่าย distributions รายไตรมาส,
และมี holdings `1,106` ณ 13 ส.ค. 2026. Max drawdown, recovery date และ daily-NAV
history ที่ตรวจสอบได้คือ `ไม่พบข้อมูลที่ยืนยันได้` จาก official sources ที่ reviewed.

## Driver notes

- Confirmed structure: passive index-tracking exposure to the Russell 2000 Growth
  segment; the prospectus describes representative-sampling indexing and no active/options overlay thesis.
- Published-return precision matters: the complete official 2016-2025 table is
  rounded to 0.1%, so cumulative/CAGR outputs are rounded-input calculations.
- Observed regime points: 2020 เป็นปีบวกสูงสุดและ 2022 เป็นปีลบสูงสุดจาก complete
  rows; ไม่ตีความเป็น causal event attribution.

## Sources

- [iShares IWO product page](https://www.ishares.com/us/products/239709/ishares-russell-2000-growth-etf) — official current NAV/price/YTD, issuer 10-year return, benchmark, fee, standard deviation, beta, holdings, and fund facts
- [iShares IWO factsheet](https://www.ishares.com/us/literature/fact-sheet/iwo-ishares-russell-2000-growth-etf-fund-fact-sheet-en-us.pdf) — official 2026-06-30 fund facts and 2021-2025 NAV TR rows
- [iShares summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-russell-2000-growth-etf-3-31.pdf) — official complete 2016-2025 calendar table, passive index exposure, and quarter observations
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — reference as-of 2025-12-31
- [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
