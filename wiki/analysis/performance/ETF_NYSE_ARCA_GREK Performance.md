---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:GREK
ticker: GREK
exchange: NYSE Arca
fund: Global X MSCI Greece ETF
tracked_index: MSCI All Greece Select 25/50 Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-29
performance_as_of: 2025-12-31
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-08-29.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/GREK
  - geography/Greece
---

# GREK Performance

> Navigation: [[ETF Region Index]] → [[Greece ETF]] → [[ETF Performance Index]]

## Bottom line

GREK เป็น passive, non-diversified single-country Greece equity ETF ที่มี
Financials เป็นแกนหลัก. Official Global X rolling `10Y NAV Total Return` อยู่ที่
`17.01%` ต่อปี ณ 2026-06-30 เทียบ tracked index `17.76%` หรือ fund-index gap
`-0.75 pp`; rolling 5Y อยู่ที่ `26.03%` เทียบ `26.83%` หรือ `-0.80 pp`.
Official NAV TR YTD ล่าสุดใน factsheet อยู่ที่ `21.99%` ณ 2026-07-31.

Annual rows 2016-2025 เป็น secondary AAII proxy ที่ compound ได้ `255.67%`
และ rounded-input CAGR `13.53%*`; มีปีบวก/ลบ `7 / 3`, ดีที่สุด 2025
`+75.10%*` และแย่ที่สุด 2018 `-29.90%*`. ตัวเลข annual proxy ไม่ใช่
issuer-published NAV calendar table และไม่ควรตีความเป็น manager alpha.

## Performance check

- `entity_key: NYSE Arca:GREK`; inception `2011-12-07`; primary exchange `NYSE Arca`.
- Objective คือ track price/yield performance ก่อนค่าธรรมเนียมของ `MSCI All Greece Select 25/50 Index`; อย่างน้อย 80% ของสินทรัพย์ลงทุนใน constituents, ADRs/GDRs หรือบริษัทที่มีความเชื่อมโยงทางเศรษฐกิจกับกรีซ.
- Metric คือ `NAV Total Return` ใน USD โดย reinvest distributions/capital gains ตาม issuer convention และหัก fund expenses; S&P 500 TR เป็น common reference เท่านั้น ไม่ใช่ tracked index.
- Total expense ratio `0.56%` (`0.55%` management fee และ `0.01%` other expenses); distribution frequency semi-annual; official 30-day SEC yield `2.22%` ณ 2026-08-28.
- Official Global X current snapshot ณ 2026-08-28: NAV `US$85.33`, market price `US$85.26`, net assets `US$343.51M`; holdings `32` ณ 2026-08-27 และ 30-day median bid/ask spread `0.45%` ณ 2026-08-27.
- Official product-page rolling performance ณ 2026-06-30: NAV TR `1Y 33.59%`, `3Y 31.38%`, `5Y 26.03%`, `10Y 17.01%`, since inception `5.71%`; tracked index `34.54%`, `32.28%`, `26.83%`, `17.76%`, `6.55%` ตามลำดับ.
- Official Global X factsheet ณ 2026-07-31: NAV TR `1M 6.39%`, `YTD 21.99%`, `1Y 34.63%`, `3Y 31.55%`, `5Y 27.58%`, `10Y 16.88%`, since inception `6.13%`; factsheet ระบุ holdings `33` และ AUM `US$313.64M` ณ วันเดียวกัน. ตัวเลขนี้เก็บแยกจาก current snapshot ที่ใหม่กว่า.
- SEC standardized table ณ 2025-12-31 รายงาน fund/index `1Y 75.12% / 76.40%`, `5Y 24.58% / 25.34%`, และ `10Y 13.54% / 14.20%`. Index history เป็น splice: FTSE/ATHEX Custom Capped ก่อน 2026-03-01 และ MSCI All Greece Select 25/50 หลังจากนั้น.

| ปี | GREK NAV TR* | MSCI All Greece Select 25/50 | S&P 500 TR |
|---|---:|---:|---:|
| 2016 | -1.20% | ไม่พบข้อมูลที่ยืนยันได้ | 11.96% |
| 2017 | 32.20% | ไม่พบข้อมูลที่ยืนยันได้ | 21.83% |
| 2018 | -29.90% | ไม่พบข้อมูลที่ยืนยันได้ | -4.38% |
| 2019 | 49.30% | ไม่พบข้อมูลที่ยืนยันได้ | 31.49% |
| 2020 | -13.30% | ไม่พบข้อมูลที่ยืนยันได้ | 18.40% |
| 2021 | 5.70% | ไม่พบข้อมูลที่ยืนยันได้ | 28.71% |
| 2022 | 3.00% | ไม่พบข้อมูลที่ยืนยันได้ | -18.11% |
| 2023 | 43.50% | ไม่พบข้อมูลที่ยืนยันได้ | 26.29% |
| 2024 | 9.70% | ไม่พบข้อมูลที่ยืนยันได้ | 25.02% |
| 2025 | 75.10% | ไม่พบข้อมูลที่ยืนยันได้ | 17.88% |

