---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:FYLD
input_ticker: FYLD
ticker: FYLD
exchange: Cboe BZX
fund: Cambria Foreign Shareholder Yield ETF
tracked_index: none; actively managed
benchmark: MSCI EAFE Index
management_mode: active-equity-long-only
active_process: systematic-active
active_process_subtype: quantitative shareholder-yield/value/quality selection
management_benchmark: MSCI EAFE Index
track_record: established
management_evidence: positive return-only
risk_evidence: not-verified
updated: 2026-09-02
performance_as_of: 2026-06-30 (official factsheet) / 2026-07-31 (secondary current)
calendar_years_as_of: 2024-12-31 (official rows) / 2025-12-31 (secondary row)
current_ytd_as_of: 2026-07-31 (secondary) / 2026-06-30 (official)
price_nav_as_of: not disclosed in reviewed official sources
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-5.md
return_basis: NAV total return; dividends and distributions reinvested; net of fund expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/FYLD
  - geography/International
  - style/active-systematic
---

# FYLD Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

FYLD คือ Cambria Foreign Shareholder Yield ETF ซึ่งเป็น active long-only
foreign-developed-equity ETF ใช้กระบวนการ systematic คัดหุ้นที่มี shareholder
yield, value และ quality สูง โดยมี management benchmark คือ MSCI EAFE Index.
Official factsheet ณ 30 มิ.ย. 2026 รายงาน rolling 10-year NAV Total Return
`11.35%` และ current YTD `13.49%`; secondary standardized capture ณ 31 ก.ค.
2026 รายงาน current YTD `22.30%*` และปี 2025 `34.20%*`.

เมื่อรวม annual rows 2016-2024 จาก official summary กับ 2025 จาก secondary
source, ช่วง 2016-2025 ให้ cumulative `153.71%*` และ rounded-input CAGR
`9.76%*`; ช่วง 2021-2025 ให้ CAGR `11.80%*`. เครื่องหมาย `*` ระบุว่าหนึ่ง
หรือหลายค่ามาจาก secondary source. ผลลัพธ์ 10-year ของกองสูงกว่า MSCI EAFE
`+1.15 pp` แบบ return-only แต่ยังไม่มี annual benchmark rows สำหรับคำนวณ hit
rate จึงจัด `management_evidence` เป็น `positive return-only` ไม่ใช่หลักฐาน
ของ persistent skill หรือ alpha.

## Performance check

- `entity_key: Cboe BZX:FYLD`; fund `Cambria Foreign Shareholder Yield ETF`; inception `2013-12-03`; listing exchange `Cboe BZX`
- Classification: `active-equity-long-only`; SEC ระบุว่ากองลงทุนอย่างน้อย 80% ใน equity securities ของ developed countries นอกสหรัฐฯ และใช้ shareholder yield/value selection; Cboe อธิบาย universe ประมาณ 100 บริษัทที่มี dividend และ net buyback ranks สูง พร้อม value/quality/low-leverage filters
- Metric: `NAV Total Return` รวม dividends/distributions ที่ reinvested และหัก fund expenses; market-price return ไม่ถูกใช้แทน NAV return
- Management benchmark: `MSCI EAFE Index`; เป็น comparator ที่สอดคล้องกับ foreign-developed-equity mandate ของกอง
- Official fund facts ณ 2026-06-30: expense ratio `0.59%`, 30-day SEC yield `3.79%`, holdings `101`, dividend frequency quarterly และ category `US Fund Foreign Small/Mid Value`
- Current official product page ระบุ FYLD เป็น actively managed ETF และใช้ systematic strategy; current dated performance fields ที่ใช้ในหน้านี้มาจาก fact sheet ซึ่งมี as-of date ชัดเจนกว่า dynamic product-page fields

| Year / window | FYLD NAV TR | MSCI EAFE Index | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | 6.53% | not disclosed | 11.96% |
| 2017 | 28.46% | not disclosed | 21.83% |
| 2018 | -13.66% | not disclosed | -4.38% |
| 2019 | 17.83% | not disclosed | 31.49% |
| 2020 | 4.35% | not disclosed | 18.40% |
| 2021 | 17.68% | not disclosed | 28.71% |
| 2022 | -5.15% | not disclosed | -18.11% |
| 2023 | 12.95% | not disclosed | 26.29% |
| 2024 | 3.22% | not disclosed | 25.02% |
| 2025 | 34.20%* | not disclosed | 17.88% |
| 2016-2025 cumulative | 153.71%* | not disclosed | 298.33% |
| 2016-2025 CAGR | 9.76%* | not disclosed | 14.82% |
| 2021-2025 cumulative | 74.64%* | not disclosed | 96.17% |
| 2021-2025 CAGR | 11.80%* | not disclosed | 14.43% |

