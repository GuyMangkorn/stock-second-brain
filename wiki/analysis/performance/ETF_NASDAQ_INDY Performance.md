---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:INDY
ticker: INDY
issuer: iShares
fund: iShares India 50 ETF
exchange: NASDAQ
tracked_index: Nifty 50 Index
benchmark: S&P 500 Total Return
inception: 2009-11-18
expense_ratio: 0.65%
updated: 2026-08-28
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - geography/India
  - ticker/INDY
---

# INDY Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

INDY ให้ผลตอบแทนเป็นบวก 5 จาก 6 ปีเต็มในช่วง 2020-2025; ใน common window
2021-2025 NAV TR สะสม `39.73%` หรือ CAGR `6.92%` เทียบกับ S&P 500 TR
`96.17%` หรือ `14.43%`. ปีดีที่สุดคือ 2021 ที่ `+19.28%` และปีแย่ที่สุดคือ
2022 ที่ `-7.86%`. Current official NAV คือ `US$43.57` ณ 2026-08-27 และ
NAV Total Return YTD ล่าสุดอยู่ที่ `-11.36%` ณ 2026-08-26.

## Performance check

- entity_key: NASDAQ:INDY
- Fund: iShares India 50 ETF
- Inception: 2009-11-18
- Latest official NAV: US$43.57 ณ 2026-08-27; closing price US$43.58 ณ 2026-08-27
- Metric: NAV Total Return รวมเงินปันผลและ capital gains ที่ reinvested และหัก fund expenses
- Tracked index (issuer benchmark): Nifty 50 Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not INDY's tracked index)
- Asset class: Equity; distribution frequency: semi-annual
- Holdings: 50 ณ 2026-08-27
- 3-year standard deviation: 13.32%; equity beta: 0.37 ณ 2026-07-31
- P/E: 21.64; P/B: 3.03 ณ 2026-08-27
- 10-year window: 2016-06-30 ถึง 2026-06-30; actual years 10.00
- 10-year NAV TR CAGR: 6.67% (issuer-reported cumulative return 90.75%; normalized Start TR value 100.00, End TR value 190.75)
- Formula: (190.75 / 100.00)^(1 / 10.00) - 1 = 6.67%
- Annual NAV TR coverage: official complete-calendar-year rows 2021-2025; 2020 is from the dated BlackRock factsheet and is kept as an additional complete row

| ปี | INDY NAV TR | S&P 500 TR |
|---|---:|---:|
| 2020 | 10.67% | 18.40% |
| 2021 | 19.28% | 28.71% |
| 2022 | -7.86% | -18.11% |
| 2023 | 17.05% | 26.29% |
| 2024 | 4.02% | 25.02% |
| 2025 | 4.42% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ INDY;
ตารางใช้ cached USD Total Return convention สำหรับ 2016-2025. 2021-2025 เป็น
common window ที่ใช้เทียบกันโดยตรง.

## Up years / Down years

- Best: 2021, `+19.28%`
- Least positive: 2024, `+4.02%`
- Worst: 2022, `-7.86%`
- Least bad down year: 2022, `-7.86%` (only down year in 2020-2025)
- 2020-2025 cumulative / CAGR: 54.64% / 7.54%
- 2021-2025 cumulative / CAGR: 39.73% / 6.92%; S&P 500 TR: 96.17% / 14.43%
- 2026 YTD: `-11.36%` NAV, as of 2026-08-26
- Standardized month-end YTD: -11.49% NAV as of 2026-06-30; kept separate from current date-to-date observation

## Risk read-through

Rolling 10-year NAV TR CAGR อยู่ที่ `6.67%`; ใน common annual window 2021-2025
INDY ให้ CAGR `6.92%` และต่ำกว่า S&P 500 TR `14.43%`. เป็น passive single-country
India large-cap equity ETF ที่มี 50 holdings, expense ratio `0.65%` และ current
sector exposure หลักคือ Financials `36.04%`, Consumer Discretionary `11.95%`,
Energy `9.48%`, Industrials `8.60%` และ Information Technology `8.13%` ณ
2026-08-27. Daily NAV history สำหรับ max drawdown และ recovery:
`ไม่พบข้อมูลที่ยืนยันได้`; จึงไม่ใช้ price drawdown แทน NAV TR drawdown.

Source-quality choice: canonical iShares INDY product page เป็น source หลักสำหรับ
current snapshot โดย separate overview endpoint ที่ให้ YTD -7.61% และ holdings
165 ณ 2026-08-25 ไม่ถูกผสมเข้ากับตัวเลข canonical snapshot.

## Sources

- [iShares INDY product page](https://www.ishares.com/us/products/239758/ishares-india-50-etf) — identity, NASDAQ listing, Nifty 50 benchmark, current NAV/YTD, rolling performance, risk and fees; as of dates 2026-06-30 to 2026-08-27
- [iShares INDY factsheet](https://www.ishares.com/us/literature/fact-sheet/indy-ishares-india-50-etf-fund-fact-sheet-en-us.pdf) — official NAV total-return definition, 2021-2025 calendar returns, inception and expense ratio
- [iShares INDY summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-india-50-etf-3-31.pdf) — official indexing objective and fund disclosures
- [BlackRock INDY factsheet as of 2025-06-30](https://www.blackrock.com/americas-offshore/en/literature/fact-sheet/indy-ishares-india-50-etf-fund-fact-sheet-en-lm.pdf) — official 2020 calendar NAV TR row
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference benchmark identity; annual rows use the cached USD total-return convention as of 2025-12-31
- ETF source batch: [[ETF_performance_sources_2026-08-28]] | [[ETF Performance Index]]
