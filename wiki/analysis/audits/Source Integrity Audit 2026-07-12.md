---
type: analysis
analysis_type: source-integrity-audit
date: 2026-07-12
scope: weekly-vault-linking-and-cleanup
source_files:
  - index.md
  - log.md
  - wiki/analysis/
  - wiki/entities/
tags:
  - analysis/source-integrity-audit
  - maintenance/queryability
  - duplicate-review
---

# Source Integrity Audit - 2026-07-12

## Scope

ตรวจ Markdown graph ทั้ง vault จำนวน 264 ไฟล์ โดยลงรายละเอียด 97 ไฟล์ใน `wiki/analysis/` และ entity hubs ใน `wiki/entities/`. ตรวจ direct entity links ของ ticker-specific decisions, valuations, และ earnings; broken wikilinks; orphan notes; exact duplicate content; กลุ่ม US covered-equity decision refresh; และกลุ่ม Dividend ETF analysis. ไม่ได้แก้ financial facts, valuation calculations, charts, JSON, raw sources, หรือ fundamentals.

## High Severity Findings

ไม่พบ High severity issue และไม่ได้พบ unsupported number, conflicting number, หรือ chart/table mismatch ใหม่ในขอบเขต linking/cleanup นี้.

## Medium Severity Findings

| Finding | Evidence | Fix / Decision |
|---|---|---|
| Analysis notes ไม่มี incoming wikilink 9 ไฟล์ | Graph baseline พบ audit 2, comparison 2, decision refresh 3, และ UNH analysis 2 ไฟล์เป็น orphan | เพิ่ม links จาก owner index (`audits/README.md`, `comparisons/README.md`, `decisions/README.md`) และเปลี่ยน confirmed UNH report paths ใน `wiki/entities/UNH.md` เป็น wikilinks. หลังแก้เหลือ 0 orphan ใน non-README analysis scope. |
| กลุ่ม US covered-equity refresh มีบทบาทคล้ายกัน 3 ไฟล์ | `2026-06-25`, `2026-06-28`, และ `2026-07-03` เป็น dated market-price snapshots | ไม่ลบ: แต่ละไฟล์มีราคา, source note, และ decision context เฉพาะวันที่; การลบจะทำให้ evidence chain ขาด. เก็บ `2026-07-03` เป็น latest แต่รักษา history ทั้งสามไฟล์. |
| กลุ่ม Dividend ETF analysis มีเนื้อหาทับซ้อนเชิงหัวข้อ | `Dividend ETF Triage`, `Full Universe Triage`, `Overlap Groups`, และ `Top 10 Holdings Tracker` | ไม่ลบ: แต่ละไฟล์มีบทบาทต่างกัน และมี incoming links สำคัญจาก ETF entities; tracker เป็น holdings workflow ล่าสุด ส่วน overlap memo เป็น fallback grouping. |

## Low Severity Findings

| Finding | Evidence | Follow-Up |
|---|---|---|
| ชื่อ basename `README.md` ซ้ำตามโครงสร้างหลายโฟลเดอร์ | พบ README หลายไฟล์ แต่ไม่พบ exact duplicate hash และไม่มี confirmed broken `[[README]]` link | ใช้ folder-qualified path หรือชื่อ note เฉพาะเมื่อลิงก์ข้ามโฟลเดอร์; ยังไม่ rename เพราะบทบาทเป็น local folder guide. |
| ตัวตรวจพบ `[[TICKER]]` ใน audit เดิม | อยู่ในข้อความอธิบาย placeholder ของ `Source Integrity Audit 2026-07-11.md` | ไม่แก้: ไม่ใช่ intended vault link และไม่ใช่ broken entity reference จริง. |

## Link And Duplicate Checks

- Ticker-specific decisions, valuations, และ earnings ที่มี entity hub: direct `[[TICKER]]` link ครบ; missing 0.
- Confirmed broken wikilinks ใน analysis scope: 0 หลังแยก placeholder `[[TICKER]]` ออกจาก intended links.
- Non-README analysis orphan notes: 9 ก่อนแก้, 0 หลังแก้.
- Exact duplicate Markdown files ใน `wiki/analysis/`: 0 จาก SHA-1 content check.
- ไม่มีไฟล์ถูกลบในรอบนี้ เพราะ candidate ทุกกลุ่มมี dated source evidence, บทบาทเฉพาะ, incoming links, หรือยังยืนยันความซ้ำแบบ lossless ไม่ได้.

## Files Not Deleted

- `wiki/analysis/decisions/US Covered Equities Decision Refresh 2026-06-25.md`
- `wiki/analysis/decisions/US Covered Equities Decision Refresh 2026-06-28.md`
- `wiki/analysis/decisions/US Covered Equities Decision Refresh 2026-07-03.md`
- `wiki/analysis/comparisons/Dividend ETF Triage 2026-06-28.md`
- `wiki/analysis/comparisons/Dividend ETF Full Universe Triage 2026-06-28.md`
- `wiki/analysis/comparisons/Dividend ETF Overlap Groups 2026-06-28.md`
- `wiki/analysis/comparisons/Dividend ETF Top 10 Holdings Tracker 2026-07-01.md`

## Follow-Up

รอบถัดไปให้ตรวจเฉพาะไฟล์ใหม่หลัง 2026-07-12 ก่อน แล้ว rerun graph checker. จะพิจารณาลบ dated refresh ได้ต่อเมื่อมี canonical history note ที่รักษาราคา, source note, decision delta, incoming links, และ unresolved risks ครบถ้วน.
