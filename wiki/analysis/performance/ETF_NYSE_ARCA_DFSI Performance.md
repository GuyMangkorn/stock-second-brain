---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DFSI
input_ticker: DFSI
ticker: DFSI
exchange: NYSE Arca
fund: Dimensional International Sustainability Core 1 ETF
tracked_index: none; actively managed
benchmark: MSCI World ex USA IMI Index (net dividends)
updated: 2026-08-30
performance_as_of: 2026-07-31
rolling_5y_as_of: not applicable (<5y history)
current_ytd_as_of: 2026-07-31
market_price_as_of: not disclosed in reviewed official source
nav_as_of: not disclosed in reviewed official source
fund_facts_as_of: 2025-10-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return
tags:
  - analysis/etf-performance
  - geography/International
  - ticker/DFSI
  - geography/developed-ex-North-America
  - style/active-systematic
  - theme/sustainability
---

# DFSI Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DFSI คือ Dimensional International Sustainability Core 1 ETF ของ Dimensional
บน NYSE Arca; identity นี้ไม่ใช่ DFIS. กองเป็น active long-only ETF แบบ systematic
ที่ลงทุนใน developed markets นอกสหรัฐฯ แบบ all-cap, ใช้ sustainability
considerations และไม่มี currency hedge. Current Dimensional fund table ที่ตรวจ
เมื่อ 30 ส.ค. 2026 แสดง 1-year annualized 20.86%, 3-year annualized 16.38%
และ since-inception annualized 20.09%. Official current table ไม่ได้ render
YTD field ใน capture ที่ตรวจได้ จึงใช้ secondary NAV total-return proxy 8.74%*
ณ 31 ก.ค. 2026 โดยติดธงแหล่งข้อมูลไว้ชัดเจน.

Complete official calendar rows ที่ยืนยันได้ตั้งแต่ 2023-2025 ให้ cumulative
return 65.42% และ rounded-input CAGR 18.27%; ปีที่ดีที่สุดคือ 2025
+33.24% และปีที่บวกน้อยที่สุดคือ 2024 +5.27%. ประวัติยังสั้นกว่า 5 ปี
และไม่ควร extrapolate เป็น long-term persistence.

## Performance check

- entity_key: NYSE Arca:DFSI; inception: 1 พ.ย. 2022; management fee 0.20%,
  other expenses 0.03%, total annual fund operating expenses 0.24% หลัง recovery
  ของ waiver เดิม 0.01%; fee waiver agreement ถึง 28 ก.พ. 2027
- Metric: NAV Total Return ใน USD รวม reinvested distributions และหัก fund
  expenses; current YTD ที่มีเครื่องหมาย * เป็น secondary
  dividend-reinvested proxy ไม่ใช่ตัวเลขที่ดึงจาก current official table
- Management mode: active-long-only; active-process subtype:
  active-systematic-sustainability-core
- Management benchmark: MSCI World ex USA IMI Index (net dividends); fund ไม่ได้
  replicate specific index และ official summary prospectus ใช้ benchmark นี้สำหรับ
  standardized comparison
- กลยุทธ์ลงทุนใน non-U.S. developed-market all-cap equities, เพิ่มน้ำหนักได้ใน
  smaller companies, lower relative price และ higher profitability พร้อมใช้
  sustainability considerations; อย่างน้อย 80% ของ net assets เป็น equities
- กองไม่มี currency hedge จึงยังรับ foreign-currency exposure เต็มตามกลยุทธ์

Official current annualized fields จาก Dimensional fund table ที่ capture ได้:

| Period | DFSI |
|---|---:|
| 1 year annualized | 20.86% |
| 3 years annualized | 16.38% |
| 5 years annualized | not applicable (<5y history) |
| 10 years annualized | not applicable (<5y history) |
| Since inception annualized | 20.09% |

Current YTD cross-check:

| Period end | DFSI NAV TR proxy | Source note |
|---|---:|---|
| 2026-07-31 | 8.74%* | FinanceCharts secondary total-return series; official current table YTD field was not available in the reviewed capture |

* เป็น secondary dividend-reinvested proxy ใช้เพื่อไม่ปล่อย current YTD เป็น
ช่องว่าง แต่ไม่ยกระดับเป็น issuer-confirmed field.

Matched official standardized performance table ณ 31 ธ.ค. 2025:

