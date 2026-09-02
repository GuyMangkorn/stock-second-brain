---
kind: etf-price-cache
competition_id: us-etf-competition-2026
source_policy: browser-direct-web
cache_role: preliminary-screen-only
updated_at: "not populated"
---

# Latest Verified ETF Price Cache

อ่านไฟล์นี้ก่อนค้นหาราคาใหม่ทุกครั้ง เพื่อใช้ราคาที่เคยยืนยันแล้วเป็นข้อมูล
ตั้งต้นในการคัดกรอง. ราคาที่อยู่ใน cache ไม่ใช่ราคาปัจจุบันโดยอัตโนมัติและไม่ใช่
แหล่งบัญชีของ ledger; ก่อนตัดสินใจต้องตรวจ freshness ตาม `config.yaml` และ refresh
เฉพาะ Ticker ที่มีผลต่อการตัดสินใจ.

ตารางนี้เป็น derived convenience view ของประวัติใน
[`price-log.md`](price-log.md). ทุกครั้งที่ได้ราคาใหม่จากหน้าเว็บโดยตรง ให้เพิ่ม
observation ลง `price-log.md` แล้วปรับแถวล่าสุดของ Ticker นี้. ห้ามใช้ search-result
snippet เป็นหลักฐานราคา.

| Ticker | Exchange-qualified identity | Price | Currency | Price basis | Source as-of | Retrieved at | Source | Direct URL | Evidence | Run ID | Status |
|---|---|---:|---|---|---|---|---|---|---|---|---|

ยังไม่มี verified browser price observation ในพอร์ตนี้.
