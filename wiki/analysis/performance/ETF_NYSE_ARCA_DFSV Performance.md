---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DFSV
ticker: DFSV
exchange: NYSE Arca
fund: Dimensional US Small Cap Value ETF
tracked_index: Russell 2000 Value (management comparison; active, not index-tracking)
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process: systematic-factor
management_benchmark: Russell 2000 Value
track_record: developing-short-live-history
management_evidence: mixed-short-track-record
risk_evidence: issuer-fields
updated: 2026-08-17
performance_as_of: 2026-06-30
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
fund_facts_as_of: 2025-12-31
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return; official 2023-2025 rows plus secondary current snapshot
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/DFSV
  - geography/United-States
---

# DFSV Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

DFSV คือ Dimensional US Small Cap Value ETF ซึ่งเป็น active long-only U.S.
small-cap value ETF ไม่ใช่กองที่ replicate index. Dimensional ใช้ integrated
research, portfolio design, portfolio management และ flexible trading process
โดยเน้น lower relative price, smaller companies และ profitability. SEC ใช้
Russell 2000 Value เป็น management benchmark; S&P 500 Total Return เป็นเพียง
common reference benchmark.

Official NAV rows สำหรับ 2023-2025 ให้ cumulative `38.78%` และ rounded-input CAGR
`11.54%`. Official quick guide ณ 2025-12-31 รายงาน 1-year NAV TR `8.51%` และ
since-inception annualized `9.25%`. Current snapshot ณ 2026-06-30 จาก Schwab ซึ่ง
เป็น secondary source รายงาน NAV TR YTD `18.7%`, 1-year `33.8%`, 3-year annualized
`16.4%` และ since-inception annualized `12.5%`; current official Dimensional table
ยังไม่พบใน text capture จึงไม่ยกระดับตัวเลขนี้เป็น official.

## Performance check

- `entity_key`: `NYSE Arca:DFSV`
- Inception date: `2022-02-23`; listing date: `2022-02-24`
- Expense ratio: `0.30%` gross and net as of 2025-12-31; management fee `0.28%` plus other expenses `0.02%` in the SEC prospectus
- Metric: official NAV Total Return includes reinvestment of dividends and other earnings; USD; market-price return remains separate
- Management mode: `active-equity-long-only`
- Active process: `systematic-factor`; market-cap weighted U.S. small-cap portfolio with lower relative price, smaller-company and profitability emphasis, plus flexible trading to manage costs and exposure
- Management benchmark: `Russell 2000 Value`; S&P 500 Total Return is retained only as the common reference benchmark
- Track-record maturity: `developing-short-live-history`; the ETF began in 2022 and does not have a verified 10-year live history
- Official 2023-2025 NAV TR: cumulative `38.78%` / rounded-input CAGR `11.54%`
- Official 2025-12-31 fields: 1-year NAV TR `8.51%`; since-inception annualized NAV TR `9.25%`; AUM `$5,978M`; `1,008` companies; turnover `8%` for the latest fiscal year
- Secondary current fields as of 2026-06-30: NAV TR YTD `18.7%`; 1-year `33.8%`; 3-year annualized `16.4%`; inception annualized `12.5%`
- Official 2024 benchmark comparison: DFSV `7.27%` versus Russell 2000 Value `8.05%`; since inception through 2024-12-31 DFSV `9.50%` versus Russell 2000 Value `5.16%`

| Year | DFSV NAV TR | Russell 2000 Value | S&P 500 TR |
|---|---:|---:|---:|
| 2023 | 19.23% | not disclosed | 26.29% |
| 2024 | 7.27% | 8.05% | 25.02% |
| 2025 | 8.51% | not disclosed | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ management benchmark ของ DFSV.
2023 และ 2024 มาจาก SEC summary prospectus; 2025 มาจาก official Dimensional
quick guide ณ 2025-12-31. FinanceCharts secondary rows แตกต่างกันเล็กน้อยและ
ไม่ถูกนำมาผสมใน official calculation.

## Up years / Down years

- Up years / Down years: `3 / 0` in the complete official 2023-2025 NAV window
- Best: 2023, `+19.23%`
- Least positive: 2025, `+8.51%`
- Official 2023-2025 rounded-input CAGR: `11.54%`
- Official 2023-2025 annual-return population standard deviation: `5.37%`
- 10-year and 2021-2025 CAGR: `ไม่พบข้อมูลที่ยืนยันได้` because the ETF began in 2022

## Risk read-through

DFSV มี small-company, value, profitability, equity-market, market-trading,
premium/discount, securities-lending และ operational risks. SEC ระบุว่า
portfolio turnover ล่าสุด `8%`; official quick guide ณ 2025-12-31 รายงาน AUM
`$5,978M` และ 1,008 companies. Prospectus อนุญาต futures และ options on futures
เพื่อเพิ่มหรือลด equity exposure ตาม cash inflows/outflows แต่ fund ไม่ใช่
derivative-heavy strategy. Official daily NAV history สำหรับ max drawdown และ
recovery ยังไม่พบข้อมูลที่ยืนยันได้.

## Active management read-through

management_mode: `active-equity-long-only`  
active_process: `systematic-factor`  
management_benchmark: `Russell 2000 Value`  
track_record: `developing-short-live-history`  
management_evidence: `mixed-short-track-record`  
risk_evidence: `issuer-fields`

- Official 2024 comparison: DFSV `7.27%` versus Russell 2000 Value `8.05%`, underperformance `-0.78 pp`.
- Official since-inception comparison through 2024-12-31: DFSV `9.50%` versus Russell 2000 Value `5.16%`, excess `+4.34 pp`.
- This is mixed benchmark-relative return evidence over a short ETF history, not alpha. No persistent manager-skill conclusion is made.
- Dimensional describes daily flexibility, research-backed size/value/profitability dimensions and cost control; process evidence does not guarantee future outperformance.

## Sources

- [Official SEC DFSV summary prospectus](https://www.sec.gov/Archives/edgar/data/1816125/000174177325001189/c497k.htm) — identity, active strategy, fee, turnover, risks, 2023-2024 returns and Russell 2000 Value comparison.
- [Official Dimensional ETF quick guide](https://my.dimensional.com/chmedia/282748/source/dimensional-etf-quick-guide.pdf) — 2025-12-31 NAV returns, expense, AUM, company count, inception and listing dates.
- [Official Dimensional DFSV fund page](https://www.dimensional.com/us-en/funds/dfsv/us-small-cap-value-etf) — current fund identity and product context; dynamic performance fields were not text-readable in this run.
- [Schwab performance page](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=dfsv) — secondary current NAV/market-price returns as of 2026-06-30.
- [FinanceCharts total-return page](https://www.financecharts.com/etfs/DFSV/performance/total-return) — secondary reconciliation rows, excluded from the official calculation.
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition and cached annual USD Total Return convention.
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
