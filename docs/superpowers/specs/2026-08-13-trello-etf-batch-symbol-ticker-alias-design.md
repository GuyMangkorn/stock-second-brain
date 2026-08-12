# Trello ETF Batch Symbol/Ticker Alias Design

## Goal

ทำให้ `trello-etf-batch` รับ Markdown table ที่ใช้หัวคอลัมน์ `Symbol` หรือ
`Ticker` ได้ เพราะทั้งสองชื่อหมายถึง ticker symbol เดียวกันใน queue นี้

## Input resolution

- ตรวจชื่อหัวคอลัมน์แบบไม่สนตัวพิมพ์เล็ก/ใหญ่
- ต้องพบ `Symbol` หรือ `Ticker` เพียงหนึ่งชื่อเท่านั้น
- หากพบทั้งสองชื่อ หรือไม่พบทั้งคู่ ให้หยุดเป็น `input-malformed`
- หลังเลือกคอลัมน์แล้ว คงกฎเดิม: trim whitespace/backticks, normalize เป็น
  uppercase, รักษาลำดับต้นฉบับ และ deduplicate โดยเก็บ occurrence แรก

## Compatibility

ลำดับ canonical symbols, `ETF queue` checklist, retry/exception semantics,
downstream handoff และ durable-output ownership ไม่เปลี่ยนแปลง การแก้ไขอยู่ที่
input-column contract และข้อความ automation ที่อธิบาย contract เท่านั้น

## Validation

อัปเดต contract assertions ที่อ้างถึง `Symbol` ให้สะท้อน alias ทั้งสองแบบ และ
ตรวจด้วยไฟล์ตัวอย่างที่ใช้ `Ticker` รวมถึงกรณีไม่มีคอลัมน์และมีทั้งสองคอลัมน์
ให้ยังถูกจัดเป็น global input failure
