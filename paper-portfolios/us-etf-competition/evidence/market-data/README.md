# Market Data Evidence

ตลาดข้อมูลใหม่มีสามชั้นและแต่ละชั้นมีหน้าที่ต่างกัน:

1. [`latest-prices.md`](latest-prices.md) — `etf-price-screen-cache` แบบ compact
   มีราคาล่าสุดและ rolling context ต่อ ticker ใช้คัดกรองเบื้องต้นเท่านั้น
2. [`price-log.md`](price-log.md) — ประวัติราคาแบบ append-only มีหนึ่งแถวต่อ
   verified observation และเป็น index ที่อ่าน tail ได้เร็ว
3. [`batches/`](batches/) — full market-data evidence แบบ immutable หนึ่งไฟล์ต่อ
   Portfolio Run รวม clock, calendar และ direct quote observations ไว้ด้วยกัน

Normal run ต้องอ่าน screen cache และเฉพาะ tail ของ price log ก่อนคัด shortlist;
ห้ามเปิด historical evidence ทั้ง tree เพื่อคัด ETF. ราคาใน cache ไม่ใช่
`decision_reference_price` โดยอัตโนมัติ: ก่อน BUY ต้อง refresh direct quote และ
อ้าง batch path พร้อม evidence ID.

โครงสร้างของ run ใหม่:

```text
captured batch JSON (staging)
        │ validate + record_market_data_batch.py
        ├── batches/{run_id}.json       full immutable evidence
        ├── price-log.md                one compact row per observation
        └── latest-prices.md             one rolling row per ticker
```

สร้าง batch ใหม่ด้วยคำสั่งนี้หลังจาก capture หลักฐานเสร็จแล้ว:

```bash
python3 ../../scripts/record_market_data_batch.py \
  --root ../.. --batch /path/to/captured-batch.json
```

ไฟล์เดิมใต้ `YYYY-MM-DD/` เป็น legacy evidence ที่ต้องคง path และเนื้อหาเดิม
ไว้เพื่อให้ run notes และ audit links เก่ายังเปิดได้. ห้าม migrate, rewrite,
move หรือ delete ไฟล์เหล่านั้น; bootstrap จาก `price-log.md` ใช้เฉพาะ recovery
เพื่อสร้าง derived screen cache และไม่สร้าง retroactive batch. Search-result
snippets เป็นเพียง discovery context ไม่ใช่หลักฐานราคาเพียงอย่างเดียว.

Quote priority: ETF.com delayedquotes API → ETF.com product page → แหล่ง direct-web เดิม.
ใช้ `scripts/fetch_etf_quotes.py` จาก portfolio root ตาม README/PROMPT เพื่อสร้าง staging
packet; ตรวจ basis/freshness และเพิ่ม evidence IDs ก่อนรวมเข้า batch. เก็บ raw API
response text ใน `visible_response_text` พร้อม hash โดยไม่แก้ข้อความหรือเวลาจาก cache.
ทุก envelope ใหม่ต้องเก็บ discovery query, direct URL, page title, response text/values,
source-as-of, retrieval timestamp และ SHA-256 content hash.
หาก source ขาดหาย stale หรือขัดแย้ง ให้ลอง fallback และบันทึก gap เฉพาะ candidate;
ใช้ BLOCKED เฉพาะ portfolio-wide failure ตาม PROMPT แทนการเติมค่า.
