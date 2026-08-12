# Trello ETF Batch Lane-Only State Design

## Goal

ลด parent state ของ `trello-etf-batch` ให้ใช้ Trello lane เป็น source of truth
เพียงอย่างเดียว และเลิกพึ่ง `trello-etf-batch-status` ใน card description.

## State model

Parent card มี state ตาม lane เท่านั้น:

- `Ready for AI`: eligible และยังไม่มี worker ทำอยู่
- `In Progress`: มี worker ทำอยู่; invocation อื่นต้องไม่อ่านเพื่อ process,
  claim ซ้ำ, reset, หรือ mutate card
- `Blocked`: มี global blocker หรือเหลือเฉพาะ terminal/unconfirmed item
  exceptions; retry ได้เมื่อผู้ใช้ย้าย parent กลับ `Ready for AI`
- `Done`: queue เสร็จและไม่มี open exception

Workflow จะไม่อ่าน, validate, เขียน, หรือใช้
`<!-- trello-etf-batch-status ... -->` เพื่อกำหนด eligibility, ownership,
retry, failure, หรือ completion. Block เดิมที่มีอยู่จะถูก preserve เป็น legacy
text และไม่ถูกลบอัตโนมัติ เพื่อไม่เพิ่ม description mutation หรือ failure
surface.

## Claim and concurrency

Claim parent โดยอ่าน exact card ใน `Ready for AI`, ย้ายไป `In Progress`, แล้ว
อ่าน exact card ซ้ำเพื่อยืนยันว่าอยู่ `In Progress`. ถ้าการ์ดไม่อยู่
`In Progress` หลัง move ให้หยุดโดยไม่ mutate เพิ่ม.

ไม่มี `claim_token` และไม่มี exactly-once distributed lock. Safety จึงอาศัย
กติกา operational ต่อไปนี้:

1. Scheduler เลือกเฉพาะ open parent ใน `Ready for AI`.
2. Scheduler เลือกได้หนึ่ง parent ต่อ run และห้ามสร้าง overlapping worker สำหรับ
   parent เดียวกัน.
3. Invocation ที่เห็น parent ใน `In Progress` ต้องคืน `batch already claimed`
   และห้ามแตะ card.
4. ถ้า worker หาย ผู้ใช้เป็นผู้ยืนยันว่าไม่มี agent ทำอยู่และย้าย card กลับ
   `Ready for AI`; workflow ไม่ auto-recover `In Progress`.

## Queue and retry derivation

`ETF queue` checklist ยังคงเป็น progress source of truth. Open exception cards
ยังเป็น source of truth ของ item blockers. ไม่ใช้ `retry_pending` flag อีกต่อไป.

ในแต่ละ selection pass ให้ derive state จาก checklist และ exception cards:

- `normal_pending`: unchecked ticker ที่ไม่มี open exception
- `retry_pending`: checked ticker ที่มี open non-terminal exception และไม่มี
  unconfirmed confirmation
- `confirmation_pending`: checked ticker ที่มี open exception ซึ่งยังต้องการ
  confirmation
- `terminal_pending`: checked ticker ที่มี open terminal exception

เลือก normal work ตาม source order ก่อน แล้วเลือก eligible retry ตาม source
order เมื่อไม่มี normal work เหลือ. `attempted_this_run` ยังป้องกัน ticker เดิม
ถูกเลือกซ้ำใน invocation เดียว.

## Transitions

- Claim: move parent `Ready for AI → In Progress`; ไม่แก้ description.
- Item success: check matching queue item หลัง downstream durable write สำเร็จ;
  ปิด matching exception หากเป็น retry.
- Item blocker: update/create child, move child ไป `Blocked`, แล้วจึง check
  matching queue item; parent คงอยู่ `In Progress` ขณะ batch ยังทำต่อ.
- Global failure หลัง claim: ไม่สร้าง ticker child, ไม่ check affected item,
  และ move parent `In Progress → Blocked`.
- Capacity exhausted พร้อม normal/retry work ที่ยังทำต่อได้: move parent
  `In Progress → Ready for AI`.
- Queue complete และไม่มี open exception: move parent `In Progress → Done`
  และ mark complete.
- เหลือเฉพาะ terminal หรือ unconfirmed-confirmation exceptions: move parent
  `In Progress → Blocked`.

Failure code ของ global stop แสดงใน run result และ automation memory; จะไม่เขียน
กลับลง parent description. Item-level reason ยังคงอยู่ใน exception child card.

## Automation selection

Scheduled dispatcher ตรวจเฉพาะ open cards ใน `Ready for AI` ของ board ที่กำหนด
และเลือก oldest eligible parent จาก configuration fields เท่านั้น. ไม่อ่านหรือ
เปรียบเทียบ status block. Cards ใน `In Progress`, `Blocked`, `Done`, หรือ lane
อื่นไม่ eligible โดยไม่คำนึงถึง description.

## Migration

ไม่ทำ bulk cleanup และไม่ rewrite card description. Legacy status blocks อาจ
ค้างอยู่ได้แต่ไม่มี semantic effect. Configuration fields เช่น `workflow`,
`input`, `mode`, `run_mode`, `batch_size`, และ optional board/list overrides
ยังคงถูก validate ตามเดิม.

## Verification

1. เพิ่ม contract test ให้ fail ก่อน implementation โดยบังคับว่า skill และ
   automation prompt ใช้ lane-only state, ไม่อ้าง `claim_token`,
   `retry_pending`, list/status agreement, หรือ status-block mutations.
2. แก้ `SKILL.md` และ `automation-prompt.md` ให้ผ่าน test โดยคง queue,
   item/global routing, batch-size, และ exception-card invariants เดิม.
3. รัน contract tests ทั้งหมด, skill validator, `git diff --check`, และตรวจ
   scoped git status.
4. Sync scheduled automation prompt โดย preserve schedule/status เดิม และ read
   back เพื่อยืนยัน contract.

## Out of scope

- ไม่เปลี่ยน downstream `check-etf-performance` หรือ source-verifier workflow
- ไม่ลบ legacy status blocks จาก Trello cards
- ไม่เพิ่ม comments, labels, หรือชื่อ card เพื่อเก็บ global failure metadata
- ไม่รับประกัน concurrent exactly-once claim หากมีหลาย dispatcher แข่งขันกัน
