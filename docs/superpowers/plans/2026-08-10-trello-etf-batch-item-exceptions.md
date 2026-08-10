# Trello ETF Batch Item Exceptions Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update the Trello ETF batch coordinator so explicit ETF-level failures create a reasoned child exception card in `Blocked`, check the handled queue item, continue within the current batch, and release unfinished parents to `Ready for AI` after `batch_size`.

**Architecture:** Keep the existing four-state parent claim machine and one-ticker `check-etf-performance` handoff. Change checklist semantics from success-only to handled-item state, use open exception cards as the retry source for checked blocked items, and preserve parent blocking only for global or user-action-required terminal/confirmation conditions. Keep the scheduler limited to `Ready for AI` so no running claim is resumed concurrently.

**Tech Stack:** Markdown skill contract, Bash static contract tests, Codex Trello automation connector.

## Global Constraints

- The card's `batch_size` remains authoritative; the coordinator processes up to that many eligible ETFs sequentially.
- Successful ETFs do not create child cards; explicit item-level failures create/reuse exactly one exception card with parent identity metadata.
- A checklist item is checked only after successful durable work or after the exception card is completely written and moved to `Blocked`.
- Global failures never create a ticker exception or check the affected queue item.
- The coordinator does not write ETF performance pages, source batches, entities, or logs.
- The automation prompt must preserve one parent per run and prohibit overlapping workers.

---

### Task 1: Add failing static contract coverage

**Files:**
- Create: `.codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh`
- Modify: `.codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh`

**Interfaces:**
- Consumes: `.codex/skills/trello-etf-batch/SKILL.md` as the first command-line argument or its default path.
- Produces: shell tests that fail against the old success-only checklist and unchecked item-block contract.

- [ ] **Step 1: Write the new failing test**

Create `test_item_exception_contract.sh` with `set -euo pipefail`, an
`assert_contains` helper, and assertions for:

```bash
assert_contains 'A checked item means the ticker has been handled'
assert_contains 'matching `ETF queue` checklist item checked'
assert_contains 'Move the exception card to the configured `Blocked` list'
assert_contains 'continue to the next unattempted eligible ticker'
assert_contains 'checked item with an open matching exception'
assert_contains 'all items checked and no open exception'
assert_contains 'unfinished normal work remains'
assert_contains 'eligible retryable exception remains'
assert_contains 'only terminal or unconfirmed confirmation exceptions remain'
assert_contains 'leaves the affected checklist item unchanged'
assert_contains 'scheduler continues to inspect only `Ready for AI`'
```

Add `assert_not_contains` and require these old contradictory phrases to be
absent:

```bash
assert_not_contains 'A checked item means the downstream performance workflow explicitly returned success for that ticker.'
assert_not_contains 'On an explicit downstream item-level failure, leave the item unchecked'
```

- [ ] **Step 2: Extend the existing batch-size test**

Append assertions to `test_batch_size_contract.sh` for:

```bash
assert_contains 'create or reuse exactly one exception card'
assert_contains 'checks that queue item'
assert_contains 'allows the current batch to continue'
assert_contains 'release a non-terminal parent back to Ready for AI'
```

- [ ] **Step 3: Run the tests and verify RED**

Run:

```bash
bash .codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh
bash .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh
```

Expected: the new test fails on missing new contract language and no skill
file has been changed yet.

---

### Task 2: Implement the item-exception continuation contract

**Files:**
- Modify: `.codex/skills/trello-etf-batch/SKILL.md`

**Interfaces:**
- Consumes: the approved design at `docs/superpowers/specs/2026-08-10-trello-etf-batch-item-exceptions-design.md`.
- Produces: the authoritative coordinator instructions for future invocations.

- [ ] **Step 1: Replace checklist semantics**

Document that a checked item means handled by downstream success or by a
successful item-level exception-card mutation. State that an open matching
exception means handled but not successfully cleared and prevents `Done`.

