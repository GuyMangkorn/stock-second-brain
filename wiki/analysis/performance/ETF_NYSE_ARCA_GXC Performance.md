---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:GXC
ticker: GXC
exchange: NYSE Arca
fund: State Street SPDR S&P China ETF
tracked_index: S&P China BMI Index
benchmark: S&P 500 Total Return
issuer: State Street Investment Management
inception: 2007-03-20
expense_ratio: 0.59% gross
updated: 2026-08-29
performance_as_of: 2026-07-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
nav_as_of: 2026-08-26
market_price_as_of: 2026-08-26
fund_facts_as_of: 2026-08-27
risk_as_of: 2026-08-26
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/GXC
  - geography/China
---

# GXC Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

GXC เป็น passive/index-tracking China equity ETF ที่ติดตาม S&P China BMI
Index. Official State Street standardized table รายงาน NAV Total Return
average annual 4.61% สำหรับ 10-year field ณ 2026-07-31 และ current NAV
YTD -6.10% ณ วันเดียวกัน. Current NAV อยู่ที่ USD 91.05 ณ 2026-08-26.
Official capture ล่าสุดไม่เปิดเผย raw 10-year endpoints หรือ calendar-year NAV
rows จึงไม่คำนวณ cumulative/2021-2025 CAGR จากข้อมูลที่ไม่เปิดเผย.

## Performance check

- entity_key: NYSE Arca:GXC; State Street ยืนยัน listing เป็น NYSE Arca,
  ticker GXC, inception 2007-03-20 และ benchmark S&P China BMI Index.
- Metric: official NAV Total Return including reinvested dividends/capital
  gains and fund expenses; market-price return kept separate.
- Tracked index: S&P China BMI Index เป็น float-adjusted market-cap-weighted
  exposure to investable China equities available to foreign investors and may
  include eligible China A Shares through Stock Connect.
- Expense ratio: gross 0.59%.
- Current NAV: US$91.05 ณ 2026-08-26; closing market price US$91.00,
  midpoint US$90.89, premium/discount -0.18%, and 30-day median bid/ask
  spread 0.22%, all as of 2026-08-26.
- 10-year NAV TR: issuer-published average annual return 4.61% ณ
  2026-07-31; raw endpoints and cumulative return are not disclosed in the
  reviewed official capture.
- Current standardized YTD: NAV -6.10%, market value -5.00%, and issuer
  benchmark -6.47%, all as of 2026-07-31. These bases are kept separate.
- Since inception standardized NAV TR: average annual 4.97% as of 2026-07-31.
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference
  benchmark, not the issuer benchmark)

| Year | GXC NAV TR | S&P China BMI TR | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | not disclosed | not disclosed | 28.71% |
| 2022 | not disclosed | not disclosed | -18.11% |
| 2023 | not disclosed | not disclosed | 26.29% |
| 2024 | not disclosed | not disclosed | 25.02% |
| 2025 | not disclosed | not disclosed | 17.88% |

The reviewed current State Street performance table discloses rolling periods
but not readable annual NAV/index rows for 2016-2025; no third-party annual
proxy is substituted. S&P 500 rows reuse the cached USD Total Return
convention for complete calendar years 2016-2025.

## Window calculations

- Official latest 10-year NAV TR: average annual 4.61% as of 2026-07-31;
  cumulative return, raw endpoints and exact daily path are not disclosed.
- 2016-2025 and 2021-2025 GXC annual-window CAGR: not disclosed because
  issuer annual NAV rows are not disclosed in the reviewed official capture.
- S&P 500 reference: 2016-2025 cumulative 298.33% / CAGR 14.82%;
  2021-2025 cumulative 96.17% / CAGR 14.43%.
- Up years / down years, best/worst calendar year and exact common-window
  spread: not disclosed.
- Current NAV TR YTD: -6.10% as of 2026-07-31.
- Source-as-of note: the prior June observation -10.99% as of 2026-06-30
  is retained in the earlier source batch; the July observation is the latest
  standardized issuer snapshot and is not arithmetically reconciled with it.

## Risk read-through

GXC มี 1,365 holdings ณ 2026-08-26 และ exposure กระจุกใน China/Hong Kong
โดย sector หลักคือ Consumer Discretionary 21.62%, Financials 18.26%,
Communication Services 13.74%, Information Technology 12.56% และ
Industrials 9.29%. Fund characteristics ณ วันเดียวกันระบุ P/B 1.40 และ
P/E FY1 11.18; 30-day SEC yield คือ 1.72%. ความเสี่ยงหลักคือ China
policy/geopolitical risk, emerging-market liquidity, ADR/H-share/A-share
structure, country concentration, sector concentration และ FX volatility.
Daily NAV history ที่ยืนยันได้สำหรับ max drawdown และ recovery:
ไม่พบข้อมูลที่ยืนยันได้.

## Driver notes

- Confirmed structure: passive objective to track the S&P China BMI Index
  before fees and expenses; the fund may include eligible China A Shares
  through Stock Connect.
- Current refresh: the official State Street July 2026 table provides
  standardized NAV/market-value/index returns through 2026-07-31, while
  current NAV and portfolio facts are dated 2026-08-26 or 2026-08-27.
- The official current capture does not provide complete annual NAV rows or
  raw 10-year endpoints, so the prior annual-row and cumulative-return gap is
  preserved rather than filled with a secondary proxy.

## Sources

- [Official State Street GXC product and performance page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-china-etf-gxc) — identity, NYSE Arca listing, benchmark, inception, current NAV/AUM, holdings, sector snapshot, standardized returns and market-price snapshot; accessed 2026-08-29.
- [Official State Street GXC factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-gxc.pdf) — fund objective, performance definition and prior dated fund characteristics.
- [SEC GXC summary prospectus](https://www.sec.gov/Archives/edgar/data/1168164/000119312526031213/d92286d497k.htm) — passive strategy and risk disclosures.
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition.
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as of 2025-12-31.
- ETF source batch: [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
