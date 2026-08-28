---
type: etf-performance
instrument_type: ETF
entity_key: NASDAQ:MCHI
ticker: MCHI
exchange: NASDAQ
fund: iShares MSCI China ETF
tracked_index: MSCI China Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-08-28
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-08-26
price_nav_as_of: 2026-08-27
source_batch: raw/imports/ETF_performance_sources_2026-08-28.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/MCHI
  - geography/China
---

# MCHI Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

MCHI เป็น passive/index-tracking China equity ETF ของ iShares ติดตาม MSCI China Index (Net). Official iShares performance table ยืนยัน rolling 10-year NAV total return cumulative `45.52%` และ CAGR `3.82%` สำหรับ 2016-06-30 ถึง 2026-06-30. Current official NAV คือ `US$55.02` ณ 2026-08-27 และ NAV TR YTD คือ `-7.93%` ณ 2026-08-26; annual NAV rows ที่เปิดเผยใน reviewed official capture ครอบคลุม 2021-2025 เท่านั้น.

## Performance check

- entity_key: NASDAQ:MCHI
- Inception: 2011-03-29
- Metric: official NAV Total Return; iShares growth-of-$10,000 convention assumes reinvested dividends/capital gains and deducts fund expenses
- Tracked index (issuer benchmark): MSCI China Index (Net)
- Expense ratio: 0.59%
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- Asset class: Equity; distribution frequency: semi-annual
- Holdings: 575 ณ 2026-08-27
- 3-year standard deviation: 21.63%; equity beta: 0.36 ณ 2026-07-31
- P/E: 13.68; P/B: 1.66 ณ 2026-08-26
- 10-year NAV TR: cumulative `45.52%` / CAGR `3.82%` for 2016-06-30 to 2026-06-30; actual elapsed years `10.00`
- Coverage/source note: official annual rows 2021-2025 are disclosed; 2016-2020 annual rows are `not disclosed` in the reviewed current capture; S&P 500 rows reuse cached USD Total Return convention as of 2025-12-31; market-price return is not mixed

### 10-year NAV TR window

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative return | CAGR | Disclosure |
|---|---|---:|---:|---:|---:|---:|---|
| 2016-06-30 | 2026-06-30 | 10.00 | 100.00 (normalized) | 145.52 (derived from official cumulative) | 45.52% | 3.82% official | Raw NAV endpoints not disclosed |

`145.52 = 100.00 × (1 + 45.52%)`; `CAGR = (145.52 / 100.00)^(1/10) - 1 = 3.82%`. The normalized endpoint is a transparent calculation from official cumulative NAV TR, not a proxy.

| Year | ETF NAV TR | Issuer benchmark TR | S&P 500 TR |
|---|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | -22.38% | -21.72% | 28.71% |
| 2022 | -22.53% | -21.93% | -18.11% |
| 2023 | -11.07% | -11.20% | 26.29% |
| 2024 | 18.06% | 19.42% | 25.02% |
| 2025 | 31.07% | 31.17% | 17.88% |
| 2026 YTD | -7.93% as of 2026-08-26 | not comparable; current year not cached | not comparable; current year not cached |

## Window read-through

- Rolling 10-year official NAV TR: cumulative `45.52%`, CAGR `3.82%`, 2016-06-30 to 2026-06-30.
- Disclosed 2021-2025 calendar slice: cumulative `-17.25%`, CAGR `-3.72%`; this is not the same window as the rolling 5-year return `-30.52%` through 2026-06-30.
- Among the disclosed annual rows, best is 2025 `+31.07%` and worst is 2022 `-22.53%`; a full 10-year best/worst ranking is not claimed because 2016-2020 rows are not disclosed.
- Month-end reference: iShares reports 10-year cumulative `45.52%` and 2026 YTD `-14.65%` as of 2026-06-30; the latest current YTD observation is `-7.93%` as of 2026-08-26.

## Risk read-through

MCHI เป็น broad single-country China equity ETF มี 575 holdings ณ 2026-08-27.
Current exposure หลักคือ Consumer Discretionary `24.12%`, Financials `19.78%`,
Communication `17.80%`, Information Technology `10.91%` และ Health Care
`5.86%` ณ 2026-08-26. ความเสี่ยงยังรวม China policy/geopolitical,
A-share/H-share/ADR access, currency, liquidity และ systematic fair-value risk.
Exchange-traded index futures may be used to offset cash/receivables for tracking
and are not the fund's defining structure. Daily NAV TR drawdown/recovery
series: `ไม่พบข้อมูลที่ยืนยันได้` ใน reviewed capture.

## Sources

- Official issuer source: https://www.ishares.com/us/products/239619/ishares-msci-china-etf
- Official factsheet: https://www.ishares.com/us/literature/fact-sheet/mchi-ishares-msci-china-etf-fund-fact-sheet-en-us.pdf
- Official summary prospectus: https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-msci-china-etf-8-31.pdf
- Official annual financial statements: https://www.ishares.com/us/literature/annual-financial-statements/afs-ishares-trust-msci-country-etfs-book1-08-31-en.pdf
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-08-28]] | [[ETF Performance Index]]
