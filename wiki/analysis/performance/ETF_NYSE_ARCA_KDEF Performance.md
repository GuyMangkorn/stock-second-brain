---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:KDEF
ticker: KDEF
exchange: NYSE Arca
fund: PLUS Korea Defense Industry Index ETF
tracked_index: Korea Defense Industry Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/KDEF
  - geography/South-Korea
---

# KDEF Performance

> Navigation: [[ETF Region Index]] → [[South Korea ETF]] → [[ETF Performance Index]]

## Bottom line

KDEF เป็น PLUS Korea Defense Industry Index ETF, canonical `NYSE Arca:KDEF`,
กองทุน passive, index-tracking equity ETF ที่ติดตาม Korea Defense Industry
Index. กองทุนเริ่มดำเนินงาน 2025-02-05 จึงมีประวัติประมาณ `1.40` ปี ณ
2026-06-30 และ `10-year NAV TR unavailable` อย่างตรงไปตรงมา. Official issuer
รายงาน since-inception NAV Total Return cumulative `105.69%` และ annualized
`67.39%` สำหรับ 2025-02-05 ถึง 2026-06-30; current standardized NAV TR YTD คือ
`-8.13%` ณ 2026-06-30. ไม่มีการสร้าง proxy หรือเติม annual rows ที่ issuer ไม่เปิดเผย.

## Performance check

- entity_key: NYSE Arca:KDEF
- Inception: 2025-02-05
- Metric: NAV Total Return including reinvested distributions and fund expenses; issuer performance table is NAV total return with distributions reinvested and expenses reflected
- Tracked index (issuer benchmark): Korea Defense Industry Index
- Benchmark: S&P 500 Total Return (USD, dividends reinvested; common reference benchmark)
- 10-year NAV TR coverage: unavailable because inception `2025-02-05` to `2026-06-30` is only `510` elapsed days, approximately `1.40` years
- Available-period NAV TR coverage: 2025-02-05 to 2026-06-30; actual elapsed period `1.40` years
- Available-period NAV TR cumulative / annualized: `105.69%` / `67.39%` (official PLUS issuer)
- Normalized NAV TR: start `100.00`; end `205.69` (official since-inception cumulative return; raw NAV endpoints are not disclosed)
- Coverage/source note: official complete-calendar annual NAV rows are not disclosed; S&P 500 2025 row reuses cached USD Total Return convention, while no matching current S&P 500 Total Return YTD was disclosed in the reviewed official capture; market-price return is not mixed

| Period | KDEF NAV TR | S&P 500 TR | Coverage note |
|---|---:|---:|---|
| 2025 calendar year | not disclosed | 17.88% | KDEF began 2025-02-05; no complete-calendar KDEF NAV row disclosed |
| 2026 YTD through 2026-06-30 | -8.13% | not disclosed | issuer current S&P 500 TR YTD not disclosed in reviewed official capture |
| KDEF inception to 2026-06-30 | 105.69% | not disclosed | no matching S&P 500 TR window in the reviewed official source set |

## Available-period comparison

- `10-year NAV TR unavailable`; KDEF has not completed 10 years of operation.
- Official since-inception NAV TR annualized return is `67.39%` for 2025-02-05 to 2026-06-30; this is not a 10-year CAGR.
- Official 2025 full-calendar NAV TR, complete annual rows, and a matching S&P 500 TR return for KDEF's exact inception-to-date window are `not disclosed`.
- Current standardized NAV TR YTD: `-8.13%` as of 2026-06-30; latest issuer NAV `US$38.83` as of 2026-07-17.

## Risk read-through

KDEF เป็น South Korea single-country, defense-industry thematic equity ETF.
Official issuer reports 20 holdings and total annual fund operating expenses
`0.65%` as of the reviewed page. SEC prospectus describes the fund as
non-diversified, normally investing at least 80% in index securities, and
concentrated in the Aerospace and Defense industry; country, sector, currency,
single-issuer and limited-history risk จึงสูงกว่ากอง broad-market. Daily NAV
history sufficient for max drawdown and recovery คือ `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official PLUS ETF product and performance page: https://plusetf.com/kdef
- SEC summary prospectus (March 30, 2026): https://www.sec.gov/Archives/edgar/data/1547950/000121390026036312/ea0282658-04_497k.htm
- Official S&P 500 index page: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- ETF source batch: [[ETF_performance_sources_2026-07-24]] | [[ETF Performance Index]]