`*` = secondary AAII annual NAV total-return rows from a previously reviewed
capture; official rolling and standardized issuer returns remain primary.

## Up years / Down years

- 2016-2025 secondary rows: up/down `7 / 3`; best 2025 `+75.10%*`; least positive 2022 `+3.00%*`; worst 2018 `-29.90%*`; least-bad down year 2016 `-1.20%*`.
- 2016-2025 secondary compound `255.67%*`; rounded-input CAGR `(1 + 2.5567)^(1/10) - 1 = 13.53%*`.
- 2021-2025 secondary compound `200.09%*`; rounded-input CAGR `(1 + 2.0009)^(1/5) - 1 = 24.58%*`; all five years were positive.
- Cached S&P 500 TR over 2021-2025 compounds `96.17%`, CAGR `14.43%`; the arithmetic common-reference difference is approximately `+10.15 pp`, not alpha.
- Cached S&P 500 TR over 2016-2025 compounds `298.33%`, CAGR `14.82%`; USD total return with dividends reinvested as of 2025-12-31.

## Risk read-through

GREK มี country, sector, FX และ liquidity concentration สูงเมื่อเทียบกับ
global diversified equity. Official sector weights ณ 2026-07-31 คือ Financials
`49.0%`, Industrials `18.7%`, Utilities `9.1%`, Consumer Discretionary `8.2%`,
Energy `6.5%`, Communication Services `4.0%`, Materials `2.8%`, Consumer Staples
`0.9%` และ Real Estate `0.9%`. Official risk snapshot ระบุ standard deviation
`19.60%`, beta เทียบ S&P 500 `1.10`, Nasdaq-100 `0.69`, MSCI EAFE `1.11` และ
MSCI EM `0.65` ณ 2026-07-31. SEC ระบุ best quarter `+31.50%` และ worst quarter
`-44.00%`; สิ่งนี้ไม่ใช่ maximum drawdown. Official daily NAV series ที่พอ
คำนวณ max drawdown และ recovery date ได้ยังเป็น `ไม่พบข้อมูลที่ยืนยันได้`.

## Source-quality choice and conflicts

Global X product page, official factsheet และ SEC prospectus เป็น source of truth
สำหรับ identity, classification, fee, NAV/market snapshot, rolling performance,
benchmark, portfolio และ risk. AAII annual rows ถูกเก็บเป็น proxy เพราะ
compound 2021-2025 `200.09%` / CAGR `24.58%` และ 2016-2025 CAGR `13.53%`
สอดคล้องกับ SEC standardized 5Y `24.58%` และ 10Y `13.54%` ภายใน rounding.

ChartRow เป็นอีก secondary capture ที่แสดง adjusted-close rows ต่างกันและให้
2021-2025 compound ประมาณ `158.89%` ซึ่งไม่ reconcile กับ SEC 5Y; จึงไม่ถูกใช้
ใน canonical table. Current AAII page capture ในรอบนี้ตอบกลับ 403 ดังนั้นไม่มี
การ overwrite ด้วยค่าที่ใหม่กว่า. Official daily NAV endpoints, issuer numeric
calendar rows 2016-2025 และ daily drawdown/recovery ยังไม่ถูกยืนยัน.

## Sources

- [Global X GREK product page](https://www.globalxetfs.com/funds/grek) — objective, index, current product snapshot, rolling performance, portfolio and risk fields.
- [GREK official factsheet](https://assets.globalxetfs.com/funds/documents/grek/Fact-Sheet_GREK.pdf) — July 2026 standardized NAV/market/index returns, holdings and AUM.
- [GREK SEC summary prospectus](https://www.sec.gov/Archives/edgar/data/1432353/000143235326000191/a497kmscigreece.htm) — exchange, fee, strategy, non-diversified status, standardized performance and best/worst quarter.
- [AAII GREK performance page](https://www.aaii.com/etf/ticker/GREK?via=emailsignup-readmore) — secondary annual NAV total-return rows from the prior reviewed capture; current access gap is disclosed above.
- [ChartRow GREK returns](https://chartrow.com/quote/grek/returns) — conflicting secondary adjusted-close capture used only for reconciliation, not canonical values.
- S&P 500 Total Return 2016-2025 cached convention from the workflow; USD dividends reinvested, as of 2025-12-31.
- [[ETF_performance_sources_2026-08-29]] | [[ETF Performance Index]]
