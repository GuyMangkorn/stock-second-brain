---
type: analysis
analysis_kind: dr-etf-classification
source_note: raw/imports/DR_all_2026-08-28.md
source: https://www.set.or.th/th/market/product/dr/marketdata
access_date: 2026-08-28
trade_date_shown: 31 ส.ค. 2569
total_dr_rows: 512
etf_labeled_rows: 66
etf_labeled_underlyings: 60
tags:
  - analysis/dr
  - screening/etf
---

# SET DR ETF Classification — 2026-08-28

## Bottom Line

จาก snapshot รายชื่อ DR ของ SET มี 512 rows; ในจำนวนนี้ 66 DR rows มีค่า `underlying` ที่ระบุคำว่า `ETF` ครอบคลุม 60 underlying labels ที่ไม่ซ้ำกัน. รายการนี้เป็นการคัดกรองจาก source label ของ SET/JSON ไม่ใช่การยืนยันว่า ETF ทุกกองเป็น passive, equity-only หรือเหมาะกับ ETF research v1

## ETF-Labeled DR

| # | Underlying as shown | DR symbol(s) | DR rows |
|---:|---|---|---:|
| 1 | ASEMI ETF | `ASEMI23`, `ASEMI24` | 2 |
| 2 | BONDAS ETF | `BONDAS19` | 1 |
| 3 | BONDUS ETF | `BONDUS01` | 1 |
| 4 | CHNXT50 ETF | `CHNXT5023` | 1 |
| 5 | CAM CSI300 ETF | `CN01` | 1 |
| 6 | CN CSI300 ETF | `CN23` | 1 |
| 7 | CNBIO ETF | `CNBIO24` | 1 |
| 8 | CNEV ETF | `CNEV24` | 1 |
| 9 | CNROBOAI ETF | `CNROBOAI23` | 1 |
| 10 | CNSEMI ETF | `CNSEMI23` | 1 |
| 11 | CNSTAR50 ETF | `CNSTAR5023` | 1 |
| 12 | CAM HSTECH ETF | `CNTECH01` | 1 |
| 13 | INVESCO DB OIL ETF | `DBO80` | 1 |
| 14 | DEAM ETF | `DEAM19` | 1 |
| 15 | DCVFMVN30 ETF | `E1VFVN3001` | 1 |
| 16 | DCVFMVN DIAMOND ETF | `FUEVFVND01` | 1 |
| 17 | SPDR GOLD (HK) ETF | `GOLD03` | 1 |
| 18 | GOLDM ETF | `GOLDM01` | 1 |
| 19 | SPDR GOLD (US) ETF | `GOLDUS03`, `GOLDUS19`, `GOLDUS80` | 3 |
| 20 | GSEMI ETF | `GSEMI24` | 1 |
| 21 | TRAHK ETF | `HK01`, `HK13` | 2 |
| 22 | HSCEI ETF | `HKCE01` | 1 |
| 23 | HSTECH ETF | `HKTECH13` | 1 |
| 24 | HSHD ETF | `HSHD23` | 1 |
| 25 | CAM MSCIINDIA ETF | `INDIA01` | 1 |
| 26 | IS INDIA CLIMATE ETF | `INDIAESG19` | 1 |
| 27 | GLOBALX JAPAN(HK)ETF | `JAP03` | 1 |
| 28 | HS JAPAN TPX100 ETF | `JAPAN10001` | 1 |
| 29 | CAM JAPAN HDG ETF | `JAPAN13` | 1 |
| 30 | JEPI ETF | `JEPI19` | 1 |
| 31 | JGRO ETF | `JGRO19` | 1 |
| 32 | JPANIME ETF | `JPANIME24` | 1 |
| 33 | JPROBOAI ETF | `JPROBOAI24` | 1 |
| 34 | JPSEMI ETF | `JPSEMI24` | 1 |
| 35 | JTEK ETF | `JTEK19` | 1 |
| 36 | CAM NASDAQ 100 ETF | `NDX01` | 1 |
| 37 | NIKKEI ETF | `NIKKEI80` | 1 |
| 38 | S&P CRUDE OIL(HK)ETF | `OIL03`, `OIL24` | 2 |
| 39 | INVESCO NDAQ100 ETF | `QQQM19` | 1 |
| 40 | REMX ETF | `REMX03` | 1 |
| 41 | SIL ETF | `SIL03` | 1 |
| 42 | SP500HK ETF | `SP50001` | 1 |
| 43 | SP500US ETF | `SP500US19`, `SP500US80` | 2 |
| 44 | SPBOND ETF | `SPBOND80` | 1 |
| 45 | SPCOM ETF | `SPCOM80` | 1 |
| 46 | SPENGY ETF | `SPENGY80` | 1 |
| 47 | SPFIN ETF | `SPFIN80` | 1 |
| 48 | SPHLTH ETF | `SPHLTH80` | 1 |
| 49 | SPTECH ETF | `SPTECH80` | 1 |
| 50 | PREMIA STAR50 ETF | `STAR5001` | 1 |
| 51 | YT TAIWAN50 ETF | `TAIWAN19` | 1 |
| 52 | KGI TAIWAN AI 50 ETF | `TAIWANAI13` | 1 |
| 53 | KGI TAIWAN HD 30 ETF | `TAIWANHD13` | 1 |
| 54 | USTR ETF | `USTR24` | 1 |
| 55 | KIM VN30 ETF | `V3011` | 1 |
| 56 | KIM VN DIAMOND ETF | `VDIAMOND11` | 1 |
| 57 | VNFIN LEAD ETF | `VNFIN24` | 1 |
| 58 | VT ETF | `VT03` | 1 |
| 59 | GLOBALX INBLU(HK)ETF | `WORLD03` | 1 |
| 60 | WORLDA ETF | `WORLDA01` | 1 |

## Important Scope Flags

- ชื่อมีสัญญาณ non-equity: `BONDAS19`, `BONDUS01`, `SPBOND80`, `DBO80`, `GOLD03`, `GOLDM01`, `GOLDUS03`, `GOLDUS19`, `GOLDUS80`, `OIL03`, `OIL24`, `SIL03`; ต้อง verify official asset class ก่อนใช้ ETF research v1
- `GOLD19` / `SPDR GOLD TRUST(GSD)` ไม่รวมใน 66 เพราะ source label ไม่มีคำว่า `ETF`; จัดเป็น unresolved fund/trust-like candidate
- `JEPI19` และ `JGRO19` ถูกนับเป็น ETF-labeled ตาม source แต่ยังไม่ได้ตรวจ management mode หรือ passive-status
- วันที่ source แสดง `31 ส.ค. 2569` (2026-08-31) ซึ่งเป็น future-dated เมื่อเทียบกับ input/access date 2026-08-28; ดู provenance และ full table ที่ [[DR_all_2026-08-28]]

## Source / Next Step

- Full 512-row source note: [[DR_all_2026-08-28]]
- Official SET page: [SET DR Market Data](https://www.set.or.th/th/market/product/dr/marketdata)
- หากต้องการทำ ETF research ต่อ ให้ resolve `EXCHANGE:TICKER` และยืนยัน official issuer/product/factsheet, benchmark, holdings, cost และ methodology แยกกอง
