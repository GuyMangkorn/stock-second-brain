---
type: analysis
analysis_type: source-integrity-audit
date: 2026-05-19
scope: agent-queryability
source_files:
  - index.md
  - log.md
  - wiki/entities/Entity Index.md
  - wiki/entities/MSFT.md
  - wiki/entities/GOOGL.md
  - wiki/entities/JNJ.md
  - raw/financials/MSFT_fundamentals.md
  - raw/financials/MSFT_fundamentals.json
  - raw/financials/GOOGL_fundamentals.md
  - raw/financials/GOOGL_fundamentals.json
  - raw/financials/JNJ_fundamentals.md
  - raw/financials/JNJ_fundamentals.json
tags:
  - analysis/source-integrity-audit
  - maintenance/queryability
---

# Source Integrity Audit - 2026-05-19

## Scope

Audit นี้ดู vault ในมุม **AI Agent queryability** มากกว่า valuation accuracy รอบใหม่ โดยอ่าน `index.md`, `log.md`, entity pages, source notes, normalized financial facts Markdown/JSON, analysis memos, `Entity Index`, และ `Portfolio Map`.

เป้าหมายคือหาว่า Agent จะดึงข้อมูลจาก Obsidian vault ได้ง่ายขึ้นตรงไหน โดยยังรักษา source integrity rules: facts ต้อง trace กลับไปที่ source note, official filing, local path, หรือ shown calculation ได้.

## High Severity Findings

ไม่พบ High severity issue จากรอบนี้: entity หลักทั้ง `MSFT`, `GOOGL`, และ `JNJ` มี source note, normalized financial facts, entity page, DCF memo, decision memo, และ dashboard link ที่ trace ได้.

## Medium Severity Findings

| Finding | Evidence | Why It Matters | Suggested Fix |
|---|---|---|---|
| Normalized JSON schema ยังไม่เหมือนกันข้าม ticker | `raw/financials/MSFT_fundamentals.json` ใช้ metric-keyed `financial_series`; `GOOGL_fundamentals.json` ใช้ statement-keyed objects; `JNJ_fundamentals.json` ใช้ `periods` เป็น object records และ `financial_series` แบบ chart-oriented. | Agent ต้องเขียน parser เฉพาะ ticker แทนที่จะ query metric เดียวข้าม coverage ได้ทันที. | Define canonical JSON contract: `periods[]`, `metrics[]`, `segments[]`, `ratios[]`, `market_data_checks[]`, `missing_data[]`, โดยทุก record มี `ticker`, `period`, `period_end`, `metric`, `value`, `unit`, `source_ref`, `calculation`. |
| Dashboard และ `Entity Index` เป็น manual Markdown tables | `index.md` และ `wiki/entities/Entity Index.md` duplicate ticker, company, latest period, และ source gap count ที่มีอยู่ใน entity frontmatter. | เมื่อ coverage โตขึ้น table อาจ stale และ Agent ต้อง reconcile หลายแหล่ง. | Add generated machine index เช่น `wiki/entities/entity_index.json` หรือ `raw/financials/coverage_index.json` แล้วให้ dashboard render/คัดลอกจาก index นั้น. |
| Chart data มี duplicate source of truth | `MSFT` และ `GOOGL` entity pages มี chart blocks ซ้ำกับ `raw/financials/*_fundamentals.md`; `JNJ` entity page เลือก delegate chart ไปที่ fundamentals file. | Duplicate chart blocks เพิ่มโอกาส chart/table drift และทำให้ Agent ไม่รู้ควร parse chart จาก entity หรือ normalized file. | ให้ `raw/financials/*.json` เป็น chart data source เดียว แล้ว entity page ใช้ summary/link หรือ embed จาก normalized file. |
| Analysis memo frontmatter ยังไม่พอสำหรับ decision query | Decision memos มี `analysis_type` และ `decision` แต่ยังไม่มี fields เช่น `action_new_capital`, `action_existing_position`, `price_used`, `price_date`, `base_fair_value`, `bull_fair_value`, `next_review_trigger`. | คำถามอย่าง "ตัวไหน WAIT เพราะ valuation?" หรือ "fair value เทียบ price ล่าสุดเท่าไร?" ต้อง parse prose/table แทนที่จะ query frontmatter. | Extend analysis frontmatter with normalized decision and valuation fields while keeping narrative Thai-first body. |
| Source note graph ยังมี edge ที่ไม่เป็นมาตรฐาน | `raw/imports/MSFT_company_deep_dive_2026-05-17.md` ไม่มี `normalized_output` frontmatter แม้ถูกใช้ update entity/fundamentals; path links บางที่เป็น wikilink บางที่เป็น raw path. | Agent query source-to-output lineage ได้ไม่ครบแบบ deterministic. | Require every source note to include `normalized_output`, `entity`, and optional `analysis_outputs`; standardize local paths as paths in frontmatter and wikilinks in narrative sections. |
| Missing data ยังไม่มี central gap ledger | Entity frontmatter มี `source_gap_count` และ `source_gaps`, แต่ยังไม่มี normalized gap records with status/priority/review_after. | Agent ตอบ "อะไร block thesis?" ได้จาก prose แต่จัดลำดับงาน follow-up ยาก. | Add `wiki/analysis/Source Gap Registry.md` หรือ `raw/financials/source_gaps.json` generated from entity frontmatter and `Missing / Unverified Data` tables. |

