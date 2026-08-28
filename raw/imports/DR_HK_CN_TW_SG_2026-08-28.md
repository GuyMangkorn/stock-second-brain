---
type: source-note
source_kind: dr-market-screen
source: https://www.set.or.th/th/market/product/dr/marketdata
source_note: raw/imports/DR_all_2026-08-28.md
screen_source: https://www.settrade.com/th/equities/dr/market-data
access_date: 2026-08-28
screen_date: 2026-08-28
selection_basis: underlying listing exchange, not company domicile
source_results: 512
selected_dr_rows: 118
hkex_stock_rows: 100
china_mainland_stock_rows: 9
singapore_stock_rows: 9
taiwan_stock_rows: 0
tags:
  - source/dr
  - source/set
  - source/settrade
  - screening/asia-listed-stocks
---

# SET DR — Hong Kong / China / Taiwan / Singapore Stocks — 2026-08-28

## Bottom Line

คัดจาก DR universe 512 rows ใน [[DR_all_2026-08-28]] โดยใช้ **ตลาดที่หุ้นอ้างอิงจดทะเบียนจริง** เป็นเกณฑ์ ไม่ใช่ประเทศ domicile ของบริษัท และตัด ETF / trust ออกจากคำว่า “หุ้น” ได้ผลดังนี้:

| Underlying listing market | DR rows | หมายเหตุ |
|---|---:|---|
| The Stock Exchange of Hong Kong Limited (HKEX) | 100 | หุ้นอ้างอิง 56 รายการ |
| Mainland China — Shanghai / Shenzhen Stock Exchange | 9 | SSE 5 + SZSE 4 |
| Singapore Exchange (SGX) | 9 | หุ้นอ้างอิง 9 รายการ |
| Taiwan Stock Exchange (TWSE) | 0 | รายการที่พบเป็น ETF ทั้งหมด |
| **รวม** | **118** | นับ DR symbols; wrapper หลายตัวของหุ้นเดียวกันยังคงแยกไว้ |

บริษัทจีนที่มี H-share จดทะเบียนใน Hong Kong จะอยู่ในกลุ่ม HKEX ตาม listing ของ underlying; ไม่ย้ายไปกลุ่ม China เพียงเพราะบริษัทมี domicile เป็นจีน

## Source Map

