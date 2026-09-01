---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FDRR
ticker: FDRR
exchange: NYSE Arca
fund: Fidelity Dividend ETF for Rising Rates
tracked_index: Fidelity Dividend Index for Rising Rates
issuer_benchmark: Fidelity Dividend Index for Rising Rates
secondary_benchmark: Russell 1000 Index
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-09-02
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-1.md
return_basis: NAV total return; distributions reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FDRR
  - geography/United-States
---

# FDRR Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

FDRR เป็น rules-based, strategic-beta U.S. equity ETF ที่เน้นหุ้น large/mid-cap
ซึ่งจ่ายและมีแนวโน้มเพิ่ม dividend และมี positive correlation กับการเพิ่มขึ้นของ
10-year U.S. Treasury yields. Official complete calendar-year NAV Total Return
2017-2025 สะสม `199.31%` หรือ rounded-input CAGR `12.95%`; ช่วง 2021-2025
สะสม `88.98%` และ CAGR `13.57%`. Current official NAV TR YTD ล่าสุดที่ตรวจพบ
คือ `8.18%` ณ 30 มิ.ย. 2026; 2016 เป็น inception-year partial ที่ไม่มี complete
calendar return จึงไม่ถูกจัดอันดับ.

## Performance check

- `entity_key: NYSE Arca:FDRR`; fund `Fidelity Dividend ETF for Rising Rates`; inception `2016-09-12`; exchange `NYSE Arca`.
- Metric: `NAV Total Return` in USD, including changes in share price and reinvestment of dividends/capital gains, with the NAV and market-price series kept separate.
- Management mode: `passive-index` / `Strategic Beta`; Fidelity states that the fund normally invests at least 80% in securities included in the underlying index or related depositary receipts.
- Tracked index and issuer benchmark: `Fidelity Dividend Index for Rising Rates`; it selects large- and mid-cap dividend-paying companies expected to continue paying and growing dividends and to have positive correlation with rising 10-year Treasury yields. Secondary benchmark: `Russell 1000 Index`.
- Expense ratio: `0.15%` gross and net as reported in the June 30, 2026 factsheet. Portfolio assets were `$708.8M` and total holdings `114` at that date.
- Current official fields: NAV TR YTD `8.18%`, 1-year NAV TR `22.91%`, 3-year annualized `18.95%`, 5-year annualized `12.00%`, and since-inception annualized `13.28%`, all as of 30 มิ.ย. 2026. Fidelity's quote page separately displayed market price `69.4146` and NAV `69.242463` in the current capture, but did not expose a quote date; these values are context-only and not used in the calendar calculations.
- 10-year NAV TR CAGR: `not applicable`; the 2016 inception-year cell is blank and only nine complete calendar years (2017-2025) are verified. Calendar-window calculation: normalized endpoints `100.00 → 299.31`; formula `(299.31 / 100.00)^(1 / 9.00) - 1 = 12.95%`, a rounded-input approximation.
- Common reference benchmark: `S&P 500 Total Return` (USD, dividends reinvested). It is not the issuer benchmark and no current same-date S&P YTD spread is inferred.

| Year | FDRR NAV TR | Fidelity Dividend Index | Russell 1000 TR | S&P 500 TR |
|---|---:|---:|---:|---:|
| 2017 | 19.51% | 19.93% | 21.69% | 21.83% |
| 2018 | -3.23% | -2.96% | -4.78% | -4.38% |
| 2019 | 26.55% | 27.01% | 31.43% | 31.49% |
| 2020 | 8.22% | 8.51% | 20.96% | 18.40% |
| 2021 | 26.02% | 26.42% | 26.45% | 28.71% |
| 2022 | -9.45% | -9.14% | -19.13% | -18.11% |
| 2023 | 13.61% | 13.87% | 26.53% | 26.29% |
| 2024 | 20.29% | 20.47% | 24.51% | 25.02% |
| 2025 | 21.18% | 21.36% | 17.37% | 17.88% |
| 2017-2025 cumulative | 199.31% | 206.72% | 248.32% | 255.78% |
| 2017-2025 CAGR | 12.95% | 13.26% | 14.87% | 15.14% |
| 2021-2025 cumulative | 88.98% | 91.23% | 89.09% | 96.17% |
| 2021-2025 CAGR | 13.57% | 13.84% | 13.59% | 14.43% |

## Up years / Down years

- Up years / Down years: `7 / 2` across complete calendar years 2017-2025.
- Best: `2019`, `+26.55%`.
- Least positive: `2020`, `+8.22%`.
- Worst: `2022`, `-9.45%`.
- Least bad down year: `2018`, `-3.23%`.
- Current official NAV TR YTD: `+8.18%` as of 30 มิ.ย. 2026; no synchronized current S&P 500 TR comparison is inferred.
- The small differences versus the Fidelity index are tracking/fee differences; the larger Russell 1000 and S&P 500 differences are reference comparisons, not arithmetic `alpha`.

## Risk read-through

Fidelity reports 3-year beta `1.00`, standard deviation `12.19%`, Sharpe ratio
`1.16`, R-squared `1.00`, tracking error `0.04%`, and alpha `-0.14` versus the
Fidelity index as of 30 มิ.ย. 2026. These are issuer risk measures and are kept
separate from annual-return arithmetic. Population standard deviation from the
nine rounded annual NAV rows is `12.03%`, not daily volatility. The year-end
observation path gives a maximum drawdown approximation of `-9.45%` in 2022, with
year-end recovery by 2023; daily maximum drawdown and recovery duration are
`ไม่พบข้อมูลที่ยืนยันได้`.

ความเสี่ยงหลักคือ U.S. equity drawdowns, value/dividend-factor rotation, sector
concentration, interest-rate sensitivity, tracking error, smaller-company
volatility, foreign exposure (a small portion of the portfolio), and derivative
or securities-lending implementation risk. The 30-day SEC yield `2.10%` is a
separate income metric and is not NAV Total Return.

## Sources

- [Fidelity FDRR June 2026 factsheet](https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F9880841.PDF) — official identity, strategy, NAV/market-price return definitions, 2017-2025 calendar returns, benchmarks, YTD/period returns, risk measures, holdings and fund facts as of 30 มิ.ย. 2026
- [Fidelity FDRR quote page](https://digital.fidelity.com/prgw/digital/research/quote/dashboard/summary?symbol=FDRR) — official current quote-page context for market price/NAV; capture did not expose a quote date
- [Fidelity FDRR summary prospectus](https://institutional.fidelity.com/app/proxy/content?literatureURL=%2FB-CT19-SUM.PDF) — official objective, risks, and fund disclosure
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached `check-etf-performance` references — common USD Total Return benchmark for 2017-2025
- Source batch: [[ETF_performance_sources_2026-09-02_run-1]]
