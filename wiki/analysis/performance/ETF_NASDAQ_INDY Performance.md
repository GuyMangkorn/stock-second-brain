---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:INDY
ticker: INDY
updated: 2026-07-19
source_batch: raw/imports/ETF_performance_sources_2026-07-19.md
return_basis: NAV total return
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
2022 ที่ `-7.86%`. NAV Total Return YTD ล่าสุดอยู่ที่ `-12.32%` ณ 16 ก.ค. 2026.

## Performance check

- `entity_key: NASDAQ:INDY`
- Fund: iShares India 50 ETF
- Inception: 18 พ.ย. 2009
- Latest official NAV: `$43.50` ณ 17 ก.ค. 2026
- Metric: `NAV Total Return` รวมเงินปันผลและ capital gains ที่ reinvested และหัก fund expenses
- Tracked index (issuer benchmark): `Nifty 50 Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark, not INDY's tracked index)
- 10-year window: `2016-06-30` ถึง `2026-06-30`
- 10-year NAV TR CAGR: `6.67%` (issuer-reported cumulative return `90.75%`; normalized `Start TR value: 100.00`, `End TR value: 190.75`, `Years: 10.00`)
- Formula: `(190.75 / 100.00)^(1 / 10.00) - 1 = 6.67%`
- Annual NAV TR coverage: official complete-calendar-year rows `2020-2025`; 2020 มาจาก BlackRock factsheet as of 2025-06-30 และ 2021-2025 มาจาก iShares product page/factsheet ล่าสุด

| ปี | INDY NAV TR | S&P 500 TR |
|---|---:|---:|
| 2020 | 10.67% | 18.40% |
| 2021 | 19.28% | 28.71% |
| 2022 | -7.86% | -18.11% |
| 2023 | 17.05% | 26.29% |
| 2024 | 4.02% | 25.02% |
| 2025 | 4.42% | 17.88% |

**Up years / Down years**

- Best: 2021, `+19.28%`
- Least positive: 2024, `+4.02%`
- Worst: 2022, `-7.86%`
- Least bad down year: 2022, `-7.86%` (only down year in 2020-2025)
- 2026 YTD: `-12.32%` NAV, as of 16 ก.ค. 2026

## Risk read-through

Rolling 10-year NAV TR CAGR อยู่ที่ `6.67%`; ใน common annual window 2021-2025
INDY ให้ CAGR `6.92%` และต่ำกว่า S&P 500 TR `14.43%`. ความผันผวน 3 ปีล่าสุด
อยู่ที่ `13.37%` และ equity beta `0.38` ณ 30 มิ.ย. 2026. Expense ratio คือ
`0.65%`; เป็น passive single-country India large-cap equity ETF ที่มี 50 holdings
และ financials คิดเป็น `36.95%` ณ 16 ก.ค. 2026. Official maximum drawdown และ
recovery date จาก daily NAV TR series: `ไม่พบข้อมูลที่ยืนยันได้`; จึงไม่ใช้ price
drawdown แทน NAV TR drawdown.

## Sources

- [iShares INDY product page](https://www.ishares.com/us/products/239758/ishares-india-50-etf) — identity, NASDAQ listing, Nifty 50 benchmark, NAV/YTD, rolling performance, risk and fees; as of dates 2026-06-30 to 2026-07-17
- [iShares INDY factsheet](https://www.ishares.com/us/literature/fact-sheet/indy-ishares-india-50-etf-fund-fact-sheet-en-us.pdf) — official NAV total-return definition, 2021-2025 calendar returns, inception and expense ratio; as of 2026-03-31
- [BlackRock INDY factsheet as of 2025-06-30](https://www.blackrock.com/americas-offshore/en/literature/fact-sheet/indy-ishares-india-50-etf-fund-fact-sheet-en-lm.pdf) — official 2020 calendar NAV TR row
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference benchmark identity; annual rows use the cached USD total-return convention as of 2025-12-31
