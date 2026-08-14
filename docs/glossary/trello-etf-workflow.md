# Trello ETF Workflow Glossary

| Term | ความหมาย |
|---|---|
| Master card | การ์ดที่ผู้ใช้สร้างใน `Backlog` และมี path ของ Markdown ETF list; เป็นเจ้าของ batch ผ่าน `parent_ari` |
| Child card | การ์ดราย ticker ที่สร้างโดย `trello-etf-backlog`; ชื่อเป็น ticker และอยู่ใน `Ready for AI` ก่อนประมวลผล |
| `parent_ari` | ARI ของ master card ใช้แยก child ที่มี ticker เดียวกันแต่คนละ batch |
| `ticker` | ETF symbol ที่ trim, uppercase และ deduplicate แล้ว; เป็น input ของ `check-etf-performance` |
| Backlog split | งานของ `trello-etf-backlog` ที่สร้าง child cards ที่ยังขาด และเลื่อน master ไป `Done` เมื่อสร้างครบ |
| Processing | งานของ `trello-etf-processing` ที่ claim child จาก `Ready for AI`, ย้ายไป `In Progress` และเรียก downstream worker |
| Result routing | งานของ `trello-etf-result` ที่ย้าย child ไป `Done` หรือ `Blocked` และบันทึก reason |
| Manager/router | `trello-etf-batch` ซึ่งอ่าน `task` และ `count` จาก scheduler prompt แล้วเรียก skill ที่เหมาะสม |
| Strict success | `PASS` + `scope: item` + `durable_write: completed` พร้อม field อื่นที่ไม่ขัดแย้ง; เท่านั้นที่ไป `Done` |
| Item failure | ผลที่ผูกกับ child ticker ได้และไม่ใช่ strict success; Skill 2 บันทึกเหตุผลและย้าย child ไป `Blocked` |
| Global failure | ปัญหา Trello, auth, board/list, config หรือ envelope ที่ระบุ owner ไม่ได้; หยุด run และไม่อ้างว่าสถานะเปลี่ยนสำเร็จ |
| `count` | positive base-10 integer ใน scheduler prompt กำหนดจำนวน master หรือ child สูงสุดที่ manager จะเลือกในหนึ่ง run |
