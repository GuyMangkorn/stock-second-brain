# Restrict `source_verifier` to ETF Performance Design

## Goal

ให้ project เรียกใช้ `source_verifier` เฉพาะ workflow ที่ใช้ skill
`check-etf-performance` และให้ agent ปฏิเสธ evidence packet ที่อยู่นอก ETF
performance review อย่างชัดเจน

## Root Cause

`AGENTS.md` กำหนด pre-save verification gate สำหรับ durable file ทุกประเภท
ขณะที่ `.codex/agents/source-verifier.toml` อธิบายบทบาทกว้างเป็น reviewer ของ
stock-second-brain โดยรวม จึงถูกนำไปใช้กับ ETF, valuation, thesis, decision,
market-move, sentiment และ audit workflows ได้

## Design

1. ปรับ `AGENTS.md` ให้ pre-save gate ของ `source_verifier` มีผลเฉพาะ
   `check-etf-performance` ที่เป็น research-bearing และกำลังจะเขียน durable
   performance outputs
2. ปรับ `.codex/agents/source-verifier.toml` ให้เป็น independent read-only
   reviewer สำหรับ ETF performance เท่านั้น โดยกำหนดว่า:
   - ตรวจเฉพาะ NAV/price total return, benchmark, calendar-year returns,
     CAGR, drawdown, recovery, distributions, expense ratio, exchange/entity
     identity และ as-of dates ของ ETF performance
   - รับเฉพาะ evidence packet ที่มาจาก `check-etf-performance`
   - ปฏิเสธหรือคืน `CHANGES_REQUIRED` เมื่อ packet เป็น stock financials,
     ETF fund facts/holdings/methodology ที่ไม่มี performance scope, DCF,
     thesis, decision, market move, sentiment หรือ source-integrity audit
   - ยังคง read-only และห้ามเขียนไฟล์ใด ๆ
3. ไม่แก้ skills หรือ workflow อื่นที่ไม่ได้เป็นตัวเรียก
   `check-etf-performance`

## Data Flow

`check-etf-performance` research/reconciliation → complete ETF performance
evidence packet → `source_verifier` review → `PASS` permits performance
durable writes; `CHANGES_REQUIRED` blocks them.

งานอื่นใน project → ไม่ dispatch `source_verifier`

## Acceptance Criteria

- ค้นใน `AGENTS.md` แล้วไม่เหลือข้อกำหนดให้ dispatch
  `source_verifier` สำหรับ durable file ทุกประเภท
- คำอธิบายและ instructions ของ agent ระบุ `check-etf-performance` เป็น
  เงื่อนไขการใช้งานอย่างชัดเจน
- งาน valuation, stock research/ingest, ETF research, decision, market-move,
  sentiment และ audit ไม่ถูกกำหนดให้ใช้ agent นี้
- ไฟล์ TOML parse ได้, diff ไม่มี whitespace error และมีการตรวจ reference
  ที่เหลือทั้งหมด

## Non-goals

- ไม่เปลี่ยน calculation rules หรือ source priority ของ ETF performance
- ไม่เปลี่ยน research delegation ของ `check-etf-performance`
- ไม่ให้ `source_verifier` เขียนหรือแก้ durable files
