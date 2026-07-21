---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:BBJP
ticker: BBJP
exchange: Cboe BZX
fund: JPMorgan BetaBuilders Japan ETF
tracked_index: Morningstar Japan Target Market Exposure Index (net total return)
benchmark: S&P 500 Total Return
updated: 2026-07-18
annual_performance_as_of: 2025-12-31
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
fund_facts_as_of: 2026-06-30
risk_as_of: not separately disclosed
distribution_as_of: 2025-12-23
source_batch: raw/imports/ETF_performance_sources_2026-07-18.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/BBJP
  - geography/Japan
---

# BBJP Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

BBJP ให้ official `NAV Total Return` เป็นบวก 6 จาก 7 complete calendar years ในช่วง
2019-2025; การทบต้นจาก annual rows ให้ cumulative `87.49%` หรือ CAGR `9.39%`.
ปีดีที่สุดคือ 2025 ที่ `+26.56%` และแย่ที่สุดคือ 2022 ที่ `-16.78%`. Current YTD
ล่าสุดจาก issuer คือ `+14.75%` ณ 30 มิ.ย. 2026; since-inception NAV annualized
return อยู่ที่ `7.95%` ณ วันเดียวกัน.

## Performance check

- `entity_key: Cboe BZX:BBJP`
- Inception: 15 มิ.ย. 2018 (fund performance); first Cboe trading date 18 มิ.ย. 2018
- Metric: `NAV Total Return` รวม dividends/capital-gains distributions reinvested
  และ fund expenses
- Issuer benchmark: `Morningstar Japan Target Market Exposure Index (net total return)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ BBJP)
- 10-year window: `not applicable` เพราะ fund performance history ยังไม่ครบ 10 ปี
- Since-inception NAV annualized return: `7.95%` ณ 30 มิ.ย. 2026 (official)
- Coverage/source note: official complete calendar years 2019-2025; `2018†` เป็น
  official inception-year partial และไม่รวมในการจัดอันดับ. S&P 500 rows ใช้ cached
  USD Total Return convention ณ 31 ธ.ค. 2025.

| ปี | BBJP NAV TR | S&P 500 TR |
|---|---:|---:|
| 2019 | 18.62% | 31.49% |
| 2020 | 15.05% | 18.40% |
| 2021 | 1.39% | 28.71% |
| 2022 | -16.78% | -18.11% |
| 2023 | 20.02% | 26.29% |
| 2024 | 7.19% | 25.02% |
| 2025 | 26.56% | 17.88% |

## Up years / Down years

- Up years / Down years: `6 / 1` ใน 2019-2025
- Best: 2025, `+26.56%`
- Least positive: 2021, `+1.39%`
- Worst: 2022, `-16.78%`
- Least bad down year: 2022, `-16.78%`
- 2019-2025 cumulative / CAGR: BBJP `87.49%` / `9.39%`; S&P 500 TR `205.41%` /
  `17.29%`
- 2021-2025 cumulative / CAGR: BBJP `37.38%` / `6.56%`; S&P 500 TR `96.17%` /
  `14.43%`
- Current YTD: `+14.75%` NAV ณ 30 มิ.ย. 2026; issuer ระบุว่า YTD เป็นข้อมูลถึง
  วันทำการสุดท้ายของเดือน

## Risk read-through

BBJP เป็น passive, single-country Japan large/mid-cap equity ETF. Official
since-inception NAV annualized return อยู่ที่ `7.95%` และ annual window 2019-2025
ให้ CAGR `9.39%`, ต่ำกว่า S&P 500 TR ในช่วงเดียวกัน. Expense ratio อยู่ที่ `0.19%`
ทั้ง gross และ net. JPMorgan ไม่เปิดเผย official standard deviation, maximum
drawdown หรือ recovery series ใน factsheet นี้; secondary ETF Central รายงาน
5-year annualized volatility `18.44%`, max drawdown `-32.66%` และ time to recover
`504 วัน` ตามตารางบนหน้า ETF Central ที่อัปเดต 22 มิ.ย. 2026; risk table ไม่เปิดเผย
as-of date แยกต่างหาก (`*` เป็น secondary adjusted-return/market-price proxy,
ไม่ใช่ official NAV drawdown). ความเสี่ยงหลักคือ Japan/country, JPY-USD FX และ
sector concentration โดย factsheet ณ 30 มิ.ย. 2026 มี Industrials `23.8%`,
Information Technology `21.7%`, Financials `17.3%` และ Consumer Discretionary
`14.2%`.

## Sources

- [JPMorgan BBJP fact sheet](https://am.jpmorgan.com/content/dam/jpm-am-aem/americas/us/en/literature/fact-sheet/etfs/FS-BBJP.PDF) — official identity, benchmark, return basis, annual NAV TR, YTD, since-inception return, expenses and holdings; as of 2026-06-30
- [Cboe BBJP new listing notice](https://www.cboe.com/us/equities/notices/new_listings/details/?etf=true&firm_name=J.P.+Morgan+Asset+Management&first_trade_dt=2018-06-18&ipo=true&symbols=BBEU%2CBBJP%2CBBRE) — Cboe BZX listing and first trading date
- [SEC BBJP summary prospectus](https://www.sec.gov/Archives/edgar/data/1485894/000119312526071745/d800751d497k.htm) — official fund objective and indexed/passive mandate; March 1, 2026
- [ETF Central BBJP](https://www.etfcentral.com/fund/BBJP) — secondary volatility, drawdown and recovery proxy; page last updated 2026-06-22 and the risk table does not disclose a separate as-of date
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference index identity
- [[ETF_performance_sources_2026-07-18]] | [[ETF Performance Index]]
