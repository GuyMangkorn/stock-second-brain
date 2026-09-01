---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:GWX
ticker: GWX
exchange: NYSE Arca
fund: State Street SPDR S&P International Small Cap ETF
tracked_index: S&P Developed Ex-U.S. Under USD2 Billion Index
benchmark: S&P 500 Total Return
updated: 2026-09-01
performance_as_of: 2026-07-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
nav_as_of: 2026-08-26
market_price_as_of: 2026-08-26
fund_facts_as_of: 2026-08-26
risk_as_of: 2026-08-25
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-6.md
return_basis: NAV total return; distributions reinvested; net of fund expenses
primary_region: International
tags:
  - analysis/etf-performance
  - ticker/GWX
  - geography/International
  - geography/international-ex-US
  - geography/global-developed
---

# GWX Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

GWX เป็น passive/index-tracking international small-cap equity ETF ที่ติดตาม S&P Developed Ex-U.S. Under USD2 Billion Index. Official issuer รายงาน latest 10-year NAV Total Return average annual `6.86%` และ current NAV YTD `7.28%` ณ 2026-07-31. Current NAV อยู่ที่ `USD 46.56` ณ 2026-08-26. Official capture ที่ตรวจสอบยังไม่เปิดเผย annual calendar rows จึงคำนวณ 2021-2025 CAGR หรือ up/down-year ranking ไม่ได้โดยไม่ผสมข้อมูลคนละฐาน.

## Performance check

- entity_key: NYSE Arca:GWX
- Inception: 2007-04-20
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index (issuer benchmark): S&P Developed Ex-U.S. Under USD2 Billion Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: issuer-labeled 10-year average annual field as of 2026-07-31; raw endpoints and exact elapsed years are not disclosed in the reviewed capture
- 10-year NAV TR CAGR: `6.86%` (official issuer average annual total return; retained as a source fact, not recomputed from undisclosed endpoints)
- 2021-2025 CAGR: not disclosed because official calendar-year NAV TR rows were not available
- Coverage/source note: GWX observations are official issuer NAV Total Return, net of fees, with distributions reinvested. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed.

| Year | GWX NAV TR | S&P 500 TR |
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

## Up years / Down years

- Up years / Down years: not disclosed because official calendar-year NAV rows are not disclosed
- Best: not disclosed
- Least positive: not disclosed
- Worst: not disclosed
- Least bad down year: not disclosed
- Current YTD: `7.28%` NAV TR as of 2026-07-31; market-value return `6.90%` and issuer-index return `5.91%` are kept separate and are not substituted for NAV TR. Current NAV is `US$46.56` as of 2026-08-26.

## Risk read-through

GWX ให้ international small-cap exposure ผ่าน passive sampling ของ S&P Developed Ex-U.S. Under USD2 Billion Index. Gross expense ratio คือ `0.40%` และ holdings คือ `2,081` ณ 2026-08-26. Official July table รายงาน 1-year NAV TR `19.13%`, 3-year `13.82%`, 5-year `5.15%`, และ 10-year `6.86%` ณ 2026-07-31; SEC prospectus ที่สิ้นสุด 2025-12-31 รายงาน 10-year NAV TR `7.00%`, ซึ่งเก็บเป็น separate as-of observation ไม่ใช่ conflict ที่นำมาผสม. Current sector weights ณ 2026-08-25 คือ Industrials `22.35%`, Materials `15.62%` และ Information Technology `13.94%`. Prospectus ยังเปิดเผย best quarter `+20.78%` ใน Q2 2020 และ worst quarter `-28.37%` ใน Q1 2020.

Max drawdown, recovery, volatility และ positive/negative-year counts ยังเป็น `ไม่พบข้อมูลที่ยืนยันได้` เพราะ reviewed issuer capture ไม่ได้ให้ daily NAV history หรือ complete annual NAV rows. Market-value return และ issuer-index return ด้านบนคงแยกจาก NAV Total Return.

## Driver notes

- Confirmed structure: passive objective to track the S&P Developed Ex-U.S. Under USD2 Billion Index before fees and expenses; the index targets developed-market companies outside the U.S. with market capitalization under US$2 billion.
- Current refresh: the official State Street July 2026 table provides standardized rolling/period returns through 2026-07-31, but it does not provide GWX calendar-year NAV rows for 2016-2025 or raw 10-year endpoints.
- Fresh source recheck on 2026-09-01 exposed an older July 09, 2026 page snapshot in the dynamic text capture, while the later official 2026-08-26 NAV/price snapshot retained above remains the higher-quality dated observation. The discrepancy is disclosed rather than silently replacing later data with the stale capture.
- The reviewed secondary annual-return table conflicted with the official prospectus 2025 NAV result, so no secondary proxy is saved and the annual window remains disclosed rather than mixed.

## Sources

- [Official GWX issuer product page](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-international-small-cap-etf-gwx) — identity, passive objective, exchange, inception, index, current NAV/AUM, holdings, sector snapshot and standardized performance; later dated capture through 2026-08-26 retained, dynamic recheck 2026-09-01 disclosed above
- [Official GWX factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-gwx.pdf) — NAV/market-value/index standardized returns and fund characteristics; prior as-of data retained where explicitly dated
- [Official SEC GWX summary prospectus](https://www.sec.gov/Archives/edgar/data/1168164/000119312526031217/d833468d497k.htm) — passive strategy, risk, 2025 year-end average annual returns, and best/worst quarters; filed 2026-01-30; accessed 2026-08-17
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as-of 2025-12-31
- ETF source batch: [[ETF_performance_sources_2026-09-01_run-6]] | [[ETF Performance Index]]
