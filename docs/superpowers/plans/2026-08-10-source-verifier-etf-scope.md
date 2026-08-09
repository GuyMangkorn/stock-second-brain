# Restrict `source_verifier` to ETF Performance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `source_verifier` run only for durable, research-bearing workflows that explicitly use `check-etf-performance`, while keeping all other project workflows free of this reviewer.

**Architecture:** Put the invocation boundary in `AGENTS.md` and put a fail-closed scope guard in `.codex/agents/source-verifier.toml`. The main agent remains the sole durable-file writer; the reviewer only validates ETF performance evidence packets and returns the existing structured verdict contract.

**Tech Stack:** Markdown project instructions, Codex custom-agent TOML, Python `tomllib`, Git.

## Global Constraints

- Dispatch `source_verifier` only from the `check-etf-performance` durable-save gate.
- Do not dispatch it for stock research/ingest, ETF fund research, valuation, decision, market-move, sentiment, or source-integrity workflows.
- Keep the reviewer read-only and preserve `PASS`, `CHANGES_REQUIRED`, and `WARNING` semantics.
- Keep the existing ETF performance source hierarchy, calculation rules, and research delegation unchanged.
- Preserve unrelated worktree changes and stage only files in this prompt's scope.

---

### Task 1: Replace the broad project pre-save gate

**Files:**
- Modify: `AGENTS.md:33-54`

**Interfaces:**
- Consumes: the existing source-integrity rules and `check-etf-performance` workflow.
- Produces: a conditional ETF performance pre-save gate with no project-wide reviewer mandate.

- [ ] **Step 1: Rewrite the gate heading and trigger**

Replace `## Pre-Save Verification Gate` with a section that states the gate
applies only to a research-bearing invocation of `check-etf-performance` that
will write durable performance outputs. State explicitly that read-only chat
and every other workflow must not dispatch `source_verifier`.

- [ ] **Step 2: Preserve the evidence packet requirements**

Keep the required packet fields, but describe them in ETF-performance terms:
candidate performance claims, return basis, benchmark, dates, units/currency,
calculations, source URLs/paths, gaps, and complete proposed performance files.

- [ ] **Step 3: Preserve verdict and fallback behavior**

Keep `PASS`, `CHANGES_REQUIRED`, `WARNING`, the single-writer rule, and the
local fallback checklist, while scoping each rule to the conditional
`check-etf-performance` gate.

- [ ] **Step 4: Check the gate text before editing the agent**

Run:

```bash
sed -n '25,75p' AGENTS.md
rg -n "before writing any durable|every durable|source_verifier|check-etf-performance" AGENTS.md
```

Expected: the gate names `check-etf-performance`; no sentence requires
`source_verifier` for every durable file.

### Task 2: Narrow the custom agent's role and fail closed

**Files:**
- Modify: `.codex/agents/source-verifier.toml:1-80`

**Interfaces:**
- Consumes: an evidence packet explicitly identified as coming from
  `check-etf-performance`.
- Produces: the existing structured review report for ETF performance only.

- [ ] **Step 1: Narrow the identity and description**

Set the description to identify `source_verifier` as an independent,
read-only reviewer for `check-etf-performance` ETF performance evidence before
durable save. Remove the broad `stock-second-brain` reviewer wording.

- [ ] **Step 2: Add an explicit scope gate**

At the beginning of `developer_instructions`, require an exact workflow marker
such as `workflow: check-etf-performance` in the parent packet. If the marker
is missing or names another workflow, do not perform source analysis; return a
structured `CHANGES_REQUIRED` report stating that the packet is out of scope
and must not be routed to this agent.

- [ ] **Step 3: Limit review criteria to ETF performance**

Retain checks for issuer/exchange identity, NAV/price total return, benchmark,
calendar-year returns, CAGR, drawdown, recovery, distributions, expense ratio,
return basis, as-of dates, source reconciliation, and calculations. Explicitly
exclude standalone stock financials, DCF, thesis/decision, market-move,
sentiment, source-integrity audits, and ETF fund facts/holdings/methodology
unless they are directly needed to validate the ETF performance packet.

- [ ] **Step 4: Preserve read-only and verdict contract**

Keep `sandbox_mode = "read-only"`, the source hierarchy, severity definitions,
and exact report sections. Ensure no instruction permits writing, staging, or
editing project files.

- [ ] **Step 5: Validate TOML syntax**

Run:

```bash
python3 -c 'import tomllib; from pathlib import Path; p=Path(".codex/agents/source-verifier.toml"); d=tomllib.loads(p.read_text()); assert d["name"] == "source_verifier"; assert d["sandbox_mode"] == "read-only"; assert "check-etf-performance" in d["description"]; assert "check-etf-performance" in d["developer_instructions"]; print("valid scoped source verifier TOML")'
```

Expected: `valid scoped source verifier TOML`.

### Task 3: Record the configuration workflow

**Files:**
- Modify: `log.md` under a new `## 2026-08-10` heading

**Interfaces:**
- Consumes: the completed `AGENTS.md` and agent-scope changes.
- Produces: one concise chronological workflow entry.

- [ ] **Step 1: Add one dated log bullet**

Record that `source_verifier` was restricted to `check-etf-performance` ETF
performance saves, that other workflows no longer dispatch it, and that TOML,
reference-scan, and whitespace checks passed. Do not add one bullet per file.

### Task 4: Verify the complete scope boundary

**Files:**
- Validate: `AGENTS.md`, `.codex/agents/source-verifier.toml`, `log.md`, and the approved design spec

**Interfaces:**
- Consumes: all changes from Tasks 1–3.
- Produces: a clean, scoped diff ready for commit.

- [ ] **Step 1: Scan all project references**

Run:

```bash
rg -n --hidden --glob '!*.git*' "source_verifier|source-verifier|check-etf-performance" AGENTS.md .codex/agents .codex/skills log.md
```

Expected: only the ETF-performance gate in `AGENTS.md`, the ETF-performance
agent instructions, and historical/log references remain; no broad pre-save
directive remains.

- [ ] **Step 2: Check whitespace and status**

Run:

```bash
git diff --check
git status --short
```

Expected: no whitespace errors and only the scoped files are modified after
the already-committed spec.

- [ ] **Step 3: Review the final diff**

Run:

```bash
git diff -- AGENTS.md .codex/agents/source-verifier.toml log.md
```

Confirm the diff does not alter ETF performance calculations, research
delegation, or unrelated source-integrity behavior.

- [ ] **Step 4: Commit the implementation**

Run:

```bash
git add -- AGENTS.md .codex/agents/source-verifier.toml log.md
git commit -m "fix: limit source verifier to ETF performance"
```

Expected: one non-empty commit containing only the implementation files.
