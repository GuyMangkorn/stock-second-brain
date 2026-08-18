---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:HEDJ
input_ticker: HEDJ
ticker: HEDJ
exchange: NYSE Arca
fund: WisdomTree Europe Hedged Equity Fund
tracked_index: WisdomTree Europe Hedged Equity Index
benchmark: S&P 500 Total Return
management_mode: passive-index
updated: 2026-08-19
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-17
fund_facts_as_of: 2026-08-17
source_batch: raw/imports/ETF_performance_sources_2026-08-19.md
return_basis: NAV total return; distributions reinvested; net of expenses
return_currency: USD
primary_region: Europe
tags:
  - analysis/etf-performance
  - ticker/HEDJ
  - geography/Europe
---

# HEDJ Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

`HEDJ` เป็น `passive-index` Europe equity ETF ที่ใช้ dividend-weighted
WisdomTree Europe Hedged Equity Index และ hedge EUR/USD เพื่อคง European
equity exposure โดยลดผลกระทบจากค่าเงิน. กองทุนจดทะเบียนบน `NYSE Arca`,
เริ่ม 31 ธ.ค. 2009 และมี net expense ratio `0.58%`.

Issuer rolling `10-year NAV Total Return CAGR` อยู่ที่ `10.73%` ณ
`2026-07-31`; current official NAV TR YTD อยู่ที่ `9.15%` ณ วันเดียวกัน.
จาก complete calendar rows 2016-2025 ที่ตรวจได้ ผลตอบแทนสะสมเป็น `153.82%`
หรือ rounded-input CAGR `9.76%`; ช่วง common window 2021-2025 สะสม `82.78%`
หรือ CAGR `12.82%`. ปี 2025 เป็นค่าคำนวณจาก official year-end NAV และ income
แล้ว reconcile กับข้อมูลรอง จึงไม่ควรอ่านเป็น issuer calendar-row โดยตรง.

## Performance check

- `entity_key: NYSE Arca:HEDJ`; WisdomTree factsheet และ SEC summary prospectus ยืนยัน fund name, ticker, NYSE Arca listing, CUSIP `97717X701` และ inception `2009-12-31`.
- Classification: `passive-index`; SEC ระบุ passive/indexing approach และ representative sampling. กองทุน seek to track the WisdomTree Europe Hedged Equity Index ก่อน fees/expenses และไม่พยายาม outperform index.
- Tracked index: `WisdomTree Europe Hedged Equity Index`; current WisdomTree index page แสดง symbol `WTEHIP`, ขณะที่ fund page/factsheet ยังแสดง related/legacy symbol `WTIDFTRH`. ใช้ชื่อ index เป็น canonical และเก็บ symbol discrepancy ไว้เป็น source note.
- Index method: dividend-paying European companies with an exporter tilt; annual dividend weighting with individual, sector and country caps. Currency hedge ใช้ euro forwards/futures และไม่รับประกันว่าจะ neutralize FX ได้ทั้งหมด.
- Return metric: NAV Total Return รวม reinvested distributions และหัก fund expenses; market-price return แยกออกจากตารางนี้. Currency เป็น USD.
- Official rolling fields ณ `2026-07-31`: NAV 1-year `18.71%`, 3-year annualized `13.54%`, 5-year annualized `10.97%`, 10-year annualized `10.73%`, since inception `8.98%`; tracked-index fields ตามลำดับ `19.27%`, `13.94%`, `11.30%`, `11.14%`, `9.41%`.
- Current snapshot ณ `2026-08-17`: NAV `USD 57.771`, closing market price `USD 57.870`, premium/discount `+0.17%`, total assets `USD 1.849bn`, aggregate hedge ratio `99.42%`, distribution yield `6.82%`, SEC 30-day yield `1.97%`. Yield ไม่ใช่ NAV TR.

| Year | HEDJ NAV TR (USD) | S&P 500 TR (USD) |
|---|---:|---:|
| 2016 | 9.30% | 11.96% |
| 2017 | 13.56% | 21.83% |
| 2018 | -9.27% | -4.38% |
| 2019 | 26.99% | 31.49% |
| 2020 | -2.90% | 18.40% |
| 2021 | 23.57% | 28.71% |
| 2022 | -10.18% | -18.11% |
| 2023 | 26.39% | 26.29% |
| 2024 | 5.65% | 25.02% |
| 2025 | 23.33%‡ | 17.88% |

