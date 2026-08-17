---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IWN
ticker: IWN
exchange: NYSE Arca
fund: iShares Russell 2000 Value ETF
tracked_index: Russell 2000 Value Index
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
  - ticker/IWN
  - geography/United-States
---

# IWN Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

IWN เป็น passive/index-tracking U.S. small-cap value equity ETF ที่ติดตาม
Russell 2000 Value Index. Official complete 2016-2025 NAV Total Return table ที่
เผยแพร่ละเอียด `0.1%` ให้ cumulative `138.50%` หรือ rounded-input CAGR `9.08%`;
เทียบกับ S&P 500 TR `298.33%` / CAGR `14.82%`. ช่วง 2021-2025 IWN compound
`51.31%` หรือ CAGR `8.64%`. Issuer-reported rolling 10-year NAV TR annualized
คือ `10.69%` และ current NAV YTD คือ `25.91%` ณ 13 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:IWN`
- Inception: 24 ก.ค. 2000; expense ratio: `0.24%`
- Metric: `NAV Total Return` รวม reinvested dividends/distributions หลัง fund expenses; currency: USD
- Issuer benchmark: `Russell 2000 Value Index` (`RU20VATR`)
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference)
- 10-year calendar-window calculation: official complete-year NAV TR rows from
  2016-2025; cumulative `138.50%`, rounded-input CAGR `9.08%` using
  `(Π(1 + annual TR))^(1 / 10) - 1`.
- Issuer 10-year NAV TR annualized field: `10.69%` ณ 30 มิ.ย. 2026; raw endpoints
  ไม่ได้เปิดเผย จึงแยกจาก calendar-window calculation `9.08%`.
- Current quote: market price `US$227.43`, NAV `US$227.41`, calculated premium
  `0.01%` ณ 14 ส.ค. 2026
- Annual coverage: official complete years 2016-2025, published at `0.1%`
  precision; ไม่มี `*` หรือ `†`.

| ปี | IWN NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 31.64% | 11.96% |
| 2017 | 7.73% | 21.83% |
| 2018 | -12.94% | -4.38% |
| 2019 | 22.17% | 31.49% |
| 2020 | 4.50% | 18.40% |
| 2021 | 27.96% | 28.71% |
| 2022 | -14.67% | -18.11% |
| 2023 | 14.42% | 26.29% |
| 2024 | 7.74% | 25.02% |
| 2025 | 12.41% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2016, `+31.64%`; least positive: 2024, `+7.74%`
- Worst: 2022, `-14.67%`; least bad down year: 2018, `-12.94%`
- 2016-2025 cumulative / CAGR: `138.50%` / `9.08%`
- 2021-2025 cumulative / CAGR: `51.31%` / `8.64%`
- Current YTD: IWN NAV `+25.91%` ณ 13 ส.ค. 2026

## Risk read-through

IWN เป็น passive U.S. small-cap value equity จึงมี value/cyclicality, financials
และ liquidity sensitivity สูงกว่า broad large-cap exposure. Official three-year
standard deviation คือ `19.10%` ณ 31 ก.ค. 2026 และ equity beta `1.08` ณ 31 ก.ค.
2026; factsheet ณ 30 มิ.ย. 2026 แสดง standard deviation `19.40%`. Best quarter
คือ `+33.29%` (ไตรมาสสิ้นสุด 31 ธ.ค. 2020) และ worst quarter คือ `-35.70%`
(ไตรมาสสิ้นสุด 31 มี.ค. 2020). Expense ratio อยู่ที่ `0.24%`, fund จ่าย
distributions รายไตรมาส, และมี holdings `1,389` ณ 11 ส.ค. 2026. Max drawdown,
recovery date และ daily-NAV history ที่ตรวจสอบได้คือ `ไม่พบข้อมูลที่ยืนยันได้`
จาก official sources ที่ reviewed.

## Driver notes

- Confirmed structure: passive index-tracking exposure to the Russell 2000 Value
  segment; no active/options overlay was identified in the reviewed official materials.
- Published-return precision matters: the complete official 2016-2025 table is
  rounded to 0.1%, so cumulative/CAGR outputs are rounded-input calculations.
- Observed regime points: 2016 เป็นปีบวกสูงสุดและ 2022 เป็นปีลบสูงสุดจาก complete
  rows; ไม่ตีความเป็น causal event attribution.

## Sources

- [iShares IWN product page](https://www.ishares.com/us/products/239712/ishares-russell-2000-value-etf) — official current NAV/price/YTD, issuer 10-year return, benchmark, fee, standard deviation, and fund facts
- [iShares IWN factsheet](https://www.ishares.com/us/literature/fact-sheet/iwn-ishares-russell-2000-value-etf-fund-fact-sheet-en-us.pdf) — official 2026-06-30 fund facts and 2021-2025 NAV TR rows
- [iShares summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-russell-2000-value-etf-3-31.pdf) — official complete 2016-2025 calendar table, fund objective, passive index exposure, and quarter observations
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — reference as-of 2025-12-31
- [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
