# Log

## 2026-05-19

- `maintenance`: Added a Git Completion Workflow to `AGENTS.md` so future
  prompt-driven durable file changes are staged selectively and committed with
  a concise message after completion.
- `maintenance`: Added a project-wide hybrid Thai/English language standard to
  `AGENTS.md`, `wiki/reference/output-contract.md`, `README.MD`, and local
  stock workflow skills so future durable analysis uses Thai-first narrative
  while preserving English headings, structured fields, and finance terms.
- `maintenance`: Created `wiki/analysis/audits/Source Integrity Audit 2026-05-19.md`
  to identify agent-queryability improvements for schema consistency, machine
  indexes, decision metadata, chart source-of-truth, and source-gap tracking.
- `maintenance`: Reorganized `wiki/analysis/` into category folders for
  decisions, valuations, earnings, catalysts, comparisons, sentiment, and
  audits; moved existing analysis memos and updated path conventions.
- `latest-results`: Created `raw/imports/JNJ_latest_results_source.md` from
  Johnson & Johnson Q1 2026 Form 10-Q, official Q1 2026 earnings release,
  presentation, transcript, FY2025 Annual Report, and fresh market-data checks;
  P1 was limited to source note creation only.
- `ingest`: Created `raw/financials/JNJ_fundamentals.md`,
  `raw/financials/JNJ_fundamentals.json`, and `wiki/entities/JNJ.md` from
  verified JNJ Q1 2026 / FY2025 source fields, with missing data recorded
  instead of inferred.
- `research`: Expanded `wiki/entities/JNJ.md` with official-source business
  model, segment mix, thesis, risks, catalysts, valuation watch items, reports,
  follow-up, and missing/unverified data sections.
- `valuation`: Created `wiki/analysis/valuations/JNJ DCF Valuation 2026-05-19.md` after
  fresh-checking JNJ price, market cap, shares, cash, debt, FCF, and guidance.
- `analysis`: Created `wiki/analysis/decisions/JNJ Decision Memo 2026-05-19.md` with a
  WAIT / AVOID-new-capital action read and updated `index.md` plus
  `wiki/entities/Entity Index.md` for the new entity.

## 2026-05-18

- `latest-results`: Created `raw/imports/GOOGL_latest_results_source.md` from
  Alphabet Q1 2026 Form 10-Q, official Q1 2026 earnings release, slides,
  transcript, FY2025 Form 10-K, and fresh market-data checks; P1 was limited to
  source note creation only.
- `ingest`: Created `raw/financials/GOOGL_fundamentals.md`,
  `raw/financials/GOOGL_fundamentals.json`, and `wiki/entities/GOOGL.md` from
  verified Alphabet Q1 2026 / FY2025 source fields, with missing data recorded
  instead of inferred.
- `research`: Expanded `wiki/entities/GOOGL.md` with official-source business
  model, segment mix, thesis, risks, catalysts, valuation watch items, reports,
  follow-up, and missing/unverified data sections.
- `valuation`: Created `wiki/analysis/valuations/GOOGL DCF Valuation 2026-05-18.md` after
  fresh-checking GOOGL price, market cap, shares, cash, debt, FCF, and guidance.
- `analysis`: Created `wiki/analysis/decisions/GOOGL Decision Memo 2026-05-18.md` with a
  WAIT / AVOID-new-capital action read and updated `index.md` plus
  `wiki/entities/Entity Index.md` for the new entity.
- `skills`: Added `stock-decision-pipeline` as the orchestrator for
  P1 -> P4 -> P6 -> P11 -> P13, clarified P1 as source discovery only, and
  documented existing-data decision memo refresh flows with fresh price checks.
- `analysis`: Created `wiki/analysis/decisions/MSFT Decision Memo 2026-05-18.md` with a WAIT-for-new-capital / HOLD-existing-core action read, using vault facts plus a fresh StockAnalysis market-data check; updated `[[MSFT]]` with the dated decision memo link and current action read.
- `valuation`: Created `wiki/analysis/valuations/MSFT DCF Valuation 2026-05-18.md` after fresh-checking MSFT price, market cap, shares, cash, debt, FCF, and guidance; updated `[[MSFT]]` with the dated valuation memo and watch item.

## 2026-05-17

- `setup`: Created initial `stock-second-brain` project scaffold with Obsidian
  folders, reference docs, and Dexter-style local skills.
- `maintenance`: Converted dashboard/entity index to Markdown tables, cleaned
  unused reference docs, and expanded chart conventions for quarterly,
  YTD, annual, segment, cash-flow, and balance-sheet comparisons.
- `skills`: Added `dcf-valuation`, `x-research`, and
  `source-integrity-audit` local skills; added valuation assumptions reference
  and README usage examples.
- `docs`: Reworked README prompt guide into scenario-based New/Existing ticker
  flows with prompt IDs P1-P14.
- `latest-results`: Created `raw/imports/MSFT_latest_results_source.md` from
  Microsoft FY26 Q3 SEC filing detail, official IR financial statements, and
  earnings call transcript.
- `ingest`: Created `raw/financials/MSFT_fundamentals.md` and
  `raw/financials/MSFT_fundamentals.json`; created `wiki/entities/MSFT.md` with
  FY26 Q3 financial facts and source-backed management commentary.
- `ingest`: Updated `raw/financials/MSFT_fundamentals.md`,
  `raw/financials/MSFT_fundamentals.json`, and `wiki/entities/MSFT.md` with
  source-label-only period normalization, explicit quarterly/YTD/annual chart
  coverage, and a missing data registry using `ไม่พบข้อมูลที่ยืนยันได้` where
  inputs were unavailable.
- `research`: Created `raw/imports/MSFT_company_deep_dive_2026-05-17.md`,
  expanded `wiki/entities/MSFT.md` into an official-source company deep dive,
  and added FY2025 annual baseline / revenue mix facts to
  `raw/financials/MSFT_fundamentals.md` and
  `raw/financials/MSFT_fundamentals.json`.
