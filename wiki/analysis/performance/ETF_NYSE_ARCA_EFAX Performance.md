---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EFAX
ticker: EFAX
exchange: NYSE Arca
fund: State Street SPDR MSCI EAFE Fossil Fuel Reserves Free ETF
tracked_index: MSCI EAFE ex Fossil Fuels Index
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-09-01
performance_as_of: 2026-07-31
rolling_10y_as_of: not applicable (<10y history)
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-5.md
return_basis: NAV total return; distributions reinvested; net of fees
return_currency: USD
primary_region: International
tags:
  - analysis/etf-performance
  - ticker/EFAX
  - geography/International
---

# EFAX Performance

> [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

EFAX เป็น passive/index-tracking international developed-market equity ETF ที่
ติดตาม `MSCI EAFE ex Fossil Fuels Index` และตัดบริษัทที่มี fossil-fuel reserves
ตามเกณฑ์ของ MSCI. Official NAV Total Return ล่าสุดที่ตรวจสอบได้คือ `+10.16%`
YTD ณ 2026-07-31 และ NAV ล่าสุดคือ `US$56.03` ณ 2026-08-28. Official capture
ที่ตรวจสอบไม่แสดง annual calendar NAV rows หรือ raw endpoints ครบ 10 ปี จึงไม่
คำนวณ calendar CAGR, up/down-year ranking หรือ 10-year NAV CAGR.

## Performance check

- `entity_key: NYSE Arca:EFAX`; fund `State Street SPDR MSCI EAFE Fossil Fuel Reserves Free ETF`; inception `2016-10-24`; listing `2016-10-25`; trading currency USD
- Classification: supported `passive-index` international developed-market equity ETF; official prospectus describes index sampling and no payoff-defining leverage, inverse, option-income, bond, commodity, or currency structure.
- Metric: `NAV Total Return` รวม reinvested dividends/capital gains และ net fund expenses; market-price return ไม่ถูกนำมาปน
- Tracked index: `MSCI EAFE ex Fossil Fuels Index`; the parent universe covers developed-market Europe, Australasia, and Far East countries excluding the U.S. and Canada.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark, not EFAX's tracked index). Cached rows are as of 2025-12-31.
- 10-year NAV TR: `not applicable (<10y history)` because the fund launched in October 2016; raw endpoints are not disclosed in the reviewed issuer capture.
- Official current performance table as of 2026-07-31: NAV YTD `10.16%`, 1-year `22.15%`, 3-year annualized `15.69%`, 5-year annualized `8.53%`, and since-inception annualized `9.29%`.
- Coverage/source note: official annual NAV rows for 2016-2025 were not readable in the reviewed SEC/prospectus capture; no secondary annual proxy is substituted.

| Year | EFAX NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | 11.96% |
| 2017 | not disclosed | 21.83% |
| 2018 | not disclosed | -4.38% |
| 2019 | not disclosed | 31.49% |
| 2020 | not disclosed | 18.40% |
| 2021 | not disclosed | 28.71% |
| 2022 | not disclosed | -18.11% |
| 2023 | not disclosed | 26.29% |
| 2024 | not disclosed | 25.02% |
| 2025 | not disclosed | 17.88% |

**Up years / Down years**

- Up years / Down years: not disclosed because official calendar-year NAV rows are not available.
- Best / least positive / worst / least bad down year: not disclosed.
- Current official NAV TR YTD: `+10.16%` as of 2026-07-31; current NAV `US$56.03`, closing price `US$55.76`, and premium/discount `-0.48%` as of 2026-08-28.

## Risk read-through

EFAX มี country, currency, foreign-market, large-/mid-cap, sector and fossil-fuel
screening risks. The issuer reports `641` holdings, forward P/E `16.76x`, P/B
`2.43x`, and fund distribution yield `3.04%` as of 2026-08-28; gross expense
ratio is `0.20%` as of 2026-08-31. The latest official 3-year NAV TR is `15.69%`
annualized, but a compatible daily NAV series for maximum drawdown, recovery,
volatility, downside capture, or risk-adjusted evidence was not verified.
Foreign-currency movements and the fossil-fuel-reserves exclusion can cause
returns to differ from a broad EAFE portfolio.

## Sources

- [State Street EFAX product page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-msci-eafe-fossil-fuel-reserves-free-etf-efax) — identity, exchange, inception, benchmark, NAV/price, holdings, fund facts, yields, and current standardized performance; accessed 2026-09-01
- [Official EFAX factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-efax.pdf) — official return basis, fees, characteristics, and performance through 2026-06-30
- [SEC EFAX summary prospectus](https://www.sec.gov/Archives/edgar/data/1168164/000119312526031207/d72607d497k.htm) — passive strategy, fees, index methodology, risk disclosures, and year-end standardized performance; January 31, 2026
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [2016-2019](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2018-2022](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2022-2025](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/)
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-5]]
