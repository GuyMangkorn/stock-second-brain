# ETF Performance Review Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an independent pre-save reviewer workflow to `check-etf-performance` that validates both the user-facing result and the complete proposed contents of planned vault changes before durable files are written.

**Architecture:** Keep trigger rules, source/metric guardrails, output contract, save convention, entity-key display rules, and the short review-gate summary in `SKILL.md`. Create sibling `workflow.md` for the detailed handoff packet, reviewer checklist, verdict format, correction loop, and fallback. The main agent remains the only durable-file writer; the reviewer returns findings only.

**Tech Stack:** Markdown skill instructions, YAML UI metadata, Obsidian wikilinks, Codex multi-agent tool when available, local checklist fallback.

## Global Constraints

- Review durable `lean` flows before save; keep read-only `mode: chat` unchanged.
- The main agent owns ticker/exchange resolution, source reconciliation, calculations, synthesis, corrections, and all durable writes.
- The reviewer must not write durable vault files or perform broad duplicate research.
- Every durable number must remain source-backed with URL/local path/filing reference or shown calculation.
- Preserve Thai-first narrative, English headings/keys/finance terms, existing filenames, region rules, and graph-link requirements.
- Use `PASS` or `CHANGES_REQUIRED`; do not save while unresolved critical or high-severity findings remain.
- If no multi-agent tool is available, run the same reviewer checklist locally and disclose the fallback when relevant.

---

### Task 1: Create the reviewer workflow reference

**Files:**
- Create: `/Users/mangkornkatawong/.codex/skills/check-etf-performance/workflow.md`
- Reference: `/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain/docs/superpowers/specs/2026-07-21-etf-performance-review-gate-design.md`

**Interfaces:**
- Consumes: the main agent's resolved entity, evidence lanes, calculations, proposed chat output, complete proposed durable file contents plus paths, and region/index changes.
- Produces: a reviewer handoff contract with a structured verdict and a bounded correction/re-review loop for `SKILL.md`.

- [x] **Step 1: Define the workflow phases**

Write the phases in this order: `prepare evidence packet` → `dispatch one fresh reviewer` → `apply findings` → `re-review when needed` → `write durable files` → `final response`.

- [x] **Step 2: Define the evidence packet**

Require the packet to include `entity_key` as the canonical exchange-qualified human-readable key (for example `NYSE Arca:VIG`), separate exchange-display/source clarification when needed, fund classification, request/window, metric and benchmark basis, source URLs, source as-of dates, raw observations, formulas and endpoint values, candidate output, the complete proposed contents of every planned durable file (performance page, dated source batch, any region/index page, and exact `log.md` bullet text), planned paths, and planned Obsidian graph/index/log edits. State that the reviewer receives enough evidence to audit but cannot write files.

- [x] **Step 3: Add the data and calculation checklist**

Require checks for ticker/exchange, passive equity classification, issuer facts, NAV Total Return versus price/market return, currency, dates, distributions, annual-year markers, cached/fresh S&P 500 TR basis, formulas, percentage rounding, CAGR eligibility/endpoints, drawdown/recovery, and best/worst ranking subsets.

- [x] **Step 4: Add the format and graph checklist**

Require checks for the exact output sections, Thai-first text, one annual table, metric labels, visible as-of dates, source links, and then verify that the candidate changes comply with the filename and region-navigation conventions owned by `SKILL.md`: resolved wikilinks, required breadcrumbs, exactly-one primary region, no duplicate performance page, and consistency between numeric source-of-truth pages and static navigation pages.

- [x] **Step 5: Specify verdicts and failure handling**

Use this shape:

```markdown
## Review verdict
- Status: `PASS` | `CHANGES_REQUIRED`
- Severity: `critical` | `high` | `medium` | `low`
- Location: `chat output` | `file path` | `source/calculation` | `graph`
- Finding: ...
- Required correction: ...
- Evidence: ...
```

Require `PASS` only when no unresolved critical/high findings remain. Require the main agent to correct or narrow-refresh evidence, replace unverifiable values with `ไม่พบข้อมูลที่ยืนยันได้` / `not disclosed`, and rerun review once when a correction changes a flagged claim or structure. Cap the loop at one re-review and disclose any remaining limitation.

- [x] **Step 6: Add the no-reviewer fallback**

State that a tool-availability failure is not permission to skip quality control: the main agent performs the identical checklist locally, records the limitation in the source batch note when saving, and proceeds only when the local gate passes.

- [x] **Step 7: Verify reference boundaries**

Keep detailed review mechanics in `workflow.md`; do not duplicate the full ETF performance rules, cached benchmark table, durable-save convention, or region convention already owned by `SKILL.md`.

### Task 2: Connect the workflow from `SKILL.md`

**Files:**
- Modify: `/Users/mangkornkatawong/.codex/skills/check-etf-performance/SKILL.md`

**Interfaces:**
- Consumes: `workflow.md` phases, packet contract, verdict semantics, and fallback.
- Produces: an explicit instruction that every durable `lean` run must complete the review gate before any vault write, while read-only `mode: chat` remains unchanged.

- [x] **Step 1: Add a concise review-gate section after mode/save selection**

Add a section that says to read `workflow.md` for durable `lean` invocations and explicit save/update/refresh/memo requests, prepare the evidence packet after research/reconciliation with the complete proposed candidate output and planned durable file contents, dispatch one independent reviewer when available, apply findings, and only then write performance/source/index/region/log files. Keep the main agent as the sole writer.

- [x] **Step 2: Preserve the read-only boundary**

State explicitly that `mode: chat` with no durable save does not create files and does not require the pre-save reviewer gate; still apply the existing `Quality Gate` locally before answering. For durable work, require the final user-facing response to stay under 200 words, summarize the reviewed result, and link files instead of pasting the full candidate output.

- [x] **Step 3: Link the detailed workflow**

Use a direct sibling link: `[workflow.md](workflow.md)`. Do not add a new skill or duplicate `workflow.md` content in the main skill.

### Task 3: Validate the skill package and references

**Files:**
- Validate: `/Users/mangkornkatawong/.codex/skills/check-etf-performance/SKILL.md`
- Validate: `/Users/mangkornkatawong/.codex/skills/check-etf-performance/workflow.md`
- Validate: `/Users/mangkornkatawong/.codex/skills/check-etf-performance/agents/openai.yaml`

**Interfaces:**
- Consumes: completed skill files.
- Produces: validator output and a manual consistency check against the design spec, `AGENTS.md`, durable-save convention, and region-navigation convention.

- [x] **Step 1: Run the skill validator**

Run `python3 /Users/mangkornkatawong/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/mangkornkatawong/.codex/skills/check-etf-performance`; expect successful YAML/name validation.

- [x] **Step 2: Run structural checks**

Confirm `workflow.md` is referenced by `SKILL.md`, every required checklist category is present, the verdict values match in both files, and there are no unresolved placeholder markers such as `TODO` or `TBD`.

- [x] **Step 3: Inspect the final diff and status**

Review only the intended skill files and plan/spec files, preserve unrelated user changes, and report any inability to write the global skill directory separately from repository verification.

---

## Self-review

- Spec coverage: architecture, packet contract, failure handling, single-writer ownership, and validation are covered by Tasks 1–3.
- Placeholder scan: no `TODO`, `TBD`, or unspecified validation step is required; each checklist step names its expected content.
- Boundary consistency: `SKILL.md` remains the compact owner of ETF rules; `workflow.md` owns the review gate; read-only chat remains outside the durable pre-save gate.
