---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:GCOW
ticker: GCOW
exchange: Cboe BZX
fund: Pacer Global Cash Cows Dividend ETF
tracked_index: Pacer Global Cash Cows Dividend Index
benchmark: MSCI World Value Index
updated: 2026-09-01
performance_as_of: 2026-07-31
annual_rows_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-5.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/GCOW
  - geography/International
---

# GCOW Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

GCOW เป็น passive global equity ETF ที่คัดหุ้น large-cap จาก developed และ global universe ด้วย free-cash-flow yield และ dividend screen. NAV Total Return ช่วง 2017-2025 ให้ผลสะสม `128.15%` หรือ rounded-input CAGR `9.60%`, ต่ำกว่า S&P 500 Total Return ที่ `15.14%` ต่อปีในช่วงเดียวกัน; ช่วง 2021-2025 CAGR อยู่ที่ `12.66%` เทียบ S&P `14.43%`. Current secondary cross-check ณ 2026-07-31 รายงาน NAV YTD `14.7%` และ 1-year `28.3%`; ตัวเลขนี้ใช้เป็น current cross-check เพราะ factsheet ทางการล่าสุดที่ใช้มี as of 2026-03-31. Annual table ใช้ official Pacer rows ถึง 2024 และระบุ 2025 ที่มาจาก secondary source แยกชัดเจน.

## Performance check

- entity_key: Cboe BZX:GCOW
- Fund: Pacer Global Cash Cows Dividend ETF
- Classification: passive index-tracking global equity ETF; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified
- Inception: 2016-02-22; total expense ratio: 0.60%; exchange: Cboe BZX
- Tracked index: Pacer Global Cash Cows Dividend Index; strategy benchmark: MSCI World Value Index
- Return basis: NAV and market-price returns include reinvested distributions; this page uses NAV Total Return where available
- Official Pacer factsheet as of 2026-03-31: NAV USD 45.98; NAV annualised return YTD 12.46%, 1-year 30.59%, 5-year 13.72%, 10-year 10.15%, and since inception 10.75%. The same factsheet reports MSCI World Value Index returns of 1.18%, 16.60%, 9.59%, 9.35%, and 9.87% for the corresponding displayed periods
- Current secondary cross-check from AAII as of 2026-07-31: NAV YTD 14.7%, 1-year 28.3%, 3-year annualised 15.6%, 5-year annualised 13.4%, and 10-year annualised 9.8%. These current values are not silently substituted for the official factsheet's dated fields
- 2017-2025: cumulative 128.15%; rounded-input CAGR 9.60%
- 2021-2025: cumulative 81.47%; rounded-input CAGR 12.66%
- Common benchmark: S&P 500 Total Return in USD with dividends reinvested; cached reference as of 2025-12-31 and used only as a broad reference

### Annual NAV TR

| Calendar year | GCOW NAV TR | S&P 500 TR |
|---|---:|---:|
| 2017 | 20.63% | 21.83% |
| 2018 | -7.56% | -4.38% |
| 2019 | 17.53% | 31.49% |
| 2020 | -4.07% | 18.40% |
| 2021 | 13.86% | 28.71% |
| 2022 | 6.09% | -18.11% |
| 2023 | 13.69% | 26.29% |
| 2024 | 3.56% | 25.02% |
| 2025* | 27.60% | 17.88% |

`*` 2025 GCOW NAV TR is a secondary AAII calendar-year value; the official Pacer rows in the source packet run through 2024. The 2017-2025 calculations therefore use one explicitly marked secondary input. จาก rounded inputs, 2017-2025 GCOW CAGR `9.60%` เทียบ S&P `15.14%` เป็น spread `-5.55` percentage points; 2021-2025 spread คือ `-1.77` percentage points. The official MSCI World Value comparison is kept in its own factsheet date window and is not backfilled into the annual table.

## Up years / Down years

- Up years: 7; down years: 2; 2026 YTD is partial and excluded
- Best year: 2025, +27.60% (secondary source)
- Least-positive year: 2024, +3.56%
- Worst year: 2018, -7.56%
- Least-bad down year: 2020, -4.07%

## Risk read-through

GCOW เป็น global cash-flow/value/dividend factor ETF จึงมี factor concentration, value-cycle, dividend-cut, sector, country และ currency risk. ผลตอบแทนที่ดีกว่า MSCI World Value ใน factsheet ช่วง 1 และ 5 ปีไม่ควรถูกเรียก `alpha` โดยอัตโนมัติ เพราะเป็น arithmetic/strategy comparison และยังมี factor exposure กับ implementation drag. Pacer factsheet รายงาน 5-year NAV annualised `13.72%` เทียบ MSCI World Value `9.59%`; annual path ชุด 2017-2025 มี population standard deviation ประมาณ `10.91%` จาก rounded rows. Daily NAV history สำหรับ maximum drawdown และ recovery ไม่ได้ยืนยัน จึงบันทึกเป็น `not disclosed` และไม่ใช้ price-only proxy.

## Sources

- [Official Pacer Global Cash Cows product page](https://www.paceretfs.com/products/cash-cows/global-etfs)
- [Official GCOW factsheet](https://www.paceretfs.com/media/gcow.pdf)
- [Official SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1616668/000089418925006680/pacerglobalcashcowsdividen.htm)
- [Secondary AAII performance page](https://www.aaii.com/etf/ticker/GCOW)
- Source batch: [[ETF_performance_sources_2026-09-01_run-5]]
