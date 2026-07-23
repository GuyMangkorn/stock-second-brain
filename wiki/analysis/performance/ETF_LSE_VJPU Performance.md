---
type: etf-performance
instrument_type: ETF
entity_key: LSE:VJPU
ticker: VFJUF
exchange: London Stock Exchange
fund: Vanguard FTSE Japan UCITS ETF - USD Hedged Accumulating
tracked_index: FTSE Japan Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-05-31
current_ytd_as_of: 2026-05-31
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VFJUF
  - geography/Japan
---

# VFJUF Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

VFJUF เป็น OTC alias ที่ resolve ได้เป็น Vanguard FTSE Japan UCITS ETF - USD Hedged Accumulating ซึ่งมี canonical issuer listing เป็น `LSE:VJPU`, ISIN `IE00BFMXZJ56`. กองทุนเป็น Irish UCITS, passive physical/index-tracking equity ETF ที่ติดตาม FTSE Japan Index และใช้ currency hedging ใน share class USD; ไม่ใช่ active, leveraged, inverse หรือ derivative-heavy ETF. Share-class inception คือ 2020-01-31 จึงยังไม่มี 10-year NAV Total Return: `10-year NAV TR unavailable`.

Official Vanguard factsheet รายงาน available-period NAV Total Return CAGR `20.29%` จาก 2020-01-31 ถึง 2026-05-31 หรือประมาณ `6.33` elapsed years. Raw NAV TR endpoints ไม่ได้เปิดเผย; normalized start `100.00` และ end ประมาณ `322.00` เป็นค่าคำนวณจาก CAGR ที่ issuer ปัดเศษ. Latest standardized NAV TR YTD ที่ยืนยันได้คือ `19.41%` ณ 2026-05-31; current 2026-07-22 YTD ไม่ได้เปิดเผยใน official capture.

## Performance check

- entity_key: `LSE:VJPU`
- Input ticker: `VFJUF` (OTC alias); canonical exchange ticker: `VJPU` on London Stock Exchange
- Inception: `2020-01-31`
- Metric: NAV Total Return; income/distributions reinvested and fund expenses reflected in NAV performance
- Tracked index: `FTSE Japan Index`; USD-hedged share class benchmark is `FTSE Japan Index Hedged in USD`
- Structure: passive/index-tracking, physical, Irish UCITS equity ETF; OCF `0.13%`; accumulated share class
- 10-year NAV TR coverage: unavailable because actual share-class history is under 10 years
- Status: `completed_available_period_no_10Y`
- Available-period NAV TR: `2020-01-31` to `2026-05-31`; actual years approximately `6.33`; official since-inception annualized return `20.29%`
- Normalized available-period TR: start `100.00`; end approximately `322.00` (calculated as `100 × (1 + 20.29%)^6.33`; raw endpoints not disclosed)
- Latest official NAV: `US$81.79` as of `2026-07-22`; this is a NAV level, not a substitute for current YTD NAV TR

### Rolling 12-month return table

These are the issuer's rolling 12-month periods, not complete calendar years. They are shown as reported and must not be relabeled as 10-year returns.

| Period | VJPU NAV TR | FTSE Japan Index Hedged in USD TR |
|---|---:|---:|
| 2020-06-01 to 2021-05-31 | 26.97% | 27.16% |
| 2021-06-01 to 2022-05-31 | 1.54% | 1.94% |
| 2022-06-01 to 2023-05-31 | 17.88% | 18.26% |
| 2023-06-01 to 2024-05-31 | 39.31% | 39.68% |
| 2024-06-01 to 2025-05-31 | 6.90% | 6.83% |
| 2025-06-01 to 2026-05-31 | 50.56% | 51.02% |

### S&P 500 Total Return reference

S&P 500 rows use the vault's cached USD Total Return convention as of 2025-12-31. The S&P table is a common reference benchmark, not the issuer benchmark, and its calendar-year windows do not exactly match Vanguard's rolling periods.

| Complete calendar year | S&P 500 TR |
|---|---:|
| 2020 | 18.40% |
| 2021 | 28.71% |
| 2022 | -18.11% |
| 2023 | 26.29% |
| 2024 | 25.02% |
| 2025 | 17.88% |

S&P 500 TR compounds to `132.26%` / CAGR `15.08%` over complete calendar years 2020-2025. This is reference-only because it is not the same start/end date as the fund's 2020-01-31 to 2026-05-31 available period. Vanguard's official five-year NAV TR CAGR is `21.83%` as of 2026-05-31; it is a five-year result, not a 10-year result.

## Up years / Down years

- Up/down counts for complete calendar years are `not disclosed` in the reviewed official capture; the issuer provides rolling 12-month periods instead.
- Best / worst reported rolling 12-month periods: `2025-06-01 to 2026-05-31`, `50.56%`; `2021-06-01 to 2022-05-31`, `1.54%`.
- Current standardized NAV TR YTD: `19.41%` as of `2026-05-31`; current `2026-07-22` YTD is `not disclosed`.
- Daily NAV history sufficient to calculate max drawdown and recovery is `ไม่พบข้อมูลที่ยืนยันได้` in this lean capture.

## Risk read-through

กองทุนมี exposure ญี่ปุ่น `100.0%` และถือหุ้นประมาณ `476` ตัว ณ 2026-06-30. USD-hedged share class ใช้ currency hedging เพื่อลดผลกระทบจาก JPY/USD แต่ Vanguard ระบุว่า hedge ไม่สามารถกำจัด currency risk ได้ทั้งหมด. Derivatives ที่เปิดเผยมีบทบาทด้าน currency hedge ไม่ใช่กลยุทธ์ leveraged, inverse หรือ derivative-heavy. ความเสี่ยงหลักจึงเป็น Japan single-country, equity/sector concentration, JPY/USD hedge-cost และ tracking difference.

## Sources

- [Official Vanguard VJPU product page](https://www.vanguard.co.uk/professional/product/etf/equity/9541/ftse-japan-ucits-etf-usd-hedged-accumulating)
- [OTC VFJUF alias cross-check](https://stockanalysis.com/quote/otc/VFJUF/) (secondary market identity; canonical issuer listing remains `LSE:VJPU`)
- [Official Vanguard VJPU factsheet](https://fund-docs.vanguard.com/FTSE_Japan_UCITS_ETF_USD_Hedged_Accumulating_9541_EU_INT_UK_EN.pdf)
- [Official Vanguard Funds plc annual report](https://fund-docs.vanguard.com/etf-annual-report.pdf)
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
