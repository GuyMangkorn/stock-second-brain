---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FIVA
ticker: FIVA
exchange: NYSE Arca
fund: Fidelity International Value Factor ETF
tracked_index: Fidelity International Value Factor Index (Net)
benchmark: Fidelity International Value Factor Index (Net)
updated: 2026-09-01
performance_as_of: 2026-07-31
annual_rows_as_of: 2026-06-30
current_ytd_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-6.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FIVA
  - geography/International
---

# FIVA Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

FIVA เป็น passive strategic-beta international equity ETF ที่ใช้ Fidelity International Value Factor Index ซึ่งเป็น rules-based factor index. Official NAV TR rows ที่ยืนยันได้ครอบคลุม 2019-2025: ผลตอบแทนสะสม `119.94%` หรือ rounded-input CAGR `11.92%`; ช่วง 2021-2025 CAGR `13.32%`, ต่ำกว่า S&P 500 TR ที่ `14.43%`. Latest YTD cross-check คือ `+16.70%` ณ 2026-07-31 จาก secondary source; Fidelity official factsheet รายงาน `+14.34%` ณ 2026-06-30.

## Performance check

- entity_key: NYSE Arca:FIVA
- Fund: Fidelity International Value Factor ETF
- Classification: passive index-tracking / strategic-beta equity ETF; no leverage, inverse, option-income, bond, commodity, currency, multi-asset or derivative-defined payoff was identified
- Inception: 2018-01-16; total expense ratio: 0.18% as of 2026-06-30; exchange: NYSE Arca
- Tracked index: Fidelity International Value Factor Index (Net), a rules-based index for large- and mid-capitalization developed international companies with attractive valuations
- Return basis: NAV Total Return includes changes in share price and reinvestment of dividends and capital gains; market-price return is kept separate
- Official quote snapshot crawled 2026-09-01: NAV USD 39.837917; market price USD 39.74
- YTD: official Fidelity NAV TR `14.34%` as of 2026-06-30; latest secondary NAV TR cross-check `16.70%` as of 2026-07-31
- 2019-2025: cumulative `119.94%`; rounded-input CAGR `11.92%`
- 2021-2025: cumulative `86.88%`; rounded-input CAGR `13.32%`
- Common benchmark: S&P 500 Total Return in USD with dividends reinvested; cached reference as of 2025-12-31 and used only as a broad reference

### Annual NAV TR

| Calendar year | FIVA NAV TR | S&P 500 TR |
|---|---:|---:|
| 2019 | 19.70% | 31.49% |
| 2020 | -1.68% | 18.40% |
| 2021 | 16.05% | 28.71% |
| 2022 | -10.42% | -18.11% |
| 2023 | 20.26% | 26.29% |
| 2024 | 3.34% | 25.02% |
| 2025 | 44.65% | 17.88% |

จาก rounded annual inputs, 2019-2025 FIVA CAGR `11.92%` เทียบ S&P `17.29%` เป็น spread `-5.37` percentage points. ช่วง 2021-2025 FIVA CAGR `13.32%` เทียบ S&P `14.43%` เป็น spread `-1.10` percentage points. Fidelity factsheet ไม่รายงาน 2018 calendar row แม้กองทุนเริ่มต้นในเดือนมกราคม จึงไม่ backfill ปีดังกล่าว.

## Up years / Down years

- Up years: 5; down years: 2
- Best year: 2025, +44.65%
- Least-positive year: 2024, +3.34%
- Worst year: 2022, -10.42%
- Least-bad down year: 2020, -1.68%

## Risk read-through

FIVA มี value-factor, country/currency, foreign-market, turnover และ tracking risk. Calendar-row population standard deviation 2019-2025 อยู่ที่ประมาณ `16.76%`; Fidelity รายงาน 3-year standard deviation `13.24%`, beta `1.00`, Sharpe `1.32` และ tracking error `0.10` เทียบ Fidelity International Value Factor Index ณ 2026-06-30. ค่าใช้จ่ายสุทธิ `0.18%` และ turnover rate `69%` ณ 2026-06-30. Daily NAV history สำหรับ maximum drawdown และ recovery ไม่ได้ยืนยัน จึงบันทึกเป็น `not disclosed`. FIVA เป็น passive implementation จึงไม่ตีความ spread จาก benchmark ว่าเป็น manager alpha.

## Sources

- [Official Fidelity FIVA factsheet](https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F9887716.PDF) — identity, strategy, annual NAV rows, official June 2026 YTD, fees and risk fields
- [Official Fidelity FIVA quote](https://digital.fidelity.com/prgw/digital/research/quote/dashboard/summary?symbol=FIVA) — current NAV, market price and primary exchange
- [FIVA SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/945908/000094590826000084/filing10958.htm) — objective, passive strategy, fees, exchange and manager disclosures
- [Schwab FIVA performance page](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=fiva) — secondary July 2026 NAV YTD cross-check
- Source batch: [[ETF_performance_sources_2026-09-01_run-6]]