Official SEC summary-prospectus chart supplies the 2016-2024 NAV rows. `‡`
2025 is calculated as `(2025 year-end NAV 53.11 + 2025 income 0.87) / 2024
year-end NAV 43.85 - 1 = 23.33%`, using the official WisdomTree factsheet;
AAII's dated annual NAV row rounds to `23.3%` and is used only as a
reconciliation check. S&P 500 TR is a cached USD common reference, not HEDJ's
strategy benchmark.

## Up years / Down years

- Complete 2016-2025 NAV TR up/down: `7 / 3`.
- Best NAV TR year: `2019 +26.99%`; least positive: `2024 +5.65%`.
- Worst NAV TR year: `2022 -10.18%`; least-bad down year: `2020 -2.90%`.
- 2016-2025 cumulative NAV TR: `+153.82%`; rounded-input CAGR: `9.76%`; population annual-return standard deviation: `13.76%`.
- 2021-2025 cumulative NAV TR: `+82.78%`; rounded-input CAGR: `12.82%`; population annual-return standard deviation: `14.04%`; up/down `4 / 1`.
- Cached S&P 500 TR compounds to `+298.33%` / `14.82%` over 2016-2025 and `+96.17%` / `14.43%` over 2021-2025. This is a common reference only; no manager-skill or alpha claim is made.

## Risk read-through

HEDJ's core trade-off is European equity exposure plus a near-full EUR hedge,
not a low-risk substitute for a global index. As of `2026-08-17`, Germany,
France, Spain and the Netherlands together represented about `81.50%` of the
country allocation. The largest sectors were Industrials `23.11%`, Financials
`16.71%`, Consumer Staples `12.42%`, Consumer Discretionary `11.93%` and
Information Technology `11.76%`. Top holdings included BBVA `7.27%`, ASML
`7.26%`, Santander `4.62%` and Siemens `4.33%`.

The hedge can reduce direct EUR/USD volatility, but forward-contract basis,
counterparty and hedge-cost risk remain. Dividend weighting and the exporter
screen can create sector/country tilts versus market-cap-weighted Europe. The
13.76% annual-return dispersion is a calendar-return statistic, not a
risk-adjusted measure. Official daily NAV history sufficient to verify maximum
drawdown and recovery was not disclosed in the reviewed sources;
`risk-adjusted evidence: not-verified`.

## Sources

- [WisdomTree HEDJ product page](https://www.wisdomtree.com/us/products/equity/hedj) — official current identity, NAV/price, rolling performance, hedge ratio, assets, holdings, countries and sectors; current page snapshot through `2026-08-17` / month-end performance through `2026-07-31`.
- [WisdomTree HEDJ factsheet](https://www.wisdomtree.com/-/media/us-media-files/documents/resource-library/fund-fact-sheets/international-equity/wisdomtree-factsheet-hedj-1056.pdf) — official exchange, inception, fee, NAV/index rolling fields, year-end NAV/income observations and portfolio facts as of `2026-06-30`.
- [SEC HEDJ summary prospectus](https://www.sec.gov/Archives/edgar/data/1350487/000121465925011291/hedj73125497k.htm) — official passive/indexing classification, objective, index construction, risks, NYSE Arca listing and 2016-2024 annual-return chart; August 2025.
- [WisdomTree Europe Hedged Equity Index page](https://www.wisdomtree.com/us/indexes/wtehip) and [rules-based methodology](https://www.wisdomtree.com/us/media/core-equity-index-methodology) — official index identity, dividend/country/sector rules and EUR hedge methodology.
- [AAII HEDJ performance page](https://www.aaii.com/etf/ticker/HEDJ) — secondary dated annual NAV row used to reconcile the calculated 2025 return; as of `2026-06-30`.
- S&P 500 index definition and cached `2016-2025` USD Total Return convention — common reference only; original URLs are preserved in [[ETF_performance_sources_2026-08-19]].
- ETF source batch: [[ETF_performance_sources_2026-08-19]] | [[ETF Performance Index]]

## Follow-up

- Refresh the official month-end NAV TR/YTD fields and hedge ratio on the next run.
- Recheck the `WTIDFTRH` versus `WTEHIP` index-symbol display after WisdomTree updates its fund page or factsheet.
- Verify an official daily NAV series if WisdomTree publishes one that supports drawdown and recovery calculations.
