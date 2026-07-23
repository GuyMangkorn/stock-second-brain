---
type: progress-ledger
input: raw/imports/tradingview_etf_list_filtered_2026-07-22.md
input_count: 125
processed_count: 7
remaining_count: 118
queue_policy: sequential; one ticker per user continuation
updated: 2026-07-23
---

# TradingView ETF Performance Progress

รายการอ้างอิงคือ `Remaining ETFs` ใน [[tradingview_etf_list_filtered_2026-07-22]] และมีทั้งหมด `125` rows. รายการ `Removed as Already Researched` ไม่อยู่ใน queue นี้. รอบนี้ประมวลผลเฉพาะ row `1-7` และหยุดตามกติกา sequential queue; rows หลังจากนี้ยังไม่ถูกประมวลผลใน ledger นี้.

## Terminal status register

| Order | Input ticker | Status | Canonical entity_key | Reason / coverage | Performance file | Source batch |
|---:|---|---|---|---|---|---|
| 1 | EWY | `completed_10Y` | `NYSE Arca:EWY` | Passive/index-tracking South Korea equity ETF; official NAV TR annual rows 2016-2025 and official rolling 10Y NAV TR CAGR `16.72%` for 2016-06-30 to 2026-06-30; current YTD `75.82%` as of 2026-07-21. | [[ETF_NYSE_ARCA_EWY Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 2 | DBJP | `completed_10Y` | `NYSE Arca:DBJP` | Passive/index-tracking Japan equity ETF with USD/JPY hedge; official rolling 10Y NAV TR CAGR `17.28%` for 2016-06-30 to 2026-06-30; official annual rows 2016-2024; 2025/current YTD not disclosed. | [[ETF_NYSE_ARCA_DBJP Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 3 | WDTRF | `completed_available_period_no_10Y` | `LSE:DXJA` | Input OTC alias for WisdomTree Japan Equity UCITS ETF - USD Hedged Acc; official annual NAV TR rows 2018-2025, available-period 2017-03-07 to 2026-06-30 (9.31 years), since-inception NAV TR CAGR `17.07%`, current YTD `21.90%` as of 2026-06-30; 10-year NAV TR unavailable. | [[ETF_LSE_DXJA Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 4 | FLTW | `completed_available_period_no_10Y` | `NYSE Arca:FLTW` | Passive/indexed Taiwan equity ETF; official NAV TR rows 2018-2025, available-period inception 2017-11-02 to 2026-06-30 (8.66 years), 2018-2025 annualized return `14.36%`, 2021-2025 CAGR `13.48%`, current YTD `63.10%` as of 2026-07-10; 10-year NAV TR unavailable. | [[ETF_NYSE_ARCA_FLTW Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 5 | ISRVF | `completed_10Y` | `LSE:IJPD` | Input OTC alias for iShares MSCI Japan USD Hedged UCITS ETF (Acc); official rolling 10Y NAV TR cumulative `381.35%` and CAGR `17.02%` for 2016-06-30 to 2026-06-30; official calendar rows 2016-2025; current YTD `17.84%` as of 2026-07-20. | [[ETF_LSE_IJPD Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 6 | EPP | `completed_10Y` | `NYSE Arca:EPP` | Official iShares passive/index-tracking equity ETF; official rolling 10Y NAV TR cumulative `103.63%` and CAGR `7.37%` for 2016-06-30 to 2026-06-30; official calendar rows 2016-2025; current YTD `11.23%` as of 2026-07-21. | [[ETF_NYSE_ARCA_EPP Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 7 | DXJJF | `completed_10Y` | `LSE:DXJ` | Input OTC alias for WisdomTree Japan Equity UCITS ETF - USD Hedged; official ten complete calendar-year NAV TR rows 2016-2025 compound to cumulative `268.73%` and CAGR `13.94%`; current official YTD `21.90%` as of 2026-06-30; latest issuer NAV US$55.035 as of 2026-07-22. | [[ETF_LSE_DXJ Performance]] | [[ETF_performance_sources_2026-07-23]] |

## Queue pointer

- Completed: `7/125`
- Next ticker: `INCO` (row `8`)
- Allowed terminal statuses: `completed_10Y`, `completed_available_period_no_10Y`, `unsupported ETF type`, `unresolved ticker/data gap`
- No ticker after `DXJJF` was searched, compared, dispatched, or processed in this round.
