---
type: source-integrity-audit
scope: empty graph nodes in ETF performance and index-linked vault files
audited_on: 2026-08-27
---

# Source Integrity Audit 2026-08-27

## Scope

ตรวจ `wiki/analysis/performance/`, [[ETF Index]], [[ETF Performance Index]] และ
ไฟล์ Markdown อื่นใน vault เพื่อหา node ที่เป็นไฟล์ศูนย์ไบต์, whitespace-only หรือ
มีเฉพาะ frontmatter โดยอ่าน `index.md` และ `log.md` เป็นบริบทก่อนแก้ไข.

## Findings by Severity

### High

ไม่พบ High finding.

### Medium

พบไฟล์ Markdown ศูนย์ไบต์ที่ถูก track อยู่ 3 ไฟล์ใน root ของ vault:

- `AVDV.md`
- `AVUV.md`
- `DFAS.md`

ไฟล์เหล่านี้ถูกอ้างถึงจาก `log.md:86-88` เป็น ticker-only wikilinks และสร้าง blank
graph nodes แม้ปัจจุบันมี canonical performance pages ของทั้งสามกองแล้ว.

### Low

ไม่พบไฟล์ว่าง, whitespace-only หรือ frontmatter-only ใน
`wiki/analysis/performance/` ซึ่งมี Markdown `260` ไฟล์ หรือใน
`wiki/entities/ETF Index.md`. การ scan ทั้ง vault ไม่พบ zero-byte file อื่นหลังแก้ไข.

## Fixes And Deletion Record

- ลบ `AVDV.md`, `AVUV.md` และ `DFAS.md` ซึ่งไม่มีเนื้อหาและไม่มีข้อมูลให้ preserve.
- เปลี่ยนลิงก์เก่าใน `log.md:86-88` เป็น
  `[[ETF_NYSE_ARCA_AVUV Performance]]`, `[[ETF_CBOE_BZX_DFAS Performance]]`
  และ `[[ETF_NYSE_ARCA_AVDV Performance]]`; คงข้อความ historical finding เดิม
  และระบุว่า “at that time”.
- ตรวจ `git diff --check` ผ่าน และยืนยันว่า canonical performance pages ทั้งสาม
  มีอยู่จริงและไม่เปล่า.

## Follow-up

หาก workflow ถูก block เพราะ ticker ยังไม่มี artifact ให้ใช้ inline code เช่น
`TICKER` แทน ticker-only wikilink จนกว่าจะมี owner page ที่ยืนยันแล้ว เพื่อไม่ให้
เกิด unresolved blank node ใน Obsidian graph.
