---
kind: etf-price-cache
competition_id: us-etf-competition-2026
source_policy: browser-direct-web
cache_role: preliminary-screen-only
updated_at: "2026-09-03T08:15:41Z"
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
| SPY | NYSEARCA:SPY | 765.16 | USD | completed-session adjusted close | 2026-09-02T16:00:00-04:00 | 2026-09-03T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/spy/history/ | [quote](2026-09-03/quote_SPY_20260903T080324Z_run-20260903-040324.json) | run-2026-09-03-040324-et | VERIFIED_COMPLETED_SESSION_CLOSE |
| VOO | NYSEARCA:VOO | 703.41 | USD | completed-session close | 2026-09-02T16:00:00-04:00 | 2026-09-03T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/voo/history/ | [quote](2026-09-03/quote_VOO_20260903T080324Z_run-20260903-040324.json) | run-2026-09-03-040324-et | WITHIN_1_TRADING_DAY_PRELIMINARY |
| DGRO | NYSEARCA:DGRO | 79.17 | USD | completed-session close | 2026-09-02T16:00:00-04:00 | 2026-09-03T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/dgro/history/ | [quote](2026-09-03/quote_DGRO_20260903T080324Z_run-20260903-040324.json) | run-2026-09-03-040324-et | WITHIN_1_TRADING_DAY_PRELIMINARY |
| VEA | NYSEARCA:VEA | 72.59 | USD | completed-session close | 2026-09-02T16:00:00-04:00 | 2026-09-03T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/vea/history/ | [quote](2026-09-03/quote_VEA_20260903T080324Z_run-20260903-040324.json) | run-2026-09-03-040324-et | WITHIN_1_TRADING_DAY_PRELIMINARY |
| VIGI | NASDAQ:VIGI | 98.20 | USD | completed-session close | 2026-09-02T16:00:00-04:00 | 2026-09-03T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/vigi/history/ | [quote](2026-09-03/quote_VIGI_20260903T080324Z_run-20260903-040324.json) | run-2026-09-03-040324-et | WITHIN_1_TRADING_DAY_PRELIMINARY |
| SCHC | NYSEARCA:SCHC | 50.75 | USD | completed-session close | 2026-09-02T16:00:00-04:00 | 2026-09-03T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/schc/history/ | [quote](2026-09-03/quote_SCHC_20260903T080324Z_run-20260903-040324.json) | run-2026-09-03-040324-et | WITHIN_1_TRADING_DAY_PRELIMINARY |
| DMXF | NASDAQ:DMXF | 85.65 | USD | latest visible completed-session close; Sep 2 close missing | 2026-09-01T16:00:00-04:00 | 2026-09-03T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/dmxf/history/ | [quote](2026-09-03/quote_DMXF_20260903T080324Z_run-20260903-040324.json) | run-2026-09-03-040324-et | WITHIN_1_TRADING_DAY_PRELIMINARY_LIQUIDITY_FAIL |
| SCHA | NYSEARCA:SCHA | 34.04 | USD | completed-session close | 2026-09-02T16:00:00-04:00 | 2026-09-03T08:15:41Z | StockAnalysis.com | https://stockanalysis.com/etf/scha/history/ | [quote](2026-09-03/quote_SCHA_20260903T080324Z_run-20260903-040324.json) | run-2026-09-03-040324-et | WITHIN_1_TRADING_DAY_PRELIMINARY |

ราคาข้างต้นเป็น verified browser observations จากรอบนี้ โดยใช้ completed-session
close ของ 2 กันยายน 2026 เป็น decision reference สำหรับทุก ticker ที่มีแถวปิด
ครบ; ไม่ใช้ pre-market หรือ after-hours. DMXF มีเพียงแถวปิดล่าสุด 1 กันยายนบนหน้า
ประวัติ และจึงถูกเก็บเป็น preliminary พร้อม liquidity failure. Cache นี้ยังไม่ใช่
การยืนยัน admission หรือ reference price สุดท้ายสำหรับ BUY/SELL.
