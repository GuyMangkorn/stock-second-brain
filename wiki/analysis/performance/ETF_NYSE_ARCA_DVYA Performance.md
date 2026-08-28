---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DVYA
ticker: DVYA
exchange: NYSE Arca
fund: iShares Asia/Pacific Dividend ETF
tracked_index: Dow Jones Asia/Pacific Select Dividend 50 Index (Net)
benchmark: S&P 500 Total Return
inception: 2012-02-23
management_mode: passive-index
updated: 2026-08-28
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-25
nav_as_of: 2026-08-26
market_price_as_of: 2026-08-26
holdings_as_of: 2026-08-26
risk_as_of: 2026-07-31
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - geography/Asia-Pacific
  - ticker/DVYA
  - geography/developed-asia-pacific
  - style/dividend
---

# DVYA Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

DVYA ให้ cumulative `NAV Total Return` `60.39%` หรือ CAGR `9.91%` ใน complete
calendar years 2021-2025 เทียบ S&P 500 TR `96.17%` / `14.43%`; เป็นบวก 4 ปี
และลบ 1 ปี. ปีดีที่สุดคือ 2025 `+30.16%`, ปีแย่ที่สุดคือ 2022 `-2.12%`, และ
current official YTD คือ `+21.45%` ณ 25 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:DVYA`
- Fund: iShares Asia/Pacific Dividend ETF; inception `2012-02-23`; expense ratio
  `0.49%`
- Metric: `NAV Total Return` ใน USD รวม dividends และ capital-gains
  distributions reinvested หลัง fund expenses
- Issuer benchmark: `Dow Jones Asia/Pacific Select Dividend 50 Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ DVYA)
- Management mode: `passive-index`
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `6.90%`; normalized Start TR value `100.00`; End TR
  value `194.89`; official cumulative return `94.89%`; Years `10.00`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`. Raw daily NAV TR endpoints
  ไม่ได้เปิดเผย; normalized endpoints derive from the issuer's cumulative return.
- Annual coverage: official complete calendar years 2021-2025; ไม่มี `*` หรือ
  `†`. iShares states that the underlying index changed from the Dow Jones
  Asia/Pacific Select Dividend 30 Index to the Select Dividend 50 Index on
  `2020-06-22`.

| ปี | DVYA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2021 | 4.23% | 28.71% |
| 2022 | -2.12% | -18.11% |
| 2023 | 13.96% | 26.29% |
| 2024 | 5.99% | 25.02% |
| 2025 | 30.16% | 17.88% |

S&P 500 rows ใช้ cached USD Total Return convention, dividends reinvested,
reference as-of `2025-12-31`. DVYA 2021-2025 cumulative/CAGR คือ `60.39%` /
`9.91%`; S&P 500 TR คือ `96.17%` / `14.43%`.

## Up years / Down years

- Up years / Down years: `4 / 1` ใน 2021-2025
- Best: 2025, `+30.16%`
- Least positive: 2024, `+5.99%`
- Worst: 2022, `-2.12%`
- Least bad down year: 2022, `-2.12%`
- Current YTD: DVYA `+21.45%` NAV TR ณ `2026-08-25`

## Risk read-through

Official rolling 10-year NAV CAGR `6.90%` ณ 30 มิ.ย. 2026 ต่ำกว่า S&P 500 TR
อย่างมาก แม้ปี 2025 จะ outperform จาก international dividend/value rebound. DVYA
เป็น passive developed Asia-Pacific high-dividend equity ETF; มี 50 holdings ณ
26 ส.ค. 2026, 3-year standard deviation `13.97%` และ equity beta `0.51` ณ
31 ก.ค. 2026. Expense ratio `0.49%`; 30-day SEC yield `4.55%` และ 12-month
trailing yield `4.37%` ณ 31 ก.ค. 2026.

Underlying exposure กระจุกใน Australia `42.15%`, Hong Kong `24.39%`, Singapore
`19.07%` และ Japan `8.88%` ณ 26 ส.ค. 2026; sector ใหญ่คือ Financials `32.85%`
และ Materials `16.13%`. จึงไม่ใช่ broad Asia-Pacific market proxy และยังไวต่อ
FX, commodity/materials และวัฏจักรเศรษฐกิจของประเทศหลัก. Latest official NAV คือ
`$52.14` และ closing market price `$52.11` ณ 26 ส.ค. 2026.

Official daily NAV TR index levels สำหรับคำนวณ maximum drawdown และ recovery date:
`ไม่พบข้อมูลที่ยืนยันได้`; ไม่ใช้ secondary price proxy ปะปนกับ NAV TR ranking.

## Sources

- [iShares DVYA product page](https://www.ishares.com/us/products/239443/ishares-asiapacific-dividend-etf) — current NAV/price, YTD NAV TR, exchange, benchmark, inception, holdings, exposures, risk and fees; current snapshot through 2026-08-26
- [Official DVYA factsheet](https://www.ishares.com/us/literature/fact-sheet/dvya-ishares-asia-pacific-dividend-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 annual NAV TR, rolling 10-year NAV TR and return definition; as of 2026-06-30
- [DVYA summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-asia-pacific-dividend-etf-4-30.pdf) — passive/index-tracking objective, NYSE Arca listing, index methodology and risks; dated 2025-08-29
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference identity; annual rows reuse the cached convention
- [[ETF_performance_sources_2026-08-28]] | [[ETF Performance Index]]
