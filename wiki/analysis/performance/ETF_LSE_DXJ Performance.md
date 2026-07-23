---
type: etf-performance
instrument_type: ETF
entity_key: LSE:DXJ
ticker: DXJ
user_alias: DXJJF
exchange: LSE
fund: WisdomTree Japan Equity UCITS ETF - USD Hedged
isin: IE00BVXC4854
tracked_index: WisdomTree Japan Hedged Equity UCITS Index
benchmark: S&P 500 Total Return
updated: 2026-07-23
annual_window: 2016-2025
annual_rows_as_of: 2026-06-30
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-07-22
source_batch: raw/imports/ETF_performance_sources_2026-07-23.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/DXJ
  - ticker/DXJJF
  - geography/Japan
---

# DXJ Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

DXJJF เป็น OTC alias ของ WisdomTree Japan Equity UCITS ETF - USD Hedged
(ISIN IE00BVXC4854); canonical identity ที่ issuer ยืนยันคือ LSE:DXJ.
Official NAV Total Return มี 10 complete calendar yearsในช่วง 2016-2025
ทบต้นได้ cumulative 268.73% และ CAGR ประมาณ 13.94% เทียบกับ S&P 500 TR
14.82%. Current official YTD อยู่ที่ 21.90% ณ 2026-06-30 และ latest official
NAV อยู่ที่ US$55.035 ณ 2026-07-22.

## Performance check

- entity_key: LSE:DXJ (input alias: DXJJF; issuer does not list the OTC alias)
- Inception: 2015-05-18
- Metric: NAV Total Return ใน USD, net of fees, with distributions reinvested at NAV on the ex-dividend date
- Tracked index (issuer benchmark): WisdomTree Japan Hedged Equity UCITS Index (USD, Bloomberg WTIDJHUT)
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index)
- 10-year coverage: ten complete calendar years, 2016-2025; official daily endpoints are not disclosed
- Start date: 2015-12-31; End date: 2025-12-31
- Start TR value: 100.00 normalized; End TR value: 368.73 normalized; Actual years: 10.00
- 10-year NAV TR CAGR: approximately 13.94%, calculated from rounded official annual rows
- Formula: (End TR / Start TR)^(1 / Years) - 1 = (368.73 / 100.00)^(1 / 10.00) - 1 = 13.94%
- Coverage/source note: all ETF annual rows are official complete calendar-year NAV TR, net of fees, in USD. No proxy or partial year is used; normalized endpoints are derived from the rounded annual inputs, not published raw NAV levels.

| Year | DXJ / DXJJF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 0.73% | 11.96% |
| 2017 | 22.17% | 21.83% |
| 2018 | -18.71% | -4.38% |
| 2019 | 18.53% | 31.49% |
| 2020 | 2.82% | 18.40% |
| 2021 | 18.07% | 28.71% |
| 2022 | 6.48% | -18.11% |
| 2023 | 40.46% | 26.29% |
| 2024 | 30.55% | 25.02% |
| 2025 | 31.19% | 17.88% |

S&P 500 เป็น common reference benchmark ไม่ใช่ issuer benchmark ของ DXJ;
ตาราง S&P ใช้ cached USD Total Return convention ณ 2025-12-31.

## Up years / Down years

- Up years / Down years: 9 / 1
- Best: 2023, +40.46%
- Least positive: 2016, +0.73%
- Worst: 2018, -18.71%
- Least bad down year: 2018, -18.71%
- 2021-2025 cumulative / CAGR: 202.44% / 24.77%; S&P 500 TR: 96.17% / 14.43%
- Current YTD: +21.90% NAV as of 2026-06-30; official performance beyond this date is not disclosed

## Risk read-through

DXJ เป็น passive, physically fully replicated, single-country Japan equity ETF.
ดัชนีใช้ dividend-weighted and risk-screened constituents และ hedge JPY/USD
ด้วย currency forward contracts; จึงยังมี country, sector, dividend/value,
hedge-cost และ hedge-imperfection risk. TER 0.48% ณ 2026-07-22. Annual-return
population standard deviation จาก rounded 2016-2025 inputs อยู่ที่ 16.69%
(เป็น calculation ไม่ใช่ issuer 3-year volatility). Japan exposure 100% และ
sector ใหญ่สุดคือ Industrials 24.82%, Financials 22.19% และ Consumer
Discretionary 17.33% ณ 2026-07-22. Official daily NAV history สำหรับ
max drawdown และ recovery: ไม่พบข้อมูลที่ยืนยันได้. OTC alias liquidity:
secondary quote context only and not used for NAV TR.

## Sources

- WisdomTree official product page:
  https://www.wisdomtree.com/gb/products/equities/wisdomtree-japan-equity-ucits-etf---usd-hedged
- Official WisdomTree factsheet:
  https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BVXC4854/
- WisdomTree performance definition:
  https://www.wisdomtree.eu/de-de/etfs/export-tilted/wisdomtree-japan-equity-ucits-etf-usd-hedged
- S&P 500 index page:
  https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-23]]
