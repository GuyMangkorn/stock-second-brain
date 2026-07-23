---
type: etf-performance
instrument_type: ETF
entity_key: XETRA:VJPA
ticker: VJPA
input_ticker: VGDTF
exchange: Deutsche Börse (Xetra)
fund: Vanguard FTSE Japan UCITS ETF (USD) Accumulating
tracked_index: FTSE Japan Index
benchmark: S&P 500 Total Return
updated: 2026-07-24
performance_as_of: 2026-06-30
current_ytd_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-07-24.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/VGDTF
  - ticker/VJPA
  - geography/Japan
---

# VGDTF / VJPA Performance

> Navigation: [[ETF Region Index]] → [[Japan ETF]] → [[ETF Performance Index]]

## Bottom line

VGDTF เป็น OTC alias ของ Vanguard FTSE Japan UCITS ETF (USD) Accumulating, share class ISIN `IE00BFMXYX26`. Vanguard's June 2026 factsheet identifies the EUR Deutsche Börse trading line as `VJPA`; therefore the canonical entity is recorded as `XETRA:VJPA`, while `VGDTF` remains the input alias. กองทุนเป็น passive physical/index-tracking Japan equity ETF และมี ongoing charges figure `0.10%`.

กองทุนเริ่ม share class วันที่ `2019-09-24` จึงยังไม่มี 10-year NAV Total Return: official 10-year field เป็น `—`. Available-period NAV TR จาก `2019-09-24` ถึง `2026-06-30` ครอบคลุมประมาณ `6.77` elapsed years และ issuer รายงาน since-inception NAV TR CAGR `9.96%`; raw NAV TR endpoints ไม่ได้เปิดเผย. Normalized endpoint ที่คำนวณจาก official CAGR อยู่ที่ประมาณ `100.00` ถึง `190.09` และไม่ใช่ raw NAV endpoint.

สำหรับ complete calendar years `2020-2025`, official KIID calendar rows (ปัดเศษหนึ่งตำแหน่ง) compound เป็นประมาณ `56.32%` หรือ CAGR `7.73%`, เทียบกับ S&P 500 Total Return `132.26%` หรือ `15.08%`. Current standardized NAV TR YTD คือ `15.27%` ณ `2026-06-30`.

## Performance check

- `entity_key`: `XETRA:VJPA`
- Input alias: `VGDTF`
- Fund: Vanguard FTSE Japan UCITS ETF (USD) Accumulating
- Share-class ISIN: `IE00BFMXYX26`
- Asset class / type: Equity / Index
- Investment method: Physical
- Inception: `2019-09-24`
- Ongoing charges figure: `0.10%`
- Tracked index: FTSE Japan Index
- Strategy: passive/indexing; Vanguard says the fund acquires index constituents physically and may use sampling where full replication is not practicable.
- Primary metric: official NAV Total Return, with gross income reinvested and net of fees/expenses.
- `10-year NAV TR`: unavailable; issuer reports `—` because the share class has less than 10 years of history.
- Available-period coverage: `2019-09-24` to `2026-06-30`, approximately `6.77` years.
- Official available-period NAV TR CAGR: `9.96%`.
- Raw start/end NAV TR values: `ไม่พบข้อมูลที่ยืนยันได้`.
- Normalized illustration from the official CAGR: start `100.00`, end approximately `190.09`; calculated illustration only, not a disclosed NAV endpoint or proxy.
- Current standardized NAV TR YTD: `15.27%` as of `2026-06-30`.
- Latest issuer NAV: `US$81.79` as of `2026-07-22`.
- Market-price returns are not mixed into the NAV TR metric.

## Annual NAV total return

Official KIID calendar-year rows are available for complete years `2020-2025` and are shown at the source's one-decimal precision. `2019` is an incomplete share-class inception year and is not presented as a complete calendar-year return.

| Year | VJPA NAV TR | FTSE Japan Index TR | S&P 500 TR |
|---|---:|---:|---:|
| 2019 | not disclosed (partial inception year) | not disclosed | not comparable; ETF partial |
| 2020 | 14.1% | 14.2% | 18.40% |
| 2021 | 1.1% | 1.2% | 28.71% |
| 2022 | -15.9% | -15.8% | -18.11% |
| 2023 | 19.5% | 19.6% | 26.29% |
| 2024 | 7.7% | 7.8% | 25.02% |
| 2025 | 25.2% | 25.3% | 17.88% |
| 2026 YTD | 15.27% | not disclosed in reviewed capture | not comparable; current year not cached |

### Window calculations

| Window | VJPA NAV TR | S&P 500 TR | VJPA minus S&P CAGR |
|---|---:|---:|---:|
| 2020-2025 | approximate cumulative `56.32%`; CAGR `7.73%` | cumulative `132.26%`; CAGR `15.08%` | `-7.35 pp` |
| 2021-2025 | approximate cumulative `37.00%`; CAGR `6.50%` | cumulative `96.17%`; CAGR `14.43%` | `-7.93 pp` |

The 2020-2025 and 2021-2025 VJPA calculations use official KIID rows rounded to one decimal, so the derived cumulative/CAGR values are approximate. S&P 500 rows use the cached USD Total Return convention for complete calendar years `2016-2025`, with dividends reinvested and as-of `2025-12-31`; 2026 is not used in the S&P comparison.

## Up years / Down years

For the six complete disclosed years `2020-2025`, VJPA had `5` up years and `1` down year.

- Best year: `2025`, `25.2%`
- Worst year: `2022`, `-15.9%`
- Current YTD: `15.27%` as of `2026-06-30`

## Risk read-through

The fund is a single-country Japan equity exposure. As of `2026-06-30`, Vanguard reported `476` stocks and Japan exposure of `100.00%`; the latest issuer page reports price/earnings `18.9x` and price/book `1.9x` as of `2026-06-30`. Daily NAV history sufficient to calculate maximum drawdown and recovery duration: `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- Official Vanguard product page: https://www.vanguard.co.uk/professional/product/etf/equity/9674/vanguard-ftse-japan-ucits-etf-usd-accumulating
- Official June 2026 factsheet: https://fund-docs.vanguard.com/FTSE_Japan_UCITS_ETF_USD_Accumulating_9674_EU_INT_EN.pdf
- Official KIID with calendar-year performance rows: https://fund-docs.vanguard.com/ie00bfmxyx26-en.pdf
- OTC alias cross-check (not used for NAV TR): https://stockanalysis.com/quote/otc/VGDTF/
- Official S&P 500 index page and cached USD Total Return convention: https://www.spglobal.com/spdji/en/indices/equity/sp-500/
- Dated source batch: [[ETF_performance_sources_2026-07-24]]

