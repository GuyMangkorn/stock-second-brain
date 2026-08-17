---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IWM
ticker: IWM
exchange: NYSE Arca
fund: iShares Russell 2000 ETF
tracked_index: Russell 2000 Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-08-13
rolling_10y_as_of: 2026-06-30
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IWM
  - geography/United-States
---

# IWM Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

IWM เป็น passive/index-tracking U.S. small-cap broad equity ETF ที่ติดตาม
Russell 2000 Index. Official complete 2016-2025 NAV Total Return table ที่
เผยแพร่ละเอียด `0.1%` ให้ cumulative `148.94%` หรือ rounded-input CAGR `9.55%`;
เทียบกับ S&P 500 TR `298.33%` / CAGR `14.82%`. ช่วง 2021-2025 IWM compound
`33.60%` หรือ CAGR `5.96%`. Issuer-reported rolling 10-year NAV TR annualized
คือ `11.53%` และ current NAV YTD คือ `23.73%` ณ 13 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:IWM`
- Inception: 22 พ.ค. 2000; expense ratio: `0.19%` ตาม current prospectus
- Metric: `NAV Total Return` รวม reinvested dividends/distributions หลัง fund expenses; currency: USD
- Issuer benchmark: `Russell 2000 Index` (`RU20INTR`)
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference)
- Issuer 10-year NAV TR annualized field: `11.53%` ณ 30 มิ.ย. 2026; raw endpoints
  ไม่ได้เปิดเผย จึงแยกจาก calendar-window calculation `9.55%`.
- Complete calendar-year inputs: official iShares professional table for 2016-2025,
  published at `0.1%` precision. The current U.S. factsheet provides a higher-
  precision 2021-2025 cross-check, but it is not mixed into the complete-window
  calculation.
- Current quote: market price `US$305.09`, NAV `US$304.98`, calculated premium
  `0.04%` ณ 14 ส.ค. 2026

| ปี | IWM NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 21.4% | 11.96% |
| 2017 | 14.7% | 21.83% |
| 2018 | -11.0% | -4.38% |
| 2019 | 25.4% | 31.49% |
| 2020 | 19.9% | 18.40% |
| 2021 | 14.6% | 28.71% |
| 2022 | -20.5% | -18.11% |
| 2023 | 16.8% | 26.29% |
| 2024 | 11.4% | 25.02% |
| 2025 | 12.7% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2019, `+25.4%`
- Least positive: 2024, `+11.4%`
- Worst: 2022, `-20.5%`
- Least bad down year: 2018, `-11.0%`
- 2016-2025 cumulative / CAGR: `148.94%` / `9.55%`
- 2021-2025 cumulative / CAGR: `33.60%` / `5.96%`
- Current YTD: IWM NAV `+23.73%` ณ 13 ส.ค. 2026

## Risk read-through

IWM เป็น passive U.S. small-cap equity ที่มี broad small-cap, cyclicality,
liquidity และ equity drawdown sensitivity. Official three-year standard deviation
คือ `19.97%` ณ 31 ก.ค. 2026; factsheet ณ 30 มิ.ย. 2026 แสดง `19.98%`. Expense
ratio อยู่ที่ `0.19%`, fund จ่าย distributions รายไตรมาส, และมี holdings `1,965`
ณ 13 ส.ค. 2026. Max drawdown, recovery date และ daily-NAV history ที่ตรวจสอบได้
คือ `ไม่พบข้อมูลที่ยืนยันได้` จาก official sources ที่ reviewed.

## Driver notes

- Confirmed structure: passive index-tracking exposure to the Russell 2000 small-cap
  segment; no active/options overlay was identified in the reviewed official materials.
- Published-return precision matters: the complete official 2016-2025 professional
  table is rounded to 0.1%, so cumulative/CAGR outputs are rounded-input estimates.
- Observed regime points: 2019 เป็นปีบวกสูงสุดและ 2022 เป็นปีลบสูงสุดจาก complete
  rows; ไม่ตีความเป็น causal event attribution.

## Sources

- [iShares IWM product page](https://www.ishares.com/us/products/239710/ishares-russell-2000-etf) — official current NAV/price/YTD, issuer 10-year return, benchmark, fee, standard deviation, and fund facts
- [iShares IWM factsheet](https://www.ishares.com/us/literature/fact-sheet/iwm-ishares-russell-2000-etf-fund-fact-sheet-en-us.pdf) — official 2026-06-30 fund facts and higher-precision 2021-2025 cross-check
- [iShares professional performance page](https://www.ishares.com/uk/professionals/en/products/239710/ishares-russell-2000-etf?siteEntryPassthrough=true&switchLocale=y) — official complete 2016-2025 calendar table at 0.1% precision
- [iShares summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-russell-2000-etf-3-31.pdf) — fund objective, passive index exposure, benchmark, and fee context
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as-of 2025-12-31
- [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
