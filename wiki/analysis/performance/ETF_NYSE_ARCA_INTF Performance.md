---
type: etf-performance
instrument_type: ETF
entity_key: NYSE Arca:INTF
input_ticker: INTF
ticker: INTF
exchange: NYSE Arca
fund: iShares International Equity Factor ETF
tracked_index: STOXX International Equity Factor Index (USD) (Net)
benchmark: S&P 500 Total Return
management_mode: passive-index / strategic-beta
updated: 2026-08-30
performance_as_of: 2026-08-27
calendar_years_as_of: 2025-12-31
current_ytd_as_of: 2026-08-27
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: official NAV total return; distributions and capital gains reinvested; fund expenses deducted
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/INTF
  - geography/International
---

# INTF ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

INTF เป็น passive, rules-based multifactor ETF ของ iShares ที่ให้ exposure หุ้น
developed markets นอกสหรัฐฯ โดยคัดเลือกตาม value, quality, momentum, low
volatility และ size factors. Official benchmark ปัจจุบันคือ `STOXX International
Equity Factor Index (USD) (Net)` และกองทุนจดทะเบียนบน NYSE Arca ตั้งแต่ 28 เม.ย.
2015.

Official current product page รายงาน NAV Total Return YTD `+16.19%` ณ 27 ส.ค.
2026 และ NAV `US$42.87` ณ 28 ส.ค. 2026. Factsheet ณ 30 มิ.ย. 2026 รายงาน
rolling NAV TR แบบ annualized ที่ 1 ปี `23.46%`, 3 ปี `19.01%`, 5 ปี `10.27%`,
10 ปี `9.85%` และ since inception `7.80%`.

ช่วง 2021-2025 จาก official calendar rows ให้ cumulative `+65.86%` และ
rounded-input CAGR `+10.65%*`; benchmark series ที่แสดงใน factsheetให้
`+65.19%` และ `+10.56%*`. อย่างไรก็ดี benchmark เปลี่ยนจาก MSCI World ex USA
Diversified Multiple-Factor Index เป็น STOXX International Equity Factor Index
เมื่อ 1 มิ.ย. 2022 จึงต้องรักษา splice นี้ไว้ และไม่ตีความผลต่าง `+0.09 pp` เป็น
alpha หรือ pure manager skill.

## Performance check

- `entity_key: NYSE Arca:INTF`; `input_ticker: INTF`; CUSIP `46434V274`; fund launch `28 เม.ย. 2015`; listing exchange `NYSE Arca`
- Classification: supported passive/index-tracking equity ETF with strategic-beta multifactor selection; not an actively managed long-only manager strategy
- Issuer benchmark: `STOXX International Equity Factor Index (USD) (Net)`; common reference คือ `S&P 500 Total Return` และไม่ใช่ strategy-aligned benchmark
- Return metric: official NAV total return; dividends and capital gains are reinvested and fund expenses are deducted; return currency คือ USD
- Current facts as of `2026-08-28`: NAV `US$42.87`, closing price `US$42.99`, fund net assets `US$3,777,012,995`, shares outstanding `88.10M`, premium/discount `0.28%`, and 30-day median bid/ask spread `0.05%`
- Portfolio facts: `480` holdings as of `2026-08-27`, expense ratio `0.16%`, P/E `17.62x`, P/B `2.20x`, 3-year beta `0.60`, and 3-year standard deviation `12.14%`

### Calendar-year NAV total return

| Year | INTF NAV TR (USD) | Reported benchmark TR (USD) |
|---|---:|---:|
| 2021 | 11.49% | 11.61% |
| 2022 | -12.36% | -12.44% |
| 2023 | 18.35% | 18.15% |
| 2024 | 5.89% | 5.96% |
| 2025 | 35.45% | 35.02% |

จากตัวเลข annual rows ที่ issuer แสดงแบบปัดเศษ คำนวณได้ดังนี้:

