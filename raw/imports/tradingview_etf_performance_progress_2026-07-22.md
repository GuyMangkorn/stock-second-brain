---
type: progress-ledger
input: raw/imports/tradingview_etf_list_filtered_2026-07-22.md
input_count: 125
processed_count: 1
remaining_count: 124
queue_policy: sequential; one ticker per user continuation
updated: 2026-07-23
---

# TradingView ETF Performance Progress

รายการอ้างอิงคือ `Remaining ETFs` ใน [[tradingview_etf_list_filtered_2026-07-22]] และมีทั้งหมด `125` rows. รายการ `Removed as Already Researched` ไม่อยู่ใน queue นี้. รอบนี้ประมวลผลเฉพาะ row `1` และหยุดตามกติกา sequential queue; rows หลังจากนี้ยังไม่ถูกประมวลผลใน ledger นี้.

## Terminal status register

| Order | Input ticker | Status | Canonical entity_key | Reason / coverage | Performance file | Source batch |
|---:|---|---|---|---|---|---|
| 1 | EWY | `completed_10Y` | `NYSE Arca:EWY` | Passive/index-tracking South Korea equity ETF; official NAV TR annual rows 2016-2025 and official rolling 10Y NAV TR CAGR `16.72%` for 2016-06-30 to 2026-06-30; current YTD `75.82%` as of 2026-07-21. | [[ETF_NYSE_ARCA_EWY Performance]] | [[ETF_performance_sources_2026-07-23]] |

## Queue pointer

- Completed: `1/125`
- Next ticker: `DBJP` (row `2`)
- Allowed terminal statuses: `completed_10Y`, `completed_available_period_no_10Y`, `unsupported ETF type`, `unresolved ticker/data gap`
- No ticker after `EWY` was searched, compared, dispatched, or processed in this round.
