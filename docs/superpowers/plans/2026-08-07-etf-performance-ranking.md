# ETF Performance Ranking Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans or superpowers:subagent-driven-development to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply the approved 2016-2025 ETF performance-ranking design to the current performance pages and publish reproducible USA Top 10 and non-U.S. Regional Top 5 outputs.

**Architecture:** Keep each ETF performance page as the numeric source of truth. Use a dated comparison page for the calculated ranking, a dated raw/import note for the source-confidence and exclusion audit, and `wiki/entities/ETF Index.md` for the reusable prompt. Add only navigation links and one workflow log entry to existing indexes.

**Tech Stack:** Obsidian Markdown, local performance-page parsing, deterministic percentile/score calculations, shell-based validation.

## Global Constraints

- Use the common complete-calendar window `2016-2025`.
- Rank `NAV Total Return` only, including reinvested distributions and fund expenses; do not mix price return, market-price return, YTD, partial years, currencies, or incompatible bases.
- Require 10 annual observations and at least eight `official` or `official-derived` annual rows; allow no more than two `AI-derived` rows.
- Use verified underlying exposure and exactly one `primary region`; never use listing-exchange location as exposure region.
- Apply the spec's `60/25/15` components, confidence weights, tie-breakers, and one-winner-per-non-U.S.-region selection rule.
- Keep the final narrative Thai-first, concise, and explicitly label the screen as performance research rather than a recommendation or portfolio-fit claim.

### Task 1: Extract and validate the current candidate universe

**Files:**
- Read: `wiki/analysis/performance/ETF_* Performance.md`
- Read: `wiki/analysis/comparisons/* ETF.md`
- Read: `wiki/analysis/performance/ETF Performance Index.md`
- Read: `wiki/analysis/performance/README.md`

- [x] Parse each performance owner for canonical `entity_key`, fund, return basis, primary region, annual 2016-2025 NAV TR rows, and per-row source-confidence labels.
- [x] Exclude incomplete, unresolved, unsupported, incompatible, or materially non-continuous records with one exact reason per candidate.
- [x] Verify that every eligible record has 10 complete annual observations, no more than two AI-derived rows, and at least eight official/official-derived rows.

### Task 2: Calculate and audit the ranking

**Files:**
- Read: `docs/superpowers/specs/2026-07-26-etf-performance-ranking-prompt-design.md`

- [x] Calculate yearly cross-sectional percentiles, confidence-weighted annual component, Consistency, Downside stability, Total Score, positive-year count, longest positive streak, worst year, and annual volatility.
- [x] Rank the USA pool and select 10; rank the non-U.S. pool, keep the highest scorer per primary region, and select five regional winners.
- [x] Recompute component totals from displayed intermediate values and record the confidence mix, including the explicit `AI-derived = 0.25` rule and whether it was used.

### Task 3: Publish the durable ranking evidence

**Files:**
- Create: `wiki/analysis/comparisons/ETF Performance Ranking 2026-08-07.md`
- Create: `raw/imports/ETF_performance_ranking_sources_2026-08-07.md`

- [x] Write methodology, eligibility, USA Top 10, Non-U.S. Regional Top 5, exclusions, source-confidence mix, formulas, displayed intermediate values, source links, and Thai-first decision read.
- [x] Keep the ranking page's links pointed to existing performance owners and record local source paths plus underlying source links in the dated raw note.

### Task 4: Add the reusable prompt and navigation

**Files:**
- Modify: `wiki/entities/ETF Index.md`
- Modify: `wiki/analysis/performance/ETF Performance Index.md`
- Modify: `wiki/analysis/comparisons/README.md`
- Modify: `log.md`

- [x] Add a reusable prompt implementing the approved ranking design to `ETF Index.md`.
- [x] Link the dated ranking from the performance and comparison indexes without duplicating owner tables.
- [x] Append one dated workflow bullet listing the main files and outcome.

### Task 5: Verify and commit

- [x] Run a fresh validator for 10-year coverage, confidence weights, component/Total Score reconciliation, exact selection counts, distinct non-U.S. regions, exclusions, and wikilink resolution.
- [x] Inspect `git diff --check`, `git status --short`, and the final diff for unrelated changes.
- [x] Stage only the files in this plan and commit with a concise message.
