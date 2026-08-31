---
name: research-card-intake
description: Create project-local Markdown Research Cards from an authorized ETF or Stock ticker list.
---

# Research Card Intake

ใช้ skill นี้เมื่อผู้ใช้ขอสร้าง เพิ่ม หรือ queue งานวิจัยอย่างชัดเจน โดยให้
ใช้ queue ที่เก็บในโปรเจกต์เป็น source of truth เดียว

Use this project-scoped skill when the user clearly asks to create, add, queue,
or seed research work. Intake materializes a Research Batch and Ready Research
Cards; it does not start research. The Markdown card frontmatter is the sole
state owner.

## Accepted input

The user may provide:

- comma-separated tickers;
- a Markdown bullet list;
- a Markdown table with `Ticker`/`Symbol` and optional `Type`, `Workflow`
  columns; or
- a project-relative Markdown input file.

For one instrument type, state ETF or Stock once. A mixed table must include an
explicit `Type` value for every row. Reject ambiguity before writing anything.
ETF defaults to `check-etf-performance`. The future Stock default is
`official-source-stock-research` in deep-dive mode, but Stock creation is
disabled until its processor is delivered in V1.

## Invocation

Run the deterministic command surface from the saved project checkout:

```text
python3 scripts/research_queue.py intake --tickers "VIG,DGRO" --type ETF
python3 scripts/research_queue.py intake --input-file watchlist.md
python3 scripts/research_queue.py intake --tickers "VIG,DGRO" --type ETF --dry-run
```

An explicit create/add/queue request is authorized to write without another
confirmation. Use `--dry-run` when the user asks to preview normalization. Do
not infer a type from a ticker or a title, and do not call a research workflow
during Intake.

## Duplicate and batch rules

Normalize ticker case and whitespace, preserve first-seen order, and collapse
duplicate input rows. An active Ready, In Progress, or Blocked card for the
same instrument/workflow is returned as `reused`; a terminal card does not
prevent a new refresh card. Each authorized submission creates one Research
Batch. Batch Done means cards were materialized, not that their research is
complete. The JSON result reports `created`, `reused`, and `rejected` items.

## Safety

Only project-relative input files are accepted. Never create migration-only
metadata, Trello synchronization, or a second state field. Preserve unrelated
working-tree changes. The queue manager owns claims and processing after this
skill returns.
