---
type: etf-performance
instrument_type: ETF
entity_key: Cboe BZX:GSWO
input_ticker: GSWO
ticker: GSWO
exchange: Cboe BZX
fund: Goldman Sachs ActiveBeta World Equity ETF
tracked_index: Goldman Sachs ActiveBeta World Equity Index
benchmark: S&P 500 Total Return
management_mode: passive-index / strategic-beta
updated: 2026-08-30
performance_as_of: 2026-07-31
calendar_years_as_of: not applicable (2026 strategy change)
current_ytd_as_of: 2026-07-31
price_nav_as_of: not disclosed in reviewed official sources
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: official NAV total return; distributions reinvested; net of management fees and operating expenses
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/GSWO
  - geography/International
---

# GSWO ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

GSWO เป็นกองทุน passive, rules-based strategic-beta ที่ติดตาม `Goldman Sachs
ActiveBeta World Equity Index` และให้ exposure หุ้น large-/mid-cap ใน developed
markets รวมสหรัฐฯ โดยใช้ factor tilts ด้าน value, momentum และ quality. Goldman
ระบุว่ากองทุนไม่ใช่ actively managed และไม่ได้พยายาม outperform ดัชนีที่ติดตาม.

จุดสำคัญของการอ่านผลตอบแทนคือชื่อ/ดัชนี/วัตถุประสงค์ของกองทุนเปลี่ยนจาก
`Goldman Sachs ActiveBeta World Low Vol Plus Equity ETF` (`GLOV`) เป็น GSWO หลัง
ปิดทำการวันที่ 4 ก.พ. 2026. ดังนั้นผลตอบแทนก่อนวันดังกล่าวเป็นประวัติของ
predecessor strategy และไม่ควรถูกนำไปทำเป็น 2021-2025 CAGR, alpha หรือหลักฐาน
ของ current-strategy skill.

Official Goldman factsheet ณ 31 ก.ค. 2026 รายงาน NAV total return 1 เดือน
`+0.42%`, YTD `+11.27%`, 1 ปีแบบ annualized `+18.46%`, 3 ปีแบบ annualized
`+17.00%` และ since inception แบบ annualized `+13.00%`. ตัวเลข 3 ปีและ
since inception จึงเป็น predecessor-linked periods; official current-strategy
calendar-year history, 10-year CAGR, drawdown และ recovery duration ยัง
`ไม่พบข้อมูลที่ยืนยันได้`.

## Performance check

- `entity_key: Cboe BZX:GSWO`; `input_ticker: GSWO`; CUSIP `38149W739`; fund inception `15 มี.ค. 2022`; listing exchange `Cboe BZX`
- Classification: supported passive/index-tracking equity ETF with strategic-beta factor construction; not an active long-only manager strategy
- Issuer benchmark: `Goldman Sachs ActiveBeta World Equity Index` (Net Total Return, Unhedged, USD); common reference คือ `S&P 500 Total Return` และไม่ใช่ management benchmark
- Return metric: official NAV total return; distributions are reinvested and NAV performance includes management fees and operating expenses; return currency คือ USD
- Current fee/fund facts as of `2026-07-31`: total expense ratio `0.15%`, number of holdings `763`, net assets `US$1,726.01M`, P/E `21.44x`, P/B `3.96x`, dividend yield `1.53%`, and weighted average market cap `US$1,138.88B`
- Methodology break: effective after close `2026-02-04`; prior performance reflects the former Low Vol Plus strategy and current published rolling periods cannot isolate post-change management evidence

| Period | GSWO NAV TR (USD) | Interpretation |
|---|---:|---|
| 1 month | 0.42% | official factsheet, as of 2026-07-31 |
| YTD | 11.27% | official factsheet, as of 2026-07-31; mixed pre-/post-change 2026 window |
| 1 year annualized | 18.46% | official factsheet; predecessor-linked history |
| 3 years annualized | 17.00% | official factsheet; predecessor-linked history |
| Since inception annualized | 13.00% | official factsheet; inception 2022-03-15 and predecessor-linked history |

ไม่มี complete calendar-year series ที่เทียบกับ current GSWO strategy ได้ใน
reviewed issuer materials. จึงไม่คำนวณ 2021-2025 CAGR, cumulative wealth,
best/worst year, up/down hit rate, excess return หรือ alpha. Cached `S&P 500
Total Return` ใช้เป็น common reference ได้ในอนาคตเมื่อมีช่วงเวลาและ strategy
definition ที่เทียบกันได้ แต่ยังไม่มี same-window comparison ที่ปลอดภัยในรอบนี้.

## Risk read-through

กองทุนมี broad global developed exposure แต่ยังมี U.S. weight `68.7%` และ
sector weights สูงสุดคือ Information Technology `29.7%`, Financials `16.5%`,
Industrials `10.5%`, Consumer Discretionary `10.3%` และ Health Care `9.6%` ณ
31 ก.ค. 2026. Top-five holdings คือ NVIDIA `5.4%`, Apple `5.1%`, Microsoft
`3.8%`, Amazon `3.0%` และ Alphabet `2.4%`.

ความเสี่ยงหลักคือ equity/market, factor และ valuation regime, U.S./mega-cap และ
sector concentration, foreign-market/currency, mid-cap volatility, index
methodology/rebalance, tracking difference, liquidity และ premium/discount.
การเปลี่ยน index และ objective ในปี 2026 เป็น structural comparability risk:
ผลตอบแทนย้อนหลังไม่ใช่ time series ของ strategy เดียวกัน. Daily NAV สำหรับ
maximum drawdown, recovery duration, downside capture, beta และ risk-adjusted
persistence ยัง `ไม่พบข้อมูลที่ยืนยันได้` จาก reviewed official sources.

## Sources

- [Goldman Sachs official GSWO factsheet](https://am.gs.com/public-assets/documents/5697e168-24d6-11ef-870d-f74b517c3b5d) — official NAV performance, return definition, fund facts, sector/country allocations, current index and risk disclosures
- [SEC strategy-change supplement](https://www.sec.gov/Archives/edgar/data/1479026/000119312525269567/d71367d497.htm) — GLOV-to-GSWO name/ticker/index/objective change, effective date, fee, factor methodology and long-only/passive description
- [Cboe GSWO listing](https://www.cboe.com/us/equities/listings/listed_products/symbols/GSWO) — exchange and symbol cross-check
- [Schwab GSWO performance page](https://www.schwab.wallst.com/Prospect/Research/etfs/performance.asp?symbol=glov) — secondary rounded-performance and GLOV-to-GSWO alias cross-check only
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
