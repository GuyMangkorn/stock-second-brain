---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:LVHI
ticker: LVHI
exchange: Cboe BZX
fund: Franklin International Low Volatility High Dividend Index ETF
tracked_index: Franklin International Low Volatility High Dividend Hedged Index-NR
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-09-02
performance_as_of: 2026-06-30
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-06
price_nav_as_of: 2026-08-06
fund_facts_as_of: 2026-06-30 / 2026-08-06
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-1.md
return_basis: NAV total return; distributions reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/LVHI
  - geography/International
---

# LVHI Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

LVHI เป็น passive, rules-based international developed-market equity ETF ที่คัด
หุ้น high-dividend และ low-volatility พร้อม currency hedge. Official NAV Total
Return ใน complete calendar years 2017-2025 สะสม `143.40%` หรือ rounded-input
CAGR `10.39%`; มีปีบวก/ลบ `7 / 2`. Best year คือ 2025 ที่ `+27.77%`, worst year
คือ 2020 ที่ `-8.79%`, และ current official NAV TR YTD ล่าสุดคือ `+18.27%` ณ
2026-08-06. ปี 2016 เป็น inception-year partial ที่ factsheet ไม่รายงานเป็น
annual NAV return จึงไม่ถูกจัดอันดับ.

## Performance check

- `entity_key: Cboe BZX:LVHI`; fund `Franklin International Low Volatility High Dividend Index ETF`; inception `2016-07-27`; listing `Cboe BZX`.
- Metric: `NAV Total Return` in USD, assuming reinvestment of all distributions and deduction of fund expenses. Market-price returns are kept separate.
- Management mode: `passive-index`; the official factsheet classifies the ETF as Indexed and Equity. The fund uses currency-related derivatives to hedge exposure; the payoff is not leverage, inverse, option-income, bond, commodity, or multi-asset.
- Tracked index: `Franklin International Low Volatility High Dividend Hedged Index-NR`; investment universe `MSCI World ex US IMI (Local) Index-NR`; expense ratio `0.40%`.
- Current official snapshot: NAV `$42.72`, NAV TR YTD `18.27%`, net assets `$5.57B`, and distribution rate at NAV `5.86%` as of 2026-08-06. Holdings `194` and 30-day SEC yield `2.85%` as of 2026-06-30.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark, not the issuer index). Cached rows are used for the identical 2017-2025 subset.
- 10-year NAV TR: `not applicable`; only nine complete annual observations are verified because the 2016 inception-year observation is not disclosed as a full calendar-year NAV return. Official since-inception NAV return is `11.26%` annualized as of 2026-06-30, kept separate from a 10-year metric.
- Coverage/source note: Franklin factsheet provides official 2017-2025 NAV rows and the current June 2026 fund facts; the product page provides the newer August 2026 NAV/YTD snapshot. No 2016 partial return is inferred.

| Year | LVHI NAV TR | S&P 500 TR |
|---|---:|---:|
| 2017 | 11.66% | 21.83% |
| 2018 | -5.44% | -4.38% |
| 2019 | 18.81% | 31.49% |
| 2020 | -8.79% | 18.40% |
| 2021 | 18.42% | 28.71% |
| 2022 | 3.80% | -18.11% |
| 2023 | 17.22% | 26.29% |
| 2024 | 15.55% | 25.02% |
| 2025 | 27.77% | 17.88% |
| 2017-2025 cumulative | 143.40% | 255.78% |
| 2017-2025 CAGR | 10.39% | 15.14% |
| 2021-2025 cumulative | 112.73% | 96.17% |
| 2021-2025 CAGR | 16.30% | 14.43% |

**Up years / Down years**

- Up years / Down years: `7 / 2` across complete calendar years 2017-2025.
- Best: 2025, `+27.77%`.
- Least positive: 2022, `+3.80%`.
- Worst: 2020, `-8.79%`.
- Least bad down year: 2018, `-5.44%`.
- Current official NAV TR YTD: `+18.27%` as of 2026-08-06; no synchronized current S&P 500 comparison is inferred.

## Risk read-through

LVHI มี annual-return population standard deviation `11.41%` ใน complete
2017-2025 rows; นี่ไม่ใช่ daily volatility. Year-end observation จาก annual rows
ให้ maximum drawdown approximation `-8.79%` ใน 2020 และ cumulative year-end
กลับเหนือจุดสูงสุดเดิมภายใน 2021; daily maximum drawdown, recovery duration,
downside capture และ compatible risk-adjusted evidence ยังเป็น `ไม่พบข้อมูลที่
ยืนยันได้`. ความเสี่ยงหลักคือ international equity, country/sector
concentration, currency hedge mismatch, dividend/value-factor rotation,
rebalancing และ derivatives counterparty/implementation risk. Expense ratio คือ
`0.40%`; official 30-day SEC yield `2.85%` และ distribution rate `5.86%` เป็นคนละ
metric กับ NAV Total Return.

## Sources

- [Franklin LVHI product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/91481/SINGLCLASS/franklin-international-low-volatility-high-dividend-index-etf/LVHI) — official identity, Cboe BZX listing, objective, index, expense ratio, current NAV/YTD, distribution rate, and fund facts through 2026-08-06
- [Franklin LVHI factsheet](https://www.franklintempleton.com/forms-literature/download/91481-FF) — official classification, return basis, 2017-2025 annual NAV rows, June 2026 holdings/yield, and since-inception return
- [Franklin LVHI summary prospectus](https://www.franklintempleton.com/forms-literature/download-preview/91481-PSUM) — official strategy and derivative/hedging disclosures
- [Cboe LVHI listing](https://www.cboe.com/us/equities/listings/listed_products/symbols/LVHI/) — exchange/ticker cross-check
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD Total Return benchmark for the 2017-2025 subset
- Source batch: [[ETF_performance_sources_2026-09-02_run-1]] | [[ETF Performance Index]]
