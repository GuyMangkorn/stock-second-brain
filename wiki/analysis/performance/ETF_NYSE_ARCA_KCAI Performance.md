---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:KCAI
ticker: KCAI
exchange: NYSE Arca
fund: KraneShares China Alpha Index ETF
tracked_index: Qi China Alpha Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/KCAI
  - geography/China
---

# KCAI Performance

> Navigation: [[ETF Region Index]] → [[China ETF]] → [[ETF Performance Index]]

## Bottom line

KCAI เป็น passive/rules-based index-tracking China A-share equity ETF ของ KraneShares ติดตาม `Qi China Alpha Index` และเริ่มกองทุนเมื่อ 2024-08-27. เนื่องจากประวัติยังไม่ถึง 10 ปี จึงระบุ `10-year NAV TR unavailable` อย่างตรงไปตรงมา. Official since-inception NAV Total Return ณ 2026-06-30 รายงาน cumulative `76.27%` และ annualized `36.06%` สำหรับช่วง 2024-08-27 ถึง 2026-06-30 ประมาณ `1.84` ปี; latest NAV TR YTD คือ `4.27%` ณ 2026-06-30.

Official fund documents (prospectus, factsheet and 2026 annual shareholder report) ระบุ principal listing `NYSE Arca`, ขณะที่ current product page แสดง `Primary Exchange NYSE`; จึงใช้ canonical `NYSE Arca:KCAI` และเก็บ conflict ไว้ใน source batch.

## Performance check

- `entity_key`: `NYSE Arca:KCAI`
- Fund: KraneShares China Alpha Index ETF; asset class `Equity`; total annual fund operating expense `0.79%`
- Inception: `2024-08-27`
- Metric: official NAV Total Return, รวม reinvested distributions และ fund expenses ตาม issuer's growth/performance disclosure
- Issuer benchmark: Qi China Alpha Index; automated algorithmic machine-learning selection from the CSI 300 China A-share universe, maximum 50 securities and 5% constituent cap, rebalanced monthly
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark, not issuer benchmark)
- Type note: the prospectus states an at-least-80% policy in underlying-index securities or economically similar instruments and says the Fund is not actively managed. It is rules-based/index-tracking equity, not bond, commodity, currency trust, multi-asset, leveraged, inverse, option-income, derivative-heavy or single-stock exposure.

### Available-period NAV TR window

| Start date | End date | Actual years | Start TR value | End TR value | Cumulative return | Annualized return | Disclosure |
|---|---|---:|---:|---:|---:|---:|---|
| 2024-08-27 | 2026-06-30 | approx. 1.84 | 100.00 (normalized) | 176.27 (derived from official cumulative return) | 76.27% | 36.06% | Official since-inception NAV TR; `10-year NAV TR unavailable`; raw NAV endpoints not disclosed |

สูตร normalized endpoint: `100.00 × (1 + 76.27%) = 176.27`; ค่านี้ derive จาก issuer-reported since-inception cumulative return ไม่ใช่ raw NAV endpoint และไม่ใช่ proxy. Annualized return `36.06%` เป็นตัวเลขที่ issuer รายงาน.

### Annual NAV Total Return

| Period | KCAI NAV TR | Qi China Alpha Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2024 | not disclosed (partial inception year) | not disclosed | not comparable; ETF partial |
| 2025 | not disclosed | not disclosed | 17.88% |
| 2026 YTD | 4.27% | 5.20% | not comparable; current year not cached |

KraneShares' current product page and June 2026 factsheet disclose rolling/YTD and since-inception performance but do not disclose complete calendar-year Fund NAV rows for 2024 or 2025 in the reviewed capture. The 2026 YTD NAV and index rows are current month-end figures as of `2026-06-30`; S&P 500 is shown only as a common reference and is not used to manufacture a 10-year or same-start-date proxy.

### Available-period read-through

- `10-year NAV TR unavailable`: official inception `2024-08-27` is less than 10 elapsed years as of `2026-06-30`.
- Since-inception NAV TR: cumulative `76.27%`; issuer annualized return `36.06%`; actual elapsed period approximately `1.84` years.
- Latest official NAV TR YTD: `4.27%` as of `2026-06-30`; 1-year NAV TR `42.84%` as of `2026-06-30`.
- Calendar best/worst year ranking: `not disclosed` because complete calendar-year NAV rows are not disclosed in the reviewed official materials.

## Risk read-through

KCAI เป็น non-diversified China A-share exposure. KraneShares reports `40` holdings and net assets about `$3.24M` as of `2026-07-20/22`, with total annual fund operating expense `0.79%`; June 2026 sector exposure is Financials `41.50%`, Industrials `20.57%`, Information Technology `17.93%`, Materials `11.08%`, and Consumer Discretionary `9.49%`. Stock Connect/QFI access, China policy, liquidity, currency, financial-sector concentration and model/index risk can increase volatility. Daily NAV history sufficient for fund-level max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

## Sources

- Official KraneShares KCAI product page: https://kraneshares.com/etf/kcai/
- Official KraneShares KCAI factsheet: https://kraneshares.com/resources/factsheet/kcai_factsheet.pdf
- Official KraneShares KCAI 2026 annual shareholder report: https://kraneshares.com/resources/compliance/2026_05_29_kcai_annual.TSR.report.pdf
- Official KraneShares KCAI statutory prospectus: https://kraneshares.com/resources/compliance/2024_08_28_kcai_statutory.prospectus.pdf
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]]
- Navigation: [[China ETF]] | [[ETF Region Index]] | [[ETF Performance Index]]
