---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:PXF
ticker: PXF
exchange: NYSE Arca
fund: Invesco RAFI Developed Markets ex-U.S. ETF
tracked_index: RAFI Fundamental Select Developed ex-US 1000 Index
issuer_benchmark: MSCI EAFE Index (USD)
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-09-02
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-03-31
current_ytd_as_of: 2026-05-31
fund_facts_as_of: 2026-03-31 / 2026-07-02
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-1.md
return_basis: NAV total return; distributions reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/PXF
  - geography/International
---

# PXF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

PXF เป็น passive, rules-based developed-markets ex-U.S. equity ETF ที่ถ่วงน้ำหนัก
ด้วย fundamental measures ไม่ใช่ market capitalization. Official complete
calendar-year NAV Total Return 2016-2025 สะสม `152.81%` หรือ rounded-input CAGR
`9.72%`; ช่วง 2021-2025 สะสม `84.55%` และ CAGR `13.04%`. Official rolling
10-year NAV annualized return คือ `10.71%` ณ 31 มี.ค. 2026 ซึ่งเป็นคนละ window
กับ calendar-year CAGR. Current issuer NAV TR YTD ล่าสุดที่ตรวจพบคือ `19.82%`
ณ 31 พ.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:PXF`; fund `Invesco RAFI Developed Markets ex-U.S. ETF`; inception `2007-06-25`; exchange `NYSE Arca`.
- Metric: `NAV Total Return` in USD, with distributions reinvested and fund expenses reflected. Market-price returns are kept separate.
- Management mode: `passive-index`; Invesco describes the fund as based on a fundamental index and states that the fund and index are reconstituted annually.
- Tracked index: current `RAFI Fundamental Select Developed ex-US 1000 Index`, which selects developed-market ex-U.S. equities using book value, cash flow, sales, and dividends. The current index replaced `FTSE RAFI Developed ex U.S. 1000 Index` after 21 มี.ค. 2025; the change is disclosed, not backfilled as an unchanged index series.
- Expense ratio: `0.43%`; issuer benchmark: `MSCI EAFE Index (USD)`; common reference benchmark: `S&P 500 Total Return` (USD, dividends reinvested).
- Current official fields: NAV TR YTD `19.82%` as of 31 พ.ค. 2026 and SEC 30-day yield `2.18%` as of 2 ก.ค. 2026. The latest captured issuer page did not disclose a same-date current NAV/market-price quote.
- Official rolling 10-year NAV annualized return: `10.71%` as of 31 มี.ค. 2026. Calendar-window calculation uses complete 2016-2025 rows: normalized endpoints `100.00 → 252.81`; formula `(252.81 / 100.00)^(1 / 10.00) - 1 = 9.72%`. This is a rounded-input approximation, not a replacement for the issuer's rolling figure.
- Coverage: Invesco's Q1 2026 factsheet provides complete 2016-2025 NAV rows and official benchmark rows; the product page provides the newer YTD and yield fields.

| Year | PXF NAV TR | MSCI EAFE NR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 6.51% | 1.00% | 11.96% |
| 2017 | 24.78% | 25.03% | 21.83% |
| 2018 | -15.12% | -13.79% | -4.38% |
| 2019 | 17.81% | 22.01% | 31.49% |
| 2020 | 3.08% | 7.82% | 18.40% |
| 2021 | 15.20% | 11.26% | 28.71% |
| 2022 | -9.24% | -14.45% | -18.11% |
| 2023 | 18.90% | 18.24% | 26.29% |
| 2024 | 4.35% | 3.82% | 25.02% |
| 2025 | 42.26% | 31.22% | 17.88% |
| 2016-2025 cumulative | 152.81% | 119.58% | 298.33% |
| 2016-2025 CAGR | 9.72% | 8.18% | 14.82% |
| 2021-2025 cumulative | 84.55% | 53.32% | 96.17% |
| 2021-2025 CAGR | 13.04% | 8.92% | 14.43% |

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016-2025.
- Best: `2025`, `+42.26%`.
- Least positive: `2024`, `+4.35%`.
- Worst: `2018`, `-15.12%`.
- Least bad down year: `2022`, `-9.24%`.
- Current official NAV TR YTD: `+19.82%` as of 31 พ.ค. 2026; no synchronized current S&P 500 TR comparison is inferred.
- Differences versus MSCI EAFE or S&P 500 are arithmetic reference comparisons. They are not `alpha`, particularly because PXF is passive and its underlying index changed in 2025.

## Risk read-through

Population standard deviation from the ten rounded annual NAV rows is `15.85%`;
this is not daily volatility. The year-end observation path gives a maximum
drawdown approximation of `-15.12%` in 2018, with cumulative year-end wealth back
above the prior high by 2020. Daily maximum drawdown, recovery duration, downside
capture, and compatible risk-adjusted evidence are `ไม่พบข้อมูลที่ยืนยันได้`.

ความเสี่ยงหลักคือ foreign currency and country exposure, developed-market equity
drawdowns, fundamental/value-factor underperformance, index-reconstitution and
tracking risk, small/mid-cap exposure, liquidity, and possible regional or sector
concentration. The SEC yield `2.18%` is a separate income metric and is not NAV
Total Return.

## Sources

- [Invesco PXF product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-rafi-developed-markets-ex-u-s-etf.html) — official identity, exchange, inception, index methodology/change, expense ratio, current YTD NAV return, and SEC yield
- [Invesco PXF Q1 2026 factsheet](https://www.invesco.com/content/dam/invesco/us/en/product-documents/etf/fact-sheet/pxf-invesco-ftse-rafi-developed-markets-ex-u-s-etf-fact-sheet.pdf) — official 2016-2025 NAV/benchmark rows, rolling returns, return basis, holdings, and fund facts as of 31 มี.ค. 2026
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD Total Return benchmark for 2016-2025
- Source batch: [[ETF_performance_sources_2026-09-02_run-1]]
