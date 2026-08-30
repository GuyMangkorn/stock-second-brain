---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:HFXI
input_ticker: HFXI
ticker: HFXI
exchange: NYSE Arca
fund: NYLIM FTSE International Equity Currency Neutral ETF
tracked_index: FTSE Developed ex North America 50% Hedged to USD Net Tax (US RIC) Index
benchmark: S&P 500 Total Return
updated: 2026-08-30
performance_as_of: 2026-07-31
rolling_5y_as_of: 2026-07-31
current_ytd_as_of: 2026-07-31
market_price_as_of: 2026-08-28
nav_as_of: 2026-08-28
fund_facts_as_of: 2026-04-30
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/HFXI
  - geography/developed-ex-North-America
  - style/currency-hedged
---

# HFXI Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

HFXI เป็น passive developed-markets ex-North America ETF ที่ hedge currency
ประมาณ 50% ต่อ USD จึงลดการ bet ค่าเงินเมื่อเทียบกับกอง unhedged หรือ fully hedged.
Official NYLIM performance table ณ 31 ก.ค. 2026 รายงาน NAV Total Return `18.81%`
YTD, `31.68%` 1-year, `18.90%` 3-year annualized, `12.31%` 5-year annualized,
`11.31%` 10-year annualized และ `9.30%` since inception. จาก complete calendar
rows 2016-2025, ผลตอบแทนสะสมแบบ rounded-input คือ `148.73%` หรือ CAGR `9.54%`;
best year คือ 2025 `+30.09%` และ worst yearคือ 2018 `-11.95%`.

## Performance check

- `entity_key: NYSE Arca:HFXI`; inception: 22 ก.ค. 2015; total annual fund
  operating expenses `0.20%` (management fee `0.19%` และ other expenses `0.01%`)
- Metric: `NAV Total Return` ใน USD รวม reinvested distributions และหัก fund
  expenses; index return เป็น net of component management fees แต่ไม่หัก fund
  expenses ของ HFXI
- Issuer benchmark: `FTSE Developed ex North America 50% Hedged to USD Net Tax
  (US RIC) Index`
- Common benchmark: `S&P 500 Total Return` ใช้เป็น USD reference เท่านั้น ไม่ใช่
  strategy-matched benchmark
- Management mode: `passive-index`; กองใช้ monthly currency forwards เพื่อ hedge
  ประมาณครึ่งหนึ่งของ foreign-currency exposure

Official current NAV TR performance ณ 31 ก.ค. 2026:

| Period | HFXI NAV TR |
|---|---:|
| YTD | 18.81% |
| 1 year | 31.68% |
| 3 years annualized | 18.90% |
| 5 years annualized | 12.31% |
| 10 years annualized | 11.31% |
| Since inception annualized | 9.30% |

Matched fund/index table ที่เปิดเผยใน official fact sheet ณ 30 เม.ย. 2026:

| Period | HFXI NAV TR | FTSE 50% Hedged index | Return-only difference |
|---|---:|---:|---:|
| QTD | 1.29% | 1.39% | -0.10 pp |
| YTD | 1.29% | 1.39% | -0.10 pp |
| 1 year | 25.82% | 26.43% | -0.61 pp |
| 3 years annualized | 16.13% | 16.53% | -0.40 pp |
| 5 years annualized | 10.34% | 10.67% | -0.33 pp |
| 10 years annualized | 10.17% | 10.55% | -0.38 pp |
| Since inception annualized | 8.18% | 8.60% | -0.42 pp |

ผลต่างเป็นเพียง return-only tracking observation; ไม่เรียกว่า `alpha` และไม่ใช่
หลักฐานของ manager skill.

## Calendar performance

Official fact sheet เปิดเผย complete calendar-year NAV rows ดังนี้:

| Year | HFXI NAV TR | FTSE 50% Hedged index | S&P 500 TR reference |
|---|---:|---:|---:|
| 2016 | 3.50% | 4.10% | 11.96% |
| 2017 | 21.73% | 22.49% | 21.83% |
| 2018 | -11.95% | -11.83% | -4.38% |
| 2019 | 22.93% | 23.15% | 31.49% |
| 2020 | 7.20% | 7.57% | 18.40% |
| 2021 | 13.88% | 14.15% | 28.71% |
| 2022 | -10.63% | -10.33% | -18.11% |
| 2023 | 19.45% | 19.76% | 26.29% |
| 2024 | 7.58% | 7.92% | 25.02% |
| 2025 | 30.09% | 30.67% | 17.88% |