- [ ] **Step 2: Expand pending-set definitions**

Keep `normal_pending` limited to unchecked tickers without open exceptions.
Allow `retry_pending` selection from checked tickers with an open
non-terminal exception whose confirmation is `none` or `confirmed`.
Define confirmation and terminal pending from open exception metadata rather
than requiring the queue item to be unchecked.

- [ ] **Step 3: Change item-level failure ordering**

For each explicit item block, keep the parent claim, create or reuse one
standard exception, write complete metadata including `reason`, move it to
`Blocked`, then check the matching queue item. Only after those mutations,
add `attempted_this_run`, increment `processed_count`, and continue while
capacity remains. A failed exception mutation is global and must not check the
item.

- [ ] **Step 4: Update retry and finalization**

State that checked queue items may be retried through open exception identity.
Require every queue item checked and zero open exceptions before `Done`.
Release unfinished normal work or retryable exceptions to `Ready for AI`
after batch capacity with the derived retry flag. Preserve `Blocked` for
terminal/confirmation-only queues and global failures.

- [ ] **Step 5: Update exception and automation language**

Describe exception cards as Trello child records linked by `parent_ari` and
`parent_url`; prohibit child cards for successes. Update the recurring
automation contract to say item-level blocks are checked, the current batch
continues, and unfinished non-terminal parents return to `Ready for AI`.

- [ ] **Step 6: Run focused verification**

Run both static tests and:

```bash
git diff --check -- .codex/skills/trello-etf-batch/SKILL.md .codex/skills/trello-etf-batch/tests
```

Expected: both tests exit `0`, old contradictory phrases are absent, and
the diff is scoped to the documented contract.

---

### Task 3: Align the scheduled automation prompt

**Files:**
- External automation: `loops-trello-etf-batch` prompt through
  `codex_app__automation_update`.

**Interfaces:**
- Consumes: the current automation configuration and updated skill contract.
- Produces: a scheduler prompt that selects one parent from `Ready for AI`,
  respects the parent's `batch_size`, and describes child exceptions.

- [ ] **Step 1: Preserve current automation fields**

Read the current automation configuration and retain its id, name, schedule,
model, reasoning effort, project target, and status. Change only the prompt.

- [ ] **Step 2: Update prompt behavior**

Keep exact-field validation, oldest eligible parent selection, Ready-only
inspection, no running-parent selection, and no overlapping workers. Replace
the hard-coded one-ETF sentence with card-authoritative `batch_size`
language: item-level blocks create/update one child in `Blocked`, check the
queue item, continue within the batch, and release unfinished non-terminal
parents to `Ready for AI`.

- [ ] **Step 3: Read back the automation**

Confirm the saved prompt contains the child/checklist/release language and no
instruction to resume an `In Progress` parent.

---

### Task 4: Regression verification and commit

**Files:**
- Modify: `.codex/skills/trello-etf-batch/SKILL.md`
- Modify: `.codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh`
- Create: `.codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh`

**Interfaces:**
- Consumes: completed Tasks 1–3.
- Produces: a committed implementation with passing static tests and a scoped diff.

- [ ] **Step 1: Run focused tests**

```bash
bash .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh
bash .codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh
```

Expected: both commands exit `0` with no assertion failures.

- [ ] **Step 2: Run syntax and whitespace checks**

```bash
bash -n .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh
bash -n .codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh
git diff --check
```

Expected: all commands exit `0`.

- [ ] **Step 3: Review scope**

```bash
git status --short
git diff --stat
```

Stage only the skill and its two contract tests; do not restage the committed
design or plan.

- [ ] **Step 4: Commit**

```bash
git add .codex/skills/trello-etf-batch/SKILL.md \
  .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh \
  .codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh
git commit -m "feat: continue ETF batches after item blocks"
```

Expected: one non-empty implementation commit containing only the coordinator
contract and static tests.
