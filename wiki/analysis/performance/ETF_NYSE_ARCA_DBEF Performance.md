---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:DBEF
input_ticker: DBEF
ticker: DBEF
exchange: NYSE Arca
fund: Xtrackers MSCI EAFE Hedged Equity ETF
tracked_index: MSCI EAFE US Dollar Hedged Index
issuer_benchmark: MSCI EAFE US Dollar Hedged Index
benchmark: S&P 500 Total Return
management_mode: passive-index
active_process: not applicable
management_benchmark: not applicable
track_record: established
management_evidence: not applicable
risk_evidence: issuer-beta; secondary-standard-deviation; daily-NAV-drawdown-not-verified
updated: 2026-09-01
performance_as_of: 2025-12-31 (secondary calendar rows) / 2026-06-30 (official rolling)
calendar_years_as_of: 2025-12-31 (secondary NAV rows)
rolling_10y_as_of: 2026-06-30
current_ytd_as_of: 2026-07-31 (secondary)
price_nav_as_of: not used
fund_facts_as_of: 2026-06-30
source_batch: raw/imports/ETF_performance_sources_2026-09-01_run-3.md
return_basis: NAV total return; dividends reinvested; net of expenses
return_currency: USD
primary_region: International
tags:
  - analysis/etf-performance
  - ticker/DBEF
  - geography/International
---

# DBEF ETF Performance