- INTF 2021-2025 cumulative `+65.86%`; CAGR `+10.65%*`
- Reported benchmark composite 2021-2025 cumulative `+65.19%`; CAGR `+10.56%*`
- Return-only fund-minus-benchmark CAGR difference `+0.09 pp*`; ไม่เรียกว่า alpha เพราะ benchmark มี 2022 splice และ ETF เป็น passive
- 4/5 ปีเป็นบวก; best year คือ 2025 `+35.45%`; worst year คือ 2022 `-12.36%`

### Rolling and current performance

| Window | INTF NAV TR (USD) | Benchmark TR (USD) | As of |
|---|---:|---:|---|
| 1 year annualized | 23.46% | 23.38% | 2026-06-30 |
| 3 years annualized | 19.01% | 18.73% | 2026-06-30 |
| 5 years annualized | 10.27% | 10.05% | 2026-06-30 |
| 10 years annualized | 9.85% | 9.80% | 2026-06-30 |
| Since inception annualized | 7.80% | 7.75% | 2026-06-30 |
| Current YTD | 16.19% | ไม่พบข้อมูลที่ยืนยันได้ใน current product capture | 2026-08-27 |

Rolling performance fields are issuer-reported average annual returns; the
calendar CAGR is independently calculated from rounded issuer rows. The
benchmark history before 2022-06-01 is the MSCI multifactor series and the later
history is the STOXX series, so all benchmark comparisons retain this splice.
Cached `S&P 500 Total Return` remains a common USD reference only; no same-window
S&P excess or alpha claim is made in this page.

## Risk read-through

Current sector weights as of 27 ส.ค. 2026 ได้แก่ Financials `27.25%`, Industrials
`17.69%`, Information Technology `10.14%`, Consumer Discretionary `9.18%`,
Health Care `7.80%`, Materials `7.17%`, Consumer Staples `5.50%`, Energy `5.17%`,
Utilities `4.09%`, Communication `3.10%`, Real Estate `2.40%` และ Cash/Derivatives
`0.51%`. Geographic exposures สูงสุดคือ Japan `24.71%`, United Kingdom `12.40%`,
Switzerland `8.09%`, Canada `7.48%`, France `7.01%`, Germany `6.91%` และ Australia
`6.55%`.

Top holdings ใน factsheet ณ 30 มิ.ย. 2026 ได้แก่ ASML `2.88%`, Novartis `2.18%`,
Royal Bank of Canada `1.23%`, ABB `1.17%`, HSBC `1.08%`, Roche `1.03%`, Nestlé
`0.99%`, Mitsubishi UFJ `0.94%`, BHP `0.93%` และ AstraZeneca `0.93%`; รวม
`13.36%` จากน้ำหนักที่ประกาศแบบปัดเศษ.

ความเสี่ยงหลักคือ factor-regime และ value/quality/momentum/size/low-volatility
selection, country/sector/FX, developed-market cycle, tracking difference,
index methodology/rebalance, liquidity และ premium/discount. Low-volatility
factor ไม่ได้ทำให้กองทุนปราศจาก downside. Daily NAV history สำหรับ maximum
drawdown, recovery duration, downside capture และ risk-adjusted persistence ยัง
`ไม่พบข้อมูลที่ยืนยันได้`; issuer beta/std-dev ล่าสุดที่ยืนยันได้คือ `0.60`/
`12.14%` ณ 31 ก.ค. 2026.

## Sources

- [iShares official INTF product page](https://www.blackrock.com/us/individual/products/272822/ishares-msci-international-multi-factor-etf) — current YTD/NAV/price/assets, benchmark, holdings, portfolio characteristics, exposures and performance tables
- [iShares official June 2026 factsheet](https://www.blackrock.com/us/individual/literature/fact-sheet/intf-ishares-international-equity-factor-etf-fund-fact-sheet-en-us.pdf) — calendar-year rows, annualized NAV/benchmark returns, benchmark splice disclosure, fee, risk and top holdings
- [iShares official prospectus](https://www.ishares.com/us/literature/prospectus/p-ishares-trust-non-us-factor-style-cap-7-31.pdf) — INTF objective, NYSE Arca listing, rules-based STOXX index and principal risks
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common reference-benchmark definition only
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
