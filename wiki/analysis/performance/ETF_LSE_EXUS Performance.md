---
type: etf-performance
instrument_type: ETF
entity_key: London Stock Exchange:EXUS
input_ticker: XTMWF
ticker: EXUS
exchange: London Stock Exchange
fund: Xtrackers MSCI World ex USA UCITS ETF 1C
tracked_index: MSCI World ex USA Index
benchmark: S&P 500 Total Return
management_mode: passive-index-tracking
updated: 2026-08-30
performance_as_of: 2025-12-31
calendar_years_as_of: 2025-12-31
current_ytd_as_of: not disclosed in reviewed official sources
price_nav_as_of: 2026-07-31
fund_facts_as_of: 2026-07-31
source_batch: raw/imports/ETF_performance_sources_2026-08-30.md
return_basis: official share-class total return; reinvested dividends; net of fund fees
return_currency: USD
tags:
  - analysis/etf-performance
  - ticker/EXUS
  - ticker/XTMWF
  - geography/International
---

# XTMWF / EXUS ETF Performance

> Navigation: [[ETF Region Index]] → [[International ETF]] → [[ETF Performance Index]]

## Bottom line

XTMWF เป็น OTC input alias ของ official USD listing `London Stock Exchange:EXUS`
สำหรับ Xtrackers MSCI World ex USA UCITS ETF 1C, ISIN `IE0006WW1TQ4`. กองทุน
เป็น passive, physically replicated, accumulating equity UCITS ETF ที่ติดตาม
`MSCI World ex USA Index` และมี all-in fee `0.15%` ต่อปี. Official Xtrackers
factsheet ระบุ LSE `EXUS` เป็น USD และ LSE `XMWX` เป็น GBP; vault จึงใช้ `LSE:EXUS`
ให้ตรงกับ share-class/return currency ของ input alias.

Official past-performance document ยืนยัน complete calendar row ที่อ่านได้คือ
ปี 2025: กองทุน `+32.00%` เทียบ MSCI World ex USA Index `+31.90%`. Share class
เริ่ม 6 มี.ค. 2024 จึงไม่มี 2021-2025 CAGR หรือ 10-year field ที่ใช้ได้ และ
2024 เป็น inception partial. Current official YTD ยัง `ไม่พบข้อมูลที่ยืนยันได้`
จาก reviewed issuer sources; latest official USD NAV ที่อ่านได้คือ `US$46.68`
และ total fund assets `US$7.75B` ณ 31 ก.ค. 2026.

## Performance check

- `entity_key: London Stock Exchange:EXUS`; `input_ticker: XTMWF`; official USD listing `London Stock Exchange:EXUS`; ISIN `IE0006WW1TQ4`; share-class/fund launch `6 มี.ค. 2024`
- Classification: supported passive/index-tracking equity UCITS ETF; DWS ระบุ passively managed, direct physical replication และ capitalizing income treatment
- Metric: official share-class total return สะท้อน daily NAV และ reinvested dividends; DWS past-performance document หัก fund fees แล้ว; return currency คือ USD
- Issuer benchmark: `MSCI World ex USA Index` (USD, large-/mid-cap developed markets excluding the U.S.); common reference ใน table คือ `S&P 500 Total Return` (USD, dividends reinvested) ไม่ใช่ strategy-aligned benchmark
- All-in fee: `0.15% p.a.`; latest official factsheet ณ 31 ก.ค. 2026 รายงาน NAV per share `US$46.68`, total fund assets `US$7.75B`, total shares outstanding `159.85M`, และ index constituents `756`
- Official complete calendar performance as of `2025-12-31`: fund `+32.00%` versus MSCI World ex USA `+31.90%`; return-only fund-minus-index observation คือ `+0.10 pp`, ไม่ใช่ alpha
- Current official NAV TR YTD: `ไม่พบข้อมูลที่ยืนยันได้`; secondary YTD/market-price figures are not substituted into the official performance record
- 10-year NAV TR, 2021-2025 CAGR, 2024 full-year return, up/down-year count across a comparable long window, best/worst multi-year window, maximum drawdown, recovery duration, downside capture, and risk-adjusted persistence: `not applicable` หรือ `ไม่พบข้อมูลที่ยืนยันได้` เพราะ share class ใหม่และ reviewed official history มีเพียง 2025 complete row

| Year | EXUS share-class TR (USD) | MSCI World ex USA Index TR (USD) | S&P 500 TR (USD; common ref.) |
|---|---:|---:|---:|
| 2025 | 32.00% | 31.90% | 17.88% |

ปี 2025 เป็นปีเดียวที่เป็น complete calendar observation ใน official past-
performance document. กองทุนชนะ issuer benchmark `0.10 pp` จากตัวเลขที่แสดงแบบ
ปัดเศษ; ไม่ตีความเป็น manager skill เพราะกองทุนเป็น passive และ sample มีเพียง
หนึ่งปี. S&P 500 แสดงเป็น common USD reference เท่านั้น.

## Risk read-through

EXUS ให้ broad developed-market exposure นอกสหรัฐฯ ครอบคลุม 22 จาก 23
developed-market countries และประมาณ 85% market representation ตาม official
factsheet. Top-ten holdings ณ 31 ก.ค. 2026 ได้แก่ ASML `2.56%`, HSBC `1.36%`,
Roche `1.23%`, Royal Bank of Canada `1.15%`, Novartis `1.10%`, Nestlé `1.01%`,
Shell `0.96%`, AstraZeneca `0.96%`, Siemens `0.95%` และ Mitsubishi UFJ `0.93%`;
รวมประมาณ `12.21%` จากน้ำหนักที่ประกาศแบบปัดเศษ.

ความเสี่ยงหลักคือ developed ex-U.S./country, FX, sector cycle, valuation,
tracking error, premium/discount, liquidity และ short-history risk. Official
factsheet ระบุว่า price swings และ currency markets อาจผันผวนสูง และ KID ระบุ
การใช้ derivatives อาจเกิดได้ในเทคนิคการจัดการกองทุน แต่ structure ที่ยืนยันได้
ของ share class นี้คือ direct physical replication ไม่ใช่ leveraged, inverse
หรือ derivative-heavy ETF. Daily NAV history สำหรับ drawdown/recovery และ
official current risk statistics ยัง `ไม่พบข้อมูลที่ยืนยันได้`.

## Sources

- [Xtrackers official July 2026 factsheet](https://etf.dws.com/download/asset/2f21a294-623d-484f-9432-0d08a953b3ce) — identity, USD/GBP listings, inception, physical replication, fee, NAV/assets, index constituents and top holdings
- [Xtrackers official past-performance document](https://etf.dws.com/Download/Past%20Performance/IE0006WW1TQ4/IE/EN) — 2025 share-class and MSCI benchmark returns, reinvested-dividend/net-fee basis
- [Xtrackers official Key Information Document](https://etf.dws.com/en/AssetDownload/Index/73f2266f-b86c-4ec6-a80f-8ee675d176e5/DWS-PRIIPSKID-IE0006WW1TQ4-IE-en-2026-03-06.pdf) — passive objective, index, daily NAV return treatment, accumulation, currency and risk disclosures
- [StockAnalysis XTMWF profile](https://stockanalysis.com/quote/otc/XTMWF/) — secondary OTC alias/name cross-check only; not used for official return values
- [S&P 500 index definition](https://www.spglobal.com/spdji/en/indices/equity/sp-500/) — common reference-benchmark definition
- [[ETF_performance_sources_2026-08-30]] | [[ETF Performance Index]]
