---
type: etf-performance
instrument_type: ETF
entity_key: LSE:HEDK
input_ticker: WEEUF
ticker: HEDK
exchange: London Stock Exchange
fund: WisdomTree Europe Equity UCITS ETF - USD Hedged Acc
isin: IE00BYQCZP72
tracked_index: WisdomTree Europe Hedged Equity UCITS Index
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-08-19
performance_as_of: 2025-12-31
available_period_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-11
fund_facts_as_of: 2026-08-11
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; USD; net of expenses; accumulating
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/HEDK
  - ticker/WEEUF
  - geography/Europe
---

# HEDK Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

WEEUF เป็น OTC input alias ของ official USD London listing `LSE:HEDK` สำหรับ
WisdomTree Europe Equity UCITS ETF - USD Hedged Acc. ใน complete calendar window
2017-2025 มี 6 ปีบวก / 3 ปีลบ; official NAV Total Return จาก rounded calendar
rows ให้ cumulative `132.80%` และ CAGR `9.84%`, เทียบ S&P 500 TR ที่
`255.78%` / `15.14%` ในช่วงเดียวกัน. ปีดีที่สุดคือ 2019 ที่ `+27.22%` และแย่ที่สุด
คือ 2022 ที่ `-10.04%`. Latest official NAV TR YTD คือ `+9.03%` ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: LSE:HEDK`; `input_ticker: WEEUF`; official WisdomTree listing table maps the USD London line to `HEDK`, ISIN `IE00BYQCZP72`; the OTC alias is retained for traceability.
- Fund: `WisdomTree Europe Equity UCITS ETF - USD Hedged Acc`; inception `1 พ.ย. 2016`; exchange `London Stock Exchange`; use of income `Accumulating`; official base/NAV currency `USD`.
- Classification: supported `passive-index` equity ETF. WisdomTree describes physical full replication and a fund objective to track the WisdomTree Europe Hedged Equity UCITS Index before fees and expenses.
- Metric: `NAV Total Return` รวม distributions ที่ reinvested และ fund expenses; official factsheet rows are net of fees and shown in the listing currency, USD.
- Tracked index: `WisdomTree Europe Hedged Equity UCITS Index`, a rules-based fundamentally weighted Eurozone equity index using dividend history, global-revenue/exporter exposure, quality/momentum risk screening and ESG criteria; the index methodology uses forward contracts to reduce EUR/USD fluctuations.
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของ HEDK). The official tracked-index comparison shows fund-minus-index annual gaps of approximately `-0.06` to `-0.55` percentage points, retained as passive tracking evidence rather than alpha.
- Official current fields: NAV `US$44.125`, fund AUM `US$116.18m`, and TER `0.58%` as of `11 ส.ค. 2026`; these quote/fund-fact fields are not used in return calculations.
- Official performance as of `31 ก.ค. 2026`: NAV TR YTD `9.03%`, 1-year `18.57%`, 3-year annualised `13.19%`, and issuer available-period annualised return since inception `10.85%`. The last field is not relabelled as a 10-year CAGR.
- 10-year NAV TR: `not applicable (<10 years)`; official inception `2016-11-01` to latest verified performance `2026-07-31` is less than 10.00 elapsed years. The 2016 inception partial is omitted because no official partial-year row was retained.
- Coverage/source note: official WisdomTree calendar rows cover complete years `2017-2025`; S&P 500 rows use the cached USD Total Return convention for the same subset of `2016-2025`.

| Year | HEDK NAV TR | S&P 500 TR |
|---|---:|---:|
| 2017 | 13.74% | 21.83% |
| 2018 | -9.14% | -4.38% |
| 2019 | 27.22% | 31.49% |
| 2020 | -2.50% | 18.40% |
| 2021 | 23.68% | 28.71% |
| 2022 | -10.04% | -18.11% |
| 2023 | 25.73% | 26.29% |
| 2024 | 5.66% | 25.02% |
| 2025 | 22.87% | 17.88% |

**Up years / Down years**

- Up years / Down years: `6 / 3` ใน 2017-2025
- Best: 2019, `+27.22%`
- Least positive: 2024, `+5.66%`
- Worst: 2022, `-10.04%`
- Least bad down year: 2020, `-2.50%`
- 2017-2025 cumulative/CAGR: HEDK `132.80%` / `9.84%`; S&P 500 TR `255.78%` / `15.14%`
- 2021-2025 cumulative/CAGR: HEDK `81.61%` / `12.68%`; S&P 500 TR `96.17%` / `14.43%`
- Current official HEDK NAV TR YTD: `+9.03%` ณ 31 ก.ค. 2026; tracked-index YTD `+9.11%` on the same date.

## Risk read-through

Issuer available-period annualised NAV TR ตั้งแต่ inception อยู่ที่ `10.85%` ณ
31 ก.ค. 2026; annual-return volatility แบบ population จาก official rounded
calendar rows 2017-2025 คือ `14.33%`. Daily NAV history ที่เพียงพอสำหรับ
maximum drawdown และ recovery ยังไม่ถูกเปิดเผย จึงรายงาน `risk-adjusted evidence:
not-verified` และไม่ใช้ market-price proxy แทน NAV risk metric.

กองทุนมี Eurozone country/sector concentration และ hedge/forward risk. Official
country weights ณ 31 ก.ค. 2026 ได้แก่ Germany `22.83%`, France `21.45%`, Spain
`19.56%`, Netherlands `17.62%`, และ Italy `5.51%`; sector weights เด่นคือ
Industrials `20.91%`, Financials `17.21%`, Consumer Staples `13.82%`, Consumer
Discretionary `12.60%`, และ Information Technology `10.86%`. WisdomTree ระบุว่า
forwards ที่ roll รายเดือนช่วยลด EUR/USD volatility แต่ไม่สามารถ offset ได้สมบูรณ์.
TER `0.58%` และ dividend-weighted/fundamentally screened construction อาจทำให้
behavior ต่างจาก market-cap Europe index.

## Sources

- [WisdomTree HEDK/HEDS product page](https://www.wisdomtree.com/ie/products/equities/wisdomtree-europe-equity-ucits-etf---usd-hedged-acc) — official identity, LSE/SIX listings, inception, USD NAV, TER, structure, index and current fund fields.
- [WisdomTree HEDK factsheet](https://dataspanapi.wisdomtree.com/pdr/documents/FACTSHEET/UCITS/EU/EN-GB/IE00BYQCZP72/) — official NAV Total Return definition, 2017-2025 calendar rows, tracked-index rows, rolling/YTD fields and exposure snapshots as of 31 Jul 2026.
- [StockAnalysis WEEUF page](https://stockanalysis.com/quote/otc/WEEUF/) — secondary OTC alias/name cross-check only; not used for the official performance calculation.
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached workflow references — USD Total Return with dividends reinvested, reference as-of 31 Dec 2025.
- ETF source batch: [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]
