---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:IDMO
input_ticker: IDMO
ticker: IDMO
exchange: NYSE Arca
fund: Invesco S&P International Developed Momentum ETF
tracked_index: S&P World Ex-U.S. Momentum Index
benchmark: S&P World Ex-U.S. Momentum Index
updated: 2026-08-30
performance_as_of: 2025-12-31
rolling_5y_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
market_price_as_of: not disclosed in reviewed official source
nav_as_of: not disclosed in reviewed official source
fund_facts_as_of: 2025-12-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/IDMO
  - geography/developed-ex-North-America
  - style/passive-index
  - theme/momentum
---

# IDMO Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IDMO คือ Invesco S&P International Developed Momentum ETF บน NYSE Arca ซึ่ง
ติดตาม S&P World Ex-U.S. Momentum Index. กองลงทุนอย่างน้อย 90% ใน securities
ของ index และ reconstitute/rebalance semi-annually. Official Invesco performance
source ณ 31 ธ.ค. 2025 รายงาน NAV Total Return 1-year 41.85%, 3-year annualized
24.64%, 5-year 13.99%, 10-year 12.12% และ since inception 8.62%.
Current YTD ที่พบจาก secondary Schwab performance page คือ 10.5%* ณ 31 ก.ค.
2026; official Invesco current month-end YTD ไม่ได้ render ใน reviewed page.

Official calendar rows 2016-2025 ให้ IDMO cumulative 213.90% และ rounded-input
CAGR 12.12%; 2021-2025 cumulative 92.45% และ CAGR 13.99%. ใน 2016-2025
มี 8 up years / 2 down years, best yearคือ 2025 +41.85% และ worst yearคือ
2018 -16.58%. Underlying index row ปี 2016 ไม่ available และเริ่มใช้งาน
S&P World Ex-U.S. Momentum Index ตั้งแต่ 18 มี.ค. 2016; จึงไม่สร้าง full
fund/index series จากข้อมูลที่ขาด.

## Performance check

- entity_key: NYSE Arca:IDMO; fund inception: 24 ก.พ. 2012; management fee and
  total expense ratio 0.25%; 30-day SEC yield 2.41%; holdings 180 ณ 31 ธ.ค. 2025
- Metric: NAV Total Return ใน USD รวม reinvested distributions และหัก fund
  expenses; market-price return แยกจาก NAV return
- Management mode: passive-index; tracked index และ management benchmark คือ
  S&P World Ex-U.S. Momentum Index
- กองเน้น securities ที่มี highest momentum score จาก S&P World Ex-U.S. Index,
  ซึ่งครอบคลุม developed markets excluding the U.S. and South Korea
- Index name เปลี่ยนจาก S&P Momentum Developed ex-U.S. & South Korea LargeMidCap
  เป็น S&P World Ex-U.S. Momentum Index มีผลหลัง close 31 พ.ค. 2024 โดย official
  filing ระบุว่า methodology ไม่เปลี่ยน

Official performance ณ 31 ธ.ค. 2025:

| Period | IDMO NAV TR | S&P World Ex-U.S. Momentum | Return-only difference |
|---|---:|---:|---:|
| 1 year | 41.85% | 42.65% | -0.80 pp |
| 3 years annualized | 24.64% | 25.03% | -0.39 pp |
| 5 years annualized | 13.99% | 14.27% | -0.28 pp |
| 10 years annualized | 12.12% | not available | not applicable |
| Since inception annualized | 8.62% | not available | not applicable |

Current YTD cross-check:

| Period end | IDMO NAV TR proxy | Source note |
|---|---:|---|
| 2026-07-31 | 10.5%* | Schwab secondary performance page; official Invesco current month-end field was not available in the reviewed capture |

* เป็น secondary NAV field rounded to one decimal; ไม่ใช้แทน official Invesco
current performance. Return-only differences ต่อ underlying index เป็น
tracking/implementation observations ไม่เรียกว่า alpha.

## Calendar performance

Official Invesco calendar-year NAV rows and underlying index rows:

