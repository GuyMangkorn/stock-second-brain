---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:EFAV
ticker: EFAV
exchange: Cboe BZX
fund: iShares MSCI EAFE Min Vol Factor ETF
tracked_index: MSCI EAFE Minimum Volatility (USD) Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-18
performance_as_of: 2026-07-16
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-16
nav_as_of: 2026-07-17
market_price_as_of: 2026-07-16
distribution_as_of: 2026-06-18
fund_facts_as_of: 2026-03-31
risk_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-18.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/EFAV
  - geography/developed-ex-US-Canada
  - factor/minimum-volatility
---

# EFAV Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

EFAV ให้ cumulative `NAV Total Return` `78.42%` หรือ CAGR `5.96%` ใน complete
calendar years 2016-2025 เทียบ S&P 500 TR `298.33%` / `14.82%`; เป็นบวก 7 ปี
และลบ 3 ปี. ปีดีที่สุดคือ 2025 `+26.16%`, แย่ที่สุดคือ 2022 `-14.76%`, และ
current YTD คือ `+6.50%` ณ 16 ก.ค. 2026.

## Performance check

- `entity_key: Cboe BZX:EFAV`
- Inception: 18 ต.ค. 2011; expense ratio: `0.20%`
- Metric: `NAV Total Return` ใน USD รวม dividends และ capital-gains
  distributions reinvested หลัง fund expenses
- Issuer benchmark: `MSCI EAFE Minimum Volatility (USD) Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `6.02%`; normalized Start TR value: `100.00`; End TR
  value: `179.38`; Years: `10.00`; official cumulative return: `79.38%`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`. Normalized endpoints derive
  from official cumulative return; issuer ไม่เปิด raw NAV TR index levels.
- Annual coverage: official complete years 2016-2025; ไม่มี `*` หรือ `†`.

| ปี | EFAV NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | -1.86% | 11.96% |
| 2017 | 21.57% | 21.83% |
| 2018 | -5.80% | -4.38% |
| 2019 | 16.78% | 31.49% |
| 2020 | 0.19% | 18.40% |
| 2021 | 7.02% | 28.71% |
| 2022 | -14.76% | -18.11% |
| 2023 | 11.98% | 26.29% |
| 2024 | 5.28% | 25.02% |
| 2025 | 26.16% | 17.88% |

## Up years / Down years

- Up years / Down years: `7 / 3` ใน 2016-2025
- Best: 2025, `+26.16%`; least positive: 2020, `+0.19%`
- Worst: 2022, `-14.76%`; least bad down year: 2016, `-1.86%`
- 2021-2025 cumulative: EFAV `35.68%`, CAGR `6.29%`; S&P 500 TR `96.17%`,
  CAGR `14.43%`
- Current YTD: EFAV `+6.50%` NAV ณ 16 ก.ค. 2026

## Risk read-through

Official rolling 10-year NAV CAGR `6.02%` ณ 30 มิ.ย. 2026 ใกล้ calendar-window
CAGR `5.96%` แต่ยังต่ำกว่า S&P 500 TR มาก. EFAV เป็น passive developed
ex-U.S./Canada minimum-volatility factor ETF; 3-year standard deviation `10.46%`
และ equity beta เทียบ S&P 500 `0.28` ณ 30 มิ.ย. 2026 สนับสนุน behavior ที่ลด
ความผันผวนในช่วงล่าสุด แต่ไม่รับประกัน downside protection. ความเสี่ยงหลักยังเป็น
international equity, country, factor และ FX sensitivity. Expense ratio `0.20%`.
Issuer ไม่เปิด official maximum drawdown/recovery series จึงระบุ
`ไม่พบข้อมูลที่ยืนยันได้`; price และ NAV ล่าสุดมีคนละ as-of date จึงไม่คำนวณ
premium/discount จาก snapshot นี้.

## Sources

- [iShares EFAV product page](https://www.ishares.com/us/products/239626/ishares-msci-eafe-minimum-volatility-etf)
- [Official fact sheet](https://www.ishares.com/us/literature/fact-sheet/efav-ishares-msci-eafe-min-vol-factor-etf-fund-fact-sheet-en-us.pdf) | [summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-edge-msci-min-vol-eafe-etf-7-31.pdf)
- [Cboe EFAV listing](https://www.cboe.com/us/equities/listings/listed_products/symbols/EFAV)
- [[ETF_performance_sources_2026-07-18]] | [[ETF Performance Index]]
