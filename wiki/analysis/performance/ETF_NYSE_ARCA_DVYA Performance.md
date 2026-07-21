---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DVYA
ticker: DVYA
exchange: NYSE Arca
fund: iShares Asia/Pacific Dividend ETF
tracked_index: Dow Jones Asia/Pacific Select Dividend 50 Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-19
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-16
nav_as_of: 2026-07-17
market_price_as_of: 2026-07-16
fund_facts_as_of: 2026-03-31
risk_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-19.md
return_basis: NAV total return
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
current YTD คือ `+14.28%` ณ 16 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:DVYA`
- Fund: iShares Asia/Pacific Dividend ETF; inception `23 ก.พ. 2012`; expense ratio
  `0.49%`
- Metric: `NAV Total Return` ใน USD รวม dividends และ capital-gains
  distributions reinvested หลัง fund expenses
- Issuer benchmark: `Dow Jones Asia/Pacific Select Dividend 50 Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ DVYA)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `6.90%`; normalized Start TR value: `100.00`; End TR
  value: `194.89`; Years: `10.00`; official cumulative return: `94.89%`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`. Normalized endpoints derive
  from issuer cumulative return; raw NAV TR index levels ไม่ได้เปิดเผย
- Annual coverage: official complete calendar years 2021-2025; ไม่มี `*` หรือ `†`.
  The issuer notes that the underlying index changed from the Dow Jones Asia/Pacific
  Select Dividend 30 Index to the Select Dividend 50 Index on 22 มิ.ย. 2020.

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
- Current YTD: DVYA `+14.28%` NAV ณ 16 ก.ค. 2026

## Risk read-through

Official rolling 10-year NAV CAGR `6.90%` ณ 30 มิ.ย. 2026 ต่ำกว่า S&P 500 TR
อย่างมาก แม้ปี 2025 จะ outperform จาก international dividend/value rebound. DVYA
เป็น passive developed Asia-Pacific high-dividend equity ETF; portfolio มี 50
holdings, 3-year standard deviation `13.57%` และ equity beta เทียบ S&P 500 `0.54`
ณ 30 มิ.ย. 2026. ความเสี่ยงเชิงโครงสร้างคือ sector concentration ใน Financials
`33.79%` และ geographic concentration ใน Australia `42.56%`, Hong Kong `24.78%`
และ Singapore `19.35%` ณ 16 ก.ค. 2026; จึงไม่ใช่ broad Asia-Pacific market proxy.
Expense ratio `0.49%` สูงกว่ากอง broad-market หลายกอง และผลตอบแทนยังไวต่อ FX,
commodity/materials และวัฏจักรเศรษฐกิจของประเทศหลัก.

Latest official NAV คือ `$49.52` ณ 17 ก.ค. 2026; closing market price `$49.39`
ณ 16 ก.ค. 2026 และ issuer-reported premium/discount `-0.17%` ณ 16 ก.ค. 2026.
Official daily NAV TR index levels สำหรับคำนวณ maximum drawdown และ recovery date:
`ไม่พบข้อมูลที่ยืนยันได้`; ไม่ใช้ secondary price proxy ปะปนกับ NAV TR ranking.

## Sources

- [iShares DVYA product page](https://www.ishares.com/us/individual/products/239443/ishares-asiapacific-dividend-etf) — current NAV/price, YTD NAV TR, exchange, benchmark, inception, holdings, exposures, premium/discount, risk and fees
- [Official DVYA factsheet](https://www.ishares.com/us/literature/fact-sheet/dvya-ishares-asiapacific-dividend-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 annual NAV TR, rolling 10-year NAV TR and return definition
- [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/930667/000119312525192514/d904293d497k.htm) — passive/index-tracking objective, listing and risk disclosure
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference identity; annual rows reuse the cached skill convention
- [[ETF_performance_sources_2026-07-19]] | [[ETF Performance Index]]
