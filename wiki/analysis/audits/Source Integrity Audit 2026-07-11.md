---
type: analysis
analysis_type: source-integrity-audit
date: 2026-07-11
scope: graph-link-repair-and-selected-etf-entities
source_files:
  - index.md
  - log.md
  - wiki/entities/Entity Index.md
  - wiki/entities/ETF Index.md
  - wiki/analysis/comparisons/Dividend ETF Full Universe Triage 2026-06-28.md
  - wiki/analysis/comparisons/Dividend ETF Top 10 Holdings Tracker 2026-07-01.md
tags:
  - analysis/source-integrity-audit
  - maintenance/queryability
  - entity-graph
---

# Source Integrity Audit - 2026-07-11

## Scope

ตรวจ graph queryability ของ company-specific decisions, valuations, earnings, multi-ticker comparison notes, และ selected ETF entities หลังทำตามแผน Graph Link Repair + Selected ETF Entities. ไม่ได้แก้ financial facts, charts, JSON, หรือ 100-row ETF universe data.

## High Severity Findings

ไม่พบ High severity issue. การแก้รอบนี้เป็น graph/backlink maintenance และไม่ได้เปลี่ยนตัวเลขการเงินหรือ valuation calculation.

## Medium Severity Findings

| Finding | Evidence | Fix |
|---|---|---|
| Company analysis pages ขาด direct entity edge | Baseline checker พบ 70 ticker-specific analysis notes ที่ไม่มี `[[TICKER]]`. | เติม `Entity: [[TICKER]]` ใน decisions, valuations, และ earnings ที่มี `ticker:` frontmatter. |
| Multi-ticker notes ขาด related-entity section | Baseline checker พบ 4 notes: 3 US covered refreshes และ 1 screener triage. | เพิ่ม `## Related Entities` โดย link เฉพาะ existing company entities. |
| ETF comparison universe ไม่มี durable selected-entity layer | Baseline ไม่มี selected ETF entity files และไม่มี ETF index. | สร้าง 3 selected ETF hubs พร้อม `entity_key: EXCHANGE:TICKER` และแยก `ETF Index`. |

## Low Severity Findings

| Finding | Evidence | Follow-Up |
|---|---|---|
| Selected ETF price/NAV, expense ratio, และ current distribution ยังไม่ normalized | ETF entities บันทึกเป็น source gaps และใช้ tracker/official snapshots ที่มีอยู่แล้ว | Refresh official product pages/factsheets ก่อน allocation decision. |

## Before / After Check

| Check | Before | After |
|---|---:|---:|
| Ticker-specific analysis notes without direct entity link | 70 | 0 |
| Multi-ticker notes without `Related Entities` | 4 | 0 |
| Selected ETF entities | 0 | 3 |
| ETF Index | 0 | 1 |
| ETF universe rows | 100 | 100 |

## Chart / Table Checks

- ไม่ได้แก้ chart blocks, normalized JSON, fundamentals tables, หรือ DCF tables.
- ETF tracker ยังมี `100` universe rows และใช้เป็น comparison source of truth ต่อไป.
- Selected ETF entity values are links/summaries of existing tracker and official-source snapshots; no new unreferenced financial metric was introduced.

## Source Gap Summary

ทั้ง `ETF_AMEX_DGRO`, `ETF_AMEX_VIG`, และ `ETF_NASDAQ_VIGI` มี source gaps ที่ระบุไว้ใน entity frontmatter: current price/NAV และ expense ratio/current distribution data ยังไม่ถูก normalize ในรอบนี้.

## Fixes Applied

- Added direct entity links to ticker-specific analysis notes.
- Added related-entity sections to multi-ticker notes.
- Created three selected ETF entities and `[[ETF Index]]`.
- Added ETF navigation links to `index.md`, `Portfolio Map`, and ETF comparison notes.
- Appended one workflow entry to `log.md`.

## Follow-Up

1. Refresh official ETF price/NAV, expense ratio, and distribution data before treating the three entities as allocation-ready.
2. Keep the remaining 97 ETF rows in comparison notes until they become held, watchlisted, or durable research candidates.
3. Re-run the graph checker after future entity or analysis-page additions.
