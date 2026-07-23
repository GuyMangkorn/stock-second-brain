---
type: progress-ledger
input: raw/imports/tradingview_etf_list_filtered_2026-07-22.md
input_count: 125
processed_count: 18
remaining_count: 107
queue_policy: sequential; one ticker per user continuation
updated: 2026-07-24
---

# TradingView ETF Performance Progress

รายการอ้างอิงคือ `Remaining ETFs` ใน [[tradingview_etf_list_filtered_2026-07-22]] และมีทั้งหมด `125` rows. รายการ `Removed as Already Researched` ไม่อยู่ใน queue นี้. รอบนี้ประมวลผลเฉพาะ row `1-18` และหยุดตามกติกา sequential queue; rows หลังจากนี้ยังไม่ถูกประมวลผลใน ledger นี้.

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
| 8 | INCO | `completed_10Y` | `NYSE Arca:INCO` | Official Columbia indexed/passive India consumer equity ETF; issuer 10-year average annual NAV TR `8.72%` as of 2026-05-31; disclosed annual rows 2021-2025 compound to 5-year CAGR `11.16%`; current YTD `-9.92%` as of 2026-05-31; latest NAV US$59.45 as of 2026-06-23. | [[ETF_NYSE_ARCA_INCO Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 9 | AIA | `completed_10Y` | `NASDAQ:AIA` | Passive/index-tracking Asia ex Japan equity ETF; official rolling 10-year NAV TR cumulative `298.99%` / CAGR `14.84%` for 2016-06-30 to 2026-06-30; official annual rows 2021-2025; current date-to-date YTD `40.47%` as of 2026-07-21; NAV US$136.34 as of 2026-07-21. | [[ETF_NASDAQ_AIA Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 10 | HEWJ | `completed_10Y` | `NYSE Arca:HEWJ` | Passive/index-tracking Japan equity ETF with USD hedge overlay; official rolling 10-year NAV TR cumulative `391.99%` / CAGR `17.27%` for 2016-06-30 to 2026-06-30; official annual rows 2021-2025; current date-to-date YTD `18.81%` as of 2026-07-17; NAV US$62.22 as of 2026-07-20. | [[ETF_NYSE_ARCA_HEWJ Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 11 | SMIN | `completed_10Y` | `Cboe BZX:SMIN` | Passive/index-tracking India small-cap equity ETF; official rolling 10-year NAV TR cumulative `152.70%` / CAGR `9.71%` for 2016-06-30 to 2026-06-30; official annual rows 2021-2025 compound to 5-year CAGR `12.90%`; current date-to-date YTD `-0.58%` as of 2026-07-21; NAV US$69.69 as of 2026-07-21. | [[ETF_CBOE_BZX_SMIN Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 12 | IHREF | `completed_10Y` | `LSE:SJPA` | Input OTC alias for iShares Core MSCI Japan IMI UCITS ETF; official LSE:SJPA listing for ISIN `IE00B4L5YX21`; official rolling 10-year NAV TR cumulative `147.80%` / CAGR `9.50%` for 2016-06-30 to 2026-06-30; official 2021-2025 rows compound to 5-year CAGR `6.33%`; current date-to-date YTD `12.55%` as of 2026-07-17; NAV US$77.53 as of 2026-07-17. | [[ETF_LSE_SJPA Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 13 | EWT | `completed_10Y` | `NYSE Arca:EWT` | Passive/index-tracking Taiwan single-country equity ETF; official rolling 10-year NAV TR cumulative `552.21%` / CAGR `20.63%` for 2016-06-30 to 2026-06-30; official 2021-2025 rows compound to 5-year CAGR `12.01%`; current date-to-date YTD `50.68%` as of 2026-07-20; NAV US$95.76 as of 2026-07-20. | [[ETF_NYSE_ARCA_EWT Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 14 | JPXN | `completed_10Y` | `NYSE Arca:JPXN` | Passive/index-tracking Japan equity ETF; official U.S. iShares page resolves the input ticker to NYSE Arca (not separate TSE:1364); official rolling 10-year NAV TR cumulative `142.85%` / CAGR `9.28%` for 2016-06-30 to 2026-06-30; official 2021-2025 rows compound to 5-year CAGR `6.19%`; current date-to-date YTD `15.60%` as of 2026-07-21; NAV US$98.72 as of 2026-07-22. | [[ETF_NYSE_ARCA_JPXN Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 15 | GMF | `completed_10Y` | `NYSE Arca:GMF` | Passive/index-sampling emerging Asia-Pacific equity ETF; official State Street 10-year NAV TR average annual return `9.94%` for 2016-06-30 to 2026-06-30; official NAV/distribution workbooks calculate cumulative `158.00%` and 2021-2025 CAGR `4.20%`; latest standardized NAV TR YTD `12.56%` as of 2026-06-30; NAV US$152.77 as of 2026-07-22. | [[ETF_NYSE_ARCA_GMF Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 16 | AAXJ | `completed_10Y` | `NASDAQ:AAXJ` | Passive/index-tracking Asia ex Japan equity ETF; official rolling 10Y NAV TR cumulative `164.36%` / CAGR `10.21%` for 2016-06-30 to 2026-06-30; official 2021-2025 rows compound to `15.04%` / CAGR `2.84%`; current NAV `US$113.07` and NAV TR YTD `21.30%` as of 2026-07-22. | [[ETF_NASDAQ_AAXJ Performance]] | [[ETF_performance_sources_2026-07-23]] |
| 17 | MKOR | `unsupported ETF type` | `NYSE Arca:MKOR` | Official Matthews Korea Active ETF; issuer confirms Primary Exchange `NYSE Arca` and an unconstrained all-cap, fundamental bottom-up active strategy. It fails the passive/index-tracking equity gate; no performance page or 10-year NAV TR comparison created. | not applicable | [[ETF_performance_sources_2026-07-23]] |
| 18 | FLKR | `completed_available_period_no_10Y` | `NYSE Arca:FLKR` | Passive/index-tracking South Korea equity ETF; official inception `2017-11-02` and issuer 10-year field `—`; official 2018-2025 NAV TR rows compound to `53.85%` / CAGR `5.53%`; 2021-2025 CAGR `4.59%`; current NAV TR YTD `86.35%` as of 2026-07-07. | [[ETF_NYSE_ARCA_FLKR Performance]] | [[ETF_performance_sources_2026-07-24]] |

## Queue pointer

- Completed: `18/125`
- Next ticker: `VPL` (row `19`)
- Allowed terminal statuses: `completed_10Y`, `completed_available_period_no_10Y`, `unsupported ETF type`, `unresolved ticker/data gap`
- No ticker after `FLKR` was searched, compared, dispatched, or processed in this round.
