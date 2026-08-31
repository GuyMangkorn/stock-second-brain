# Research Queue

โฟลเดอร์นี้คือคิวปฏิบัติการของโปรเจกต์ โดย Markdown Research
Card under `cards/` represents one instrument plus one explicit Research
Workflow. Each authorized Intake submission has one batch under `batches/`.

## Operating surface

- [[Research Queue Intake.base]] คือ Base Board projection สำหรับ Ready และ
  Blocked cards.
- [[Research Queue Monitor.base]] คือ native Bases monitor สำหรับทุกสถานะและ
  lease/result metadata ของการ์ด
- `python3 scripts/research_queue.py` owns the deterministic file protocol.
- `.runtime/` contains the renewable project lease plus its local inter-process
  lock and is ignored by Git.

frontmatter `status` เป็น source of truth เดียว Base Board และ Bases เป็นเพียง
projection; classic Kanban ไม่ใช่ state owner มนุษย์ทำ hold, unblock หรือ cancel
ได้ ส่วน automation เท่านั้นที่ claim `In Progress` และปิด `Done` หลังได้รับ
`research_handoff` ที่ถูกต้อง

## One-time Trello seed

อ่านเฉพาะ ticker จาก Ready และ Blocked ของ [บอร์ด Trello เดิม](https://trello.com/b/jzj3oa9O/stock-analysis-task)
ทันทีระหว่าง cutover แล้วส่งผ่าน Intake ปกติด้วย `seed` ห้ามคัดลอก description,
provenance, status หรือ comment และห้ามแก้ Trello ตัวเลข checkpoint 69 Ready +
3 Blocked (รวม 72 ticker) เป็นเพียง design-time context จากบอร์ดดังกล่าว ไม่ใช่
source of truth; ต้องอ่าน live board ใหม่ก่อน seed ทุกครั้ง หลัง seed แล้ว
scheduled selection อ่านเฉพาะโฟลเดอร์นี้

## Card status vocabulary

เส้นทางอัตโนมัติคือ `Ready` → `In Progress` → `Done` ส่วน item-level errors ไป
ที่ `Blocked`; มนุษย์ย้าย `Blocked` กลับ `Ready` ได้ `Cancelled` เป็น terminal
outcome ที่มนุษย์กำหนด การ์ด terminal ทุกใบคง path เดิมเพื่อ link และ Git history
