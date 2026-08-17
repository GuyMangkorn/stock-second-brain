# Active Equity ETF Performance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend `check-etf-performance` to support active long-only equity ETFs with benchmark-relative management evidence, then safely requeue the exact DISV Trello child card.

**Architecture:** Keep one ETF-performance entry point with explicit `passive-index` and `active-equity-long-only` classification branches. Preserve the existing research profiles, durable-write review gate, and seven-field Trello handoff; add active-specific benchmark, excess-return, track-record, and risk-evidence contracts inside the performance skill only.

**Tech Stack:** Markdown skill contracts, YAML skill interface metadata, Bash/Ripgrep static contract tests, Python `quick_validate.py`, Git, Codex Trello connector.

## Global Constraints

- Support active long-only public-equity ETFs only; continue rejecting bond, commodity, currency, multi-asset, leveraged, inverse, defined-outcome, covered-call, option-income, single-stock option, and derivative-heavy ETFs.
- Keep `official-source-etf-research` and other ETF v1 research routes passive/index-only.
- Preserve `execution_profile: interactive-delegated|scheduled-inline` behavior exactly; scheduled-inline must not dispatch any worker, reviewer, or `source_verifier`.
- Preserve the complete seven-field `trello_handoff` and Trello result-router decision matrix.
- Never call arithmetic excess return `alpha`; use identical periods, currencies, and total-return bases for every comparison.
- Preserve unrelated dirty-worktree changes and stage only files owned by this implementation.
- Do not move DISV until all local validation passes; directly confirm every Trello read and mutation.

---

### Task 1: Add the Active-ETF Contract Test

**Files:**
- Create: `scripts/test_active_equity_etf_performance_contract.sh`
- Read: `/Users/mangkornkatawong/.codex/skills/check-etf-performance/SKILL.md`
- Read: `/Users/mangkornkatawong/.codex/skills/check-etf-performance/workflow.md`
- Read: `AGENTS.md`

**Interfaces:**
- Consumes: the current user-level `check-etf-performance` skill and project rules.
- Produces: one deterministic shell test returning exit code `0` only when the active-long-only classification, metrics, review fields, and scheduled-inline safeguards are all present.

- [ ] **Step 1: Create the static contract test**

Create `scripts/test_active_equity_etf_performance_contract.sh` with executable content:

```bash
#!/usr/bin/env bash
set -euo pipefail

project_root="/Users/mangkornkatawong/Documents/STOCK_PROJECT/stock-second-brain"
skill_root="/Users/mangkornkatawong/.codex/skills/check-etf-performance"
skill_file="$skill_root/SKILL.md"
workflow_file="$skill_root/workflow.md"
rules_file="$project_root/AGENTS.md"

assert_contains() {
  local file_path="$1"
  local expected="$2"
  if ! grep -Fq -- "$expected" "$file_path"; then
    echo "missing contract text in $file_path: $expected" >&2
    exit 1
  fi
}

assert_contains "$skill_file" 'active-equity-long-only'
assert_contains "$skill_file" 'passive-index'
assert_contains "$skill_file" 'systematic-active'
assert_contains "$skill_file" 'management_benchmark'
assert_contains "$skill_file" 'Excess CAGR'
assert_contains "$skill_file" 'positive return-only'
assert_contains "$skill_file" 'negative return-only'
assert_contains "$skill_file" 'risk-adjusted evidence not verified'
assert_contains "$skill_file" 'covered-call'
assert_contains "$skill_file" 'reviewer_dispatch: not-attempted-by-design'

assert_contains "$workflow_file" 'Management mode'
assert_contains "$workflow_file" 'Active process subtype'
assert_contains "$workflow_file" 'Management benchmark selection reason'
assert_contains "$workflow_file" 'Risk-adjusted evidence'
assert_contains "$workflow_file" 'scheduled-local'

assert_contains "$rules_file" 'active long-only equity ETFs'
assert_contains "$rules_file" 'official-source-etf-research'

echo 'active equity ETF performance contract: PASS'
```

- [ ] **Step 2: Run the test and verify the current contract fails**

Run:

```bash
bash scripts/test_active_equity_etf_performance_contract.sh
```

Expected: non-zero exit with the first missing active-equity contract string, currently `active-equity-long-only`.

---

### Task 2: Extend the ETF Performance Skill

**Files:**
- Modify: `/Users/mangkornkatawong/.codex/skills/check-etf-performance/SKILL.md`
- Test: `scripts/test_active_equity_etf_performance_contract.sh`