Annual FYLD rows for 2016-2024 are from Cambria's official summary-prospectus
chart; 2025 `34.20%*` is a secondary NAV total-return row. S&P 500 TR rows use
the cached USD total-return convention for complete calendar years 2016-2025.
Annual MSCI EAFE benchmark rows are `not disclosed` in the reviewed sources and
are not inferred.

## Rolling and current performance

| Period (as of 2026-06-30) | FYLD NAV TR | MSCI EAFE Index | Return-only difference |
|---|---:|---:|---:|
| YTD | 13.49% | 9.84% | +3.65 pp |
| 1 year | 29.81% | 20.80% | +9.01 pp |
| 5 year annualized | 11.16% | 9.60% | +1.56 pp |
| 10 year annualized | 11.35% | 10.20% | +1.15 pp |
| Since inception annualized | 7.73% | 7.44% | +0.29 pp |

Official Cambria fact-sheet returns are NAV total returns with distributions
reinvested; periods longer than one year are annualized. The latest official
current-period value is `13.49%` YTD as of 2026-06-30. A secondary capture
reports `22.30%*` YTD as of 2026-07-31; it is retained separately because the
provider and as-of date differ. Current S&P 500 TR is `12.34%` YTD as of
2026-09-01, but it is not directly compared with FYLD's earlier as-of dates.

## Calendar performance

For the blended 2016-2025 window, including the marked secondary 2025 row, FYLD
has `8 / 2` up/down years. Best year is 2025 `+34.20%*`; least positive is 2024
`+3.22%`; worst is 2018 `-13.66%`; and least-bad down year is 2022 `-5.15%`.
Because the strategy/objective changed on 2020-06-01, 2016-2019 rows are useful
historical context but are not perfectly like-for-like evidence for the current
systematic process; the earlier strategy tracked the Cambria Foreign Shareholder
Yield Index.

## Risk read-through

The official 2026-06-30 fact sheet reports 101 holdings, with sector weights of
Energy `25.0%`, Financials `23.2%`, Industrials `13.8%`, Consumer Discretionary
`9.9%` and Consumer Staples `8.1%`. Country weights include Japan `25.0%`,
Britain `14.0%`, France `11.1%`, Canada `11.0%` and Hong Kong `7.9%`.

Key risks are energy/financials and country concentration, foreign-currency and
developed-market exposure, value/small-mid-cap cyclicality, systematic-process
or model behavior, active deviations from MSCI EAFE, and ETF
premium/discount/liquidity. Official compatible daily NAV history for maximum
drawdown, recovery, downside capture, tracking error or risk-adjusted
persistence was not verified; `risk_evidence` remains `not-verified`. A dated
official NAV/market-price pair was also not disclosed in the reviewed sources.

## Active management read-through

- `management_mode`: `active-equity-long-only`
- `active_process`: `systematic-active`; the process ranks developed ex-US stocks using shareholder yield (dividends, buybacks and debt paydown) alongside value, quality and leverage filters, with an approximately equal-weight portfolio
- `management_benchmark`: `MSCI EAFE Index`; selected as the official strategy-aligned comparator before assessing results
- `track_record`: `established`; fund inception is 2013-12-03
- `management_evidence`: `positive return-only`; official 10-year annualized NAV TR `11.35%` exceeds MSCI EAFE `10.20%` by `+1.15 pp`, but annual benchmark rows and a compatible hit rate are not disclosed
- `risk_evidence`: `not-verified`; return-only differences are not called alpha and no daily-NAV drawdown/recovery series was verified

## Sources

- [Cambria FYLD official product page](https://www.cambriafunds.com/fyld) — identity, Cboe BZX listing, inception, active classification, strategy, expense ratio and issuer facts
- [Cambria FYLD fact sheet](https://www.cambriafunds.com/assets/docs/FYLD-FactSheet.pdf) — official 2026-06-30 NAV returns, MSCI EAFE comparison, holdings, sector/country weights, yield and fund facts
- [FYLD summary prospectus, SEC](https://www.sec.gov/Archives/edgar/data/1529390/000121390025083085/ea0253992-03_497k.htm) — active strategy, equity mandate, fees, turnover, risk disclosures and 2020 strategy change
- [Cboe FYLD listing](https://www.cboe.com/us/equities/listings/listed_products/symbols/FYLD/) — exchange listing and shareholder-yield selection description
- [Cambria FYLD historical summary](https://cambriafunds.com/assets/docs/Cambria_FYLD_Summary.pdf) — official 2016-2024 annual NAV return chart
- [AAII FYLD performance](https://www.aaii.com/etf/ticker/FYLD) — secondary 2025 annual row and current YTD through 2026-07-31
- [S&P Dow Jones Indices current all-returns table](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization) — current S&P 500 Total Return reference as of 2026-09-01
- [[ETF_performance_sources_2026-09-02_run-5]] | [[ETF Performance Index]]
