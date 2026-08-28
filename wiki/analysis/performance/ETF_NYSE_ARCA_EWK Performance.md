---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:EWK
input_ticker: EWK
ticker: EWK
exchange: NYSE Arca
fund: iShares MSCI Belgium ETF
tracked_index: MSCI Belgium IMI 25/50 Index (Net)
benchmark: S&P 500 Total Return
inception: 1996-03-12
management_mode: passive-index
updated: 2026-08-28
performance_as_of: 2026-06-30
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-08-26
nav_as_of: 2026-08-27
market_price_as_of: 2026-08-27
holdings_as_of: 2026-08-26
risk_as_of: 2026-07-31
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return; dividends and capital gains reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EWK
  - geography/Belgium
---

# EWK Performance

> Navigation: [[ETF Region Index]] → [[Belgium ETF]] → [[ETF Performance Index]]

## Bottom line

EWK คือ iShares MSCI Belgium ETF ที่จดทะเบียนบน `NYSE Arca` และเป็น
passive, single-country equity ETF ซึ่งติดตาม `MSCI Belgium IMI 25/50 Index
(Net)`. Official 2021-2025 NAV Total Return สะสม `41.43%` หรือ rounded-input
CAGR `7.18%`; issuer rolling 10-year NAV TR มี cumulative `98.26%` และ CAGR
`7.08%` ณ 30 มิ.ย. 2026. Current official NAV TR YTD ล่าสุดคือ `15.23%` ณ
26 ส.ค. 2026; latest NAV คือ `USD 27.68` ณ 27 ส.ค. 2026.

## Performance check

- `entity_key: NYSE Arca:EWK`; Fund: iShares MSCI Belgium ETF; inception
  `1996-03-12`; expense ratio `0.49%`; semi-annual distributions
- Metric: issuer `NAV Total Return` in USD, with dividends and capital gains
  reinvested and fund expenses deducted; market-price return is not mixed into
  NAV calculations
- Issuer benchmark: `MSCI Belgium IMI 25/50 Index (Net)`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ strategy-appropriate benchmark ของ Belgium single-country ETF)
- Management mode: `passive-index`; official objective คือ track a broad-based
  index composed of Belgian equities
- Official rolling 10-year window: `2016-06-30` to `2026-06-30`, `10.00 elapsed
  years`; NAV TR cumulative `98.26%`, CAGR `7.08%`; normalized endpoints are
  `100.00` and `198.26` from issuer cumulative return
- Current official snapshot: NAV `$27.68`, closing market price `$27.77`, and
  1-day NAV change `+$0.03 (+0.10%)` as of `2026-08-27`; net assets
  `$170,492,901`; current YTD NAV TR `15.23%` as of `2026-08-26`
- Annual coverage: complete official calendar years 2021-2025; no `*` or `†`
  markers. EWK began tracking the current IMI 25/50 index on `2012-11-09`; prior
  index history uses the MSCI Belgium Investable Market Index

| ปี | EWK NAV TR | MSCI Belgium IMI 25/50 Index (Net) | S&P 500 TR |
|---|---:|---:|---:|
| 2021 | 12.92% | 8.02% | 28.71% |
| 2022 | -14.08% | -15.89% | -18.11% |
| 2023 | 7.46% | 7.71% | 26.29% |
| 2024 | 0.51% | 0.51% | 25.02% |
| 2025 | 34.96% | 35.30% | 17.88% |

S&P 500 rows ใช้ cached USD Total Return convention, dividends reinvested,
reference as-of `2025-12-31`. EWK 2021-2025 NAV rows compound to `41.43%` /
`7.18%`; tracked index rows to `33.08%` / `5.88%`; arithmetic fund-minus-index
CAGR gap `+1.30 pp` ไม่เรียกว่า alpha. Cached S&P 500 TR คือ `96.17%` / `14.43%`,
จึงมี arithmetic EWK gap `-7.25 pp` เทียบ common reference นี้.

## Up years / Down years

- Complete 2021-2025 NAV TR up/down: `4 / 1`
- Best NAV TR year: 2025, `+34.96%`
- Least positive year: 2024, `+0.51%`
- Worst NAV TR year: 2022, `-14.08%`
- Current official NAV TR YTD: `+15.23%` as of `2026-08-26`

## Risk read-through

EWK เป็น single-country ETF ที่มี concentration สูงกว่ากอง broad Europe. Current
exposure ณ 26 ส.ค. 2026 มี Health Care `28.01%`, Consumer Staples `23.77%`,
Financials `16.78%`, Real Estate `9.36%`, Materials `7.31%` และ Industrials
`5.80%`; มี `38` holdings ณ 26 ส.ค.; P/E `19.22` และ P/B `1.80` ณ 26 ส.ค.;
3-year standard deviation `14.38%` และ beta `0.54` ณ 31 ก.ค. 2026; 30-day SEC
yield `1.75%` และ 12-month trailing yield `1.83%` ณ 31 ก.ค. 2026.

ความเสี่ยงหลักคือ Belgium/country concentration, sector/top-holdings concentration,
EUR/USD FX, small-fund size, liquidity, systematic fair-value pricing และ equity
volatility. Fund-minus-index gap เป็น tracking/fee/timing evidence ไม่ใช่ manager
skill. Official daily NAV series สำหรับคำนวณ maximum drawdown และ recovery date:
`ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Official iShares EWK product page](https://www.ishares.com/us/products/239610/ishares-msci-belgium-etf) — current NAV/price/YTD, exchange, benchmark, assets, holdings, exposures, rolling performance, fees and distributions; latest official capture through 2026-08-27
- [Official EWK factsheet](https://www.ishares.com/us/literature/fact-sheet/ewk-ishares-msci-belgium-etf-fund-fact-sheet-en-us.pdf) — official 2021-2025 NAV/index rows, rolling 10-year fields, return definitions, fee, launch, holdings, top holdings and benchmark-history note as of 2026-06-30
- [SEC EWK summary prospectus](https://www.ishares.com/us/literature/prospectus/p-ishares-inc-americas-emea-developed-8-31.pdf) — official NYSE Arca identity, objective, index methodology and risks
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference identity; annual rows reuse the cached skill convention
- [[ETF_performance_sources_2026-08-28]] | [[ETF Performance Index]]