| Source | ใช้ยืนยัน |
|---|---|
| [SET DR Market Data](https://www.set.or.th/th/market/product/dr/marketdata) | แหล่งข้อมูลต้นทางของ DR universe |
| [[DR_all_2026-08-28]] | 512 source rows และค่า `symbol / underlying / page` ที่นำมาคัดกรอง |
| [SETTRADE DR Market Data](https://www.settrade.com/th/equities/dr/market-data) | ตัวกรอง `ตลาดหลักทรัพย์ของสินทรัพย์อ้างอิง` และผลลัพธ์ HKEX / SSE / SGX / TWSE |
| SETTRADE DR quote pages | ลิงก์ตลาดอ้างอิงและ stock code ของ 4 SZSE rows ซึ่งไม่แสดงเป็นตัวเลือกแยกใน filter page |

## Reporting Scope

- snapshot นี้มีเฉพาะรายชื่อ DR และ underlying ไม่มีราคา, NAV, issuer, ISIN, conversion ratio หรือข้อมูลการเงิน
- `DR rows` หมายถึงจำนวน symbols ใน SET ไม่ใช่จำนวนหุ้นอ้างอิงที่ไม่ซ้ำกัน
- คง spelling ของ `underlying` ตาม source เช่น `BILIBI`, `CHHONGQ`, `CNRE` และ `NTES`; ไม่แก้ชื่อโดยไม่มี source block ใหม่
- input note ระบุ `trade_date_shown: 31 ส.ค. 2569` (`2026-08-31`) ซึ่งเป็น future-dated เมื่อเทียบกับ access date; การ screen นี้ใช้ snapshot ที่ SETTRADE แสดงล่าสุดวันที่ 28 ส.ค. 2569 และเก็บ anomaly เดิมไว้

## Extracted Facts

### Hong Kong — HKEX-listed stocks

กรองด้วย `The Stock Exchange of Hong Kong Limited` แล้วตัด rows ที่ `underlying` เป็น ETF ออก เหลือ 100 DR rows:

| Underlying as shown | DR symbol(s) | DR rows |
|---|---|---:|
| AIA | `AIA06`, `AIA19`, `AIA23` | 3 |
| ANTA | `ANTA13`, `ANTA23` | 2 |
| BABA | `BABA01`, `BABA06`, `BABA13`, `BABA19`, `BABA23`, `BABA80` | 6 |
| BIDU | `BIDU01`, `BIDU06`, `BIDU23`, `BIDU80` | 4 |
| BILIBI | `BILIBILI01` | 1 |
| BIREN | `BIREN23` | 1 |
| BYDCOM | `BYDCOM01`, `BYDCOM80` | 2 |
| CATL | `CATL01`, `CATL23`, `CATL80` | 3 |
| CHHONGQ | `CHHONGQ19` | 1 |
| CHMOBILE | `CHMOBILE19`, `CHMOBILE23` | 2 |
| CMBANK | `CMBANK23` | 1 |
| GAC | `GAC03` | 1 |
| GANFENG | `GANFENG23`, `GANFENG80` | 2 |
| GDS | `GDS23` | 1 |
| GEELY | `GEELY06`, `GEELY80` | 2 |
| GIGA | `GIGA23`, `GIGA80` | 2 |
| HAIERS | `HAIERS19` | 1 |
| HANSOH | `HANSOH19` | 1 |
| HKEX | `HKEX23` | 1 |
| HORIZON | `HORIZON23` | 1 |
| HUAHONG | `HUAHONG23` | 1 |
| ICBC | `ICBC06`, `ICBC19` | 2 |
| JD | `JD80` | 1 |
| JDHEAL | `JDHEAL19` | 1 |
| JLMAG | `JLMAG80` | 1 |
| KINGSOFT | `KINGSOFT23` | 1 |
| KUAISH | `KUAISH01`, `KUAISH06`, `KUAISH23`, `KUAISH80` | 4 |
| LAOPU | `LPGOLD13` | 1 |
| LENOVO | `LENOVO13` | 1 |
| MAOGEP | `MAOGEP80` | 1 |
| MEITUAN | `MEITUAN19`, `MEITUAN23`, `MEITUAN80` | 3 |
| MIDEA | `MIDEA80` | 1 |
| MIXUE | `MIXUE80` | 1 |
| MNSO | `MNSO80` | 1 |
| MONTAGE | `MONTAGE80` | 1 |
| NONGFU | `NONGFU80` | 1 |
| NTES | `NETEASE80` | 1 |
| PETROCN | `PETROCN80` | 1 |
| PINGAN | `PINGAN01`, `PINGAN80` | 2 |
| POPMART | `POPMART23`, `POPMART80` | 2 |
| SENSE | `SENSE23` | 1 |
| SINOBIO | `SINOBIO19` | 1 |
| SMIC | `SMIC01`, `SMIC03`, `SMIC13`, `SMIC23` | 4 |
| SUNNY | `SUNNY19`, `SUNNY80` | 2 |
| TENCENT | `TENCENT01`, `TENCENT06`, `TENCENT11`, `TENCENT13`, `TENCENT19`, `TENCENT23`, `TENCENT80` | 7 |
| TME | `TME23` | 1 |
| TRIPCOM | `TRIPCOM23`, `TRIPCOM80` | 2 |
| UBTECH | `UBTECH23` | 1 |
| VGT | `VGT80` | 1 |
| WUXI | `WUXI06`, `WUXI13` | 2 |
| WUXIAT | `WUXIAT80` | 1 |
| XIAOMI | `XIAOMI01`, `XIAOMI13`, `XIAOMI19`, `XIAOMI23`, `XIAOMI80` | 5 |
| XPENG | `XPENG03` | 1 |
| YOFC | `YOFC23` | 1 |
| ZAI | `ZAI23` | 1 |
| ZIJIN | `ZIJIN13`, `ZIJIN23`, `ZIJIN80` | 3 |

### Mainland China — SSE / SZSE-listed stocks

ตลาดอ้างอิงยืนยันจากลิงก์ `สินทรัพย์อ้างอิง` ใน SETTRADE quote page ของแต่ละ DR:

| Exchange | Underlying as shown | Stock code | DR symbol |
|---|---|---:|---|
| SSE | CAMBRI | `688256` | [CAMBRI80](https://www.settrade.com/th/equities/dr/quote/CAMBRI80/overview) |
| SSE | CNRE | `600111` | [CNRE80](https://www.settrade.com/th/equities/dr/quote/CNRE80/overview) |
| SSE | CYPC | `600900` | [CYPC80](https://www.settrade.com/th/equities/dr/quote/CYPC80/overview) |
| SSE | HYGON | `688041` | [HYGON80](https://www.settrade.com/th/equities/dr/quote/HYGON80/overview) |
| SSE | MOUTAI | `600519` | [MOUTAI80](https://www.settrade.com/th/equities/dr/quote/MOUTAI80/overview) |
| SZSE | IFLYTEK | `002230` | [IFLYTEK80](https://www.settrade.com/th/equities/dr/quote/IFLYTEK80/overview) |
| SZSE | NAURA | `002371` | [NAURA80](https://www.settrade.com/th/equities/dr/quote/NAURA80/overview) |
| SZSE | TONGFU | `002156` | [TONGFU23](https://www.settrade.com/th/equities/dr/quote/TONGFU23/overview) |
| SZSE | ZJINNO | `300308` | [ZJINNO80](https://www.settrade.com/th/equities/dr/quote/ZJINNO80/overview) |

### Singapore — SGX-listed stocks

กรองด้วย `Singapore Exchange` แล้วตัด ETF / trust-like instrument ออก เหลือ 9 DR rows:

| Underlying as shown | DR symbol | DR rows |
|---|---|---:|
| DBS | `DBS19` | 1 |
| SEMB | `SEMB19` | 1 |
| SGX | `SGX19` | 1 |
| SIA | `SIA19` | 1 |
| SINGTEL | `SINGTEL80` | 1 |
| STEG | `STEG19` | 1 |
| THAIBEV | `THAIBEV19` | 1 |
| UOB | `UOB19` | 1 |
| VENTURE | `VENTURE19` | 1 |

### Taiwan — TWSE-listed stocks

ไม่พบ DR ที่เป็น **หุ้น** จดทะเบียนใน TWSE ใน snapshot นี้ (`0 rows`). ตัวกรอง Taiwan Stock Exchange พบ 3 rows แต่ทั้งหมดเป็น ETF:

| DR symbol | Underlying as shown | Reason excluded |
|---|---|---|
| `TAIWAN19` | YT TAIWAN50 ETF | ETF |
| `TAIWANAI13` | KGI TAIWAN AI 50 ETF | ETF |
| `TAIWANHD13` | KGI TAIWAN HD 30 ETF | ETF |

## Exclusions / Edge Cases

- Singapore filter มี `BONDAS19` (`BONDAS ETF`), `GOLD19` (`SPDR GOLD TRUST(GSD)`) และ `INDIAESG19` (`IS INDIA CLIMATE ETF`) แต่ไม่ใช่หุ้น จึงไม่รวมใน 9 rows
- Shanghai filter มี `CN23` และ `CNSTAR5023` ซึ่งเป็น ETF จึงไม่รวมใน 5 SSE stocks
- `GRAB80` เป็นบริษัทสิงคโปร์แต่ SETTRADE ชี้ underlying ไปที่ NASDAQ; จึงไม่ใช่ SGX-listed stock ตามเกณฑ์นี้
- `TSEMI03` และ `TSEMI23` ไม่ใช่ TWSE-listed stock; SETTRADE ชี้ underlying ไปที่ NASDAQ (`TSEM`)
- SETTRADE filter page ไม่แสดง `Shenzhen Stock Exchange` เป็นตัวเลือกแยก แต่ quote pages ของ `IFLYTEK80`, `NAURA80`, `TONGFU23` และ `ZJINNO80` แสดงลิงก์ SZSE โดยตรง จึงรวมไว้ใน Mainland China

## Missing / Unverified Data

- raw JSON ต้นทางไม่มี exchange, legal name, ISIN หรือ official listing code; HKEX / SGX / TWSE grouping มาจาก exchange filter ของ SETTRADE และ mainland stock code มาจาก underlying links ของ quote pages
- ไม่ได้ตรวจว่า DR แต่ละตัวมีสถานะ active, liquidity, issuer, conversion ratio หรือสิทธิประโยชน์ล่าสุดอย่างไร
- หากต้องการจัดตาม **ประเทศ domicile ของบริษัท** แทน listing exchange ต้องทำ classification ชุดใหม่ เพราะบริษัทจีนหลายรายอยู่ใน HKEX table ผ่าน H-shares

## Handoff For Ingest / Next Research

ใช้ไฟล์นี้เป็นรายการคัดกรอง DR หุ้นเอเชียเท่านั้น หากจะทำ company research หรือ ETF research ให้ resolve underlying เป็น `EXCHANGE:TICKER` และสร้าง source note/facts แยกตาม instrument; ไม่ควรนำตารางนี้ไปเป็น financial fundamentals โดยตรง
