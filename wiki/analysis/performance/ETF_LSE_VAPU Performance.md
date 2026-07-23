---
type: etf-performance
instrument_type: ETF
entity_key: LSE:VAPU
ticker: VFPAF
canonical_ticker: VAPU
exchange: London Stock Exchange
fund: Vanguard FTSE Developed Asia Pacific ex Japan UCITS ETF (USD) Accumulating
share_class: USD Accumulating
isin: IE00BK5BQZ41
tracked_index: FTSE Developed Asia Pacific ex Japan Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VFPAF
  - geography/Asia-Pacific
---

# VFPAF / VAPU Performance

> Navigation: [[ETF Region Index]] → [[Asia-Pacific ETF]] → [[ETF Performance Index]]

## Bottom line

VFPAF เป็น OTC alias ของ Vanguard FTSE Developed Asia Pacific ex Japan UCITS ETF (USD) Accumulating ซึ่ง issuer ระบุ canonical LSE ticker เป็น `VAPU` (`LSE:VAPU`, ISIN `IE00BK5BQZ41`). กองทุนเป็น passive/index-tracking physical equity ETF ที่ติดตาม FTSE Developed Asia Pacific ex Japan Index. Share-class inception คือ `2019-09-24`; ดังนั้น `10-year NAV TR unavailable`. Official available-period NAV Total Return CAGR คือ `13.96%` สำหรับ `2019-09-24` ถึง `2026-06-30` หรือประมาณ `6.765` ปี. Latest standardized NAV TR YTD คือ `47.09%` ณ `2026-06-30`; 2026-07-22 date-to-date YTD ไม่ได้เปิดเผยใน reviewed official capture.

## Performance check

- Input ticker: `VFPAF` (OTC alias)
- Canonical entity_key: `LSE:VAPU`
- Fund: Vanguard FTSE Developed Asia Pacific ex Japan UCITS ETF (USD) Accumulating
- ISIN: `IE00BK5BQZ41`
- Inception: `2019-09-24`
- Asset class / type: Equity; passive/index-tracking; physical
- Tracked index: FTSE Developed Asia Pacific ex Japan Index
- Ongoing Charges Figure: `0.15%`
- Metric: NAV Total Return, net of fees, with dividends and capital-gains distributions reinvested
- Available-period window: `2019-09-24` → `2026-06-30`
- Actual elapsed years: `6.765`
- Start/end TR values: `not disclosed` in the reviewed official capture
- Available-period NAV TR CAGR: `13.96%`
- Official 10-year field: `—`; `10-year NAV TR unavailable`
- Latest standardized NAV TR YTD: `47.09%` as of `2026-06-30`
- Latest official NAV: `US$55.71` as of `2026-07-22`; this is a NAV observation, not a substitute for a current date-to-date NAV TR return
- Issuer benchmark: FTSE Developed Asia Pacific ex Japan Index; common comparison benchmark: S&P 500 Total Return (USD, dividends reinvested)

### Rolling 12-month NAV Total Return

Vanguard's factsheet provides rolling 12-month annual observations rather than a complete calendar-year NAV table. These periods are shown with their exact dates and are not labelled as calendar-year returns.

| Period | VAPU NAV TR (net of expenses) | FTSE Developed Asia Pacific ex Japan Index TR |
|---|---:|---:|
| 2020-07-01 to 2021-06-30 | 44.95% | 45.13% |
| 2021-07-01 to 2022-06-30 | -21.91% | -21.88% |
| 2022-07-01 to 2023-06-30 | 7.54% | 7.62% |
| 2023-07-01 to 2024-06-30 | 7.31% | 7.41% |
| 2024-07-01 to 2025-06-30 | 12.95% | 12.97% |
| 2025-07-01 to 2026-06-30 | 72.75% | 72.97% |

หมายเหตุ: The source PDF presents these six rolling periods as a horizontal date sequence; the table preserves the exact sequence and does not convert it into calendar-year performance.

### S&P 500 Total Return reference

The following complete calendar-year S&P 500 TR rows use the cached USD Total Return convention as of `2025-12-31`. They are a reference comparison only; their calendar windows are not aligned with VFPAF's `2019-09-24` to `2026-06-30` since-inception window.

| Calendar year | S&P 500 TR |
|---|---:|
| 2020 | 18.40% |
| 2021 | 28.71% |
| 2022 | -18.11% |
| 2023 | 26.29% |
| 2024 | 25.02% |
| 2025 | 17.88% |

- S&P 500 TR calendar reference `2020-2025`: cumulative `132.26%`, CAGR `15.08%`
- No date-aligned S&P 500 TR CAGR is claimed for the VFPAF since-inception window.

## Performance read-through

- Official available-period NAV TR CAGR: `13.96%` for approximately `6.765` years; raw start/end TR values and cumulative return are `not disclosed`.
- Official five-year NAV TR CAGR: `11.95%` as of `2026-06-30`; it is not a 10-year result.
- The rolling 12-month fund rows generally stayed close to the issuer benchmark, with the largest disclosed gap in the reviewed set around `0.18 percentage points`.
- Current standardized NAV TR YTD: `47.09%` as of `2026-06-30`; current `2026-07-22` date-to-date YTD and daily NAV history sufficient for max drawdown/recovery are `ไม่พบข้อมูลที่ยืนยันได้`.

## Risk read-through

VAPU มีหุ้นประมาณ `376` ตัว as of `2026-06-30`; country exposure หลักคือ South Korea `54.8%`, Australia `29.5%`, Hong Kong `8.3%`, Singapore `6.5%`, และ New Zealand `0.9%`. Three-year annualized tracking error คือ `0.10%` as of `2026-06-30`. ความเสี่ยงหลักคือ concentration ใน South Korea, regional FX และ equity-market volatility แม้กองทุนจะเป็น passive physical replication.

## Sources

- Official product page: [Vanguard FTSE Developed Asia Pacific ex Japan UCITS ETF (USD) Accumulating](https://www.vanguard.co.uk/uk-fund-directory/product/etf/equity/9676/ftse-developed-asia-pacific-ex-japan-ucits-etf-usd-accumulating)
- Official factsheet: [VAPU / 9676 factsheet](https://fund-docs.vanguard.com/FTSE_Developed_Asia_Pacific_ex_Japan_UCITS_ETF_USD_Accumulating_9676_EU_INT_UK_EN.pdf)
- Official annual report: [Vanguard Funds plc annual report](https://fund-docs.vanguard.com/etf-annual-report.pdf)
- Official prospectus: [Vanguard ETF prospectus](https://fund-docs.vanguard.com/etf-prospectus-en.pdf)
- OTC alias cross-check: [VFPAF market identity page](https://stockanalysis.com/quote/otc/VFPAF/); used only to cross-check the input alias, not as a NAV TR source
- Common reference benchmark: [S&P 500 official index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); annual rows use the cached USD Total Return convention as of `2025-12-31`
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
