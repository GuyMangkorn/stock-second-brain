---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:VTWO
ticker: VTWO
exchange: NASDAQ
fund: Vanguard Russell 2000 ETF
tracked_index: Russell 2000 Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-06-22
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VTWO
  - geography/United-States
---

# VTWO Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

VTWO เป็น passive/full-replication U.S. small-cap broad equity ETF ที่ติดตาม
Russell 2000 Index. Official annual NAV Total Return 2016-2025 compound เป็น
`151.67%` หรือ rounded-input CAGR `9.67%`; เทียบกับ S&P 500 TR `298.33%` หรือ
CAGR `14.82%`. ช่วง 2021-2025 VTWO compound `34.66%` หรือ CAGR `6.13%`.
Issuer-reported rolling 10-year NAV TR annualized คือ `11.68%` และ current NAV
YTD คือ `22.60%` ณ 2026-06-30.

## Performance check

- entity_key: NASDAQ:VTWO
- Inception: 2010-09-20
- Expense ratio: `0.06%`
- Metric: NAV Total Return แบบ pre-tax รวม dividends และ capital-gains distributions
  reinvested หลัง fund expenses; currency: USD
- Tracked index (issuer benchmark): Russell 2000 Index; passive/full replication
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ issuer benchmark ของ VTWO)
- Official rolling 10-year NAV TR: `11.68%` average annual return ณ 2026-06-30;
  raw TR endpoints และ exact elapsed years ไม่ได้เปิดเผย จึงไม่คำนวณ
  endpoint-based CAGR ซ้ำ
- Official annual rows: complete calendar years 2016-2025 from Vanguard's
  profile table as of 2025-12-31. S&P rows reuse the cached USD Total Return
  convention as of 2025-12-31; market-price return is not mixed.
- Formula: cumulative `= product(1 + annual NAV TR) - 1`; rounded-input CAGR
  `= product(1 + annual NAV TR)^(1 / 10) - 1`

| Year | VTWO NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 21.33% | 11.96% |
| 2017 | 14.70% | 21.83% |
| 2018 | -10.98% | -4.38% |
| 2019 | 25.61% | 31.49% |
| 2020 | 20.10% | 18.40% |
| 2021 | 14.81% | 28.71% |
| 2022 | -20.40% | -18.11% |
| 2023 | 17.00% | 26.29% |
| 2024 | 11.57% | 25.02% |
| 2025 | 12.88% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016-2025
- Best: 2019, `25.61%`
- Least positive: 2024, `11.57%`
- Worst: 2022, `-20.40%`
- Least bad down year: 2018, `-10.98%`
- 2016-2025 cumulative / CAGR: `151.67%` / `9.67%`
- 2021-2025 cumulative / CAGR: `34.66%` / `6.13%`
- Current YTD: NAV `22.60%`, market-price `22.63%`, and issuer benchmark
  `22.57%`, all for the period ended 2026-06-30
- Latest captured quote: market price `US$120.46`, NAV `US$120.52`, price/NAV
  discount `-0.05%` calculated from `120.46 / 120.52 - 1`, as of 2026-06-22

## Risk read-through

Issuer-reported rolling 10-year NAV TR annualized return is `11.68%` as of
2026-06-30, versus the rounded-input 2016-2025 calendar CAGR of `9.67%`; these
are different windows. VTWO has broad small-cap, cyclicality, liquidity, and
equity drawdown sensitivity. Expense ratio is `0.06%`, and the fund uses passive
full replication. Official three-year standard deviation is `19.99%`, based on
monthly returns, as of 2026-06-30. Max drawdown, recovery date, and a daily-NAV
volatility series are `ไม่พบข้อมูลที่ยืนยันได้` from the reviewed official sources.

## Driver notes

- Confirmed structure: passive full-replication exposure to the U.S. small-cap
  Russell 2000 segment; the factsheet reports 2,011 holdings as of 2026-06-30.
- Observed regime points: 2019 was the best complete year at `+25.61%`, while
  2022 was the worst at `-20.40%`. These are return observations, not causal
  event attribution.
- Reconciliation note: the direct 2026-06-30 factsheet is the source for current
  NAV YTD and rolling fields. Other advisor/fund-list HTML captures showed
  conflicting YTD or inception metadata; those fields were not mixed into this
  page.

## Sources

- [Vanguard VTWO factsheet](https://workplace.vanguard.com/assets/corp/fund_communications/pdf_publish/us-products/fact-sheet/F3351.pdf) — official fund facts, 2026-06-30 NAV/market-price/benchmark returns, expense ratio, and standard deviation
- [Vanguard VTWO performance page](https://investor.vanguard.com/investment-products/etfs/profile/vtwo) — official annual NAV Total Return rows and quote inputs
- [Vanguard VTWO factsheet mirror](https://fund-docs.vanguard.com/FA3351_SPM.pdf) — official fund identity, exchange, return basis, and risk-field cross-check
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as-of 2025-12-31
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
