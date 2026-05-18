---
name: source-integrity-audit
description: Audit stock-second-brain for uncited numbers, stale market data, source conflicts, chart/table mismatches, orphan notes, missing entity links, and unresolved source gaps.
---

# Source Integrity Audit

Use this skill when the user asks to lint, audit, clean, verify, inspect source
quality, find stale data, find hallucinations, or maintain the vault.

## Language Standard

Follow `wiki/reference/output-contract.md`: write findings, severity rationale,
fix explanations, and follow-up notes primarily in Thai, while keeping file
paths, headings, source labels, metric names, and finance terms in English.

## Audit Scope

Check:

- unsupported or uncited numbers
- current-data claims that are stale or lack date/time
- source conflicts
- calculations without formula or denominator
- charts whose data does not match the nearby Markdown table or normalized file
- entity pages without source notes or normalized financial facts
- source notes not linked from entity pages
- analysis memos not linked back to relevant entities
- missing `log.md` entries
- orphan files
- duplicated ticker pages
- unresolved `Missing / Unverified Data`
- Dataview/plugin-specific blocks if the vault is intended to stay Markdown-first

## Required Workflow

1. Read `index.md` and `log.md`.
2. List entity pages, source notes, financial facts, and analysis memos.
3. Sample or inspect each relevant file depending on scope.
4. Check every chart block against nearby tables or JSON sidecar when present.
5. Search for risky terms and uncited numeric claims:
   - `%`, `$`, `USD`, `revenue`, `EPS`, `P/E`, `target`, `upside`, `downside`
   - `rough`, `estimate`, `implied`, `proxy`, `not verified`
6. Separate findings by severity.
7. If the user asked for fixes, patch the files and update `log.md`.
8. Always save an audit memo unless the user asks for chat-only output.

## Output File

```text
wiki/analysis/Source Integrity Audit YYYY-MM-DD.md
```

Append `log.md`.

## Severity Levels

| Severity | Meaning |
|---|---|
| High | Unsupported number, source conflict, wrong chart data, stale current market data presented as current, or thesis-changing issue. |
| Medium | Missing source link, weak provenance, unclear calculation, missing entity/source backlink. |
| Low | Formatting drift, stale follow-up, minor naming inconsistency, dashboard table not updated. |

## Memo Sections

- `# Source Integrity Audit - YYYY-MM-DD`
- `## Scope`
- `## High Severity Findings`
- `## Medium Severity Findings`
- `## Low Severity Findings`
- `## Chart / Table Checks`
- `## Source Gap Summary`
- `## Fixes Applied`
- `## Follow-Up`

## Fix Rules

- Do not silently delete facts. Either add the source, mark the claim as
  unverified, or move it into `Missing / Unverified Data`.
- If a chart and table disagree, prefer the source table and fix the chart.
- If a current-data value is stale, either refresh it or label the date clearly.
- If a source conflict cannot be resolved, record both sources and the conflict.

## Stop Conditions

Stop and ask for a narrower scope when:

- the vault is too large for one pass and the user did not specify a subset
- required files are missing or unreadable
- a source conflict requires fresh web research but web access is unavailable
