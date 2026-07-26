---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:INQQ
ticker: INQQ
exchange: NYSE Arca
fund: INQQ The India Internet ETF
tracked_index: INQQ The India Internet Index
benchmark: S&P 500 Total Return
updated: 2026-07-26
performance_as_of: 2026-03-31
current_ytd_as_of: 2026-03-31
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/INQQ
  - geography/India
---

# INQQ Performance

> Navigation: [[ETF Region Index]] → [[India ETF]] → [[ETF Performance Index]]

## Bottom line

INQQ เป็น passive/index-tracking, non-diversified India internet/e-commerce equity ETF ที่ติดตาม INQQ The India Internet Index และ canonical key คือ `NYSE Arca:INQQ` ตาม SEC prospectus, factsheet และ shareholder report. Inception `2022-04-05` ถึง latest reviewed official numeric month-end `2026-03-31` มี `3.986311` elapsed years จึงระบุชัดว่า `10-year NAV TR unavailable`. Official available-period NAV TR annualized คือ `-7.83%`; official latest numeric YTD ที่ยืนยันได้คือ `-26.17%` ณ `2026-03-31`. The issuer's later month-end page is available but its numeric fields were not exposed in the reviewed capture, so no later YTD value is filled.

## Performance check

- entity_key: `NYSE Arca:INQQ`
- ISIN/CUSIP: `not disclosed in reviewed official capture` / `301505558`
- Inception: `2022-04-05` in the issuer fund-materials page and annual report; factsheet says `2022-04-06` (one-day source discrepancy retained)
- Asset class / structure: Equity; indexed; non-diversified; India internet/e-commerce companies and depositary receipts
- Tracked index: INQQ The India Internet Index
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Expense ratio: `0.86%`
- 10-year NAV TR: `unavailable`; official history is under 10 years
- Available-period window: `2022-04-05` to `2026-03-31`; actual years `3.986311`
- Start TR value: `not disclosed`
- End TR value: `not disclosed`
- Official available-period NAV TR: average annual `-7.83%` as of `2026-03-31`
- Official numeric YTD: `-26.17%` as of `2026-03-31`
- Formula for endpoint-derived CAGR: `CAGR = (End TR / Start TR)^(1 / actual years) - 1`; issuer supplies the annualized since-inception result but not raw endpoints, so no endpoint value is invented

Complete calendar-year NAV rows were not disclosed in the reviewed official capture. The table preserves that gap and separates the issuer's fiscal-year shareholder-report result from calendar-year returns. S&P 500 rows are cached USD Total Return reference rows; they are not used to create a fabricated same-window CAGR.

| Period | ETF NAV TR | S&P 500 TR |
|---|---:|---:|
| 2022 | not disclosed; partial inception year | -18.11% (not comparable) |
| 2023 | not disclosed | 26.29% (not comparable) |
| 2024 | not disclosed | 25.02% (not comparable) |
| 2025 | not disclosed | 17.88% (not comparable) |
| FY ended 2025-08-31 | -0.40% | not comparable; fiscal-period result |
| 2026 YTD | -26.17% as of 2026-03-31 | not comparable; later current-year cache not used |

## Up years / Down years

- Complete calendar-year up/down count: `not disclosed`; official calendar NAV rows are unavailable in the reviewed capture
- Best / worst calendar year: `not disclosed`
- Available-period NAV TR: issuer average annual `-7.83%` from `2022-04-05` to `2026-03-31`
- 10-year NAV TR: unavailable due to inception `2022-04-05`
- Fiscal-year cross-check: NAV total return `-0.40%` for FY ended `2025-08-31`; this is not a calendar-year row and is not blended into the calendar table
- Current numeric NAV TR YTD: `-26.17%` as of `2026-03-31`
- Current later month-end YTD: `ไม่พบข้อมูลที่ยืนยันได้` in the reviewed official capture; the official web page exposes placeholders rather than numeric values, and a secondary data page was not used to fill the gap

## Risk read-through

INQQ เป็นกองทุนเฉพาะธีมและ non-diversified: India/currency/foreign-ownership/liquidity risk ผสมกับ technology, internet และ e-commerce concentration. Official factsheet ณ `2026-03-31` แสดง 28 holdings, India exposure `100%`, และ sector weightsนำโดย E-Commerce `42.06%` และ Fintech `40.84%`. Daily NAV history สำหรับ max drawdown/recovery: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official EMQQ Global / INQQ fund materials: https://emqqglobaletfs.com/inqq-fund-materials
- Official INQQ factsheet: https://21674083.fs1.hubspotusercontent-na1.net/hubfs/21674083/Fund%20Documents/Fact%20Sheets/INQQ%20ETF%20Fact%20Sheet.pdf
- Official SEC summary prospectus: https://www.sec.gov/Archives/edgar/data/1452937/000121390024113356/ea0224782-04_497k.htm
- Official annual shareholder report: https://emqqglobaletfs.com/hubfs/Fund%20Documents/Annual%20Report/INQQ%20Annual%20Report.pdf?hsLang=en
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
