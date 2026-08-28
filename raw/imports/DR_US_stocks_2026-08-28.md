---
type: source-note
source_kind: set-dr-us-stock-screen
source: https://www.set.or.th/th/market/product/dr/marketdata
source_note: raw/imports/DR_all_2026-08-28.md
raw_copy: raw/imports/DR_all_2026-08-28.json
access_date: 2026-08-28
trade_date_shown: 31 ส.ค. 2569
trade_date_iso: 2026-08-31
trade_date_status: future_relative_to_input_date
scope: SET DR rows with a US-listed common-stock underlying
total_source_rows: 512
selected_us_stock_rows: 271
distinct_us_stock_underlyings: 149
tags:
  - source/dr
  - source/set
  - screening/us-stock
---

# SET DR U.S.-Listed Stock Screen — 2026-08-28

## Provenance

- Source หลัก: [SET DR Market Data](https://www.set.or.th/th/market/product/dr/marketdata)
- Source snapshot: [[DR_all_2026-08-28]] และ `raw/imports/DR_all_2026-08-28.json`
- ตรวจซ้ำจากตาราง SET ที่เลือก `Trade Date 31 Aug 2026`; ตารางแสดง `Stock Exchange of Underlying` และ `Underlying Type` รายแถว
- หน้า SET แสดงข้อมูลการซื้อขาย/สถิติของแถวที่ตรวจเมื่อ `27 Aug 2026`; เก็บความไม่สอดคล้องของวันที่ตาม source เดิม ไม่ตีความเป็นข้อมูลวันใหม่

## Reporting Scope

ตีความ “หุ้นอเมริกา” ในไฟล์นี้ตามตลาดของ underlying ไม่ใช่สัญชาติบริษัท โดยคัดเฉพาะแถวที่ SET ระบุพร้อมกันว่า:

- `Underlying Type = Foreign Common Stock`
- `Stock Exchange of Underlying` เป็น `The Nasdaq Stock Market`, `The Nasdaq Global Select Market`, `The New York Stock Exchange` หรือ `The New York Stock Exchange Archipelago`

ดังนั้นอาจมี foreign issuer หรือ ADR ที่ซื้อขายในตลาดสหรัฐฯ รวมอยู่ด้วย ส่วน ETF/fund และ `Units of Foreign Collective Investment Scheme` ไม่รวม แม้จะจดทะเบียนบนตลาดสหรัฐฯ

| Item | Value |
|---|---:|
| Source DR rows | 512 |
| Selected U.S.-listed common-stock DR rows | 271 |
| Distinct underlying labels | 149 |
| Nasdaq Stock Market rows | 158 |
| Nasdaq Global Select Market rows | 23 |
| New York Stock Exchange rows | 90 |

ตัวเลขเป็น row counts จาก snapshot/ตาราง SET ไม่ใช่ market-value calculations

## Screening Notes

- รายการด้านล่างจัดกลุ่มตาม `underlying` เพื่อให้อ่านง่าย แต่เก็บ DR symbol ทุกตัวที่ผ่านเกณฑ์ไว้ครบ
- `APPL03` คง `underlying: APPL` ตาม JSON ต้นทาง; ประกาศ SET ของรายการนี้ระบุ underlying จริงเป็น AppLovin Corporation (`APP`) บน Nasdaq จึงถือเป็น source-label alias/data-quality caveat ไม่แก้ค่าเงียบ ๆ ในไฟล์นี้
- `SPACEX` รวมอยู่เพราะตาราง SET ระบุเป็น `Foreign Common Stock` บน Nasdaq; ยังไม่ได้ทำ issuer-level verification เพิ่มนอกเหนือจาก source screen
- ไฟล์นี้เป็นรายชื่อคัดกรองเท่านั้น ยังไม่มี price, conversion ratio, issuer, ISIN, currency หรือ valuation facts ที่ normalize

## Extracted U.S.-Listed Stock DR

| # | Underlying | Stock Exchange of Underlying | DR symbol(s) | DR rows |
|---:|---|---|---|---:|
| 1 | `AAOI` | The Nasdaq Stock Market | `AAOI03`, `AAOI23` | 2 |
| 2 | `AAPL` | The Nasdaq Global Select Market | `AAPL01`, `AAPL03`, `AAPL19`, `AAPL80` | 4 |
| 3 | `ABBV` | The New York Stock Exchange | `ABBV19`, `ABBV80` | 2 |
| 4 | `ABNB` | The Nasdaq Stock Market | `ABNB06` | 1 |
| 5 | `ADBE` | The Nasdaq Stock Market | `ADBE03`, `ADBE06` | 2 |
| 6 | `AFRM` | The Nasdaq Stock Market | `AFRM03` | 1 |
| 7 | `ALAB` | The Nasdaq Stock Market | `ALAB01`, `ALAB23` | 2 |
| 8 | `AMAT` | The Nasdaq Stock Market | `AMAT01`, `AMAT19`, `AMAT23` | 3 |
| 9 | `AMD` | The Nasdaq Stock Market | `AMD03`, `AMD23`, `AMD80` | 3 |
| 10 | `AMGN` | The Nasdaq Stock Market | `AMGN06` | 1 |
| 11 | `AMKR` | The Nasdaq Stock Market | `AMKR03`, `AMKR23` | 2 |
| 12 | `AMPX` | The New York Stock Exchange | `AMPX03` | 1 |
| 13 | `AMZN` | The Nasdaq Stock Market | `AMZN01`, `AMZN03`, `AMZN06`, `AMZN19`, `AMZN23`, `AMZN80` | 6 |
| 14 | `ANET` | The New York Stock Exchange | `ANET23`, `ANET80` | 2 |
| 15 | `APLD` | The Nasdaq Stock Market | `APLD03` | 1 |
| 16 | `APPL` | The Nasdaq Stock Market | `APPL03` | 1 |
| 17 | `ASTS` | The Nasdaq Stock Market | `ASTS01`, `ASTS03`, `ASTS23` | 3 |
| 18 | `AVGO` | The Nasdaq Stock Market | `AVGO23`, `AVGO80` | 2 |
| 19 | `AXP` | The New York Stock Exchange | `AXP06` | 1 |
| 20 | `BAC` | The New York Stock Exchange | `BAC03` | 1 |
| 21 | `BDX` | The New York Stock Exchange | `BDX06` | 1 |
| 22 | `BE` | The New York Stock Exchange | `BE03` | 1 |
| 23 | `BKNG` | The Nasdaq Stock Market | `BKNG03`, `BKNG80` | 2 |
| 24 | `BKSY` | The New York Stock Exchange | `BKSY03` | 1 |
| 25 | `BLK` | The New York Stock Exchange | `BLK06` | 1 |
| 26 | `BOEING` | The New York Stock Exchange | `BOEING80` | 1 |
| 27 | `BRKB` | The New York Stock Exchange | `BRKB23`, `BRKB80` | 2 |
| 28 | `CAT` | The New York Stock Exchange | `CAT19` | 1 |
| 29 | `CBRS` | The Nasdaq Stock Market | `CBRS03` | 1 |
| 30 | `CCJ` | The New York Stock Exchange | `CCJ23` | 1 |
| 31 | `CDNS` | The Nasdaq Stock Market | `CDNS23` | 1 |
| 32 | `CEG` | The Nasdaq Stock Market | `CEG23` | 1 |
| 33 | `CIEN` | The New York Stock Exchange | `CIEN03` | 1 |
| 34 | `CME` | The Nasdaq Stock Market | `CME03` | 1 |
| 35 | `COHR` | The New York Stock Exchange | `COHR23`, `COHR80` | 2 |
| 36 | `COIN` | The Nasdaq Stock Market | `COIN01`, `COIN23`, `COIN80` | 3 |
| 37 | `COSTCO` | The Nasdaq Stock Market | `COSTCO19`, `COSTCO80` | 2 |
| 38 | `CRDO` | The Nasdaq Stock Market | `CRDO23` | 1 |
| 39 | `CRM` | The New York Stock Exchange | `CRM01`, `CRM06`, `CRM80` | 3 |
| 40 | `CRSP` | The Nasdaq Stock Market | `CRSP03` | 1 |
| 41 | `CRWD` | The Nasdaq Stock Market | `CRWD06`, `CRWD80` | 2 |
| 42 | `CRWV` | The Nasdaq Stock Market | `CRWV03`, `CRWV23` | 2 |
| 43 | `CSCO` | The Nasdaq Stock Market | `CSCO06` | 1 |
| 44 | `DASH` | The Nasdaq Stock Market | `DASH03` | 1 |
| 45 | `DDOG` | The Nasdaq Stock Market | `DDOG19` | 1 |
| 46 | `DELL` | The New York Stock Exchange | `DELL19`, `DELL23` | 2 |
| 47 | `DISNEY` | The New York Stock Exchange | `DISNEY19` | 1 |
| 48 | `DOLLARG` | The New York Stock Exchange | `DOLLARG80` | 1 |
| 49 | `DUOL` | The Nasdaq Stock Market | `DUOL06` | 1 |
| 50 | `EOSE` | The Nasdaq Stock Market | `EOSE03`, `EOSE23` | 2 |
| 51 | `ESTEE` | The New York Stock Exchange | `ESTEE80` | 1 |
| 52 | `ETN` | The New York Stock Exchange | `ETN03`, `ETN23` | 2 |
| 53 | `EXPE` | The Nasdaq Stock Market | `EXPE06` | 1 |
| 54 | `FABRINET` | The New York Stock Exchange | `FABRINET03`, `FABRINET23` | 2 |
| 55 | `FCX` | The New York Stock Exchange | `FCX23` | 1 |
| 56 | `FSLR` | The Nasdaq Stock Market | `FSLR03` | 1 |
| 57 | `FTNT` | The Nasdaq Stock Market | `FTNT03` | 1 |
| 58 | `FWONK` | The Nasdaq Stock Market | `FWONK06` | 1 |
| 59 | `GEV` | The New York Stock Exchange | `GEV23`, `GEV80` | 2 |
| 60 | `GFS` | The Nasdaq Stock Market | `GFS03` | 1 |
| 61 | `GLW` | The New York Stock Exchange | `GLW80` | 1 |
| 62 | `GOOG` | The Nasdaq Global Select Market | `GOOG06`, `GOOG23`, `GOOG80` | 3 |
| 63 | `GOOGL` | The Nasdaq Stock Market | `GOOGL01`, `GOOGL03`, `GOOGL19` | 3 |
| 64 | `GRAB` | The Nasdaq Stock Market | `GRAB80` | 1 |
| 65 | `GSUS` | The New York Stock Exchange | `GSUS06` | 1 |
| 66 | `HIMS` | The New York Stock Exchange | `HIMS03` | 1 |
| 67 | `HOOD` | The Nasdaq Stock Market | `HOOD03`, `HOOD06`, `HOOD80` | 3 |
| 68 | `IBM` | The New York Stock Exchange | `IBM06`, `IBM23` | 2 |
| 69 | `INFQ` | The New York Stock Exchange | `INFQ03` | 1 |
| 70 | `INTEL` | The Nasdaq Stock Market | `INTEL01`, `INTEL03`, `INTEL19`, `INTEL23` | 4 |
| 71 | `IONQ` | The New York Stock Exchange | `IONQ03`, `IONQ23` | 2 |
| 72 | `ISRG` | The Nasdaq Stock Market | `ISRG01`, `ISRG06`, `ISRG19`, `ISRG80` | 4 |
| 73 | `JCI` | The New York Stock Exchange | `JCI03` | 1 |
| 74 | `JNJ` | The New York Stock Exchange | `JNJ03` | 1 |
| 75 | `JOBY` | The New York Stock Exchange | `JOBY03` | 1 |
| 76 | `JPMUS` | The New York Stock Exchange | `JPMUS06`, `JPMUS19` | 2 |
| 77 | `KLAC` | The Nasdaq Stock Market | `KLAC01`, `KLAC19`, `KLAC23` | 3 |
| 78 | `KO` | The New York Stock Exchange | `KO80` | 1 |
| 79 | `LITE` | The Nasdaq Stock Market | `LITE01`, `LITE23`, `LITE80` | 3 |
| 80 | `LLY` | The New York Stock Exchange | `LLY23`, `LLY80` | 2 |
| 81 | `LRCX` | The Nasdaq Stock Market | `LRCX01`, `LRCX19`, `LRCX23`, `LRCX80` | 4 |
| 82 | `LULU` | The Nasdaq Stock Market | `LULU06` | 1 |
| 83 | `MA` | The New York Stock Exchange | `MA80` | 1 |
| 84 | `MELI` | The Nasdaq Stock Market | `MELI06`, `MELI23` | 2 |
| 85 | `META` | The Nasdaq Stock Market | `META01`, `META06`, `META23`, `META80` | 4 |
| 86 | `MICRON` | The Nasdaq Stock Market | `MICRON01`, `MICRON03`, `MICRON19`, `MICRON23`, `MICRON80` | 5 |
| 87 | `MKSI` | The Nasdaq Stock Market | `MKSI03` | 1 |
| 88 | `MNST` | The Nasdaq Stock Market | `MNST06` | 1 |
| 89 | `MP` | The New York Stock Exchange | `MP23`, `MP80` | 2 |
| 90 | `MPWR` | The Nasdaq Stock Market | `MPWR23` | 1 |
| 91 | `MRAM` | The Nasdaq Stock Market | `MRAM03` | 1 |
| 92 | `MRVL` | The Nasdaq Stock Market | `MRVL06`, `MRVL23`, `MRVL80` | 3 |
| 93 | `MS` | The New York Stock Exchange | `MS06` | 1 |
| 94 | `MSFT` | The Nasdaq Global Select Market | `MSFT01`, `MSFT03`, `MSFT06`, `MSFT19`, `MSFT23`, `MSFT80` | 6 |
| 95 | `NBIS` | The Nasdaq Stock Market | `NBIS01`, `NBIS03`, `NBIS23`, `NBIS80` | 4 |
| 96 | `NDAQ` | The Nasdaq Stock Market | `NDAQ06` | 1 |
| 97 | `NEE` | The New York Stock Exchange | `NEE80` | 1 |
| 98 | `NEM` | The New York Stock Exchange | `NEM06`, `NEM23` | 2 |
| 99 | `NET` | The New York Stock Exchange | `NET03` | 1 |
| 100 | `NFLX` | The Nasdaq Stock Market | `NFLX06`, `NFLX80` | 2 |
| 101 | `NIKE` | The New York Stock Exchange | `NIKE80` | 1 |
| 102 | `NOW` | The New York Stock Exchange | `NOW19`, `NOW23` | 2 |
| 103 | `NVDA` | The Nasdaq Global Select Market | `NVDA01`, `NVDA03`, `NVDA06`, `NVDA19`, `NVDA23`, `NVDA80` | 6 |
| 104 | `NVTS` | The Nasdaq Stock Market | `NVTS03`, `NVTS23` | 2 |
| 105 | `OKLO` | The New York Stock Exchange | `OKLO03`, `OKLO23` | 2 |
| 106 | `ON` | The Nasdaq Stock Market | `ON23` | 1 |
| 107 | `ONDS` | The Nasdaq Stock Market | `ONDS03` | 1 |
| 108 | `ONON` | The New York Stock Exchange | `ONON03` | 1 |
| 109 | `ORCL` | The New York Stock Exchange | `ORCL01`, `ORCL06`, `ORCL19`, `ORCL23`, `ORCL80` | 5 |
| 110 | `OXY` | The New York Stock Exchange | `OXY03` | 1 |
| 111 | `PANW` | The Nasdaq Stock Market | `PANW19`, `PANW80` | 2 |
| 112 | `PEP` | The Nasdaq Stock Market | `PEP80` | 1 |
| 113 | `PFIZER` | The New York Stock Exchange | `PFIZER19` | 1 |
| 114 | `PLAB` | The New York Stock Exchange | `PLAB03` | 1 |
| 115 | `PLTR` | The Nasdaq Stock Market | `PLTR01`, `PLTR03`, `PLTR06`, `PLTR23` | 4 |
| 116 | `PNG` | The New York Stock Exchange | `PNG80` | 1 |
| 117 | `PWR` | The New York Stock Exchange | `PWR03` | 1 |
| 118 | `PYPL` | The Nasdaq Stock Market | `PYPL06` | 1 |
| 119 | `QBTS` | The Nasdaq Stock Market | `QBTS03` | 1 |
| 120 | `QCOM` | The Nasdaq Stock Market | `QCOM06`, `QCOM23` | 2 |
| 121 | `RBLX` | The New York Stock Exchange | `RBLX06` | 1 |
| 122 | `RGTI` | The Nasdaq Stock Market | `RGTI03`, `RGTI23` | 2 |
| 123 | `RKLB` | The Nasdaq Stock Market | `RKLB01`, `RKLB03`, `RKLB23`, `RKLB80` | 4 |
| 124 | `SBUX` | The Nasdaq Stock Market | `SBUX80` | 1 |
| 125 | `SEAGATE` | The Nasdaq Stock Market | `SEAGATE23` | 1 |
| 126 | `SHOP` | The Nasdaq Stock Market | `SHOP03`, `SHOP06` | 2 |
| 127 | `SMCI` | The Nasdaq Stock Market | `SMCI03` | 1 |
| 128 | `SMR` | The New York Stock Exchange | `SMR03`, `SMR23` | 2 |
| 129 | `SNDK` | The Nasdaq Stock Market | `SNDK03`, `SNDK23`, `SNDK80` | 3 |
| 130 | `SNOW` | The New York Stock Exchange | `SNOW06`, `SNOW23` | 2 |
| 131 | `SOFI` | The Nasdaq Stock Market | `SOFI23` | 1 |
| 132 | `SPACEX` | The Nasdaq Stock Market | `SPACEX01`, `SPACEX03`, `SPACEX06`, `SPACEX23`, `SPACEX80` | 5 |
| 133 | `SPOT` | The New York Stock Exchange | `SPOT06` | 1 |
| 134 | `STM` | The New York Stock Exchange | `STM03` | 1 |
| 135 | `SYM` | The Nasdaq Stock Market | `SYM03`, `SYM23` | 2 |
| 136 | `SYNP` | The Nasdaq Stock Market | `SYNP03`, `SYNP23` | 2 |
| 137 | `TER` | The Nasdaq Stock Market | `TER01`, `TER23`, `TER80` | 3 |
| 138 | `TRVUS` | The New York Stock Exchange | `TRVUS06` | 1 |
| 139 | `TSEMI` | The Nasdaq Stock Market | `TSEMI03`, `TSEMI23` | 2 |
| 140 | `TSLA` | The Nasdaq Global Select Market | `TSLA01`, `TSLA03`, `TSLA23`, `TSLA80` | 4 |
| 141 | `UBER` | The New York Stock Exchange | `UBER06` | 1 |
| 142 | `UNH` | The New York Stock Exchange | `UNH19` | 1 |
| 143 | `USAR` | The Nasdaq Stock Market | `USAR03` | 1 |
| 144 | `VICR` | The Nasdaq Stock Market | `VICR80` | 1 |
| 145 | `VISA` | The New York Stock Exchange | `VISA06`, `VISA80` | 2 |
| 146 | `VRT` | The New York Stock Exchange | `VRT01`, `VRT23`, `VRT80` | 3 |
| 147 | `VST` | The New York Stock Exchange | `VST03` | 1 |
| 148 | `WDC` | The Nasdaq Stock Market | `WDC03` | 1 |
| 149 | `WMT` | The Nasdaq Stock Market | `WMT06`, `WMT80` | 2 |

## Missing / Unverified Data

- ชื่อบริษัทเต็ม, issuer, ISIN, conversion ratio, currency, market data และ corporate domicile: ไม่ได้เก็บใน source JSON ที่ผู้ใช้ให้
- การคัดกรองนี้ยืนยันตลาดและประเภทหลักทรัพย์ตามตาราง SET ที่ตรวจ ณ access date แต่ไม่ได้ยืนยัน legal domicile หรือสิทธิ/ข้อจำกัดของแต่ละ DR
- วันที่ `trade_date_shown: 31 ส.ค. 2569` เป็น future-dated เมื่อเทียบกับ `access_date/input date: 2026-08-28`; คงไว้ตาม source meaning

## Handoff For Ingest

ใช้ไฟล์นี้เป็น source-of-truth ของรายชื่อ DR หุ้นที่ underlying อยู่บนตลาดสหรัฐฯ สำหรับทำ research ต่อ โดยควร resolve `EXCHANGE:TICKER` และตรวจ official issuer/SET factsheet แยก instrument ก่อนสร้าง normalized company facts หรือ decision memo
