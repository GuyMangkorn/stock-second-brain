---
kind: etf-price-log
competition_id: us-etf-competition-2026
append_only: true
canonical_history: true
source_policy: browser-direct-web
---

# ETF Price Log

ไฟล์นี้เป็นประวัติราคาแบบ append-only สำหรับให้ Portfolio Run ในอนาคตอ่านราคา
เดิมก่อน refresh. ให้เพิ่มหนึ่งแถวต่อหนึ่ง verified observation จากหน้าเว็บจริง
โดยเก็บ `price`, `price_basis`, `source_as_of`, `retrieved_at`, `source`, URL,
หลักฐานในเครื่อง และ `run_id`. ราคาที่เก่าหรือ stale ใช้ได้เฉพาะ preliminary
screening; final decision ต้องผ่าน freshness gate ใน `config.yaml`.

| Observation ID | Run ID | Ticker | Exchange-qualified identity | Price | Currency | Price basis | Source as-of | Retrieved at | Source | Direct URL | Evidence | Status |
|---|---|---|---|---:|---|---|---|---|---|---|---|---|

ยังไม่มี verified browser price observation ในพอร์ตนี้.
