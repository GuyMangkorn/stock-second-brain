---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IPAC
ticker: IPAC
exchange: NYSE Arca
fund: iShares Core MSCI Pacific ETF
tracked_index: MSCI Pacific IMI Index (Net)
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-07-22
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/IPAC
  - geography/Asia-Pacific
---

# IPAC Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

IPAC เป็น passive/index-tracking equity ETF ที่ติดตาม MSCI Pacific IMI Index (Net). Official iShares performance data ให้ rolling 10-year NAV Total Return CAGR `9.23%` สำหรับ `2016-06-30` ถึง `2026-06-30` ครบ `10.00 elapsed years`. ใน common calendar rows `2021-2025` NAV TR compound เป็น `35.41%` หรือ CAGR `6.25%`, เทียบกับ S&P 500 Total Return `96.17%` หรือ `14.43%`; IPAC ต่ำกว่าประมาณ `8.18 pp` ต่อปีในหน้าต่างนี้.

## Performance check

- entity_key: `NYSE Arca:IPAC`
- Fund: iShares Core MSCI Pacific ETF
- Inception: `2014-06-10`
- Asset class / type: Equity; passive/index-tracking
- Tracked index: MSCI Pacific IMI Index (Net)
- Expense ratio: `0.09%`
- Metric: NAV Total Return including reinvested distributions and fund expenses
- Official 10-year window: `2016-06-30` → `2026-06-30`
- Actual elapsed years: `10.00`
- Official 10-year NAV TR cumulative: `141.81%`
- Official 10-year NAV TR CAGR: `9.23%`
- Raw start/end NAV TR values: `not disclosed` in the reviewed official capture; normalized TR is `100.00` → `241.81` from the published cumulative result, not a raw NAV endpoint
- Issuer benchmark: MSCI Pacific IMI Index (Net); common comparison benchmark: S&P 500 Total Return (USD, dividends reinvested)
- Current NAV TR YTD: `13.75%` as of `2026-07-22`

### Annual NAV Total Return

Official iShares calendar-year NAV rows visible in the reviewed capture cover `2021-2025`. Rows for `2016-2020` are `not disclosed`; they are not reconstructed from a proxy.

| Year | IPAC NAV TR | MSCI Pacific IMI Index (Net) | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | not disclosed | not disclosed | 11.96% |
| 2017 | not disclosed | not disclosed | 21.83% |
| 2018 | not disclosed | not disclosed | -4.38% |
| 2019 | not disclosed | not disclosed | 31.49% |
| 2020 | not disclosed | not disclosed | 18.40% |
| 2021 | 3.03% | 2.53% | 28.71% |
| 2022 | -13.31% | -13.06% | -18.11% |
| 2023 | 14.33% | 14.36% | 26.29% |
| 2024 | 5.56% | 6.26% | 25.02% |
| 2025 | 25.62% | 24.42% | 17.88% |

### Common 2021-2025 calculation

- IPAC NAV TR: `1.0303 × 0.8669 × 1.1433 × 1.0556 × 1.2562 - 1 = 35.41%`; CAGR `6.25%`
- S&P 500 TR: `1.2871 × 0.8189 × 1.2629 × 1.2502 × 1.1788 - 1 = 96.17%`; CAGR `14.43%`
- Relative CAGR: IPAC trails S&P 500 TR by approximately `8.18 percentage points`

## Up years / Down years

- Complete disclosed years `2021-2025`: up `4`, down `1`
- Best disclosed year: `2025`, `25.62%`
- Worst disclosed year: `2022`, `-13.31%`
- Available disclosed calendar-period cumulative/CAGR: `35.41% / 6.25%` for `2021-2025`
- Official rolling 10-year NAV TR cumulative/CAGR: `141.81% / 9.23%` for `2016-06-30` to `2026-06-30`
- Current YTD: `13.75%` as of `2026-07-22`; this is a separate current date-to-date observation from the standardized `2026-06-30` rolling-period data

## Risk read-through

IPAC มี 1,370 holdings as of `2026-07-22`; geographic exposure หลักคือ Japan `69.37%`, Australia `19.46%`, Singapore `5.17%`, Hong Kong `4.97%`, และ cash/derivatives `0.45%`. Three-year standard deviation คือ `13.01%` as of `2026-07-22`. ความเสี่ยงหลักคือ country concentration ใน Japan, regional FX และความผันผวนของ equity markets; daily NAV history ที่ยืนยันได้เพียงพอสำหรับคำนวณ max drawdown/recovery ไม่ได้เปิดเผยใน reviewed capture.

## Sources

- Official issuer product/performance page: [iShares Core MSCI Pacific ETF](https://www.ishares.com/us/products/264619/ishares-core-msci-pacific-etf)
- Official factsheet: [IPAC fact sheet](https://www.ishares.com/us/literature/fact-sheet/ipac-ishares-core-msci-pacific-etf-fund-fact-sheet-en-us.pdf)
- Official prospectus: [IPAC summary prospectus](https://www.ishares.com/us/literature/summary-prospectus/sp-ishares-core-msci-pacific-etf-7-31.pdf)
- Official report: [iShares semi-annual report](https://www.ishares.com/us/literature/semi-annual-report/sar-ipac-en.pdf)
- Common reference benchmark: [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); annual rows use the cached USD Total Return convention as of `2025-12-31`
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
