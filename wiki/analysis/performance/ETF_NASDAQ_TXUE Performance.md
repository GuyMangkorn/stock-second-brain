---
type: etf-performance
instrument_type: ETF
entity_key: Nasdaq:TXUE
input_ticker: TXUE
ticker: TXUE
exchange: Nasdaq
fund: Thornburg International Equity ETF
tracked_index: none; actively managed
benchmark: MSCI EAFE Index
management_mode: active-equity-long-only
active_process: fundamental-active
active_process_subtype: bottom-up fundamental developed international equity
management_benchmark: MSCI EAFE Index
track_record: insufficient
management_evidence: insufficient
risk_evidence: not-verified
updated: 2026-09-02
performance_as_of: 2026-06-30 (official table) / 2026-08-28 (current YTD)
calendar_years_as_of: not applicable (no complete calendar year)
current_ytd_as_of: 2026-08-28
price_nav_as_of: 2026-08-27
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-09-02_run-5.md
return_basis: NAV total return; distributions reinvested; net of fund expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/TXUE
  - geography/International
  - style/active-fundamental
---

# TXUE Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

TXUE คือ Thornburg International Equity ETF กอง active long-only แบบ bottom-up
fundamental ที่จดทะเบียนบน Nasdaq และเริ่มดำเนินงาน 21 ม.ค. 2025. Official
Thornburg page รายงาน current NAV Total Return YTD `16.36%` ณ 28 ส.ค. 2026;
จึงยังไม่มี complete calendar year, 10-year CAGR หรือ 2021-2025 comparison.

ตาราง official ณ 30 มิ.ย. 2026 ให้ NAV YTD `9.81%` เทียบ MSCI EAFE `9.44%`
(return-only difference `+0.37 pp`), 1-year `18.42%` เทียบ `20.23%`
(`-1.81 pp`) และ inception `25.72%` เทียบ `26.21%` (`-0.49 pp`). ช่วงเวลาสั้น
และไม่มี complete-year hit rate จึงยังไม่ใช่หลักฐานของ manager skill.

## Performance check

- `entity_key: Nasdaq:TXUE`; fund `Thornburg International Equity ETF`; inception `21 ม.ค. 2025`; exchange `Nasdaq`
- Classification: `active-equity-long-only`; SEC ระบุว่ากองลงทุนอย่างน้อย 80% ในหุ้น common stock/ฝากใบแสดงสิทธิของบริษัท non-U.S. developed และใช้ bottom-up fundamental analysis; currency forwards อาจใช้เพื่อ hedge แต่ไม่ใช่ payoff-defining structure
- Metric: `NAV Total Return` ใน USD รวม distributions ที่ reinvested และหัก fund expenses; market-price return แยกจาก NAV return
- Management benchmark: `MSCI EAFE Index`; เป็น issuer-designated strategy-aligned comparator. `S&P 500 Total Return` เป็น common USD reference เท่านั้น
- Fund facts ณ 28 ส.ค. 2026: net assets `US$557.96M`, NAV `US$36.42`, total expense ratio `0.65%`, distribution frequency annual
- Pricing snapshot ณ 27 ส.ค. 2026: NAV `US$36.25`, closing price `US$36.37`, premium `0.31%`, 30-day median bid-ask spread `0.28%`, average volume `34,340`
- Current S&P 500 Total Return common reference คือ `12.34%` YTD ณ 1 ก.ย. 2026; ไม่เทียบตรงกับ TXUE `16.36%` เพราะคนละ as-of date

| Period (as of 2026-06-30) | TXUE NAV TR | MSCI EAFE Index | Return-only difference |
|---|---:|---:|---:|
| YTD | 9.81% | 9.44% | +0.37 pp |
| 1 year | 18.42% | 20.23% | -1.81 pp |
| Inception | 25.72% | 26.21% | -0.49 pp |

