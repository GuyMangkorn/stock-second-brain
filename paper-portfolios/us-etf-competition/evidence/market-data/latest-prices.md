---
kind: etf-price-cache
competition_id: us-etf-competition-2026
source_policy: browser-direct-web
cache_role: preliminary-screen-only
updated_at: "2026-09-04T08:42:28Z"
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
| SPY | NYSEARCA:SPY | 773.17 | USD | completed-session adjusted close | 2026-09-03T16:00:00-04:00 | 2026-09-04T08:42:28Z | StockAnalysis.com | https://stockanalysis.com/etf/spy/history/ | [quote](2026-09-04/quote_SPY_20260904T080254Z_run-20260904-040254.json) | run-2026-09-04-040254-et | VERIFIED_COMPLETED_SESSION_CLOSE |
| VOO | NYSEARCA:VOO | 710.72 | USD | completed-session close | 2026-09-03T16:00:00-04:00 | 2026-09-04T08:42:28Z | StockAnalysis.com | https://stockanalysis.com/etf/voo/history/ | [quote](2026-09-04/quote_VOO_20260904T080254Z_run-20260904-040254.json) | run-2026-09-04-040254-et | VERIFIED_COMPLETED_SESSION_CLOSE |
| DGRO | NYSEARCA:DGRO | 79.61 | USD | completed-session close | 2026-09-03T16:00:00-04:00 | 2026-09-04T08:42:28Z | StockAnalysis.com | https://stockanalysis.com/etf/dgro/history/ | [quote](2026-09-04/quote_DGRO_20260904T080254Z_run-20260904-040254.json) | run-2026-09-04-040254-et | VERIFIED_COMPLETED_SESSION_CLOSE |
| VEA | NYSEARCA:VEA | 73.44 | USD | completed-session close | 2026-09-03T16:00:00-04:00 | 2026-09-04T08:42:28Z | StockAnalysis.com | https://stockanalysis.com/etf/vea/history/ | [quote](2026-09-04/quote_VEA_20260904T080254Z_run-20260904-040254.json) | run-2026-09-04-040254-et | VERIFIED_COMPLETED_SESSION_CLOSE |
| VIGI | NASDAQ:VIGI | 99.82 | USD | completed-session close | 2026-09-03T16:00:00-04:00 | 2026-09-04T08:42:28Z | StockAnalysis.com | https://stockanalysis.com/etf/vigi/history/ | [quote](2026-09-04/quote_VIGI_20260904T080254Z_run-20260904-040254.json) | run-2026-09-04-040254-et | VERIFIED_COMPLETED_SESSION_CLOSE |
| SCHC | NYSEARCA:SCHC | 51.48 | USD | completed-session close | 2026-09-03T16:00:00-04:00 | 2026-09-04T08:42:28Z | StockAnalysis.com | https://stockanalysis.com/etf/schc/history/ | [quote](2026-09-04/quote_SCHC_20260904T080254Z_run-20260904-040254.json) | run-2026-09-04-040254-et | VERIFIED_COMPLETED_SESSION_CLOSE |
| DMXF | NASDAQ:DMXF | 87.22 | USD | completed-session close | 2026-09-03T16:00:00-04:00 | 2026-09-04T08:42:28Z | StockAnalysis.com | https://stockanalysis.com/etf/dmxf/history/ | [quote](2026-09-04/quote_DMXF_20260904T080254Z_run-20260904-040254.json) | run-2026-09-04-040254-et | VERIFIED_COMPLETED_SESSION_CLOSE_LIQUIDITY_FAIL |
| SCHA | NYSEARCA:SCHA | 34.21 | USD | completed-session close | 2026-09-03T16:00:00-04:00 | 2026-09-04T08:42:28Z | StockAnalysis.com | https://stockanalysis.com/etf/scha/history/ | [quote](2026-09-04/quote_SCHA_20260904T080254Z_run-20260904-040254.json) | run-2026-09-04-040254-et | VERIFIED_COMPLETED_SESSION_CLOSE |

ราคาข้างต้นเป็น verified browser observations จากรอบนี้ โดยใช้ completed-session
close ของ 3 กันยายน 2026 เป็น decision reference; ไม่ใช้ pre-market หรือ
after-hours. DMXF มี completed-session close แล้ว แต่ยังถูกกันออกจาก admission
เพราะ median dollar volume ต่ำกว่าเกณฑ์. Cache นี้ยังไม่ใช่การยืนยัน admission
หรือ reference price สุดท้ายสำหรับ BUY/SELL.
