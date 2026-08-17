---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EPOL
ticker: EPOL
exchange: NYSE Arca
fund: iShares MSCI Poland ETF
tracked_index: MSCI Poland IMI 25/50 Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-13
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-08-14
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EPOL
  - geography/Poland
---

# EPOL Performance

> Navigation: [[ETF Region Index]] → [[Poland ETF]] → [[ETF Performance Index]]

## Bottom line

EPOL ให้ cumulative `NAV Total Return` ประมาณ `154.36%` ใน complete calendar
years 2016-2025 หรือ rounded-input CAGR `9.79%`; บวก 5 ปีและลบ 5 ปี. ปีดีที่สุด
คือ 2025 `+76.25%` และแย่ที่สุดคือ 2022 `-24.53%`. Current official NAV TR YTD
คือ `+26.40%` ณ 2026-08-13. ใน common window 2021-2025 EPOL ให้ CAGR
`16.89%` เทียบ S&P 500 TR `17.34%`; tracked-index comparison ใน factsheet
แสดง 5Y `16.54%` เทียบ MSCI Poland IMI 25/50 `16.91%` หรือ tracking gap
`-0.37 pp`.

## Performance check

- `entity_key: NYSE Arca:EPOL`; inception `2010-05-25`; exchange `NYSE Arca`.
- Metric: `NAV Total Return` (USD), distributions reinvested หลังหัก fund expenses.
- Tracked index (issuer benchmark): `MSCI Poland IMI 25/50 Index`.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ EPOL).
- Expense ratio `0.59%`; distribution frequency semi-annual; official net assets `US$859.8M`, NAV `US$44.43`, closing price `US$44.45` ณ 2026-08-14.
- Official rolling performance ณ 2026-06-30: NAV TR `1Y 25.00%`, `3Y 32.43%`, `5Y 16.54%`, `10Y 11.71%`, inception `6.12%`; benchmark `25.90%`, `32.52%`, `16.91%`, `12.18%`, `6.70%`.
- Current official YTD NAV TR: `+26.40%` ณ 2026-08-13. Same-date tracked-index YTD was not disclosed in the reviewed current page.
- Annual coverage: official complete calendar years 2016-2025; 2016-2020 issuer table values are rounded to one decimal and 2021-2025 use the official U.S. page values to two decimals.
- S&P 500 cache 2016-2025: cumulative `298.33%`; CAGR `14.82%` from rounded annual inputs.

| ปี | EPOL NAV TR | MSCI Poland IMI 25/50 | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 2.80% | 3.70% | 11.96% |
| 2017 | 52.70% | 53.80% | 21.83% |
| 2018 | -14.30% | -14.00% | -4.38% |
| 2019 | -5.60% | -4.60% | 31.49% |
| 2020 | -8.20% | -8.30% | 18.40% |
| 2021 | 12.15% | 13.37% | 28.71% |
| 2022 | -24.53% | -24.82% | -18.11% |
| 2023 | 50.13% | 52.23% | 26.29% |
| 2024 | -2.58% | -2.04% | 25.02% |
| 2025 | 76.25% | 75.05% | 17.88% |

## Up years / Down years

- Up years / Down years: `5 / 5` ใน 2016-2025.
- Best: 2025, `+76.25%`; least positive: 2021, `+12.15%`.
- Worst: 2022, `-24.53%`; least bad down year: 2018, `-14.30%`.
- 2016-2025 EPOL cumulative `154.36%` / CAGR `9.79%`; 2021-2025 cumulative `118.18%` / CAGR `16.89%`.
- 2021-2025 tracked-index cumulative `122.49%` / CAGR `17.34%`; EPOL trailed by about `-0.46 pp` CAGR. The official rolling 5Y gap is `-0.37 pp`.
- Current YTD: EPOL NAV `+26.40%` ณ 13 ส.ค. 2026; this is not compared with a same-date S&P or tracked-index return.

## Risk read-through

EPOL เป็น passive single-country Poland equity exposure with concentration in
Financials `44.17%`, Energy `13.43%`, and Consumer Discretionary `13.20%` ณ
2026-08-14; the fund held 32 names. Official 3-year standard deviation คือ
`21.37%`, equity beta `0.55`, P/E `16.13` และ P/B `2.08` จาก the reviewed
issuer snapshot. PLN/USD country and FX risk, sector concentration, emerging/
European cycle risk, and liquidity risk matter more than broad global ETF
diversification. Official daily NAV maximum drawdown and recovery date are
`ไม่พบข้อมูลที่ยืนยันได้`; annual returns show meaningful downside in 2018,
2020, 2022, and 2024.

## Sources

- [iShares EPOL product page](https://www.ishares.com/us/products/239676/ishares-msci-poland-etf) — current YTD, fund facts, holdings, exposures, and fees.
- [iShares EPOL performance page](https://www.ishares.com/us/products/239676/ishares-msci-poland-capped-etf?fundSearch=true&qt=EPOL) — official rolling, cumulative, calendar 2021-2025, and benchmark returns.
- [BlackRock EPOL calendar-year performance](https://www.ishares.com/ch/professionals/en/products/239676/ishares-msci-poland-capped-etf) — official USD calendar rows 2016-2025.
- [EPOL summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-poland-capped-etf-8-31.pdf) — fund objective, ticker, exchange, and fee disclosures.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
