---
kind: etf-price-cache
competition_id: us-etf-competition-2026
source_policy: browser-direct-web
cache_role: preliminary-screen-only
updated_at: "2026-09-02T16:18:43Z"
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
| SPY | NYSEARCA:SPY | 765.35 | USD | intraday displayed price | 2026-09-02T12:17:00-04:00 | 2026-09-02T16:29:35Z | StockAnalysis.com | https://stockanalysis.com/etf/spy/history/ | [quote](2026-09-02/quote_SPY_20260902T161843Z_run-20260902-121843.json) | run-2026-09-02-121843-et | WITHIN_1_TRADING_DAY_PRELIMINARY |
| VOO | NYSEARCA:VOO | 703.90 | USD | intraday displayed price | 2026-09-02T12:06:00-04:00 | 2026-09-02T16:29:35Z | StockAnalysis.com | https://stockanalysis.com/etf/voo/ | [quote](2026-09-02/quote_VOO_20260902T161843Z_run-20260902-121843.json) | run-2026-09-02-121843-et | WITHIN_1_TRADING_DAY_PRELIMINARY |
| DGRO | NYSEARCA:DGRO | 79.15 | USD | intraday displayed price | 2026-09-02T12:09:00-04:00 | 2026-09-02T16:29:35Z | StockAnalysis.com | https://stockanalysis.com/etf/dgro/ | [quote](2026-09-02/quote_DGRO_20260902T161843Z_run-20260902-121843.json) | run-2026-09-02-121843-et | WITHIN_1_TRADING_DAY_PRELIMINARY |
| VEA | NYSEARCA:VEA | 72.44 | USD | intraday displayed price | 2026-09-02T11:43:00-04:00 | 2026-09-02T16:29:35Z | StockAnalysis.com | https://stockanalysis.com/etf/vea/ | [quote](2026-09-02/quote_VEA_20260902T161843Z_run-2026-09-02-121843.json) | run-2026-09-02-121843-et | WITHIN_1_TRADING_DAY_PRELIMINARY |
| VIGI | NASDAQ:VIGI | 97.95 | USD | intraday displayed price | 2026-09-02T11:09:00-04:00 | 2026-09-02T16:29:35Z | StockAnalysis.com | https://stockanalysis.com/etf/vigi/ | [quote](2026-09-02/quote_VIGI_20260902T161843Z_run-2026-09-02-121843.json) | run-2026-09-02-121843-et | WITHIN_1_TRADING_DAY_PRELIMINARY |
| SCHC | NYSEARCA:SCHC | 50.66 | USD | today's opening value displayed by issuer | 2026-09-02 | 2026-09-02T16:29:35Z | Schwab Asset Management | https://www.schwabassetmanagement.com/products/schc | [quote](2026-09-02/quote_SCHC_20260902T161843Z_run-20260902-121843.json) | run-2026-09-02-121843-et | WITHIN_1_TRADING_DAY_PRELIMINARY_TIME_NOT_DISCLOSED |
| DMXF | NASDAQ:DMXF | 85.95 | USD | intraday displayed price | 2026-09-02T10:43:00-04:00 | 2026-09-02T16:29:35Z | StockAnalysis.com | https://stockanalysis.com/etf/dmxf/history/ | [quote](2026-09-02/quote_DMXF_20260902T161843Z_run-20260902-121843.json) | run-2026-09-02-121843-et | WITHIN_1_TRADING_DAY_PRELIMINARY |

ราคาข้างต้นเป็น verified browser observations จากรอบนี้. ภายใต้ policy ปัจจุบัน
quote ของ SPY, VOO, DGRO, VEA, VIGI, SCHC และ DMXF อยู่ภายใน gate หนึ่ง US
trading day ในเชิง preliminary; SCHC ใช้ today's opening value ที่หน้า issuer
ไม่เปิดเผยเวลา. Cache นี้ยังไม่ใช่การยืนยัน admission หรือ reference price
สุดท้ายสำหรับ BUY/SELL.
