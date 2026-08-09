---
type: source-integrity-audit
scope: vault linking, backlinks, duplicates, US entry refresh, ETF analysis
audited_on: 2026-08-09
---

# Source Integrity Audit 2026-08-09

## Scope

ตรวจ Obsidian graph จาก `index.md`, `log.md`, `wiki/analysis/`,
`wiki/entities/` และลิงก์ที่เกี่ยวข้องทั้งหมดใน vault. Inventory ก่อนเพิ่ม audit
memo และ fixes รอบนี้มี
Markdown `441` ไฟล์, analysis notes `271` ไฟล์ และ entity hubs `42` ไฟล์.
ตรวจ wikilinks `3,378` รายการ, incoming links, ticker-to-entity edges,
orphan notes, duplicate basenames, exact duplicate content และกลุ่ม US entry
refresh / Dividend ETF analysis.

## Findings by Severity

### High

ไม่พบ High finding. ไม่พบ unsupported number, valuation conflict, chart/table
mismatch หรือ source integrity issue ที่ต้องหยุดการใช้งาน vault.

### Medium

| Finding | Evidence | Action |
|---|---|---|
| Stale KPHO link ใน workflow log | `log.md:11` เดิมชี้ไป `[[ETF_NYSE_ARCA_KPHO Performance]]` ซึ่งถูกแทนด้วย `wiki/analysis/performance/ETF_NYSE_KPHO Performance.md` | แก้เป็น canonical link ที่ยืนยันจาก `ETF Performance Index`, Vietnam ETF และ source batch แล้ว |
| Existing ETF entity hubs ขาด backlink จาก performance owner | `wiki/analysis/performance/ETF_AMEX_DGRO Performance.md`, `ETF_AMEX_DIVI Performance.md`, `ETF_AMEX_VIG Performance.md`, `ETF_NASDAQ_VIGI Performance.md` | เพิ่ม `Entity` edge ไปยัง hub ที่มีอยู่จริงทั้ง 4 หน้า |
| Performance pages 139 ไฟล์ยังไม่มี entity hub คู่กัน | `wiki/analysis/performance/ETF_* Performance.md`; `wiki/entities/ETF Index.md` ระบุว่า comparison universe ไม่จำเป็นต้องมี entity page จนกว่าจะมี allocation/watchlist/research workflow | ไม่สร้าง hub แบบกวาด; บันทึกเป็น documented gap และรอการยกระดับ ticker แบบมีข้อมูล/บทบาทรองรับ |

### Low

| Finding | Evidence | Follow-up |
|---|---|---|
| Intentional redirect ไม่มี incoming link | `wiki/analysis/performance/ETF Performance Regime Matrix.md` มี `redirect_to: ETF Performance Index` และลิงก์ปลายทางถูกต้อง | คงไว้เพื่อ backward compatibility; ไม่ลบ redirect |
| Duplicate basename เป็น local README เท่านั้น | พบ `README.md` ซ้ำตามโฟลเดอร์; ไม่พบ duplicate basename อื่น | ไม่ rename เพราะแต่ละไฟล์เป็น folder guide คนละบทบาท |
| Exact duplicate content | ไม่พบ exact duplicate group ใน non-README Markdown | ไม่ลบไฟล์ |

## Graph Checks

- Ticker-specific company decisions `40`, valuations `38` และ earnings `1` ที่มี
  entity hub มี direct entity link ครบ.
- Performance pages ที่มี existing entity hub มี `4` หน้า และแก้ครบ; อีก `139`
  หน้าไม่มี endpoint ใน `wiki/entities/` จึงไม่ถือเป็น broken link.
- หลังแยก template/example placeholders (`AGENTS.md`, audit เก่า และ reference
  templates) ไม่เหลือ confirmed broken wikilink ใน analysis graph.
- Analysis non-README orphan มี `1` หน้า คือ redirect matrix ตามรายการ Low;
  entity hubs ทั้ง `42` มี incoming link.
- ไม่มี exact duplicate content และไม่มีชื่อไฟล์ซ้ำที่เป็น durable note.

## Duplicate Review

### US entry refresh group

ตรวจไฟล์ต่อไปนี้:

- `wiki/analysis/decisions/US Covered Equities Decision Refresh 2026-06-25.md`
- `wiki/analysis/decisions/US Covered Equities Decision Refresh 2026-06-28.md`
- `wiki/analysis/decisions/US Covered Equities Decision Refresh 2026-07-03.md`

เก็บทั้งสามไฟล์ โดย `2026-07-03` เป็น latest note แต่แต่ละไฟล์มี dated quote
snapshot, source note และ decision context ของวันนั้นต่างกัน. การลบไฟล์เก่าจะ
ทำให้ historical evidence และ unresolved risk context หาย จึงไม่มีไฟล์ที่ลบ.

### ETF analysis group

ตรวจไฟล์ต่อไปนี้:

- `wiki/analysis/comparisons/Dividend ETF Triage 2026-06-28.md`
- `wiki/analysis/comparisons/Dividend ETF Full Universe Triage 2026-06-28.md`
- `wiki/analysis/comparisons/Dividend ETF Overlap Groups 2026-06-28.md`
- `wiki/analysis/comparisons/Dividend ETF Top 10 Holdings Tracker 2026-07-01.md`

ไม่ลบ: Triage คือ quick shortlist, Full Universe คือ 100-row scoring,
Overlap Groups คือ portfolio-role grouping และ Top 10 Holdings Tracker คือ
ล่าสุดด้าน holdings verification. ทุกไฟล์มี incoming links หรือ source/role
เฉพาะ และไม่ใช่เนื้อหาซ้ำแบบ lossless.

## Fixes And Deletion Record

- แก้ `log.md` และเพิ่ม entity backlinks ใน performance owners 4 หน้า.
- เพิ่มไฟล์ audit นี้และ workflow bullet หนึ่งรายการใน `log.md`.
- ลบ `0` ไฟล์. ไม่แตะ `raw/imports/`, `raw/financials/`, `raw/funds/`, entity
  hubs, source notes, fundamentals, หรือ dated latest notes.

## Follow-up

รอบถัดไปให้ตรวจไฟล์ที่เพิ่มหลัง 2026-08-09 ก่อน และทบทวนการยกระดับ ETF จาก
comparison universe เป็น entity เฉพาะเมื่อมี source-backed allocation,
watchlist หรือ research workflow; อย่าสร้าง entity hub จาก ticker เพียงอย่างเดียว.
