---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:FLAU
ticker: FLAU
exchange: NYSE Arca
fund: Franklin FTSE Australia ETF
tracked_index: FTSE Australia Capped Index-NR
benchmark: S&P 500 Total Return
updated: 2026-07-22
performance_as_of: 2026-03-31
current_ytd_as_of: 2026-07-02
price_nav_as_of: 2026-07-17
source_batch: raw/imports/ETF_performance_sources_2026-07-22.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - ticker/FLAU
  - geography/Australia
---

# FLAU Performance

> Navigation: [[ETF Region Index]] → [[Australia ETF]] → [[ETF Performance Index]]

## Bottom line

FLAU ให้ `NAV Total Return` เป็นบวก 6 จาก 8 complete calendar years ในช่วง
2018-2025; การทบต้นจาก annual rows ให้ cumulative `66.33%` หรือ CAGR `6.57%`.
ปีดีที่สุดคือ 2019 ที่ `+23.20%` และแย่ที่สุดคือ 2018 ที่ `-12.25%`. Official
issuer YTD ล่าสุดที่ยืนยันได้คือ `+7.34%` ณ 2 ก.ค. 2026; issuer แสดง NAV ล่าสุด
`US$34.04` ณ 17 ก.ค. 2026 แต่ยังไม่เปิดเผย YTD ใหม่ใน capture เดียวกัน. Secondary
total-return proxy ล่าสุดอยู่ที่ `+10.91%*` ณ 15 ก.ค. 2026 และไม่ใช่ official NAV.

## Performance check

- `entity_key: NYSE Arca:FLAU`
- Inception: 2 พ.ย. 2017
- Metric: `NAV Total Return` รวมเงินปันผล reinvested และ fund expenses
- Tracked index (issuer benchmark): `FTSE Australia Capped Index-NR`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ FLAU)
- 10-year NAV TR CAGR: `ไม่พบข้อมูลที่ยืนยันได้` เพราะ official history ยังไม่ครบ
  10 ปี; 2016 อยู่ก่อนกองทุนเริ่มต้นและ 2017 เป็น inception-year partial ที่
  factsheet ไม่แสดงเป็นตัวเลข
- Since-inception NAV annualized return: `7.88%` ณ 31 พ.ค. 2026 จาก issuer
- Annual coverage: official complete calendar years 2018-2025 จาก [issuer factsheet](https://www.franklintempleton.com/forms-literature/download/FLAU-FF); annual-row CAGR เป็น calculation จากตัวเลขที่ issuer ปัดเศษ
- S&P 500 cache 2018-2025: cumulative `192.03%`; CAGR `14.33%` จาก rounded
  annual inputs; เป็น common reference ไม่ใช่ issuer benchmark

| ปี | FLAU NAV TR | S&P 500 TR |
|---|---:|---:|
| 2018 | -12.25% | -4.38% |
| 2019 | 23.20% | 31.49% |
| 2020 | 11.04% | 18.40% |
| 2021 | 9.93% | 28.71% |
| 2022 | -5.42% | -18.11% |
| 2023 | 13.38% | 26.29% |
| 2024 | 0.92% | 25.02% |
| 2025 | 16.47% | 17.88% |

## Up years / Down years

- Up years / Down years: `6 / 2` ใน 2018-2025
- Best: 2019, `+23.20%`
- Least positive: 2024, `+0.92%`
- Worst: 2018, `-12.25%`
- Least bad down year: 2022, `-5.42%`
- 2018-2025 cumulative / CAGR: FLAU `66.33%` / `6.57%`; S&P 500 TR `192.03%` /
  `14.33%`
- 2021-2025 cumulative / CAGR: FLAU `38.56%` / `6.74%`; S&P 500 TR `96.17%` /
  `14.43%`
- Current YTD: official FLAU NAV `+7.34%` ณ 2 ก.ค. 2026 จาก [issuer product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26365/SINGLCLASS/franklin-ftse-australia-etf); latest official NAV `US$34.04` ณ 17 ก.ค. 2026. Secondary total-return proxy `+10.91%*` ณ 15 ก.ค. 2026 จาก [FinanceCharts](https://www.financecharts.com/etfs/FLAU/performance) is separate and not used in NAV rankings.

## Risk read-through

FLAU เป็น passive, indexed, single-country Australia equity ETF. Annual-return
population standard deviation จาก rounded 2018-2025 rows อยู่ที่ `11.06%` และ
issuer รายงาน 3-year NAV standard deviation `16.99%` ณ 31 มี.ค. 2026. Expense
ratio คือ `0.09%` และจ่าย distribution แบบ semi-annual. Sector exposure ล่าสุดที่
issuer แสดง ณ 2 ก.ค. 2026 กระจุกใน Financials `36.94%` และ Materials `25.40%`,
จึงมี country, commodity และ FX sensitivity; ไม่ควรตีความเป็น crisis hedge.
Maximum drawdown และ recovery จาก daily NAV TR ยัง `ไม่พบข้อมูลที่ยืนยันได้` ใน
issuer capture จึงไม่คำนวณจาก annual table. `*` คือ secondary dividend-reinvested
total-return proxy ที่รวม price appreciation และ reinvested dividends แต่ไม่ใช่
official NAV series.

## Sources

- [Franklin Templeton FLAU product page](https://www.franklintempleton.com/investments/options/exchange-traded-funds/products/26365/SINGLCLASS/franklin-ftse-australia-etf) — identity, NYSE Arca, inception, benchmark, expense ratio, current YTD/NAV, classification, sectors and distribution frequency
- [Franklin Templeton FLAU factsheet](https://www.franklintempleton.com/forms-literature/download/FLAU-FF) — official NAV return definition, 2018-2025 calendar rows, since-inception return and 3-year standard deviation; as of 31 มี.ค. 2026
- [FinanceCharts FLAU performance](https://www.financecharts.com/etfs/FLAU/performance) — secondary current total-return proxy, as of 15 ก.ค. 2026; not NAV
- [Official S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common-reference index identity and methodology
- [S&P U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — cached S&P 500 TR reference through 2025
- [[ETF_performance_sources_2026-07-22]] | [[ETF Performance Index]]
