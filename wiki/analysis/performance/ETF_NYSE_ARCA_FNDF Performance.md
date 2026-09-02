---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FNDF
input_ticker: FNDF
ticker: FNDF
exchange: NYSE Arca
fund: Schwab Fundamental International Equity ETF
tracked_index: RAFI Fundamental High Liquidity Developed ex US Large Index (Net)
benchmark: RAFI Fundamental High Liquidity Developed ex US Large Index (Net)
management_mode: passive-index
updated: 2026-09-02
performance_as_of: 2025-12-31 (official calendar) / 2026-07-31 (official standardized)
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-31
fund_facts_as_of: 2026-08-31 / 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-09-02_recheck.md
return_basis: NAV total return; distributions reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FNDF
  - geography/International
---

# FNDF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

FNDF เป็น passive, rules-based international large-company ETF ที่ใช้ fundamental
weighting ซึ่งมี value/yield tilt มากกว่าการถ่วงน้ำหนักตาม market cap. Official NAV
Total Return ช่วง 2016-2025 สะสม `158.78%`; official SEC 10-year average annual
NAV TR คือ `9.98%` ขณะที่ rounded-input calendar CAGR จาก annual rows คือ `9.97%`.
มีปีบวก/ลบ `8 / 2`. Best year คือ 2025 ที่ `+40.73%`, worst year คือ 2018 ที่
`-14.19%`, และ current official NAV TR YTD ล่าสุดคือ `+20.44%` ณ 2026-07-31.
Issuer rolling 10-year NAV TR อยู่ที่ `11.73%` ณ วันเดียวกัน ซึ่งเป็นคนละ window
กับ calendar CAGR.

## Performance check

- `entity_key: NYSE Arca:FNDF`; fund `Schwab Fundamental International Equity ETF`; inception `2013-08-15`; exchange `NYSE Arca, Inc.`
- Tracked index: `RAFI Fundamental High Liquidity Developed ex US Large Index (Net)`; objective คือวัดหุ้น developed markets นอกสหรัฐฯ ที่จัดน้ำหนักตาม fundamental size/weight.
- Metric: `NAV Total Return` in USD, including reinvested distributions and net of expenses. Market-price returns are kept separate.
- Current official snapshot: NAV `US$55.66`, bid/ask midpoint `US$55.53`, premium/discount `-0.17%`, net assets `US$26.18B`, and holdings `906` as of 2026-08-31.
- Expense ratio `0.25%`, portfolio turnover `12.46%` as of 2026-07-31, 3-year beta versus benchmark `1.00`, and 3-year standard deviation `13.99%`.
- Under the current SEC prospectus, the fund normally invests at least 90% of net assets in index stocks or depositary receipts; it does not hedge foreign-currency exposure and may use forwards for securities awaiting settlement.
- The issuer benchmark changed on 2024-06-21 from `Russell RAFI Developed ex US Large Company Index (Net)` to the current `RAFI Fundamental High Liquidity Developed ex US Large Index (Net)`; this history is not silently treated as one unchanged index.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark; cached 2016-2025 convention as of 2025-12-31).
- 10-year window: `2015-12-31` to `2025-12-31`; normalized TR values `100.00 → 258.78`; `Years: 10.00`.
- Official SEC 10-year average annual NAV TR: `9.98%` as of 2025-12-31; rounded-row calculation: `9.97%`; issuer rolling 10-year NAV TR: `11.73%` as of 2026-07-31. Formula: `(End TR / Start TR)^(1 / Years) - 1`.
- Coverage/source note: SEC summary prospectus provides official 2016-2025 annual NAV rows and the 9.98% 10-year field. The current Schwab product page provides standardized NAV performance through 2026-07-31 and current price/NAV/fund facts through 2026-08-31.

| Year / window | FNDF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 7.70% | 11.96% |
| 2017 | 23.81% | 21.83% |
| 2018 | -14.19% | -4.38% |
| 2019 | 18.41% | 31.49% |
| 2020 | 4.02% | 18.40% |
| 2021 | 14.52% | 28.71% |
| 2022 | -7.77% | -18.11% |
| 2023 | 20.34% | 26.29% |
| 2024 | 2.65% | 25.02% |
| 2025 | 40.73% | 17.88% |
| 2016-2025 cumulative | 158.78% | 298.33% |
| 2016-2025 CAGR | 9.97% | 14.82% |
| 2021-2025 cumulative | 83.62% | 96.17% |
| 2021-2025 CAGR | 12.92% | 14.43% |

**Up years / Down years — complete 2016-2025 window**

- Up years / Down years: `8 / 2`.
- Best: 2025, `+40.73%`.
- Least positive: 2024, `+2.65%`.
- Worst: 2018, `-14.19%`.
- Least bad down year: 2022, `-7.77%`.
- Current official NAV TR YTD: `+20.44%` as of 2026-07-31; no synchronized current S&P 500 comparison is inferred.

## Risk read-through

FNDF มี 3-year standard deviation `13.99%` และ beta `1.00` เทียบ benchmark ณ
2026-07-31; official snapshot มี 906 holdings, expense ratio `0.25%`, and TTM
distribution yield `3.01%`. Fundamental reweighting, value/yield exposure, foreign
currency, developed-market country/sector concentration, tracking difference,
liquidity, and premium/discount เป็นความเสี่ยงหลัก. Reviewed official sources did
not provide a daily NAV series sufficient to verify maximum drawdown, recovery
duration, downside capture, or compatible risk-adjusted evidence; those metrics
จึงเป็น `ไม่พบข้อมูลที่ยืนยันได้` และไม่ได้แทนด้วย market-price proxy.

## Sources

- [Schwab Asset Management FNDF product page](https://www.schwabassetmanagement.com/products/fndf) — official identity, NYSE Arca listing, inception, index, expense ratio, current NAV/price, holdings, fund facts, standardized NAV returns, and benchmark-change note.
- [SEC FNDF Summary Prospectus, June 26, 2026](https://www.sec.gov/Archives/edgar/data/1454889/000088454626000305/c497k.htm) — official objective, distribution-reinvestment basis, risk disclosures, and 2016-2025 annual NAV total returns.
- [Schwab FNDF performance page](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=fndf) — official platform cross-check for current standardized return fields.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD Total Return benchmark for complete 2016-2025 calendar years.
- [[ETF_performance_sources_2026-09-02_recheck]] | [[ETF Performance Index]]
