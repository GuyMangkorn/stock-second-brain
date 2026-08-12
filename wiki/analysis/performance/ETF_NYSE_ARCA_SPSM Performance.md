---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:SPSM
ticker: SPSM
exchange: NYSE Arca
fund: State Street SPDR Portfolio S&P 600 Small Cap ETF
tracked_index: S&P SmallCap 600 Index
benchmark: S&P 500 Total Return
updated: 2026-08-12
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-08-11
source_batch: raw/imports/ETF_performance_sources_2026-08-12.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/SPSM
  - geography/United-States
---

# SPSM Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

SPSM เป็น passive/index-tracking U.S. small-cap equity ETF ที่ติดตาม S&P SmallCap 600 Index. Official issuer รายงาน 10-year NAV Total Return annualized `11.61%` ณ 2026-06-30 แต่ไม่เปิดเผย raw endpoints หรือ annual calendar rows ใน capture ที่ตรวจสอบ. Current issuer NAV YTD คือ `23.89%` ณ 2026-06-30.

## Performance check

- entity_key: NYSE Arca:SPSM
- Inception: 2013-07-08; listing date: 2013-07-09
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Tracked index (issuer benchmark): S&P SmallCap 600 Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: issuer-labeled 10-year annualized field as of 2026-06-30; exact raw endpoints and elapsed years are not disclosed in the reviewed capture
- 10-year NAV TR CAGR: `11.61%` (official issuer average annual total return; retained as a source fact, not recomputed from undisclosed endpoints)
- 2021-2025 CAGR: not disclosed because official calendar-year NAV TR rows were not available
- Coverage/source note: SPSM performance observations are official issuer NAV Total Return, net of fees, with distributions reinvested. S&P 500 rows reuse the cached USD Total Return convention as of 2025-12-31; market-price return is not mixed.

| Year | SPSM NAV TR | S&P 500 TR |
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
- Current YTD: `23.89%` as of 2026-06-30; latest NAV `US$57.68`, closing price `US$57.69`, and official premium/discount `+0.02%` as of 2026-08-11

## Risk read-through

SPSM ให้ broad U.S. small-cap exposure ผ่าน S&P SmallCap 600 Index. Gross/net expense ratio คือ `0.03%`; AUM คือ `US$17,250.35M` ณ 2026-08-11 และ distribution frequency เป็น quarterly. Official issuer tracking differences เทียบกับ tracked index อยู่ที่ `-0.01 pp` สำหรับ YTD, `-0.03 pp` สำหรับ 1-year, `-0.03 pp` สำหรับ 3-year, `-0.03 pp` สำหรับ 5-year และ `-0.04 pp` สำหรับ 10-year; index return เป็น gross of fund fees ขณะที่ fund return เป็น net of fees.

Max drawdown, recovery, volatility และ positive/negative-year counts ยังเป็น `ไม่พบข้อมูลที่ยืนยันได้` เพราะ reviewed issuer capture ไม่ได้ให้ daily NAV history หรือ complete annual NAV rows. Market-price figures above are kept separate from NAV Total Return.

## Driver notes

- Confirmed structure: passive objective to track the S&P SmallCap 600 Index before fees and expenses; the tracked index is float-adjusted, market-cap weighted, and rebalanced quarterly.
- Data limitation: the issuer performance table provides rolling/period returns through 2026-06-30 but not SPSM calendar-year NAV rows for 2016-2025 or raw 10-year endpoints.

## Sources

- [Official SPSM issuer product page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-portfolio-sp-600-small-cap-etf-spsm) — identity, fund facts, price/NAV, performance table; accessed 2026-08-12; price/NAV as of 2026-08-11 and performance as of 2026-06-30
- [Official SPSM factsheet](https://www.ssga.com/library-content/products/factsheets/etfs/us/factsheet-us-en-spsm.pdf) — fund facts and standardized performance; as of 2026-06-30
- [S&P SmallCap 600](https://www.spglobal.com/spdji/en/indices/equity/sp-600/) and [S&P U.S. Indices Methodology](https://www.spglobal.com/spdji/en/methodology/article/sp-us-indices-methodology/) — tracked-index context; accessed 2026-08-12
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — benchmark definition
- Cached S&P 500 TR references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); reference as-of 2025-12-31
- ETF source batch: [[ETF_performance_sources_2026-08-12]] | [[ETF Performance Index]]
