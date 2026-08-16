---
type: etf-performance
instrument_type: ETF
entity_key: LSE:USSC
ticker: USSC
input_ticker: ZPRVF
exchange: London Stock Exchange
fund: State Street SPDR MSCI USA Small Cap Value Weighted UCITS ETF
tracked_index: MSCI USA Small Cap Value Weighted Index
benchmark: S&P 500 Total Return
updated: 2026-08-17
performance_as_of: 2026-07-31
calendar_years_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-08-17.md
return_basis: NAV total return / Fund Net
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/USSC
  - ticker/ZPRVF
  - geography/United-States
---

# USSC Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

ZPRVF เป็น OTC alias ของ USD share class `LSE:USSC` ของ State Street SPDR MSCI USA Small Cap Value Weighted UCITS ETF ซึ่งเป็น passive/index-tracking U.S. small-cap value equity ETF. ใน complete calendar window 2016-2025 มี 8 ปีบวก / 2 ปีลบ; official Fund Net/NAV Total Return compound เป็น `191.31%` หรือ rounded-input CAGR `11.28%`, เทียบ S&P 500 TR `298.33%` / `14.82%`. ปีดีที่สุดคือ 2021 ที่ `+35.40%`, แย่ที่สุดคือ 2018 ที่ `-14.31%`, และ current NAV TR YTD ล่าสุดคือ `+20.29%` ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: LSE:USSC`; input card ticker: `ZPRVF` (OTC alias)
- Classification: supported passive/index-tracking equity UCITS ETF; official USD listing LSE:USSC; ISIN `IE00BSPLC413`
- Inception: 18 ก.พ. 2015; expense ratio/TER `0.30%`; income treatment: accumulation
- Metric: `NAV Total Return` / official `Fund Net` รวม fund expenses และ income ที่สะสมใน NAV; currency USD
- Tracked index (issuer benchmark): `MSCI USA Small Cap Value Weighted Index` (Net Total Return)
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference benchmark ไม่ใช่ tracked index ของกองทุน)
- 2016-2025 calendar NAV TR: cumulative `191.31%`; rounded-input CAGR `11.28%`
- 2021-2025 calendar NAV TR: cumulative `83.97%`; rounded-input CAGR `12.97%`
- 10-year NAV TR window: `2016-07-31` to `2026-07-31`; official cumulative `213.35%` and annualized `12.10%`. Raw NAV endpoints are not disclosed; normalized TR index `100.00 → 313.35`, `Years: 10.00`; formula `(End TR / Start TR)^(1 / Years) - 1`
- Coverage/source note: official State Street Fund Net calendar rows cover 2016-2025 and the official rolling/current fields are as of 31 ก.ค. 2026. No `*` proxy or `†` partial-year marker is used in the complete-year table.

| Year | USSC Fund Net / NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | 25.83% | 11.96% |
| 2017 | 9.37% | 21.83% |
| 2018 | -14.31% | -4.38% |
| 2019 | 23.80% | 31.49% |
| 2020 | 8.46% | 18.40% |
| 2021 | 35.40% | 28.71% |
| 2022 | -10.23% | -18.11% |
| 2023 | 21.18% | 26.29% |
| 2024 | 9.67% | 25.02% |
| 2025 | 13.89% | 17.88% |

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016-2025
- Best: 2021, `+35.40%`; least positive: 2020, `+8.46%`
- Worst: 2018, `-14.31%`; least bad down year: 2022, `-10.23%`
- 2016-2025 CAGR: `11.28%`; 2021-2025 CAGR: `12.97%`
- Current YTD: official Fund Net/NAV TR `+20.29%` as of 31 ก.ค. 2026. The latest official S&P 500 TR page shows `+14.04%` as of 16 ส.ค. 2026; that date is not synchronized and is not used as a same-date table comparator.
- Latest official NAV: `US$96.48` as of 14 ส.ค. 2026; market-price observations on the EUR listing are kept separate from USD NAV TR.

## Risk read-through

Rolling 10-year NAV TR annualized `12.10%` ณ 31 ก.ค. 2026 ต่างจาก 2016-2025 calendar CAGR `11.28%` เพราะเป็นคนละ endpoint/window. Official 3-year standard deviation คือ `18.28%` และ annualized tracking error `0.07%` ณ วันเดียวกัน. Small-cap/value factor, financials concentration, liquidity, valuation และ USD/share-class currency risk เป็นประเด็นหลัก. Official daily NAV history สำหรับคำนวณ maximum drawdown และ recovery ไม่ได้อยู่ใน reviewed capture จึงรายงานเป็น `ไม่พบข้อมูลที่ยืนยันได้` และไม่สร้างตัวเลข proxy.

## Sources

- [State Street official USSC/ZPRV product page](https://www.ssga.com/ie/en_gb/institutional/etfs/state-street-spdr-msci-usa-small-cap-value-weighted-ucits-etf-zprv-gy) — identity, official listings, inception, current NAV, rolling/current Fund Net performance, annual rows, standard deviation and tracking error; observations through 14 ส.ค. / 31 ก.ค. / 13 ส.ค. 2026 as labelled
- [State Street official factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/emea/factsheet-emea-en_gb-zprv-gy.pdf) — ISIN, LSE:USSC USD listing, TER, accumulation, index, replication and Fund Net calendar/rolling performance; factsheet dated 30 มิ.ย. 2026 with performance through 31 ก.ค. 2026
- [Secondary ZPRVF OTC identity cross-check](https://stockanalysis.com/quote/otc/ZPRVF/) — OTC alias and fund identity; not used for NAV Total Return ranking
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- [S&P DJI current index returns](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?parentIdentifier=f33eb5c2-5231-4c16-bc59-38407c3d2f2f&sourceIdentifier=home-page) — latest current S&P 500 TR YTD snapshot used only with its visible 16 ส.ค. 2026 as-of date
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); cached reference as-of 31 ธ.ค. 2025
- ETF source batch: [[ETF_performance_sources_2026-08-17]] | [[ETF Performance Index]]