> [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DBEF เป็น passive, physical, developed-markets equity ETF ที่ติดตาม `MSCI
EAFE US Dollar Hedged Index` และใช้ forward currency contracts เพื่อ hedge
ความผันผวนระหว่าง USD กับสกุลเงินนอกสหรัฐฯ. Official DWS Q2 2026 factsheet
รายงาน NAV Total Return annualized 10 ปี `12.66%` ณ 30 มิ.ย. 2026 เทียบกับ
issuer benchmark `12.90%`; ตัวเลขนี้เป็น rolling window และไม่ใช่ calendar
proxy ด้านล่าง.

Complete calendar rows 2016–2025 จาก secondary NAV series ให้ cumulative
`171.24%` และ rounded-input CAGR `10.49%*`; ช่วง 2021–2025 ให้ cumulative
`90.67%` และ CAGR `13.78%*`. Current YTD NAV return ที่พบจาก secondary
source คือ `14.1%*` ณ 31 ก.ค. 2026; official current YTD ที่ใหม่กว่านี้
`ไม่พบข้อมูลที่ยืนยันได้` ในชุด issuer materials ที่ตรวจสอบ.

## Fund and measurement

- กองทุน: Xtrackers MSCI EAFE Hedged Equity ETF; `entity_key: NYSE Arca:DBEF`; inception `2011-06-08`; exchange `NYSE Arca`
- Classification: supported passive/index-tracking international equity ETF; currency-hedging derivatives เป็น implementation ของกลยุทธ์ ไม่ใช่ leverage, inverse, option-income หรือ derivative-defined payoff
- Official ETF factsheet ณ 30 มิ.ย. 2026: holdings `690`, net assets `US$9,039,408,798.94`, gross/net expense ratio `0.35%`, SEC 30-day yield `2.05%`, beta `0.72`
- Primary metric: USD `NAV Total Return`, net of fund expenses, with dividends reinvested where applicable. Market-price return ไม่ถูกนำมาปนในตาราง
- Official rolling fields ณ 30 มิ.ย. 2026: 1Y `27.58%`, 3Y annualized `18.49%`, 5Y annualized `13.76%`, 10Y annualized `12.66%`, since inception annualized `10.42%`; corresponding issuer benchmark `27.86%`, `18.74%`, `13.95%`, `12.90%`, `10.73%`
- Current secondary NAV YTD: `+14.1%*` ณ 31 ก.ค. 2026; exact current official NAV/YTD snapshot `ไม่พบข้อมูลที่ยืนยันได้` จาก reviewed Q2 factsheet
- Common benchmark: `S&P 500 Total Return` in USD with dividends reinvested; ใช้เป็น reference เท่านั้น ไม่ใช่ strategy-aligned benchmark ของ DBEF

## Annual performance

Annual rows below are a secondary NAV total-return series; `*` marks secondary
data and they are not an issuer-published numeric calendar table. S&P 500 rows
use the workflow's cached USD Total Return convention for the same complete
calendar years.

| Calendar year | DBEF NAV TR* | MSCI EAFE US Dollar Hedged Index | S&P 500 Total Return |
|---|---:|---:|---:|
| 2016 | +5.70%* | not disclosed | +11.96% |
| 2017 | +16.60%* | not disclosed | +21.83% |
| 2018 | -9.30%* | not disclosed | -4.38% |
| 2019 | +24.40%* | not disclosed | +31.49% |
| 2020 | +2.30%* | not disclosed | +18.40% |
| 2021 | +19.30%* | not disclosed | +28.71% |
| 2022 | -4.70%* | not disclosed | -18.11% |
| 2023 | +19.70%* | not disclosed | +26.29% |
| 2024 | +14.00%* | not disclosed | +25.02% |
| 2025 | +22.90%* | not disclosed | +17.88% |

- Complete 2016–2025 proxy: cumulative `+171.24%`, rounded-input CAGR `10.49%*`; annual-return population standard deviation `11.26%`
- Complete 2021–2025 proxy: cumulative `+90.67%`, rounded-input CAGR `13.78%*`; S&P 500 over the same cached window was `+96.17%` cumulative / `14.43%` CAGR
- Official issuer benchmark annual rows were not disclosed in the reviewed Q2 factsheet, so no annual active-difference series is fabricated

## Up years / Down years

- Up years / Down years: `8 / 2` across complete calendar years 2016–2025
- Best: 2019, `+24.40%*`; least positive: 2020, `+2.30%*`
- Worst: 2018, `-9.30%*`; least bad down year: 2022, `-4.70%*`
- 2016–2025 cumulative / rounded-input CAGR: `171.24%` / `10.49%*`
- 2021–2025 cumulative / rounded-input CAGR: `90.67%` / `13.78%*`
- Current secondary NAV YTD: `+14.1%*` ณ 31 ก.ค. 2026; ไม่ผสมกับ market-price return หรือ official rolling fields

## Risk read-through

DBEF มี equity-market, developed-ex-market, country/sector, FX-hedge,
liquidity, counterparty และ tracking risk. Official factsheet เปิดเผย beta
`0.72` ณ 30 มิ.ย. 2026; secondary AAII รายงาน standard deviation `9.6%` ณ
31 ก.ค. 2026 ซึ่งควรถือเป็น cross-check ไม่ใช่ issuer field. จาก annual NAV
proxy maximum year-end drawdown คือ `-9.30%` ใน 2018 และ cumulative year-end
กลับสูงกว่าจุดสูงสุดเดิมใน 2019; daily NAV drawdown, exact recovery date และ
recovery duration `ไม่พบข้อมูลที่ยืนยันได้`.

Currency hedge ช่วยลดผลกระทบจากการเปลี่ยนแปลงของสกุลเงินนอก USD แต่ hedge
อาจไม่สมบูรณ์ มีต้นทุน และอาจลดประโยชน์เมื่อ foreign currency แข็งค่า. DWS
ระบุว่ากองทุนใช้ forward foreign-currency contracts; derivatives จึงเป็น
ส่วนของการ hedge/implementation และไม่เปลี่ยน classification เป็นกองทุน
ที่มี derivative-defined payoff.

ผลตอบแทน calendar proxy ของ DBEF ต่ำกว่า S&P 500 ใน 2016–2024 หลายปี แต่
สูงกว่าใน 2025; ความแตกต่างนี้สะท้อน exposure developed ex-US และ currency
hedge ไม่ใช่หลักฐาน manager skill. สำหรับ passive tracking ควรติดตาม hedge
effectiveness, ค่าใช้จ่าย, tracking difference และผลกระทบจาก FX regime.

## Sources

- [DWS official DBEF Q2 2026 factsheet](https://etf.dws.com/download/asset/0eb88b89-c04c-4170-b412-80462e8598e1) — official identity, strategy, rolling NAV/index returns, fund facts and beta as of 30 มิ.ย. 2026
- [SEC 2025 DBEF summary prospectus](https://www.sec.gov/Archives/edgar/data/1503123/000008805325000874/k100125dbef.htm) — NYSE Arca identity, objective, 80% equity policy, index and currency-hedging implementation
- [DWS currency-hedged ETF explanation](https://etf.dws.com/en-us/etf-knowledge/focus-topics-etf-investment-strategies/currency-hedged-etfs-mitigating-currency-risks-from-international-equities/) — hedge role and DBEF expense ratio cross-check
- [AAII DBEF profile](https://www.aaii.com/etf/ticker/DBEF) — secondary annual NAV rows, current YTD proxy and standard-deviation cross-check as of 31 ก.ค. 2026
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition
- Cached S&P 500 Total Return references: [S&P DJI historical research](https://www.spglobal.com/spdji/en/documents/research/research-sp-500-low-volatility-index-five-decades-of-history.pdf?force_download=true), [2023 U.S. Equities Market Attributes](https://www.spglobal.com/spdji/en/documents/commentary/market-attributes-us-equities-202307.pdf), [2021 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes-december-2021/), and [2025 S&P DJI market attributes](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/); cached reference as of 31 ธ.ค. 2025
- [[ETF_performance_sources_2026-09-01_run-3]] — source map, raw observations, calculations, reconciliation and scheduled-local verification record

\* Secondary source or calculation from secondary annual rows; not an issuer-reported calendar NAV field.
