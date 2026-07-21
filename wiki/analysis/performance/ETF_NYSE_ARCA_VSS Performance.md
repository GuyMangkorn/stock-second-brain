---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:VSS
ticker: VSS
exchange: NYSE Arca
fund: Vanguard FTSE All-World ex-US Small-Cap ETF
tracked_index: FTSE Global Small Cap ex US Index
benchmark: S&P 500 Total Return
updated: 2026-07-18
performance_as_of: 2026-07-13
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-13
price_nav_as_of: 2026-06-22
distribution_as_of: 2026-06-23
fund_facts_as_of: 2026-03-31
source_batch: raw/imports/ETF_performance_sources_2026-07-18.md
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
current YTD คือ `+6.36%` ณ 13 ก.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:VSS` (คำขอ `AMEX-VSS` ถูก resolve เป็น primary listing นี้)
- Inception: 2 เม.ย. 2009; expense ratio: `0.06%` ณ 27 ก.พ. 2026
- Metric: `NAV Total Return` แบบ pre-tax รวม dividends และ capital-gains
  distributions reinvested หลัง fund expenses
- Issuer benchmark: `FTSE Global Small Cap ex US Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference)
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`
- 10-year NAV TR CAGR: `8.26%`; normalized Start TR value: `100.00`; calculated
  End TR value: `221.15`; Years: `10.00`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`. End value เป็น calculation
  จาก official CAGR ที่ปัดเศษแล้ว; Vanguard ไม่เปิด raw TR endpoints ใน snapshot นี้.
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
- Current YTD: VSS `+6.36%` NAV ณ 13 ก.ค. 2026

## Risk read-through

Official rolling 10-year NAV CAGR `8.26%` สูงกว่า calendar-window CAGR เพราะ
ใช้คนละ endpoints. VSS เป็น passive international ex-U.S. small-cap exposure;
จึงมี small-cap, country และ FX sensitivity ชัด และปีลบทั้งสองปีลดมากกว่า
`-18%`. Expense ratio อยู่ที่ `0.06%`. Vanguard snapshot ไม่เปิด official
maximum drawdown/recovery series จึงระบุ `ไม่พบข้อมูลที่ยืนยันได้`; price/NAV pair
ล่าสุดที่ยืนยันได้เป็น 22 มิ.ย. 2026 และไม่ควรใช้เป็น current quote.

## Sources

- [Vanguard VSS product page](https://investor.vanguard.com/investment-products/etfs/profile/vss)
- [Vanguard Advisors VSS page](https://advisors.vanguard.com/investments/products/vss/vanguard-ftse-all-world-ex-us-small-cap-etf)
- [Official fact sheet](https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3184.pdf) | [prospectus](https://fund-docs.vanguard.com/p3184.pdf)
- [[ETF_performance_sources_2026-07-18]] | [[ETF Performance Index]]
