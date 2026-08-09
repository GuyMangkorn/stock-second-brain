# Source Verifier Sub-Agent Design

## Goal

เพิ่ม project-scoped Codex sub-agent สำหรับตรวจความถูกต้องของข้อมูลก่อนเขียน
ไฟล์ถาวรใน stock-second-brain โดยให้ agent ค้นหาแหล่งข้อมูลเพิ่มเติม,
เปรียบเทียบ definitions และ source dates, แล้วส่ง verdict กลับให้ main agent
เป็นผู้ตัดสินใจเรื่องการแก้ไขและการบันทึก

## Scope

- ตรวจทุก workflow ที่กำลังจะเขียน durable project files
- ตรวจตัวเลข, period, unit, currency, metric definition, as-of date,
  calculation, source provenance และ source conflicts
- ใช้แหล่งทางการก่อน และค้นหา source อิสระเพิ่มเติมเมื่อ claim มีสาระสำคัญ
  หรือมีข้อขัดแย้ง
- reviewer ทำงานแบบ read-only และห้ามเขียน vault files
- main agent เป็นผู้เขียนไฟล์ถาวรเพียงรายเดียว
- read-only `chat` ที่ไม่มีการ save ไม่ต้องผ่าน pre-save gate

## Architecture

สร้าง `.codex/agents/source-verifier.toml` เป็น custom agent แบบ read-only
และเพิ่ม pre-save protocol ใน `AGENTS.md` เพื่อให้ main agent ทำตามลำดับนี้:

```text
draft candidate output
  -> prepare evidence packet
  -> dispatch source_verifier sub-agent
  -> receive structured verdict
  -> PASS: save
     CHANGES_REQUIRED: correct and review again
     WARNING: ask user confirmation, then save if confirmed
```

Codex custom-agent files เป็น TOML ที่มี `name`, `description` และ
`developer_instructions` ตาม [official OpenAI documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents)
ส่วน `AGENTS.md` เป็น project-level trigger ที่บอก main agent ให้ dispatch
reviewer ก่อน durable write

## Reviewer Contract

### Input

Main agent ส่ง evidence packet ที่มี:

- scope และรายการไฟล์ที่จะเขียนหรือแก้
- candidate values พร้อม period, unit, currency, metric definition และ as-of date
- source URLs, local paths, filing references และ shown calculations
- source hierarchy ที่ใช้และข้อขัดแย้งที่พบแล้ว
- proposed output และ planned durable file contents ที่ reviewer ต้องตรวจ

### Review Method

1. ตรวจ source-to-claim mapping และความสดของข้อมูล
2. เปรียบเทียบ source หลักกับ source ที่สองเมื่อมีแหล่งที่เหมาะสม
3. แยกความต่างที่เกิดจาก period, definition, currency, unit, share class,
   benchmark, NAV/price basis หรือ as-of date ก่อนจัดเป็น conflict
4. ห้ามเฉลี่ยหรือเลือกค่าที่ต่างกันโดยไม่อธิบายเหตุผล
5. ถ้ายืนยันไม่ได้ ให้เสนอ `ไม่พบข้อมูลที่ยืนยันได้` หรือ `not disclosed`
   แทนการเติมค่า
6. ตรวจ calculations, denominator, rounding และ internal consistency
7. ตรวจ ownership ของ source note, fundamentals, fund facts, entity,
   valuation และ decision gap ให้ตรงกับ `AGENTS.md`

### Output

Reviewer ส่งกลับเป็น structured report:

```markdown
## Review verdict
- Status: `PASS` | `CHANGES_REQUIRED` | `WARNING`
- Highest severity: `High` | `Medium` | `Low` | `None`

| Severity | Location | Finding | Required correction | Evidence |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Source comparison
| Claim | Source 1 | Source 2 | Reconciliation |
|---|---|---|---|
| ... | ... | ... | ... |

## Save recommendation
...
```

`CHANGES_REQUIRED` ใช้เมื่อมี `High` หรือ `Medium`; main agent ต้องแก้และ
ส่ง review ใหม่ก่อนเขียนไฟล์ `WARNING` ใช้เมื่อเหลือเฉพาะ `Low`; main agent
ต้องหยุดและขอ user confirmation ก่อน save โดยควรบันทึก warning หรือ gap
ไว้ใน artifact ที่เป็นเจ้าของข้อมูลด้วย

## Failure Handling

- reviewer unavailable: main agent ทำ checklist เดียวกัน locally, เปิดเผย
  fallback และห้ามข้าม `High/Medium`
- source conflict unresolved: preserve both observations, explain source-quality
  choice, and use `ไม่พบข้อมูลที่ยืนยันได้` / `not disclosed` when needed
- reviewer must not mutate evidence, candidate files, or vault indexes
- if a correction changes a flagged claim or structure, repeat the reviewer
  before saving

## Acceptance Criteria

- มี custom agent file ที่ Codex โหลดได้และกำหนด read-only behavior
- `AGENTS.md` กำหนด pre-save dispatch, verdict handling และ single-writer rule
- agent instruction บังคับให้ compare source และระบุ source/as-of dates
- `High/Medium` ไม่สามารถผ่าน save gate ได้จนกว่าจะ review ใหม่
- `Low` ทำให้เกิด user confirmation ก่อน save
- TOML parse ได้, paths/reference links ถูกต้อง และ git diff ไม่มีไฟล์นอก scope