## Low Severity Findings

| Finding | Evidence | Suggested Fix |
|---|---|---|
| Entity aliases ยังน้อย | Entity frontmatter มี ticker/company แต่ไม่มี `aliases`, `cik`, `exchange_symbol`, `sector`, `industry`. | Add stable identity fields so Agent resolves `GOOG` vs `GOOGL`, company names, CIK, and sector queries reliably. |
| `Portfolio Map` ยังไม่สะท้อน active coverage | `wiki/overview/Portfolio Map.md` updated `2026-05-17` และ watchlist ยัง empty แม้มี active entities ใน dashboard. | Refresh overview from `Entity Index` and add watchlist/action buckets. |
| Template placeholder creates one unresolved wikilink | Local link scan found `[[TICKER_fundamentals]]` only in `wiki/reference/entity-template.md`. | This is benign, but can be escaped or documented as a template placeholder. |
| `.obsidian` files add query noise | `.obsidian/workspace.json` is dirty and `.obsidian/graph.json` is untracked. | Agent workflows should ignore `.obsidian/workspace.json`, `.obsidian/graph.json`, plugin bundles, and themes unless the task is specifically Obsidian configuration. |

## Chart / Table Checks

- `JNJ`: Entity page delegates charts to `raw/financials/JNJ_fundamentals.md`, which is the cleaner pattern for queryability.
- `MSFT`: Entity chart blocks and `raw/financials/MSFT_fundamentals.md` use matching values for the sampled quarterly, YTD, segment, cash flow, and balance sheet charts.
- `GOOGL`: Entity page and fundamentals file both use sourced values, but the entity `Quarterly YoY Comparison` chart plots `Free Cash Flow` while the normalized fundamentals `Quarterly YoY Comparison` chart plots `Net Income`. This is not a numeric contradiction, but the section title can confuse Agent parsing. Prefer explicit chart names such as `Quarterly Revenue / Operating Income / Free Cash Flow`.

## Source Gap Summary

Current source gaps look deliberate rather than hallucinated. The dashboard and entity frontmatter identify:

| Ticker | Gap Count | Main Gap Pattern |
|---|---:|---|
| MSFT | 5 | market data freshness, product-level AI revenue/margins, OpenAI-specific economics, incomplete FY2026 annual data |
| GOOGL | 6 | AI product economics, TPU economics, 2027 capex amount, equity-security gain quality, investor-specific basis/sizing |
| JNJ | 5 | product-level launch revenue/profitability, GAAP forward guidance, FY2026 full-year actuals, sequential trend coverage |

The next improvement is not more prose; it is making these gaps queryable as structured records.

## Fixes Applied

- Created this audit memo.
- No factual financial values were changed in this pass.

## Follow-Up

Recommended order:

1. Add a canonical financial JSON contract and migrate `MSFT`, `GOOGL`, and `JNJ` sidecars into the same schema.
2. Generate `entity_index.json` / `coverage_index.json` from frontmatter and JSON sidecars, then use it as the dashboard source of truth.
3. Extend analysis memo frontmatter with normalized decision and valuation fields.
4. Convert source gaps into a central structured registry with `ticker`, `gap`, `status`, `priority`, `source_context`, and `review_after`.
5. Treat chart blocks as presentation only; keep chart data in normalized JSON and reduce entity-level duplicate chart data.
6. Add an Agent query guide that says read order should be `index.md` -> machine index -> entity -> normalized JSON -> source note -> analysis memo.
