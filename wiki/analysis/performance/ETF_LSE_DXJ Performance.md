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
updated: 2026-07-22
annual_window: 2016-2025
annual_rows_as_of: 2025-12-31
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-07-20
source_batch: raw/imports/ETF_performance_sources_2026-07-22.md
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

`DXJJF` เป็น OTC alias ของ WisdomTree Japan Equity UCITS ETF - USD Hedged
(ISIN `IE00BVXC4854`); canonical identity ที่ issuer ยืนยันคือ `LSE:DXJ`.
Official `NAV Total Return` เป็นบวก 9 จาก 10 complete calendar years ใน 2016-2025,
ทบต้นจาก annual rows ได้ cumulative `268.73%` และ CAGR ประมาณ `13.94%` เทียบกับ
S&P 500 TR ที่ `14.82%`. Current official YTD อยู่ที่ `+21.90%` ณ 30 มิ.ย. 2026
และ latest official NAV อยู่ที่ `US$53.244` ณ 20 ก.ค. 2026 ([issuer page](https://www.wisdomtree.com/gb/products/equities/wisdomtree-japan-equity-ucits-etf---usd-hedged); [factsheet](https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BVXC4854/)).

## Performance check

- `entity_key: LSE:DXJ` (user alias: `OTC Markets:DXJJF`; OTC alias is secondary-mapped and not listed on the issuer page)
- Inception: 18 พ.ค. 2015
- Metric: `NAV Total Return` ใน USD, net of fees; daily NAV และ dividends reinvested ที่ NAV ใน ex-date
- Tracked index (issuer benchmark): `WisdomTree Japan Hedged Equity UCITS Index` (USD, Bloomberg `WTIDJHUT`)
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index)
- 10-year window: complete calendar years `2016-2025`; official annual rows, not a daily rolling endpoint series
- 10-year NAV TR CAGR: approximately `13.94%`; Start TR value: `100.00`; End TR value: `368.73`; Years: `10.00`
- Formula: `(End TR / Start TR)^(1 / Years) - 1`; CAGR compounds official annual rows rounded to two decimals
- Coverage/source note: official complete calendar years 2016-2025; no `*` proxy or `†` partial year. S&P 500 cache uses USD total return with dividends reinvested, reference as-of `2025-12-31`.

| ปี | DXJ / DXJJF NAV TR | S&P 500 TR |
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

**Up years / Down years**

- Up years / Down years: `9 / 1`
- Best: 2023, `+40.46%`
- Least positive: 2016, `+0.73%`
- Worst: 2018, `-18.71%`
- Least bad down year: 2018, `-18.71%` (มี down year เดียว)
- 2021-2025 cumulative / CAGR: `202.44%` / `24.77%`; S&P 500 TR `96.17%` / `14.43%`
- Current YTD: `+21.90%` NAV ณ 30 มิ.ย. 2026; official table ที่ยืนยันได้ยังไม่ extend beyond 30 มิ.ย.

## Risk read-through

DXJ เป็น passive, physically replicated, single-country Japan equity ETF ที่ hedge
JPY/USD ด้วย forward contracts; exposure จึงยังไวต่อ country, sector และ dividend/value
tilt และ hedge-cost/hedge-imperfection risk. TER อยู่ที่ `0.48%` ณ 20 ก.ค. 2026.
Annual-return standard deviation ประมาณ `16.69%` จาก rounded 2016-2025 rows
(population `σ`); official 3-year volatility, official NAV max drawdown และ recovery
date: `ไม่พบข้อมูลที่ยืนยันได้`. OTC `DXJJF` มี quote history บางและอาจไม่เหมาะกับ
price-return YTD; อย่าใช้ U.S.-listed NYSE Arca:DXJ แทน เพราะเป็นคนละ fund.

## Sources

- [WisdomTree product page](https://www.wisdomtree.com/gb/products/equities/wisdomtree-japan-equity-ucits-etf---usd-hedged) - identity, listings, inception, TER, current NAV, index and distributions
- [Official WisdomTree factsheet](https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BVXC4854/) - official NAV TR definition, annual rows 2016-2025, YTD as of 2026-06-30
- [WisdomTree performance definition](https://www.wisdomtree.eu/de-de/etfs/export-tilted/wisdomtree-japan-equity-ucits-etf-usd-hedged) - daily NAV, net-of-fees and dividend-reinvestment convention
- [OTC DXJJF historical quote](https://chartexchange.com/symbol/otc-dxjjf/historical/) - secondary alias/liquidity context, not used for NAV TR ranking
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) - common reference benchmark identity; annual cache sources are recorded in the dated source batch
