---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VSS
ticker: VSS
exchange: NYSE Arca
fund: Vanguard FTSE All-World ex-US Small-Cap ETF
tracked_index: FTSE Global Small Cap ex US Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-08-11
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-08-11
price_nav_as_of: 2026-08-11
distribution_as_of: 2026-06-23
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/VSS
  - geography/international-ex-US
---

# VSS Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

VSS ให้ cumulative `NAV Total Return` `106.58%` หรือ CAGR `7.53%` ใน complete
calendar years 2016-2025 เทียบ S&P 500 TR `298.33%` / `14.82%`; เป็นบวก 8 ปี
และลบ 2 ปี. ปีดีที่สุดคือ 2017 `+30.26%`, แย่ที่สุดคือ 2022 `-21.22%`, และ
current NAV YTD คือ `+10.86%` ณ 11 ส.ค. 2026. Factsheet ที่ปิด ณ 30 มิ.ย. 2026
รายงาน YTD `8.18%`; เป็นคนละ as-of window จึงไม่ผสมตัวเลข.

## Performance check

- `entity_key: NYSE Arca:VSS` (คำขอ `AMEX-VSS` ถูก resolve เป็น primary listing นี้)
- Inception: 2 เม.ย. 2009; expense ratio: `0.06%` ตาม factsheet ณ 30 มิ.ย. 2026
- Metric: `NAV Total Return` แบบ pre-tax รวม dividends และ capital-gains
  distributions reinvested หลัง fund expenses
- Issuer benchmark: `FTSE Global Small Cap ex US Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference)
- Official rolling 10-year NAV TR average annual return: `7.42%` ณ 31 ก.ค. 2026;
  Vanguard ไม่เปิด raw TR endpoints จึงไม่คำนวณ cumulative value จากตัวเลขนี้
- Current quote: market price `US$158.81`, NAV `US$158.05`, calculated premium
  `0.48%` ณ 11 ส.ค. 2026
- Annual coverage: official complete years 2016-2025; ไม่มี `*` หรือ `†`.

| ปี | VSS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 4.37% | 11.96% |
| 2017 | 30.26% | 21.83% |
| 2018 | -18.43% | -4.38% |
| 2019 | 21.73% | 31.49% |
| 2020 | 11.95% | 18.40% |
| 2021 | 12.81% | 28.71% |
| 2022 | -21.22% | -18.11% |
| 2023 | 15.25% | 26.29% |
| 2024 | 2.67% | 25.02% |
| 2025 | 29.99% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` ใน 2016-2025
- Best: 2017, `+30.26%`; least positive: 2024, `+2.67%`
- Worst: 2022, `-21.22%`; least bad down year: 2018, `-18.43%`
- 2021-2025 cumulative: VSS `36.70%`, CAGR `6.45%`; S&P 500 TR `96.17%`,
  CAGR `14.43%`
- Current YTD: VSS NAV `+10.86%`; market-price YTD `+11.40%`; both ณ 11 ส.ค. 2026

## Risk read-through

Official rolling 10-year NAV TR average annual return `7.42%` ณ 31 ก.ค. 2026
ยังไม่มี raw endpoints ให้คำนวณ cumulative แบบ reproducible. VSS เป็น passive
international ex-U.S. small-cap exposure; มี small-cap, country และ FX sensitivity.
Latest official three-year standard deviation อยู่ที่ `14.43%` เทียบ benchmark
`15.27%` จาก monthly returns ณ 30 มิ.ย. 2026. Prior quarter snapshot was
`13.76%` / `14.26%` ณ 31 มี.ค. 2026. Secondary price total-return history
รายงาน maximum drawdown `-43.51%` ณ 23 มี.ค. 2020 จาก peak 26 ม.ค. 2018 และ
current drawdown `-2.11%` จาก peak 11 พ.ค. 2026 ณข้อมูล 10 ส.ค. 2026; ตัวเลขนี้
ไม่ใช่ NAV-specific และ recovery date คือ `ไม่พบข้อมูลที่ยืนยันได้`. Expense ratio
อยู่ที่ `0.06%`.

## Sources

- [Vanguard Advisors VSS page](https://advisors.vanguard.com/investments/products/vss/vanguard-ftse-all-world-ex-us-small-cap-etf)
- [Vanguard VSS product page](https://investor.vanguard.com/investment-products/etfs/profile/vss)
- [Official fact sheet](https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3184.pdf) — current facts as of 30 มิ.ย. 2026 | [prospectus](https://fund-docs.vanguard.com/p3184.pdf)
- [Secondary price total-return history](https://totalrealreturns.com/n/VSS) — drawdown context only
- [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
