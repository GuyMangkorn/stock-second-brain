---
type: etf-performance
instrument_type: ETF
entity_key: Euronext Amsterdam:XUSE
input_ticker: IXUAF
ticker: XUSE
exchange: Euronext Amsterdam
fund: iShares MSCI World ex-USA UCITS ETF (USD Accumulating)
tracked_index: MSCI World Ex US Net Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-30
performance_as_of: 2026-06-30
calendar_years_as_of: not applicable (no complete calendar year)
current_ytd_as_of: 2026-08-27
price_nav_as_of: 2026-08-28
fund_facts_as_of: 2026-08-28
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: NAV total return; gross income reinvested; net of ongoing charges
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/XUSE
  - ticker/IXUAF
  - geography/International
---

# IXUAF / XUSE ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

IXUAF เป็น OTC input alias ของ official USD listing `Euronext Amsterdam:XUSE`
สำหรับ iShares MSCI World ex-USA UCITS ETF (USD Accumulating), ISIN
`IE000R4ZNTN3`. กองทุนเป็น passive, physical, accumulating equity ETF ที่
ติดตาม `MSCI World Ex US Net Index` และมี TER `0.15%`; canonical exchange ใน
vault ใช้ Euronext Amsterdam เพราะ official listing ระบุ `XUSE` เป็น USD ที่นี่
(ขณะที่ LSE `XUSE` เป็น GBP และ Xetra `IXUA` เป็น EUR).

กองทุนเริ่ม 24 ม.ค. 2025 จึงยังไม่มี complete calendar year, 10-year field
หรือ 2021-2025 CAGR ที่ยืนยันได้. Official product page รายงาน NAV Total Return
YTD `+14.27%` ณ 27 ส.ค. 2026 และ NAV ล่าสุด `US$7.34` ณ 28 ส.ค. 2026. Official
June factsheet รายงาน 1-year `+21.11%` และ since-inception annualized `+26.07%`
ณ 30 มิ.ย. 2026; ตัวเลข YTD `+9.31%` ใน factsheet เป็นคนละ as-of date จึงไม่ใช่
source conflict.

## Performance check

- `entity_key: Euronext Amsterdam:XUSE`; `input_ticker: IXUAF`; official USD listing `Euronext Amsterdam:XUSE`; ISIN `IE000R4ZNTN3`; share-class inception `24 ม.ค. 2025`; listing date `30 ม.ค. 2025`
- Classification: supported passive/index-tracking equity UCITS ETF; iShares ระบุ physical replication และ accumulating share class
- Metric: `NAV Total Return` บนฐาน USD; official performance ระบุ gross income reinvested และ net of ongoing charges; ไม่มี cash distribution ที่ต้องบวกกลับแยกต่างหาก
- Issuer benchmark: `MSCI World Ex US Net Index`; benchmark ด้านล่าง/ใน vault คือ `S&P 500 Total Return` (USD, dividends reinvested; common reference เท่านั้น ไม่ใช่ strategy-aligned benchmark)
- TER: `0.15%`; current official share-class net assets `US$3.709B`, total fund net assets `US$3.712B`, holdings `751`, P/E `19.68x`, P/B `2.45x` ณ 28 ส.ค. 2026
- Official current field as of `2026-08-27`: NAV TR YTD `+14.27%`; latest official NAV `US$7.34` as of `2026-08-28`
- Official factsheet as of `2026-06-30`: 1-month `-0.16%`, 3-month `+10.31%`, 6-month/YTD `+9.31%`, 1-year `+21.11%`, since-inception annualized `+26.07%`; MSCI benchmark rows are `-0.17%`, `+10.22%`, `+9.19%`, `+20.99%`, and `+25.86%`, respectively
- 10-year NAV TR, complete calendar rows, 2021-2025 CAGR, up/down-year count, best/worst year, maximum drawdown, recovery duration, downside capture, and risk-adjusted persistence: `ไม่พบข้อมูลที่ยืนยันได้` หรือ `not applicable` เพราะ share class ยังใหม่และ daily NAV series ไม่ได้เปิดเผยใน reviewed official sources

| As of | Metric | XUSE NAV TR (USD) | MSCI World Ex US Net |
|---|---|---:|---:|
| 2026-08-27 | YTD | 14.27% | not disclosed on current page |
| 2026-06-30 | 1 month | -0.16% | -0.17% |
| 2026-06-30 | 3 months | 10.31% | 10.22% |
| 2026-06-30 | 6 months / YTD | 9.31% | 9.19% |
| 2026-06-30 | 1 year | 21.11% | 20.99% |
| 2026-06-30 | Since inception annualized | 26.07% | 25.86% |

ไม่มีการสร้าง calendar CAGR, S&P 500 same-window comparison หรือ alpha จาก
ข้อมูลชุดนี้ เพราะยังไม่มี complete calendar history และ as-of windows ของ
กองทุนกับ cached S&P convention ไม่ตรงกัน.

## Risk read-through

XUSE ให้ developed-market equity exposure นอกสหรัฐฯ ครอบคลุม large/mid-cap
หลายประเทศ แต่ผลลัพธ์ยัง sensitive ต่อ country allocation, FX, sector cycle,
foreign-market liquidity และการที่กองทุนเพิ่งเริ่มมีประวัติ. Official sector
snapshot ณ 28 ส.ค. 2026 คือ Financials `27.76%`, Industrials `17.77%`, IT
`10.17%`, Health Care `8.87%`, Consumer Discretionary `7.61%`, Materials
`7.51%`, Consumer Staples `6.12%`, Energy `5.32%`, Communication `3.54%` และ
Utilities `3.51%`. Official page แสดง 3-year beta และ standard deviation เป็น
`-`; จึงไม่แทนด้วย OTC price, market-price return หรือ secondary drawdown proxy.

ความเสี่ยงหลักคือ developed ex-U.S./country, FX, sector/valuation,
tracking-error, premium/discount, liquidity และ short-history risk. กองทุนเป็น
physical และไม่เข้าเกณฑ์ unsupported derivative-heavy ETF ใน workflow นี้.

## Sources

- [iShares MSCI World ex-USA UCITS ETF official product page](https://www.ishares.com/uk/individual/en/products/340748/ishares-msci-world-ex-usa-ucits-etf) — identity, official listings, NAV/YTD, assets, holdings, sector and risk fields
- [iShares XUSE official factsheet](https://www.ishares.com/uk/individual/en/literature/fact-sheet/xuse-ishares-msci-world-ex-usa-ucits-etf-fund-fact-sheet-en-gb.pdf?siteEntryPassthrough=true&switchLocale=y) — 30 June 2026 NAV/benchmark rolling fields, return definition, TER and trading information
- [StockAnalysis IXUAF profile](https://stockanalysis.com/quote/otc/IXUAF/) — secondary OTC alias/name cross-check only; not used for NAV Total Return
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common reference-benchmark definition
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