- HFXI 2016-2025: cumulative `148.73%`, rounded-input CAGR `9.54%`, 8 up
  years / 2 down years.
- FTSE index 2016-2025: cumulative `157.46%`, rounded-input CAGR `9.92%`.
- S&P 500 TR reference 2016-2025: cumulative `298.33%`, rounded-input CAGR
  `14.82%`.
- HFXI 2021-2025: cumulative `70.14%`, rounded-input CAGR `11.21%`; FTSE index
  `72.87%` / `11.57%`; S&P 500 TR `96.17%` / `14.43%`.

## Up years / Down years

- Best up year: 2025 `+30.09%`
- Least positive year: 2016 `+3.50%`
- Worst down year: 2018 `-11.95%`
- Least bad down year: 2022 `-10.63%`

## Risk read-through

Fact sheet fund snapshot ณ 30 เม.ย. 2026 ระบุ total net assets `US$1.38B`,
holdings `800`, weighted average market cap `US$116.43B`, P/E `16.79x`, P/B
`1.89x`, 24 countries และ 14 currencies. Official NYLIM prices-and-yields page
แสดง NAV `US$38.22` และ market price `US$38.16` ณ 28 ส.ค. 2026; ตัวเลขนี้เป็น
price/NAV snapshot ไม่ใช่ performance return.

โครงสร้าง 50% hedge ช่วยลด currency volatility แต่ยังมี foreign-equity, country,
mid-cap, derivatives/hedge-execution, quarterly-rebalance และ tracking-error risk.
Official daily NAV TR series สำหรับ maximum drawdown, recovery duration, downside
capture, standard deviation, beta และ risk-adjusted persistence ยัง `ไม่พบข้อมูลที่
ยืนยันได้`; ไม่ใช้ market-price proxy แทน NAV TR. Secondary Schwab snapshot รายงาน
assets ประมาณ `US$2.0B` และ holdings `805`, ต่างจาก issuer fact sheet (`US$1.38B`
และ `800`) จึงเก็บ issuer เป็น source หลักและไม่ผสมตัวเลขสอง as-of windows.

## Driver notes

- Confirmed: HFXI ใช้ broad developed-market exposure ex-North America และ hedge
  ประมาณ 50% ของ currency exposure ต่อ USD แทนการเลือกทิศทางค่าเงินแบบ active.
- Confirmed: 2025 เป็นปีที่ดีที่สุดใน complete window (`+30.09%`) ขณะที่ 2018 เป็น
  ปีที่แย่ที่สุด (`-11.95%`); annual rows ไม่ควรตีความเป็น forecast.
- Judgment: performance gap ต่อ FTSE index ที่ติดลบเล็กน้อยใน matched fact-sheet
  table สอดคล้องกับ fund expenses/trading/implementation drag แต่ไม่มี daily series
  เพียงพอสำหรับแยกสาเหตุเชิงสถิติ.

## Sources

- [NYLIM HFXI product page](https://www.nylim.com/etf/nyli-ftse-international-equity-currency-neutral-etf-hfxi?ticker=HFXI)
- [NYLIM ETF performance table](https://www.nylim.com/etf)
- [NYLIM prices and yields](https://www.nylim.com/investment-products/prices-yields)
- [NYLI HFXI fact sheet](https://www.newyorklifeinvestments.com/assets/documents/index-nyli/hfxi-nyli-ftse-international-equity-currency-neutral-etf-fs.pdf)
- [SEC HFXI 497K filing index](https://www.sec.gov/Archives/edgar/data/1415995/000199937124010828-index.htm)
- [Secondary Schwab HFXI summary](https://www.schwab.wallst.com/Prospect/Research/etfs/summary.asp?symbol=hfxi)
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | [S&P DJI index returns](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization)
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
