---
kind: etf-price-cache
competition_id: us-etf-competition-2026
source_policy: browser-direct-web
cache_role: preliminary-screen-only
updated_at: "2026-09-02T15:56:32Z"
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
| SPY | NYSEARCA:SPY | 765.41 | USD | intraday displayed price | 2026-09-02T11:47:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/spy/history/ | [quote](2026-09-02/quote_SPY_20260902T155632Z_d06f3175.json) | run-2026-09-02-115632-et | STALE_FOR_DECISION |
| VOO | NYSEARCA:VOO | 704.11 | USD | intraday displayed price | 2026-09-02T11:35:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/voo/ | [quote](2026-09-02/quote_VOO_20260902T155632Z_754255ff.json) | run-2026-09-02-115632-et | STALE_FOR_DECISION |
| DGRO | NYSEARCA:DGRO | 79.25 | USD | intraday displayed price | 2026-09-02T11:35:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/dgro/ | [quote](2026-09-02/quote_DGRO_20260902T155632Z_ec779fa8.json) | run-2026-09-02-115632-et | STALE_FOR_DECISION |
| VEA | NYSEARCA:VEA | 72.44 | USD | intraday displayed price | 2026-09-02T11:43:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/vea/ | [quote](2026-09-02/quote_VEA_20260902T155632Z_767116c9.json) | run-2026-09-02-115632-et | STALE_FOR_DECISION |
| VIGI | NASDAQ:VIGI | 97.95 | USD | intraday displayed price | 2026-09-02T11:09:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/vigi/ | [quote](2026-09-02/quote_VIGI_20260902T155632Z_24d95a65.json) | run-2026-09-02-115632-et | STALE_FOR_DECISION |
| SCHC | NYSEARCA:SCHC | 51.32 | USD | prior-session close displayed price | 2026-08-31T16:00:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/schc/ | [quote](2026-09-02/quote_SCHC_20260902T155632Z_c6433118.json) | run-2026-09-02-115632-et | STALE_FOR_DECISION |
| DMXF | NASDAQ:DMXF | 85.65 | USD | prior-session close displayed price | 2026-09-01T16:00:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/dmxf/ | [quote](2026-09-02/quote_DMXF_20260902T155632Z_f9318538.json) | run-2026-09-02-115632-et | STALE_FOR_DECISION |

ราคาข้างต้นเป็น verified browser observations แต่ทุก quote เกิน freshness gate
5 นาที ณ เวลา analysis จึงใช้ได้เฉพาะ preliminary screening ไม่ใช่ reference
price สำหรับ BUY/SELL.