**Interfaces:**
- Consumes: `$check-etf-performance <TICKER>`, `mode`, `caller`, `handoff`, and validated `execution_profile` exactly as before.
- Produces: either a supported `passive-index` or `active-equity-long-only` performance result, or an existing normalized item/global failure envelope.

- [ ] **Step 1: Expand the trigger and classification gate**

Update the frontmatter description to include active equity performance and replace the passive-only guardrail with this contract:

```markdown
- Classify supported equity ETFs as `passive-index` or
  `active-equity-long-only` from an official prospectus or issuer regulatory
  document before collecting performance.
- `active-equity-long-only` requires long public equity to be the principal
  return source. Classify its process as `systematic-active`,
  `fundamental-active`, or `other-active`, and record disclosed adviser/team
  continuity.
- Return `unsupported ETF type` for bond, commodity, currency, multi-asset,
  leveraged, inverse, defined-outcome, covered-call, option-income,
  single-stock option, or other derivative-heavy funds. Incidental derivatives
  used for equitization, settlement, FX transfer, or risk management do not by
  themselves disqualify an otherwise long-only equity strategy.
- Return an item hard-data gap when official evidence cannot resolve the
  classification; never infer eligibility from a ticker, benchmark, or
  secondary label alone.
```

- [ ] **Step 2: Add active benchmark selection rules**

Insert an active benchmark contract after the existing source rules:

```markdown
### Active management benchmark

For `active-equity-long-only`, select `management_benchmark` before comparing
returns, in this order: (1) an official performance-table index explicitly
described as having a similar investment universe or strategy; (2) the
issuer-designated strategy-aligned comparative benchmark; (3) the official
broad-market benchmark when no closer official comparator is disclosed.
Record the selection reason and every rejected official alternative. Do not
select a comparator after observing performance.

Keep `S&P 500 Total Return` as the common reference benchmark under the
existing convention. Do not use it as evidence of active-management value
unless it is also the strategy-appropriate official comparator.
```

- [ ] **Step 3: Add active return and risk calculations**

Add these definitions to `Return And Risk Rules`:

```markdown
- Active annual return in percentage points:
  `Fund NAV TR - Management Benchmark TR` for identical calendar rows.
- `Excess CAGR = Fund CAGR - Management Benchmark CAGR` over identical
  endpoints and in percentage points.
- Cumulative relative wealth:
  `(1 + Fund cumulative return) / (1 + Benchmark cumulative return) - 1`.
- Annual hit rate: complete comparable years with active return `> 0`, divided
  by all complete comparable years. Treat a zero active-return year as not an
  outperformance.
- Calculate max drawdown, downside capture, tracking error, or Information
  Ratio only from compatible periodic total-return observations. Otherwise
  report `risk-adjusted evidence not verified`.
- Never label arithmetic excess return as `alpha`. Regression alpha requires a
  documented factor model and reproducible compatible-period regression.
```

- [ ] **Step 4: Add deterministic track-record and evidence labels**

Add the approved elapsed-history and management-evidence rules verbatim:

```markdown
- `track_record: insufficient` for less than three comparable elapsed years,
  `provisional` for at least three but less than five, and `established` for at
  least five.
- `management_evidence: positive` when Excess CAGR is positive and complete-
  year hit rate is at least 50%; use `positive return-only` when Excess CAGR is
  positive but compatible hit rate is unavailable.
- `management_evidence: negative` when Excess CAGR is non-positive and hit
  rate is below 50%; use `negative return-only` when Excess CAGR is negative
  but compatible hit rate is unavailable.
- Use `mixed` when Excess CAGR and hit rate disagree or no other supported
  label applies. Use `insufficient` when track record is under three comparable
  years or management-benchmark return is not verified.
- Keep `risk_evidence: positive|mixed|negative|not-verified` separate. Do not
  upgrade return-only evidence into a claim of manager skill.
```

- [ ] **Step 5: Extend the conditional output and durable-save contract**

Add these fields under `Performance check` only for active funds:

```text
management_mode: active-equity-long-only
active_process: systematic-active|fundamental-active|other-active
management_benchmark: <official strategy-aligned comparator>
track_record: insufficient|provisional|established
management_evidence: positive|positive return-only|mixed|negative|negative return-only|insufficient
risk_evidence: positive|mixed|negative|not-verified
```

Require an `Active management read-through` subsection covering excess return,
hit rate, risk evidence, expense ratio, turnover, and team/process continuity.
Preserve passive output unchanged. Permit active rows in `ETF Performance
Index.md` only with visible management mode and identical-period/return-basis
ranking rules; preserve the historical passive `2016-2025` ranking.

