# ETF Performance Review Gate Design

## Goal

Add an independent, pre-save quality gate to `check-etf-performance` so durable ETF performance outputs are reviewed for evidence, calculations, markdown format, and Obsidian graph links before any vault file is written.

## Scope

- Run the review only for durable `lean` flows: explicit skill invocation or requests to save, update, refresh, or create a memo.
- Do not add a reviewer for read-only `mode: chat` responses.
- Keep the main agent as the only writer of vault files.

## Architecture

`SKILL.md` keeps the trigger, ownership, and gate summary. A sibling `workflow.md` owns the detailed reviewer handoff contract and checklist. After main-agent research and reconciliation, the main agent launches one fresh reviewer agent with a compact evidence packet and the proposed output. The reviewer returns `PASS` or `CHANGES_REQUIRED`; the main agent corrects any findings and asks for one re-review only when corrections affect a flagged claim or structure.

## Reviewer Contract

The packet contains the resolved entity key, requested period, metric definitions, sourced observations and URLs, as-of dates, calculations/endpoints, the proposed markdown, and planned vault paths. The reviewer must not perform broad duplicate research or write files. It validates source-to-claim mapping, return-basis and time-window consistency, calculation reproducibility, table/ranking correctness, required sections, filenames, wikilinks, breadcrumbs, tags, region navigation, and planned index/log changes.

## Failure Handling

`PASS` permits saving. `CHANGES_REQUIRED` lists findings by severity and exact correction. If a primary claim cannot be verified, the main agent either resolves it from supplied or narrowly refreshed evidence, or replaces it with `ไม่พบข้อมูลที่ยืนยันได้` / `not disclosed`. A reviewer availability failure must be disclosed and the main agent performs the same checklist locally before saving.

## Validation

Validate the skill YAML and file references with `quick_validate.py`. Inspect the reviewer checklist against the existing durable-save and region-navigation requirements. No historical ETF output needs regeneration for this workflow-only change.
