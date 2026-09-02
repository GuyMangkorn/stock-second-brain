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
| obs-20260902T155632Z-SPY-daily-20260901 | run-2026-09-02-115632-et | SPY | NYSEARCA:SPY | 761.78 | USD | adjusted close | 2026-09-01T16:00:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/spy/history/ | [daily mark](2026-09-02/daily_SPY_20260901_7af56694.json) | VERIFIED_DAILY_MARK |
| obs-20260902T155632Z-SPY-intraday | run-2026-09-02-115632-et | SPY | NYSEARCA:SPY | 765.41 | USD | intraday displayed price | 2026-09-02T11:47:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/spy/history/ | [quote](2026-09-02/quote_SPY_20260902T155632Z_d06f3175.json) | STALE_FOR_DECISION |
| obs-20260902T155632Z-VOO | run-2026-09-02-115632-et | VOO | NYSEARCA:VOO | 704.11 | USD | intraday displayed price | 2026-09-02T11:35:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/voo/ | [quote](2026-09-02/quote_VOO_20260902T155632Z_754255ff.json) | STALE_FOR_DECISION |
| obs-20260902T155632Z-DGRO | run-2026-09-02-115632-et | DGRO | NYSEARCA:DGRO | 79.25 | USD | intraday displayed price | 2026-09-02T11:35:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/dgro/ | [quote](2026-09-02/quote_DGRO_20260902T155632Z_ec779fa8.json) | STALE_FOR_DECISION |
| obs-20260902T155632Z-VEA | run-2026-09-02-115632-et | VEA | NYSEARCA:VEA | 72.44 | USD | intraday displayed price | 2026-09-02T11:43:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/vea/ | [quote](2026-09-02/quote_VEA_20260902T155632Z_767116c9.json) | STALE_FOR_DECISION |
| obs-20260902T155632Z-VIGI | run-2026-09-02-115632-et | VIGI | NASDAQ:VIGI | 97.95 | USD | intraday displayed price | 2026-09-02T11:09:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/vigi/ | [quote](2026-09-02/quote_VIGI_20260902T155632Z_24d95a65.json) | STALE_FOR_DECISION |
| obs-20260902T155632Z-SCHC | run-2026-09-02-115632-et | SCHC | NYSEARCA:SCHC | 51.32 | USD | prior-session close displayed price | 2026-08-31T16:00:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/schc/ | [quote](2026-09-02/quote_SCHC_20260902T155632Z_c6433118.json) | STALE_FOR_DECISION |
| obs-20260902T155632Z-DMXF | run-2026-09-02-115632-et | DMXF | NASDAQ:DMXF | 85.65 | USD | prior-session close displayed price | 2026-09-01T16:00:00-04:00 | 2026-09-02T15:56:32Z | StockAnalysis.com | https://stockanalysis.com/etf/dmxf/ | [quote](2026-09-02/quote_DMXF_20260902T155632Z_f9318538.json) | STALE_FOR_DECISION |

ทุก observation เก็บ direct-page timestamp แล้ว และไม่ใช่ fill. ค่า
`STALE_FOR_DECISION` ใน rows ของ run เดิมสะท้อน gate 5 นาที ณ เวลานั้น; policy
ปัจจุบันเปลี่ยนเป็นหนึ่ง US trading day และ latest cache ถูก reclassify แบบ
derived โดยไม่แก้ประวัติ append-only.