- [ ] **Step 6: Run the contract test and confirm only workflow/project-rule assertions remain**

Run:

```bash
bash scripts/test_active_equity_etf_performance_contract.sh
```

Expected: non-zero exit after all `SKILL.md` assertions pass, with the next
missing string in `workflow.md` or `AGENTS.md`.

---

### Task 3: Extend the Pre-Save Review Contract and Interface Metadata

**Files:**
- Modify: `/Users/mangkornkatawong/.codex/skills/check-etf-performance/workflow.md`
- Modify: `/Users/mangkornkatawong/.codex/skills/check-etf-performance/agents/openai.yaml`
- Test: `scripts/test_active_equity_etf_performance_contract.sh`

**Interfaces:**
- Consumes: the same research evidence packet and proposed durable files.
- Produces: the same `PASS|CHANGES_REQUIRED` review verdict after validating active classification, benchmark selection, calculations, and attribution.

- [ ] **Step 1: Extend the evidence packet**

Replace the passive-only classification field and add these fields:

```markdown
- Management mode: `passive-index` | `active-equity-long-only` | unsupported
- Active process subtype: `systematic-active` | `fundamental-active` |
  `other-active` | not applicable
- Active eligibility evidence: principal asset class, derivative role, and
  official source
- Management benchmark selection reason: selected official comparator,
  hierarchy step, alternatives, currency, return basis, and index-change history
- Active calculations: matching endpoints, Excess CAGR, annual active returns,
  hit rate, cumulative relative wealth, and all inputs
- Track record: elapsed years and `insufficient|provisional|established`
- Management evidence: return label plus rationale
- Risk-adjusted evidence: metrics and inputs or `not-verified`
- Adviser/team continuity and attribution caveat: ...
```

- [ ] **Step 2: Extend the reviewer checklist**

Require the reviewer/local checklist to verify:

```markdown
- Confirm active long-only eligibility from official strategy and derivative
  disclosures; reject payoff-defining options, leverage, inverse, buffer,
  single-stock, and multi-asset structures.
- Confirm `management_benchmark` follows the documented hierarchy and was not
  selected after observing performance.
- Recompute Excess CAGR, annual active returns, hit rate, relative wealth, and
  every claimed risk metric from identical periods, currencies, and total-
  return definitions.
- Confirm elapsed-history and management-evidence labels follow the deterministic
  thresholds and that return-only evidence is not described as manager skill.
- Confirm process/team attribution matches verified tenure and continuity.
```

Keep the exact scheduled-inline audit lines and all dispatch prohibitions
unchanged.

- [ ] **Step 3: Synchronize UI metadata**

Update `agents/openai.yaml` to:

```yaml
interface:
  display_name: "ETF Performance Check"
  short_description: "Compare passive and active equity ETF performance"
  default_prompt: "Use $check-etf-performance for [TICKER], save its fresh ETF performance page, and evaluate active management against an official strategy benchmark when applicable."

policy:
  allow_implicit_invocation: true
```

- [ ] **Step 4: Run the contract test and confirm only project-rule assertions remain**

Run:

```bash
bash scripts/test_active_equity_etf_performance_contract.sh
```

Expected: non-zero exit naming the missing `AGENTS.md` active-performance scope
text; all user-level skill and workflow assertions pass.

---

### Task 4: Update Project Scope and Validate the Implementation

**Files:**
- Modify: `AGENTS.md:178-206`
- Modify: `AGENTS.md:286-288`
- Modify: `docs/superpowers/specs/2026-08-17-active-equity-etf-performance-design.md`
- Test: `scripts/test_active_equity_etf_performance_contract.sh`
- Validate: `/Users/mangkornkatawong/.codex/skills/check-etf-performance/`

**Interfaces:**
- Consumes: the expanded user-level performance skill.
- Produces: project routing rules that permit active long-only equity only in `check-etf-performance`, while preserving passive-only deep-dive routes.

- [ ] **Step 1: Update the ETF performance rule**

Replace the opening ETF-performance sentence with:

```markdown
Use `check-etf-performance` for passive index-tracking and active long-only
equity ETFs. Classify active funds from official strategy documents and assess
management evidence against an official strategy-aligned benchmark; keep raw
Total Return separate from excess return and risk-adjusted evidence.
```

Add that active-only performance pages expose management mode, benchmark,
track-record maturity, management evidence, and risk-evidence status. Preserve
the cached S&P convention and region navigation rules.