| Period | DFSI | MSCI World ex USA IMI | Return-only difference |
|---|---:|---:|---:|
| 1 year | 33.24% | 32.18% | +1.06 pp |
| Since inception annualized | 20.97% | 19.74% | +1.23 pp |

ผลต่างนี้เป็น return-only observation จาก official table ไม่เรียกว่า alpha และ
ไม่ใช่หลักฐานว่า outperformance จะคงอยู่.

## Calendar performance

Official summary prospectus เปิดเผย complete calendar-year NAV total-return rows
ที่ยืนยันได้ดังนี้:

| Year | DFSI NAV TR | S&P 500 TR reference |
|---|---:|---:|
| 2023 | 17.94% | 26.29% |
| 2024 | 5.27% | 25.02% |
| 2025 | 33.24% | 17.88% |

S&P 500 Total Return เป็น common USD reference เท่านั้น ไม่ใช่
strategy-matched benchmark ของ DFSI. Cached convention เดียวกับ ETF batch ใช้
เฉพาะ complete calendar years 2016-2025; DFSI จึงมีข้อมูลเทียบได้เฉพาะ 2023-2025
หลัง inception.

- DFSI 2023-2025: product 1.6542471, cumulative 65.42%, rounded-input CAGR
  18.27%, 3 up years / 0 down years.
- S&P 500 TR reference 2023-2025: cumulative 86.12%, rounded-input CAGR 23.01%.
- 2022 เป็น inception-year partial จึงไม่รวมใน calendar CAGR และไม่มี 5-year หรือ
  10-year calculation.

## Up years / Down years

- Best up year: 2025 +33.24%
- Least positive year: 2024 +5.27%
- Down years in the complete 2023-2025 window: none
- Prospectus quarter extremes: highest quarter +14.52% ใน 2025 Q2; lowest quarter
  -7.30% ใน 2024 Q4

## Risk read-through

Shareholder report สำหรับรอบสิ้นสุด 31 ต.ค. 2025 ระบุ net assets ประมาณ
US$855.811M, holdings 2,914, expense ratio 0.23% และ NAV return 24.93%
เทียบ benchmark 23.90%; sustainability considerations และ REIT exclusion
เป็น positive contributors ขณะที่ higher profitability detracted ในรอบดังกล่าว.
ตัวเลขนี้เป็นคนละ period กับ standardized table และไม่ผสมกันเป็น single series.

ความเสี่ยงหลักคือ foreign equity/currency, country and region concentration,
small-/mid-cap exposure, value/profitability tilts, sustainability definitions
และ data limitations, derivatives, securities lending, market premium/discount
และ strategy persistence. Official daily NAV TR series สำหรับ maximum drawdown,
recovery duration, downside capture, standard deviation, beta และ risk-adjusted
persistence ยัง ไม่พบข้อมูลที่ยืนยันได้; ไม่ใช้ market-price proxy แทน NAV TR.
Track record ต่ำกว่า 5 ปีจึงเป็น action-relevant gap.

## Driver notes

- Confirmed: DFSI ใช้ active systematic process ที่ผสาน sustainability
  considerations กับ developed ex-U.S. all-cap equity exposure และไม่ hedge FX.
- Confirmed: official 2025 standardized return +33.24% สูงกว่า official matched
  benchmark +32.18% อยู่ +1.06 pp; since inception annualized difference คือ
  +1.23 pp จาก rounded official fields.
- Judgment: observed outperformance ยังสั้นและอาจมาจาก sustainability,
  country/sector, size, value/profitability และ implementation mix; ยังไม่พอ
  ยืนยัน durable manager skill หรือ persistence.

## Sources

- [Dimensional DFSI product page](https://www.dimensional.com/us-en/funds/dfsi/international-sustainability-core-1-etf)
- [Dimensional current fund table](https://www.dimensional.com/us-en/funds)
- [SEC DFSI summary prospectus](https://www.sec.gov/Archives/edgar/data/1816125/000181612526000065/c497k.htm)
- [SEC DFSI shareholder report](https://www.sec.gov/Archives/edgar/data/1816125/000113322826000245/R2.htm)
- [SEC DFSI filing index](https://www.sec.gov/Archives/edgar/data/1816125/000168035923000130-index.htm)
- [FinanceCharts DFSI total return](https://www.financecharts.com/etfs/DFSI/performance/total-return)
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) | [S&P DJI index returns](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization)
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
