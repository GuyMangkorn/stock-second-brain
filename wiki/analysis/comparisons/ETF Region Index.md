---
type: etf-region-index
updated: 2026-08-18
scope: ETF performance navigation
tags:
  - analysis/etf-region
  - analysis/index
---

# ETF Region Index

หน้ารวมสำหรับหา ETF performance ตาม underlying exposure ของกองทุน
โดยหน้ารายกองใน [[ETF Performance Index]] ยังเป็น owner ของตัวเลขและ
driver notes ทั้งหมด

## Browse by region

| Region | ETFs | Navigation |
|---|---:|---|
| USA | 66 | [[USA ETF]] |
| Australia | 3 | [[Australia ETF]] |
| Austria | 1 | [[Austria ETF]] |
| North America | 2 | [[North America ETF]] |
| India | 15 | [[India ETF]] |
| Japan | 22 | [[Japan ETF]] |
| China | 26 | [[China ETF]] |
| Hong Kong | 2 | [[Hong Kong ETF]] |
| Indonesia | 2 | [[Indonesia ETF]] |
| Italy | 1 | [[Italy ETF]] |
| Canada | 2 | [[Canada ETF]] |
| Germany | 2 | [[Germany ETF]] |
| Greece | 1 | [[Greece ETF]] |
| Europe | 14 | [[Europe ETF]] |
| Asia ex Japan | 4 | [[Asia ex Japan ETF]] |
| Asia-Pacific | 12 | [[Asia-Pacific ETF]] |
| Emerging Markets | 5 | [[Emerging Markets ETF]] |
| International | 24 | [[International ETF]] |
| Malaysia | 1 | [[Malaysia ETF]] |
| New Zealand | 1 | [[New Zealand ETF]] |
| Netherlands | 1 | [[Netherlands ETF]] |
| Norway | 2 | [[Norway ETF]] |
| Philippines | 1 | [[Philippines ETF]] |
| Poland | 2 | [[Poland ETF]] |
| Singapore | 1 | [[Singapore ETF]] |
| South Korea | 5 | [[South Korea ETF]] |
| Spain | 1 | [[Spain ETF]] |
| Southeast Asia | 1 | [[Southeast Asia ETF]] |
| Taiwan | 2 | [[Taiwan ETF]] |
| Thailand | 1 | [[Thailand ETF]] |
| United Kingdom | 4 | [[United Kingdom ETF]] |
| Vietnam | 3 | [[Vietnam ETF]] |

## Coverage policy

- การจัดกลุ่มยึด underlying exposure ไม่ใช่ exchange ที่ ETF จดทะเบียน
- ETF แต่ละกองอยู่ใน primary region เดียวเพื่อให้ coverage ตรวจสอบได้ง่าย
- หน้าภูมิภาคเป็น static navigation summary; ไม่คัดลอก annual table หรือ narrative จากหน้ารายกอง
- Taiwan มี performance coverage เพิ่มใน batch `2026-07-23`; unresolved/unsupported products ยังไม่ถูกสร้างเป็น performance page ตาม ETF v1 gate

## Entry points

- [[ETF Performance Index]] — cross-ETF dashboard และ canonical summary metrics
- [[wiki/analysis/performance/README|ETF Performance Convention]] — owner, metric, source และ refresh rules
- [[wiki/analysis/comparisons/README|Comparison Notes]]


Coverage additions from the 2026-07-23 batch are already folded into the
canonical totals above. Unresolved/unsupported input tickers are retained in
the dated source batch and are not assigned a performance page under ETF v1.
