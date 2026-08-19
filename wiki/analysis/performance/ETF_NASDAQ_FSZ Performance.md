---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:FSZ
input_ticker: FSZ
ticker: FSZ
exchange: Nasdaq
fund: First Trust Switzerland AlphaDEX Fund
isin: US33737J2327
tracked_index: Nasdaq AlphaDEX Switzerland Index
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-08-19
performance_as_of: 2025-12-31
available_period_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-08-03
fund_facts_as_of: 2026-08-03
risk_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; USD; net of expenses; distributions reinvested
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FSZ
  - geography/Switzerland
---

# FSZ Performance

> Navigation: [[ETF Region Index]] → [[Switzerland ETF]] → [[ETF Performance Index]]

## Bottom line

FSZ คือ First Trust Switzerland AlphaDEX Fund, passive rules-based equity ETF
บน Nasdaq ที่ติดตาม `Nasdaq AlphaDEX Switzerland Index`. Official NAV Total
Return ใน complete calendar window 2016-2025 ให้ cumulative `148.00%` และ
rounded-input CAGR `9.51%`; เทียบ S&P 500 TR ที่ `298.33%` / `14.82%`. ใน
common window 2021-2025 FSZ ให้ `48.15%` / `8.18%` เทียบ S&P ที่ `96.17%` /
`14.43%`. Issuer rolling 10-year NAV TR คือ `10.05%` ณ 30 มิ.ย. 2026 และ
latest verified official NAV TR YTD คือ `+3.46%` ณ 30 มิ.ย. 2026; issuer
current NAV snapshot ใหม่กว่าคือ `US$82.02` ณ 3 ส.ค. 2026.

## Performance check

- `entity_key: NASDAQ:FSZ`; fund inception `14 ก.พ. 2012`; asset class international equity; semi-annual index rebalance; CUSIP `33737J232`; ISIN `US33737J2327`.
- Classification: supported `passive-index` equity ETF. First Trust states that the Fund seeks results corresponding generally to the price and yield of the equity `Nasdaq AlphaDEX Switzerland Index` before fees and expenses; the selection and rebalance rules are index-based.
- Metric: official `NAV Total Return` in USD, net of fund expenses, with distributions reinvested. Market-price return remains separate.
- Tracked index: `Nasdaq AlphaDEX Switzerland Index`; the index changed from the Defined Switzerland Index on `14 ก.ค. 2015`, before the complete 2016-2025 window.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark, not the tracked index). The issuer's official rolling/index rows are kept separate from the S&P comparison.
- Official current fields as of `3 ส.ค. 2026`: NAV `US$82.02`, market price `US$82.01`, net assets `US$36.91m`, 40 holdings excluding cash, and expense ratio `0.80%`. The latest official month-end performance capture is as of `30 มิ.ย. 2026`: NAV TR YTD `3.46%`, 1-year `9.55%`, 3-year annualised `12.76%`, 5-year `6.78%`, 10-year `10.05%`, and since inception `9.46%`.

| Year | FSZ NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 4.21% | 11.96% |
| 2017 | 31.26% | 21.83% |
| 2018 | -15.11% | -4.38% |
| 2019 | 25.91% | 31.49% |
| 2020 | 14.50% | 18.40% |
| 2021 | 19.34% | 28.71% |
| 2022 | -20.88% | -18.11% |
| 2023 | 22.07% | 26.29% |
| 2024 | -1.25% | 25.02% |
| 2025 | 30.16% | 17.88% |

**Up years / Down years**

- Up years / Down years: `7 / 3` ใน 2016-2025
- Best: 2017, `+31.26%`
- Least positive: 2020, `+14.50%`
- Worst: 2022, `-20.88%`
- Least bad down year: 2024, `-1.25%`
- 2016-2025 cumulative/CAGR: FSZ `148.00%` / `9.51%`; S&P 500 TR `298.33%` / `14.82%`
- 2021-2025 cumulative/CAGR: FSZ `48.15%` / `8.18%`; S&P 500 TR `96.17%` / `14.43%`

### Official tracked-index comparison

| Period ended 30 Jun 2026 | FSZ NAV TR | Nasdaq AlphaDEX Switzerland Index | Fund minus index |
|---|---:|---:|---:|
| 3 months | 4.35% | 6.52% | -2.17 pp |
| YTD | 3.46% | 3.85% | -0.39 pp |
| 1 year | 9.55% | 11.05% | -1.50 pp |
| 3 years annualised | 12.76% | 13.50% | -0.74 pp |
| 5 years annualised | 6.78% | 7.21% | -0.43 pp |
| 10 years annualised | 10.05% | 10.57% | -0.52 pp |

These are passive tracking observations from the issuer's comparison table,
not arithmetic alpha. The issuer also shows MSCI Switzerland Index as a broader
context index; it is not substituted for FSZ's tracked AlphaDEX index.

## Risk read-through

FSZ is a concentrated single-country Switzerland strategy with a rules-based
growth/value selection process rather than a market-cap broad-market portfolio.
Official sector weights as of `3 ส.ค. 2026` include Industrials `30.02%`,
Financials `19.72%`, and Health Care `19.01%`; top holdings include Sulzer
`4.75%`, Swiss Re `4.43%`, BKW `4.14%`, Flughafen Zurich `4.02%`, and Vontobel
`3.93%`. Official 3-year standard deviation is `14.51%` as of `30 มิ.ย. 2026`.

The index selection, semi-annual rebalance, small/mid-cap exposure, limited fund
size, low trading volume and Switzerland/CHF/country concentration can cause
behavior to differ from broad Switzerland or Europe market-cap indexes. First
Trust's official statistics show the Nasdaq AlphaDEX comparison, but no manager
skill or alpha claim is made here. Daily NAV history sufficient for maximum
drawdown and recovery was not disclosed in the reviewed official sources, so
`risk-adjusted evidence: not-verified` for that metric.

## Sources

- [First Trust FSZ fund page](https://www.ftportfolios.com/retail/etf/etfsummary.aspx?Ticker=FSZ) — official identity, index objective, exchange, inception, current NAV/AUM/holdings/sectors, fees and month-end performance.
- [First Trust FSZ prospectus](https://www.ftportfolios.com/LoadContent/gradkqbz8r4y) — official 2016-2025 calendar-year NAV returns, index-change history, fees, risks and annualized index comparison; performance periods ended 31 Dec 2025.
- [First Trust FSZ holdings](https://www.ftportfolios.com/Retail/etf/ETFholdings.aspx?Ticker=FSZ) — official holdings and weights as of 31 Jul 2026.
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow convention — USD Total Return with dividends reinvested; reference window 2016-2025 as of 31 Dec 2025.
- ETF source batch: [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
