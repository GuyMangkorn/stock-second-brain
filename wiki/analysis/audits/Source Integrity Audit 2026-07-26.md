---
type: analysis
analysis_type: source-integrity-audit
date: 2026-07-26
scope: etf-performance-git-pending-changes
source_files:
  - raw/imports/tradingview_etf_performance_progress_2026-07-22.md
  - raw/imports/ETF_performance_sources_2026-07-24.md
  - wiki/analysis/performance/ETF Performance Index.md
  - wiki/analysis/comparisons/ETF Region Index.md
  - wiki/analysis/comparisons/Asia-Pacific ETF.md
tags:
  - analysis/source-integrity-audit
  - maintenance/etf-performance
  - duplicate-review
---

# Source Integrity Audit - 2026-07-26

## Scope

ตรวจ pending Git changes ของ ETF performance batch 2026-07-22: queue/ledger, canonical exchange-qualified performance pages, region navigation, source-batch references, required page sections, and broken/orphan performance links.

## High Severity Findings

ไม่พบ High severity issue.

## Medium Severity Findings

| Finding | Evidence | Fix / Decision |
|---|---|---|
| KPHO มี performance page ซ้ำ โดยหน้าหนึ่งเป็น canonical เก่าและ orphan | `ETF_NYSE_ARCA_KPHO Performance.md` ใช้ `NYSE Arca:KPHO` และ source batch `2026-07-23`; canonical ล่าสุดคือ `NYSE:KPHO` ใน `ETF_NYSE_KPHO Performance.md` | ลบหน้าเก่าที่ superseded และคง canonical page ล่าสุดซึ่งมี exchange conflict note และ official source chain ครบ |

## Low Severity Findings

| Finding | Evidence | Fix / Decision |
|---|---|---|
| Region count ไม่ตรงกับ performance links จริง | Japan มี 22 และ Asia-Pacific มี 12 unique performance links | ปรับตัวนับใน `ETF Region Index.md` เป็น 22 และ 12 |
| Asia-Pacific page มี metadata เก่าและ row ซ้ำ | `updated` เดิมเป็น `2026-07-24`; `ISMJF` ซ้ำใน verified additions | ปรับเป็น `2026-07-26` และลบ duplicate row ที่ซ้ำแบบ exact |

## Verification

- Ledger: 125/125 rows; `completed_10Y` 56, `completed_available_period_no_10Y` 33, `unsupported ETF type` 36, unresolved 0.
- Queue order ตรงกับ input list.
- `git diff --check`: PASS.
- Changed performance pages มี required sections และ source blocks ครบ; index/navigation pages ไม่ใช้ template เดียวกัน.
- Performance index และ region links ที่ตรวจสอบแล้ว resolve ได้; orphan KPHO เก่าถูกนำออก.

## Follow-Up

ไม่มี unresolved integrity issue ในขอบเขต pending ETF batch นี้. ควรตรวจ `git diff` อีกครั้งก่อน stage/commit.
