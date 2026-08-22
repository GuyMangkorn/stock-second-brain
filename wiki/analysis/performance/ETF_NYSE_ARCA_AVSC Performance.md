---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:AVSC
ticker: AVSC
exchange: NYSE Arca
fund: Avantis U.S. Small Cap Equity ETF
tracked_index: not applicable (active strategy)
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process: fundamental-active
management_benchmark: Russell 2000
track_record: developing
management_evidence: mixed
risk_evidence: not-verified
updated: 2026-08-17
performance_as_of: 2026-06-30
calendar_years_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/AVSC
  - geography/United-States
---

# AVSC Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

AVSC เป็น active-equity-long-only U.S. small-cap ETF ของ Avantis ที่ใช้
fundamental-active process โดยให้น้ำหนักกับ size, value และ profitability
characteristics แทนการ replicate ดัชนี. Official issuer รายงาน current NAV TR
YTD `23.92%` ณ 2026-07-31. Factsheet ณ 2026-06-30 รายงาน 3-year annualized NAV
TR `18.50%` เทียบ Russell 2000 `18.60%`, 1-year `43.54%` เทียบ `40.78%` และ
since-inception annualized `10.24%` เทียบ `8.97%`; จึงเป็น mixed return evidence
บน track record ที่ยัง developing ตั้งแต่ 2022-01-11 ไม่ใช่หลักฐานของ alpha.

สำหรับ calendar rows ที่เปิดเผยผ่านแหล่ง secondary เดียว ตาราง 2023-2025 ให้
cumulative `40.81%` และ rounded-input CAGR `12.08%`. เนื่องจากกองเริ่มในปี 2022
จึงไม่มี 2021-2025 common window ที่ครบถ้วน และไม่เพิ่ม AVSC เข้า strict common
window ranking.

## Performance check

- `entity_key`: `NYSE Arca:AVSC`
- Inception: 2022-01-11
- Expense ratio: `0.25%` gross/net as of 2026-01-01
- Metric: official NAV Total Return includes reinvested distributions and fund expenses; USD; market-price return remains separate
- Management mode: `active-equity-long-only`
- Active process: `fundamental-active`; portfolio managers use market and company financial data, including book value, cash flows and profitability, to overweight or underweight eligible U.S. small-cap companies
- Management benchmark: `Russell 2000`, named in the official Avantis factsheet; S&P 500 Total Return is retained only as the common reference benchmark
- Track-record maturity: `developing`; the fund has less than five years of live history as of 2026-08-17
- 10-year NAV TR: not applicable (<10-year fund history)
- Official rolling NAV TR as of 2026-06-30: 1-year `43.54%`, 3-year annualized `18.50%`, since-inception annualized `10.24%`
- Official Russell 2000 comparison as of 2026-06-30: 1-year `40.78%`, 3-year annualized `18.60%`, since-inception annualized `8.97%`
- Current official NAV TR YTD: `23.92%` as of 2026-07-31
- Current NAV / market price: `$75.22` / `$75.25` as of 2026-08-14
- Secondary calendar proxy: 2023-2025 cumulative `40.81%` / rounded-input CAGR `12.08%`; S&P 500 cached 2023-2025 cumulative `86.12%` / CAGR `23.01%`
- Coverage/source note: AAII/Morningstar annual NAV observations marked `*` are a single secondary proxy. The SEC summary prospectus reports 2024 return before taxes `7.76%`, which rounds to the proxy's `7.8%`; the source difference is retained rather than mixed into the table.

| Year | AVSC secondary NAV total-return proxy* | S&P 500 TR |
|---|---:|---:|
| 2023 | 19.40% | 26.29% |
| 2024 | 7.80% | 25.02% |
| 2025 | 9.40% | 17.88% |
| 2023-2025 cumulative | 40.81% | 86.12% |
| 2023-2025 rounded-input CAGR | 12.08% | 23.01% |

`*` Annual AVSC values are AAII/Morningstar secondary NAV total-return
observations as of 2026-07-31, not a complete issuer-published calendar table.
S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31.

## Up years / Down years

- Up years / Down years: `3 / 0` in the complete 2023-2025 secondary proxy window
- Best: 2023, `+19.40%`*
- Least positive: 2025, `+9.40%`*
- Worst: no down year in the complete secondary rows
- Least bad down year: not applicable
- 2023-2025 rounded-input CAGR: `12.08%`*; S&P 500 TR CAGR: `23.01%`
- Current official NAV TR YTD: `+23.92%` as of 2026-07-31

## Risk read-through

AVSC มี small-cap, value/style, profitability/process, market-trading, liquidity,
cash-transactions และ securities-lending risks. Official factsheet ณ 2026-06-30
รายงาน AUM `$3.0B`, holdings `1,516`, quarterly distributions และ portfolio
management team 5 คน; SEC summary prospectus รายงาน portfolio turnover `5%`
สำหรับ fiscal year ล่าสุด และ best/worst quarter `+15.75%` ใน Q4 2023 / `-4.21%`
ใน Q2 2024. Annual-return population standard deviation ของ secondary rows คือ
`5.13%` แต่มีเพียงสามปีจึงไม่ใช้เป็น risk-adjusted evidence. Official daily NAV
history ที่ยืนยันได้สำหรับ max drawdown และ recovery ยังไม่พบข้อมูลที่ยืนยันได้.

## Active management read-through

management_mode: `active-equity-long-only`  
active_process: `fundamental-active`  
management_benchmark: `Russell 2000`  
track_record: `developing`  
management_evidence: `mixed`  
risk_evidence: `not-verified`

- Official 1-year comparison: AVSC `43.54%` versus Russell 2000 `40.78%`, Excess `+2.76 pp` as of 2026-06-30.
- Official 3-year annualized comparison: AVSC `18.50%` versus Russell 2000 `18.60%`, Excess `-0.10 pp`.
- Official since-inception annualized comparison: AVSC `10.24%` versus Russell 2000 `8.97%`, Excess `+1.27 pp`.
- These are reported return differences, not alpha. Compatible official calendar benchmark rows and a complete-year hit rate were not captured; the annual proxy is therefore excluded from active-skill scoring.
- Official process evidence supports a live active mandate: portfolio managers continually analyze financial and market data and make buy, sell and hold decisions using size, valuation and profitability inputs. This does not by itself establish persistent manager skill.

## Sources

- [Official Avantis AVSC product page](https://www.avantisinvestors.com/avantis-investments/avantis-us-small-cap-equity-etf/) — identity, active strategy, current NAV/market price, current YTD and fee.
- [Official Avantis AVSC factsheet](https://res.avantisinvestors.com/docs/avantis-us-small-cap-equity-avsc-etf-fact-sheet.pdf) — rolling NAV, market-price and Russell 2000 benchmark returns, inception, holdings, AUM, fee and management team as of 2026-06-30.
- [SEC AVSC summary prospectus](https://www.sec.gov/Archives/edgar/data/1710607/000171060725000415/acetftavsc497k.htm) — fees, active strategy, process, risks, turnover, inception and 2024 official return cross-check.
- [AAII AVSC annual NAV return table](https://www.aaii.com/fund/ticker/AVSC) — secondary 2023-2025 calendar NAV proxy reviewed 2026-08-17.
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition and cached annual USD Total Return convention.
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
