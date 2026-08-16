---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:RSSL
ticker: RSSL
exchange: NYSE Arca
fund: Global X Russell 2000 ETF
tracked_index: Russell 2000 RIC Capped Index
benchmark: S&P 500 Total Return
updated: 2026-08-16
performance_as_of: 2025-12-31
current_ytd_as_of: 2026-06-30
price_nav_as_of: 2026-07-31
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-16.md
return_basis: NAV total return
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/RSSL
  - geography/United-States
---

# RSSL Performance

> Navigation: [[ETF Region Index]] → [[USA ETF]] → [[ETF Performance Index]]

## Bottom line

RSSL เป็น passive/index-tracking U.S. small-cap ETF ที่ติดตาม `Russell 2000
RIC Capped Index`. กองมี complete calendar year ที่ยืนยันได้เพียง 2025 ซึ่งให้
NAV Total Return `+12.76%` เทียบกับ S&P 500 TR `+17.88%`; current official NAV TR
YTD ล่าสุดคือ `+22.52%` ณ 30 มิ.ย. 2026. Issuer รายงาน since-inception annualized
return `+22.65%` ณ วันเดียวกัน แต่ยังไม่ใช่ 10-year NAV TR CAGR.

## Performance check

- `entity_key: NYSE Arca:RSSL`
- Classification: supported passive/index-tracking U.S. equity ETF using an
  indexing approach and representative sampling; primary exchange NYSE Arca
- Inception: 4 มิ.ย. 2024; expense ratio `0.08%`; quarterly distribution
- Metric: `NAV Total Return` บนฐาน USD รวม reinvested dividends/capital gains และ
  fund expenses ตาม issuer disclosure; market-price return ไม่ถูกรวมใน ranking
- Tracked index (issuer benchmark): `Russell 2000 RIC Capped Index`
- Benchmark: `S&P 500 Total Return` (USD, dividends reinvested; common reference
  benchmark ไม่ใช่ tracked index ของ RSSL)
- 10-year NAV TR: `not applicable (<10y history)`; 2024 inception-year partial
  year ไม่ถูกจัดอันดับ และ year-end NAV TR ไม่ได้เปิดเผยใน source ที่ตรวจสอบ
- Official since-inception annualized NAV TR: `22.65%` ณ 30 มิ.ย. 2026; raw TR
  endpoints ไม่ได้เปิดเผย จึงไม่คำนวณ CAGR ซ้ำ
- Latest verified NAV: `US$114.01` ณ 31 ก.ค. 2026; เป็น NAV level ไม่ใช่ return

| Year | RSSL NAV TR | S&P 500 TR |
|---|---:|---:|
| 2025 | 12.76% | 17.88% |

## Up years / Down years

- Complete-year up/down count: `1 / 0` (2025 only)
- Best: 2025, `+12.76%`
- Least positive: 2025, `+12.76%`
- Worst / least bad down year: `not applicable` (ไม่มี complete down year)
- 2025 relative result: RSSL ต่ำกว่า S&P 500 TR `5.12 pp` (`12.76% - 17.88%`)
- Current NAV TR YTD: `+22.52%` ณ 30 มิ.ย. 2026; current-year S&P 500 TR
  comparison `not available` เพราะ cached benchmark ครอบคลุมถึง 2025-12-31 เท่านั้น

## Risk read-through

RSSL มี official standard deviation `19.00%` และ beta `1.22` เทียบกับ S&P 500 ณ
31 ก.ค. 2026. Exposure กระจายราว `1,960` holdings แต่ยังมี small-cap,
cyclicality, liquidity และ sector sensitivity สูงกว่า broad large-cap exposure.
Expense ratio ต่ำที่ `0.08%` และ quarterly distribution ช่วยลด structural drag
แต่ไม่ได้ลบความเสี่ยงของหุ้นขนาดเล็ก. Official daily NAV history สำหรับ
maximum drawdown และ recovery ยังไม่พบ จึงไม่ใช้ secondary proxy.

## Sources

- [Global X RSSL product page](https://www.globalxetfs.com/funds/RSSL) — identity, exchange, NAV/price, expense ratio, risk fields, YTD and since-inception performance; as of dates shown on page
- [Global X RSSL fact sheet](https://assets.globalxetfs.com/funds/documents/rssl/Fact-Sheet_RSSL.pdf) — inception, exchange, return definition, quarterly distribution, official NAV/market-price/index performance as of 30 Jun 2026
- [SEC 2026 RSSL summary prospectus](https://www.sec.gov/Archives/edgar/data/1432353/000143235326000232/a497krussell2000.htm) — passive strategy, index, expenses and 2025 calendar-year return
- [S&P 500 index page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) and cached [S&P 500 TR references](https://www.spglobal.com/spdji/en/commentary/article/us-equities-market-attributes/) — common USD total-return benchmark convention
- ETF source batch: [[ETF_performance_sources_2026-08-16]] | [[ETF Performance Index]]
