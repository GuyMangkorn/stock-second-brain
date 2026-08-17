---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:EUAD
ticker: EUAD
exchange: Cboe BZX
fund: Select STOXX Europe Aerospace & Defense ETF
tracked_index: STOXX Europe Total Market Aerospace & Defense Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-18
performance_as_of: 2026-06-30
rolling_10y_as_of: not applicable (<10y history)
current_ytd_as_of: not disclosed
price_nav_as_of: 2026-08-14
fund_facts_as_of: 2026-07-29
source_batch: raw/imports/ETF_performance_sources_2026-08-18.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EUAD
  - geography/Europe
---

# EUAD Performance

> Navigation: [[ETF Region Index]] → [[Europe ETF]] → [[ETF Performance Index]]

## Bottom line

EUAD เป็น passive thematic Europe aerospace-and-defense equity ETF ที่ track
`STOXX Europe Total Market Aerospace & Defense Index` และเริ่มดำเนินงานวันที่
2024-10-22 จึงไม่มี 10-year NAV TR หรือ complete 2021-2025 calendar window.
Official issuer page ไม่แสดงตัวเลข current YTD ใน static capture; secondary NAV
snapshot รายงาน YTD `+0.20%†` ณ 2026-06-30 และ since-inception annualised
`+36.80%†` ณวันเดียวกัน.

## Performance check

- `entity_key: Cboe BZX:EUAD`; ticker `EUAD`; primary exchange `Cboe BZX`; CUSIP `84858T772`; inception `2024-10-22`.
- Metric: `NAV Total Return` in USD; secondary performance source states returns assume reinvested distributions; official issuer page does not expose the numeric performance series in the reviewed static capture.
- Tracked index: `STOXX Europe Total Market Aerospace & Defense Index`; official prospectus says the fund invests at least 80% of assets in index components and uses a passive/indexing approach with replication or representative sampling.
- Expense ratio `0.50%` (management fee `0.05%` plus estimated other expenses `0.45%` in the SEC prospectus); official issuer product page also reports gross expense ratio `0.50%`.
- Official issuer snapshot as of 2026-07-29: NAV `US$43.91`, market price `US$43.98`, net assets `US$1,166,571,261`, 23 holdings and 30-day median bid-ask `0.22%`.
- Latest secondary cross-check as of 2026-08-14: closing NAV `US$47.99` and market price `US$47.89`; the date and value conflict with the older official snapshot and are not combined into a return calculation.
- 10-year NAV TR CAGR: not applicable (<10-year fund history). Available complete calendar-year NAV rows and official current YTD are not disclosed in the reviewed issuer capture.
- Secondary Schwab performance snapshot as of 2026-06-30: NAV TR YTD `+0.20%†`, 1-month `-1.0%†`, 3-month `+3.3%†`, 6-month `+0.2%†`, 1-year `-1.5%†`, and since-inception cumulative growth of a hypothetical US$10,000 to `US$17,230` (`+72.30%†`); since-inception annualised return is shown as `+36.80%†`.
- `†` identifies secondary evidence used to fill an issuer performance-display gap; it is not presented as an official issuer YTD field. S&P 500 TR is the common reference benchmark, but no same-date current comparison is claimed.

| Period | EUAD NAV TR | S&P 500 TR |
|---|---:|---:|
| 2024 inception partial | not disclosed | not comparable |
| 2025 complete calendar year | not disclosed | 17.88% |
| 2026 YTD as of 2026-06-30 | +0.20%† | not comparable |

## Up years / Down years

- Up years / Down years: not disclosed; the issuer does not provide a complete calendar-year NAV TR table for this under-two-year fund.
- Best: not disclosed.
- Least positive: not disclosed.
- Worst: not disclosed.
- Least bad down year: not disclosed.
- Current official NAV TR YTD: `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed issuer capture; secondary NAV YTD is `+0.20%†` as of 2026-06-30 and is not relabelled as a current August figure.

## Risk read-through

EUAD มี thematic และ non-diversified risk สูง: aerospace/defense spending และ
government policy, geopolitical/regulatory, foreign securities, sector
concentration, liquidity, passive-investment และ limited-history risk. Official
issuer page ณ 2026-07-29 แสดง top holdings เช่น Rolls-Royce ADR `20.59%`, Safran
ADR `19.54%`, Airbus `18.26%`, BAE Systems `10.68%` และ Rheinmetall ADR `8.17%`.
อย่างไรก็ตาม secondary holdings snapshot ณ 2026-08-14 รายงาน 33 holdings พร้อม
money-market และ swap positions รวมกันมากกว่า 60%; conflict นี้ยังไม่ถูก
reconciled จึงไม่ใช้เป็น structural weight claim. Secondary worst 3-month return
คือ `-9.9%†` ในช่วง 2025-09-30 ถึง 2025-12-31; official daily maximum drawdown,
recovery date และ volatility ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

Previous dividend payment คือ `US$0.1688` จ่าย 2025-12-31 จาก ex-date
2025-12-30; secondary trailing distribution yield แสดง `0.38%` แต่ issuer
current distribution series ไม่ปรากฏใน static capture.

## Sources

- [Select Funds EUAD fund page](https://www.select-funds.com/fund-info) — official identity, exchange, inception, fee, NAV/market-price snapshot, assets, holdings count, strategy and risk disclosures.
- [SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1484018/000148401824000217/r497e1024.htm) — official Cboe BZX listing, passive strategy, fee breakdown, index construction and risks.
- [STOXX Europe Total Market Aerospace & Defense index](https://stoxx.com/index/sxparo/) — index identity, USD net-return availability, current index context and components.
- [Charles Schwab EUAD performance page](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=euad) — secondary NAV performance snapshot through 2026-06-30 and risk-period observation.
- [Charles Schwab EUAD summary](https://www.schwab.wallst.com/Prospect/Research/etfs/summary.asp?symbol=euad) — latest secondary NAV/price, holdings conflict and distribution cross-check.
- [[ETF_performance_sources_2026-08-18]] | [[ETF Performance Index]]