Thornburg ระบุว่า total returns คำนวณจาก daily 4:00pm NAV และถือว่า
distributions ถูก reinvested ในวันจ่าย. Latest verified distribution คือ ex-date
19 ธ.ค. 2025 / payable 31 ธ.ค. 2025 จำนวน `US$0.33847` ต่อหน่วย.

## Calendar performance

SEC summary prospectus ณ 30 ธ.ค. 2025 ระบุว่ากองเพิ่งเริ่มดำเนินงานและยังไม่มี
full calendar year จึงไม่มี annual-return bar chart/table. ปี 2025 เป็น inception-
year partial และปี 2026 ยังไม่จบ; `up years / down years`, best/worst year,
2021-2025 CAGR และ 10-year CAGR จึงเป็น `not applicable` หรือ `not disclosed`.

## Up years / Down years

- Complete calendar observations: `ไม่มี`
- Best / least positive / worst / least bad down year: `not applicable`
- Current NAV TR YTD: `+16.36%` ณ 28 ส.ค. 2026; same-date MSCI EAFE return `not disclosed`

## Risk read-through

กองมี 48 holdings และ active share `80.4%` ณ 31 ก.ค. 2026; top listed position
คือ Thornburg Capital Management Fund LIQUID `5.88%` ณ 31 ส.ค. 2026. Sector
weights หลักคือ Industrials `22.7%`, Financials `19.9%`, Utilities `9.5%` และ
Cash & Equivalents `6.4%`; country weights สูงสุดคือ France `19.3%`, Japan
`14.2%` และ Germany `11.9%`.

ความเสี่ยงหลักคือ non-diversified/focused portfolio, country and foreign-currency
exposure, equity/sector concentration, foreign-market liquidity, premium/discount,
new-fund risk และ possible derivatives/currency-forward risk. Official daily NAV
series สำหรับ maximum drawdown, recovery, downside capture, tracking error หรือ
risk-adjusted persistence ยังไม่พบข้อมูลที่ยืนยันได้; `risk_evidence` จึงเป็น
`not-verified`.

## Active management read-through

- `management_mode: active-equity-long-only`; `active_process: fundamental-active`
- `management_benchmark: MSCI EAFE Index`; เลือกตาม hierarchy step 2 จาก issuer product page ก่อนดูผลตอบแทน เพราะไม่มี closer official performance-table comparator ที่เปิดเผยใน capture นี้
- `track_record: insufficient`; elapsed fund history จาก 21 ม.ค. 2025 ถึงรอบปัจจุบันยังต่ำกว่า 3 ปี
- `management_evidence: insufficient`; มีเพียง YTD/1-year/inception fields และไม่มี complete comparable-year hit rate หรือ Excess CAGR ที่รองรับการประเมิน skill
- `risk_evidence: not-verified`; return-only differences ในตารางไม่เรียกว่า alpha
- Portfolio managers คือ Lei Wang, CFA และ Matt Burdett; ประสบการณ์ของผู้จัดการก่อนกองนี้ไม่ถูกนับเป็น fund track record โดยอัตโนมัติ

## Sources

- [Thornburg TXUE official product page](https://www.thornburg.com/product/etfs/eie/TXUE/) — identity, Nasdaq, fund facts, current NAV/YTD, official benchmark, performance table, distributions, holdings, characteristics and portfolio managers
- [TXUE summary prospectus, SEC](https://www.sec.gov/Archives/edgar/data/2038383/000199937125021310/txue-497k_123025.htm) — objective, 0.65% expenses, active fundamental strategy, equity eligibility, inception-year performance gap and principal risks
- [S&P Dow Jones Indices current all-returns table](https://www.spglobal.com/spdji/en/additional-reports/all-returns/index.dot?additionalFilterCondition=&parentIdentifier=df8ec300-24ad-4c70-81d3-a3cece0200e2&sourceIdentifier=index-family-specialization) — S&P 500 Total Return current YTD reference as of 2026-09-01
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common benchmark definition; not the TXUE management benchmark
- [[ETF_performance_sources_2026-09-02_run-5]] | [[ETF Performance Index]]
