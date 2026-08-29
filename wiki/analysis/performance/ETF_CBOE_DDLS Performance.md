---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:DDLS
ticker: DDLS
exchange: Cboe BZX
updated: 2026-08-29
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
management_mode: passive-index
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/DDLS
---

# DDLS Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DDLS เป็น passive/index-tracking international small-cap equity ETF ที่มี dynamic currency hedge. Latest official standardized NAV TR YTD คือ `+6.54%` ณ 2026-07-31 และ rolling 10-year NAV average annual return คือ `9.61%` ณ วันเดียวกัน. ช่วง 2021-2025 ให้ blended cumulative `71.05%` หรือ CAGR `11.33%*` เพราะปี 2025 ใช้ secondary NAV proxy; 2016 ยังไม่มี annual row ที่ยืนยันได้. NAV ล่าสุด `USD 46.476` และ closing price `USD 46.414` ณ 2026-08-27.

## Performance check

- `entity_key: Cboe BZX:DDLS`
- Fund: WisdomTree Dynamic International SmallCap Equity Fund
- Inception: 7 ม.ค. 2016; exchange: `Cboe BZX`; expense ratio: `0.48%`
- Metric: `NAV Total Return` คำนวณจาก daily 4:00pm NAV; distributions reinvested และ fund expenses สะท้อนใน return ตาม issuer convention
- Management mode: `passive-index`
- Tracked index: `WisdomTree Dynamic International SmallCap Equity Index` (`WTISDIHD`)
- 10-year NAV TR: official average annual `9.61%` as of `2026-07-31`; raw start/end TR values and cumulative 10-year endpoint are `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed issuer capture
- Common benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference ไม่ใช่ tracked index ของ DDLS)
- Common window: `2021-2025` DDLS blended compound `71.05%` / CAGR `11.33%*`; S&P 500 cache compound `96.17%` / CAGR `14.43%`
- Coverage note: 2016 annual NAV TR is not disclosed; 2017-2024 rows are official issuer rows from the prior reviewed capture; 2025 `*` is a secondary dividend-reinvested NAV proxy and is not treated as official issuer evidence.

| ปี | DDLS NAV TR | S&P 500 TR |
|---|---:|---:|
| 2016 | ไม่พบข้อมูลที่ยืนยันได้ | 11.96% |
| 2017 | 25.02% | 21.83% |
| 2018 | -16.59% | -4.38% |
| 2019 | 24.74% | 31.49% |
| 2020 | -1.78% | 18.40% |
| 2021 | 16.11% | 28.71% |
| 2022 | -9.79% | -18.11% |
| 2023 | 15.16% | 26.29% |
| 2024 | 9.84% | 25.02% |
| 2025* | 29.10% | 17.88% |

**Up years / Down years**

- Disclosed 2017-2025 profile: `6 / 3` positive / negative years; 2016 is a gap
- Best: 2025*, **+29.10%**
- Least positive: 2024, **+9.84%**
- Worst: 2018, **-16.59%**
- Least bad down year: 2020, **-1.78%**
- Current standardized YTD: **+6.54% NAV**, as of 2026-07-31
- In the 2021-2025 blended window, DDLS beat the S&P 500 common reference only in 2022; this is not a manager-skill claim.

`*` = secondary dividend-reinvested NAV proxy for 2025. The blended 2021-2025 CAGR is not an official all-year NAV result.

## Risk read-through

Current official characteristics as of 2026-08-27 include NAV `USD 46.476`, closing price `USD 46.414`, premium/discount `-0.132%`, net assets about `USD 434.55m`, price/earnings `14.35`, price/book `1.45`, and underlying dividend yield `3.76%`. The fund reports distribution yield `6.58%`, SEC 30-day yield `3.20%`, and expense ratio `0.48%` as of the same date. Aggregate hedge ratio is `80.76%` as of 2026-08-27.

The portfolio is concentrated in developed ex-U.S./Canada small caps, with current country weights led by Japan `28.28%`, the United Kingdom `14.86%`, and Australia `9.68%`; sectors are led by Industrials `26.14%`, Financials `15.12%`, Consumer Discretionary `11.97%`, and Materials `10.43%`. The issuer states that the hedge ratio is set monthly using momentum, value, and interest-rate signals; hedging can help or hurt returns as currencies move. Official daily NAV TR history sufficient to calculate maximum drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้`.

## Driver notes

- **Currency hedge, observed structure:** the rules-based hedge reduces part of non-USD currency exposure but introduces hedge-ratio and hedge-cost sensitivity; it does not remove equity or small-cap risk.
- **2022, observed:** DDLS fell `-9.79%` versus S&P 500 TR `-18.11%`, a relative cushion during a weak global-equity year.
- **2025, data-quality caveat:** `+29.10%*` is a secondary NAV proxy, so it is useful for profile context but should not be treated as official issuer evidence.

## Sources

- [WisdomTree official product page](https://www.wisdomtree.com/us/products/equity/ddls) — current fund data, July 2026 standardized performance, hedge ratio, portfolio exposures, distributions, and risk disclosures
- [WisdomTree DDLS factsheet](https://www.wisdomtree.com/investments/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-ddls-factsheet-2194.pdf) — fund identity, Cboe listing, return basis, strategy and index context
- [WisdomTree Dynamic International SmallCap Equity Index](https://www.wisdomtree.com/us/indexes/WTISDIHD) — index construction and monthly currency hedge methodology
- [Cboe DDLS listing](https://www.cboe.com/us/equities/listings/listed_products/symbols/DDLS/) — listed-product identity and exchange context
- [AAII DDLS return history](https://www.aaii.com/etf/ticker/DDLS) — secondary 2025 NAV proxy used only because the official calendar row is not exposed
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common reference benchmark
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