- [ ] **Step 2: Split the project-level ETF v1 scope**

Replace the global passive-only sentence with:

```markdown
ETF research v1 (`official-source-etf-research` and its decision/deep-dive
routes) supports passive, index-tracking equity ETFs only. The
`check-etf-performance` workflow additionally supports active long-only equity
ETFs. Return `unsupported ETF type` for bond, commodity, currency, multi-asset,
leveraged, inverse, defined-outcome, covered-call, option-income, single-stock
option, or derivative-heavy funds.
```

- [ ] **Step 3: Run the static contract test**

Run:

```bash
bash scripts/test_active_equity_etf_performance_contract.sh
```

Expected: `active equity ETF performance contract: PASS`.

- [ ] **Step 4: Validate skill metadata and contract integrity**

Run:

```bash
python3 /Users/mangkornkatawong/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/mangkornkatawong/.codex/skills/check-etf-performance
rg -n "passive, index-tracking equity ETFs only|active-equity-long-only|unsupported ETF type|scheduled-inline|reviewer_dispatch: not-attempted-by-design" AGENTS.md /Users/mangkornkatawong/.codex/skills/check-etf-performance
git diff --check -- AGENTS.md scripts/test_active_equity_etf_performance_contract.sh docs/superpowers/specs/2026-08-17-active-equity-etf-performance-design.md
```

Expected: skill validation success; active support appears only in the
performance route; scheduled-inline safeguards and unsupported structures
remain present; no whitespace errors.

- [ ] **Step 5: Inspect status and commit only implementation-owned project files**

Run:

```bash
git status --short
git diff -- AGENTS.md scripts/test_active_equity_etf_performance_contract.sh docs/superpowers/specs/2026-08-17-active-equity-etf-performance-design.md
git add -- AGENTS.md scripts/test_active_equity_etf_performance_contract.sh docs/superpowers/specs/2026-08-17-active-equity-etf-performance-design.md
git diff --cached --check
git commit -m "feat: support active equity ETF performance"
```

Expected: only the three listed project files are staged and committed;
unrelated ETF performance/index/source/log changes remain unstaged.

---

### Task 5: Requeue the Exact DISV Trello Child

**Files:**
- No local file changes.

**Interfaces:**
- Consumes: one exact open Trello child with title `DISV`, lane `Blocked`, valid `workflow: trello-etf-item`, nonempty `parent_ari`, `ticker: DISV`, and `result_code: unsupported-etf-type` caused by active management.
- Produces: the same child in `Ready for AI` with identity preserved, stale result fields removed, and `retry_reason: active-equity-long-only-support-enabled` recorded.

- [ ] **Step 1: Resolve and verify exactly one target**

Use Trello card search for `DISV`, then direct-read every exact-name candidate.
Require exactly one card satisfying all of:

```text
name: DISV
list: Blocked
workflow: trello-etf-item
parent_ari: <nonempty exact ARI>
ticker: DISV
result_code: unsupported-etf-type
result_reason: <active-management scope reason>
```

Expected: one exact card ARI and its board ARI. Stop without mutation on zero,
multiple, malformed, or changed-state matches.

- [ ] **Step 2: Resolve the destination list**

List the exact board's open lists and require exactly one list named
`Ready for AI`. Preserve its Trello list ARI. Stop without mutation on zero or
multiple matches.

- [ ] **Step 3: Clear stale result metadata while the card is still blocked**

Build a new description by preserving all existing lines except:

```text
result_status:
result_scope:
result_code:
result_reason:
durable_write:
confirmation:
retry_reason:
```

Append exactly:

```text
retry_reason: active-equity-long-only-support-enabled
```

Update only the exact card description, directly reread it, and verify the
identity lines and retry reason are present while every stale result field is
absent. If confirmation fails, stop without moving the card.

- [ ] **Step 4: Move and confirm the exact card**

Move the exact card ARI to the resolved `Ready for AI` list ARI. Directly reread
the card and require its confirmed list name to be `Ready for AI`, with
`workflow`, `parent_ari`, `ticker`, and `retry_reason` intact.

Do not invoke `trello-etf-processing`, run ETF research, or claim a durable
write. The next scheduled manager run owns claim, research, review, and result
routing.

- [ ] **Step 5: Report the confirmed handoff state**

Report the exact DISV card ID/URL, confirmed final lane, preserved identity,
removed stale result metadata, validation commands, and implementation commit.
If any mutation was not confirmed, report its actual last-confirmed state and
do not claim successful requeue.
