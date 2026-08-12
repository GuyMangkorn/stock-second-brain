# Trello ETF Batch Item-Error Routing Design

## Goal

ให้ error ที่เกิดระหว่าง downstream ของ ETF ticker เดียวถูกจัดการเป็น
item-level exception เพื่อให้ parent checklist แสดงว่า ticker นั้นถูกจัดการ,
มี child card อธิบายเหตุผล, และ batch เดินต่อไปยัง ticker ถัดไปได้ภายใน
`batch_size`.

## Current failure

รอบ `SCHA` downstream ไม่คืน evidence เพราะ research worker ใช้งานไม่ได้และ
ส่ง handoff เป็น `ERROR / global / research-sub-agent-unavailable`. กติกาเดิม
จึงหยุดทั้ง parent, ไม่สร้าง child, ไม่ check `SCHA`, และไม่ทำ ticker ถัดไป.

## Routing design

แบ่ง error เป็นสองขอบเขต:

1. `item-level error`: error จากการประมวลผล ticker ปัจจุบันที่ downstream
   ระบุว่าเป็น `scope: item` และมี stable item error code. ใช้ flow เดียวกับ
   item blocker:
   child card ชื่อ `[BLOCKED][ETF] <TICKER> | check-etf-performance`,
   metadata ครบพร้อม `reason`, ย้าย child ไป `Blocked`, check เฉพาะ queue item
   หลัง child mutation สำเร็จ, เพิ่ม ticker ใน attempted set และ continue.
   Child เป็น `terminal: false` เพื่อให้ retry ได้.

2. `global error`: Trello/tool/auth, board/list, configuration/input,
   checklist, claim, หรือ exception-card mutation error; รวมถึง downstream
   handoff ที่ยัง `scope: global|unknown` หรือไม่มี envelope ที่ยืนยัน ticker
   ได้. กรณีนี้ไม่สร้าง child, ไม่ check queue item, block parent และหยุด.

`research-sub-agent-unavailable` ที่เกิดภายใน single-ticker downstream run
จะถูกส่งกลับเป็น `ERROR` + `scope: item` พร้อม reason ของ tickerนั้น เพื่อให้
batch ไปต่อได้. ถ้าเกิดจาก coordinator/runtime ที่ไม่สามารถผูกกับ tickerหรือ
ไม่สามารถควบคุม Trello ได้ ให้คงเป็น global.

## State and retry

- Item-level error child ใช้ `confirmation: none`, `terminal: false`, และ
  `retry: move parent to Ready for AI`.
- หลัง child update และ move สำเร็จ queue item ถูก check และนับเป็น handled.
- เมื่อ batch capacity หมดและยังมี normal work parent กลับ `Ready for AI`;
  retryable child จะไม่ทำให้ global batch ค้าง.
- เมื่อไม่มี normal work เหลือ parent จัดลำดับ open retryable children ตาม
  กติกาเดิม.
- ความล้มเหลวของการสร้าง/แก้/ย้าย child เป็น global เพราะ coordinator ไม่อาจ
  รับประกัน invariant ว่า checklist สะท้อน child ได้.

## Handoff envelope

เพิ่ม accepted mapping สำหรับ:

```text
status: ERROR
scope: item
durable_write: not_completed
exhausted: false
confirmation: none
code: research-sub-agent-unavailable | item-downstream-error
reason: <concise ticker-specific reason>
```

`ERROR` + `scope: global|unknown`, missing fields, contradictory fields, or
unknown codes ยังคงเป็น global.

## Verification

- เพิ่ม contract test ที่ fail ก่อนแก้ เพื่อบังคับให้เอกสารระบุ accepted
  item-level ERROR, child/check/continue order, และ global mutation failures.
- รัน static contract tests ทั้งหมด.
- ตรวจ automation prompt ที่ deploy จริงให้ตรงกับ skill.
- ไม่ทดสอบด้วยการสร้าง/แก้ Trello จริงในงานเอกสารนี้.