| Year | IDMO NAV TR | S&P World Ex-U.S. Momentum | S&P 500 TR reference |
|---|---:|---:|---:|
| 2016 | 0.08% | not available | 11.96% |
| 2017 | 27.90% | 28.47% | 21.83% |
| 2018 | -16.58% | -16.44% | -4.38% |
| 2019 | 24.82% | 25.56% | 31.49% |
| 2020 | 22.38% | 22.31% | 18.40% |
| 2021 | 14.31% | 14.33% | 28.71% |
| 2022 | -13.04% | -12.81% | -18.11% |
| 2023 | 21.05% | 21.23% | 26.29% |
| 2024 | 12.75% | 13.02% | 25.02% |
| 2025 | 41.85% | 42.65% | 17.88% |

Calculations from rounded official rows:

- IDMO 2016-2025: product 3.1390418, cumulative 213.90%, rounded-input CAGR
  12.12%, 8 up years / 2 down years. This is fund-only for 2016 because the
  underlying index row is not available for that year.
- IDMO 2021-2025: product 1.9244846, cumulative 92.45%, rounded-input CAGR
  13.99%; underlying index product 1.9483369, cumulative 94.83%, CAGR 14.27%.
- S&P 500 TR reference 2016-2025: cumulative 298.33%, rounded-input CAGR 14.82%;
  2021-2025: cumulative 96.17%, CAGR 14.43%.

S&P 500 Total Return เป็น common USD reference เท่านั้น ไม่ใช่
strategy-matched benchmark ของ IDMO.

## Up years / Down years

- Best year: 2025 +41.85%
- Least positive year: 2016 +0.08%
- Worst year: 2018 -16.58%
- Least bad down year: 2022 -13.04%

## Risk read-through

Official Invesco facts ณ 31 ธ.ค. 2025 ระบุ weighted market cap ประมาณ
US$98.562B, P/E 22.59x, P/B 4.34x, return on equity 15.25%, holdings 180,
management fee 0.25% และ total expense ratio 0.25%. Portfolio concentration
สามารถเปลี่ยนตาม momentum rebalance และ official prospectus ระบุว่า ณ 31 ต.ค.
2025 กองมี significant financials exposure.

ความเสี่ยงหลักคือ momentum-factor reversal, semi-annual rebalance/turnover,
foreign-market and currency exposure, country/sector concentration, valuation
and non-diversification risk, index/fair-value timing, liquidity, premium/discount
และ operational risk. Official daily NAV TR series สำหรับ maximum drawdown,
recovery duration, downside capture, beta, standard deviation และ risk-adjusted
persistence ยังไม่พบข้อมูลที่ยืนยันได้; ไม่ใช้ secondary daily series แทน NAV
TR. Underlying index history ก่อน 18 มี.ค. 2016 เป็น predecessor methodology
context และต้องไม่ตีความเป็น identical current index history.

## Driver notes

- Confirmed: IDMO เป็น passive momentum ETF ที่มี strategy-matched S&P World
  Ex-U.S. Momentum Index และ official 2021-2025 fund CAGR 13.99% ต่ำกว่า
  underlying index CAGR 14.27% อยู่ -0.28 pp.
- Confirmed: 2025 NAV return +41.85% เป็น best year ใน official 2016-2025
  rows; momentum leadership เป็น cyclical และ annual return ไม่ใช่ forecast.
- Judgment: strong 2025 ไม่เพียงพอยืนยัน persistent factor premium หลังค่าธรรมเนียม
  และ turnover; current 2026 YTD เป็น secondary rounded field ที่ต้อง refresh
  จาก official Invesco month-end data เมื่อ render ได้.

## Sources

- [Invesco IDMO product page](https://www.invesco.com/us/en/financial-products/etfs/invesco-sp-international-developed-momentum-etf.html)
- [Invesco IDMO Q4 2025 performance source](https://www.invesco.com/us-rest/contentdetail?contentId=29d107c649400410VgnVCM10000046f1bf0aRCRD)
- [SEC IDMO summary prospectus](https://www.sec.gov/Archives/edgar/data/1378872/000119312526079059/d12489d497k.htm)
- [SEC IDMO filing index](https://www.sec.gov/Archives/edgar/data/1378872/000119312526082967/000119312526082967-index.htm)
- [S&P World Ex-U.S. Momentum Index](https://www.spglobal.com/spdji/en/indices/dividends-factors/sp-world-ex-us-momentum-index/)
- [Schwab IDMO performance page](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=idmo)
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | [S&P DJI index returns](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization)
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
