---
type: etf-performance
instrument_type: ETF
entity_key: CBOE BZX:DFIC
ticker: DFIC
exchange: Cboe BZX Exchange
fund: Dimensional International Core Equity 2 ETF
benchmark: S&P 500 Total Return
management_mode: active-equity-long-only
active_process_subtype: core equity 2; systematic factor tilts with flexible implementation
management_benchmark: MSCI World ex USA IMI Index (net dividends)
updated: 2026-08-30
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-07-31
price_nav_as_of: 2026-08-18
fund_facts_as_of: 2025-10-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; dividends and other earnings reinvested; net of expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/DFIC
  - geography/International
---

# DFIC Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

DFIC เป็น active long-only ETF ของ Dimensional ที่ใช้ `Core Equity 2` process:
ลงทุนใน developed markets นอกสหรัฐฯ แบบ all-cap และให้น้ำหนักเชิงระบบกับหุ้นที่
ราคาสัมพัทธ์ต่ำกว่าและมี profitability สูงกว่า. กองทุนเริ่ม 23 มี.ค. 2022 จึงยัง
ไม่มี 10-year history และมี complete calendar years เพียง 2023-2025.

Official NAV Total Return ในสามปีเต็มสะสม `67.28%` หรือ rounded-input CAGR
`18.71%`; 2025 ดีที่สุดที่ `+36.95%` และ 2024 ต่ำสุดในช่วงที่ยังเป็นบวกที่
`+4.22%`. Official Quick Guide ณ 31 ธ.ค. 2025 รายงาน 1-year NAV `36.95%`
เทียบกับ management benchmark `32.18%` และ since-inception annualized NAV
`11.80%` เทียบ benchmark `10.49%`; เป็น return-only evidence ไม่ใช่ข้อสรุป
เรื่อง persistent manager skill. Current YTD ที่ยืนยันได้ใน reviewed capture เป็น
secondary total-return field `+12.10%*` ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: CBOE BZX:DFIC`; asset: `Dimensional International Core Equity 2 ETF`; inception: `2022-03-23`; listing: Cboe BZX Exchange
- Metric: `NAV Total Return` รวม dividends และ other earnings ที่ reinvested และหัก fund expenses; currency USD
- Management mode: `active-equity-long-only`; active-process subtype: Core Equity 2, research-led factor tilts with flexible daily implementation
- Management benchmark: `MSCI World ex USA IMI Index (net dividends)`; common benchmark: `S&P 500 Total Return` (USD, dividends reinvested)
- Official rolling 10-year NAV TR: `ไม่พบข้อมูลที่ยืนยันได้` เพราะ history เริ่มปี 2022; 2022 inception-year partial return `-17.83%` ไม่รวมใน complete-year calculation
- Complete calendar window: `2023-2025`; DFIC cumulative `67.28%`; rounded-input CAGR `18.71%`; S&P 500 cache cumulative `86.12%` / CAGR `23.01%`
- Management evidence: official 2025 1-year NAV `36.95%` vs benchmark `32.18%` (`+4.77 pp` return-only); since-inception annualized `11.80%` vs `10.49%` (`+1.31 pp`); no alpha or persistence claim
- Current YTD: `12.10%*` as of `2026-07-31`, secondary standardized total-return field because a current official Dimensional YTD field was not readable in the reviewed capture

| Year | DFIC NAV TR | S&P 500 TR |
|---|---:|---:|
| 2023 | 17.20% | 26.29% |
| 2024 | 4.22% | 25.02% |
| 2025 | 36.95% | 17.88% |

**Up years / Down years — complete 2023-2025 window**

- Up years / Down years: `3 / 0`; 2022 inception-year partial return `-17.83%` is excluded
- Best complete year: 2025, **+36.95%**; least positive: 2024, **+4.22%**
- Worst complete year: `ไม่พบข้อมูลที่ยืนยันได้` because no complete down year is in the available history
- DFIC beat the S&P 500 common reference in 2025 only (`1 / 3` complete years); this is not evidence of active-management skill

## Risk read-through

DFIC มี developed ex-U.S. country, currency, sector, valuation, small-/mid-cap และ
active-process risk. Official shareholder report ระบุ `4,215` holdings ณ
31 ต.ค. 2025 และ expense ratio `0.22%`; distribution frequency เป็น quarterly.
Secondary standardized data reports annualized volatility `14.5%` และ beta `0.85`
เทียบกับ S&P 500 as of 31 ก.ค. 2026, แต่ไม่ได้ใช้แทน official risk-adjusted skill
evidence. Official daily NAV Total Return series ที่เพียงพอสำหรับ maximum drawdown,
recovery และ persistence analysis ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Dimensional DFIC fund page](https://www.dimensional.com/us-en/funds/dfic/international-core-equity-2-etf) — official fund identity and product access point
- [DFIC summary prospectus, SEC](https://www.sec.gov/Archives/edgar/data/1816125/000181612526000072/c497k.htm) — Cboe BZX listing, objective, 2023-2025 calendar bar, 2022 partial return, 2025 1-year and since-inception benchmark comparison
- [Dimensional ETF Quick Guide](https://my.dimensional.com/chmedia/282748/source/dimensional-etf-quick-guide.pdf) — official 2025 performance, expenses, inception/listing and management-benchmark fields
- [Dimensional Equity Solutions](https://www.dimensional.com/us-en/our-approach/dimensional-equity-solutions) — Core Series process and flexible factor exposure context
- [ETF Research Center DFIC page](https://www.etfrc.com/DFIC) — secondary current standardized YTD, volatility and beta fields, marked `*`
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached source references in `check-etf-performance` — common USD total-return benchmark for 2023-2025
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
