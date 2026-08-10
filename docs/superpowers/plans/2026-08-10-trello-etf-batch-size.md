# Trello ETF Batch Size Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `trello-etf-batch` read a parent card's optional `batch_size: N` and process up to that many ETFs sequentially in one claimed automation run.

**Architecture:** Keep `check-etf-performance` as a single-ticker durable worker. Extend the Trello coordinator's pre-claim configuration validation and execution loop so one parent claim covers up to `batch_size` item attempts, with per-item checklist/exception updates and one final parent transition.

**Tech Stack:** Markdown skill contract, POSIX shell static contract test, `rg`, Git.

## Global Constraints

- The exact parent Trello URL/ARI remains required; no board-wide parent discovery.
- `batch_size` is read only from the parent description and is authoritative.
- Missing `batch_size` preserves the existing default of `1`.
- Each ETF still invokes `$check-etf-performance <TICKER>` separately with `mode: lean`.
- ETF processing is sequential; no concurrent durable writers are introduced.
- Global failures stop and block the owned parent; item failures create/reuse one exception and may consume a batch slot.
- The downstream skill remains the sole writer of ETF performance vault outputs.

---

### Task 1: Add a failing batch-size contract test

**Files:**
- Create: `.codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh`

**Interfaces:**
- Consumes: `.codex/skills/trello-etf-batch/SKILL.md` from the repository root.
- Produces: exit code `0` only when the skill contains the required batch-size contract anchors.

- [ ] **Step 1: Write the failing test**

```bash
#!/usr/bin/env bash
set -euo pipefail

skill_file="${1:-.codex/skills/trello-etf-batch/SKILL.md}"

assert_contains() {
  local needle="$1"
  rg -Fq "$needle" "$skill_file" || {
    echo "missing contract: $needle" >&2
    exit 1
  }
}

assert_contains 'batch_size: <positive integer>'
assert_contains 'If it is absent, default to `1`'
assert_contains 'The card value is authoritative'
assert_contains 'up to `batch_size` items'
assert_contains 'sequentially'
assert_contains 'while batch capacity remains'
assert_contains 'respect the parent card’s `batch_size`'
```

- [ ] **Step 2: Run the test and verify the expected failure**

Run:

```bash
bash .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh
```

Expected: FAIL because the current skill still hard-codes one automation item and has no `batch_size` contract.

### Task 2: Extend the Trello coordinator contract and loop

**Files:**
- Modify: `.codex/skills/trello-etf-batch/SKILL.md` in the card contract, execution loop, failure classification, automation contract, and completion response sections.

**Interfaces:**
- Consumes: parent description lines containing `batch_size: N`.
- Produces: a validated effective batch size and sequential per-ticker downstream handoffs under one parent claim.

- [ ] **Step 1: Add card configuration parsing and validation**

Add `batch_size: <positive integer>` as an optional one-line card key. State that absent means `1`, duplicate/conflicting/non-integer/non-positive values are pre-claim `workflow-config-mismatch`, and the card value is authoritative over generic scheduler wording. Do not infer a size from title, list, or queue length.

- [ ] **Step 2: Define the per-run capacity**

After building the canonical queue and before claiming, resolve `effective_batch_size` from the card. During the owned run, keep an in-memory `attempted_this_run` set and a `processed_count`; the loop may select at most `effective_batch_size` distinct queue items, or fewer when no eligible item remains.

- [ ] **Step 3: Update selection and downstream invocation semantics**

Preserve retry priority and recompute pending sets after every item. For each selected ticker, invoke the existing single-ticker `$check-etf-performance <TICKER>` handoff with `mode: lean`, wait for the complete envelope, and update that ticker's checklist/exception state before selecting the next ticker.

- [ ] **Step 4: Update failure behavior**

Make global failures stop the batch immediately. For explicit item-level failures, leave the item unchecked, create/reuse the exception card, add the ticker to `attempted_this_run`, and continue while capacity remains. Keep confirmation-pending and terminal exceptions out of downstream calls.

- [ ] **Step 5: Update finalization and automation wording**

Keep the parent claim through the whole bounded loop. After the final slot or exhausted queue, apply the existing done/blocked/release rules. Replace “exactly one” automation wording with an instruction to process up to the parent card's `batch_size` sequentially, while retaining the no-overlap rule. Report all attempted tickers and aggregate counts.

### Task 3: Run focused verification and inspect the diff

**Files:**
- Test: `.codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh`
- Inspect: `.codex/skills/trello-etf-batch/SKILL.md`

**Interfaces:**
- Consumes: the updated skill and contract test.
- Produces: verified exit code `0`, no stale one-item automation instructions, and a focused diff containing only the requested behavior plus its test.

- [ ] **Step 1: Run the focused contract test**

Run:

```bash
bash .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh
```

Expected: PASS with exit code `0`.

- [ ] **Step 2: Scan for contradictory one-item wording**

Run:

```bash
rg -n "exactly one eligible ETF|stop after that ETF|after this one item|single ticker invocation|batch_size|up to" .codex/skills/trello-etf-batch/SKILL.md
```

Expected: single-ticker wording remains only for each downstream handoff/envelope, while automation and loop wording uses the card-controlled batch size.

- [ ] **Step 3: Inspect repository state and commit scoped changes**

Run:

```bash
git diff --check
git status --short
git diff -- .codex/skills/trello-etf-batch/SKILL.md .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh
```

Expected: no whitespace errors; only the coordinator and focused test are uncommitted after the already committed design/plan documents.
