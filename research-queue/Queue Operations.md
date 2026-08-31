# Research Queue Operations

## Intake

ใช้คำสั่ง Intake เพื่อสร้าง Batch และการ์ด `Ready` เท่านั้น ยังไม่เริ่ม research

```bash
python3 scripts/research_queue.py intake --tickers "VIG,DGRO" --type ETF
python3 scripts/research_queue.py intake --input-file watchlist.md --dry-run
```

## Human controls

มนุษย์ใช้คำสั่งเหล่านี้สำหรับ hold, unblock และ cancel โดยไม่แก้สถานะ
`In Progress` หรือ `Done` ด้วยมือ

```bash
python3 scripts/research_queue.py hold --card-id <CARD_ID> --reason "..."
python3 scripts/research_queue.py unblock --card-id <CARD_ID>
python3 scripts/research_queue.py cancel --card-id <CARD_ID>
```

## Scheduled processing

scheduler ต้องส่ง `count`, `execution_profile: scheduled-inline` และใช้
project-local checkout เดียว เลือกด้วย `claim-next`, renew ก่อน lease สองชั่วโมง
หมดอายุและระบุ `--output` เมื่อเข้าสู่ pre-write จากนั้นเรียก workflow ที่ระบุ
ชัดเจน แล้ว route เฉพาะ `research_handoff` เจ็ดฟิลด์ที่ครบ พร้อม output ใต้
`raw/`, `wiki/`, `index.md` หรือ `log.md` ที่มีอยู่จริงและ `--commit` ดู
projection ปฏิบัติการที่ [[Research Queue Monitor.base]]
ทุก bounded run จะ recover claim ที่หมดอายุก่อนเลือกการ์ดใหม่ โดยคืนเฉพาะ
claim ที่ยืนยันได้ว่าอยู่ก่อน pre-write กลับ `Ready` และ block กรณี partial write
ที่กำกวม

เมื่อใช้ lease ต่อเนื่องให้ส่ง token เดิมกลับเข้า `renew` และ `route` แล้วเรียก
`lease-release` เมื่อจบรอบ:

```bash
python3 scripts/research_queue.py claim-next --count 1 --owner research-queue-manager --keep-lease
python3 scripts/research_queue.py renew --card-id <ID> --owner <OWNER> --lease-token <LEASE_TOKEN> --fencing-token <TOKEN> --phase pre-write --output <OUTPUT_PATH>
python3 scripts/research_queue.py route --card-id <ID> --owner <OWNER> --lease-token <LEASE_TOKEN> --fencing-token <TOKEN> --handoff-json '<SEVEN-FIELD JSON>' --output <OUTPUT_PATH> --commit
python3 scripts/research_queue.py lease-release --owner <OWNER> --lease-token <LEASE_TOKEN>
```

สำหรับ adapter ที่เรียก workflow ภายนอกโดยตรง ใช้ `process --handoff-command`
ซึ่งส่ง `RESEARCH_CARD_ID`, `RESEARCH_CARD_PATH`, `RESEARCH_TICKER`,
`RESEARCH_WORKFLOW`, `RESEARCH_PROJECT_LEASE_TOKEN`,
`RESEARCH_CARD_FENCING_TOKEN`, `RESEARCH_EXECUTION_PROFILE` และ
`RESEARCH_OUTPUT_PATHS` ผ่าน environment และรับ JSON handoff จาก stdout เท่านั้น
adapter มี timeout ที่ต่ำกว่า lease สองชั่วโมงโดยค่าเริ่มต้น; ปรับได้ด้วย
`--handoff-timeout-seconds` เมื่อจำเป็น
หาก `count` มากกว่าหนึ่งให้ใช้ `--output-map` เพื่อไม่ให้หลายการ์ดแชร์ output
scope เดียวกัน
