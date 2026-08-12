# Trello ETF Batch Item Errors Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (or superpowers:subagent-driven-development) to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Route ticker-scoped downstream `ERROR` results through the same child-card, checklist, and continue flow as item blockers, while preserving global stops for coordinator/state failures.

**Architecture:** Keep Trello mutation ownership in `trello-etf-batch`. Extend the closed handoff mapping so a selected single-ticker `ERROR` with `research-sub-agent-unavailable` or `item-downstream-error` becomes a retryable item exception even when the downstream reports `scope:global`; `scope:unknown`, invalid envelopes, global codes, and Trello/claim/configuration failures remain global. Mirror the contract in the local automation prompt and update the installed automation prompt through the automation tool.

**Tech Stack:** Markdown skill contracts, Bash/Ripgrep static contract tests, Codex automation tool, Trello connector.

## Global Constraints

- Create/reuse exactly one `[BLOCKED][ETF] <TICKER> | check-etf-performance` child for accepted item-level failures.
- Write complete child metadata before moving the child to `Blocked`.
- Check only the matching ETF queue item after child mutation succeeds.
- Continue to the next eligible ticker while `batch_size` capacity remains.
- Treat `scope:unknown`, global codes, Trello/tool/auth/board-list/configuration/input/checklist/claim and exception-card mutation failures as global.
- Do not create durable ETF vault outputs in the coordinator.

---

### Task 1: Add the failing item-error contract test

**Files:**
- Create: `.codex/skills/trello-etf-batch/tests/test_item_error_contract.sh`
- Test: `.codex/skills/trello-etf-batch/SKILL.md` and `.codex/skills/trello-etf-batch/automation-prompt.md`

**Interfaces:**
- Consumes: the current skill and automation prompt text.
- Produces: a repeatable contract test proving item-level `ERROR` routing is documented.

- [ ] **Step 1: Write the failing test**

Create a shell test that accepts a skill path and an optional automation-prompt path, then asserts:

```bash
assert_contains 'ERROR + `scope: item`'
assert_contains '`research-sub-agent-unavailable` may be item-level'
assert_contains 'item-level error'
assert_contains 'create or reuse exactly one exception card'
assert_contains 'check only the matching `ETF queue` item'
assert_contains 'continue to the next eligible ticker'
assert_contains 'Trello/tool/auth failures remain global'
assert_not_contains 'any `status: ERROR` is always global'
```

Run the same assertions against `automation-prompt.md` using its own helper.

- [ ] **Step 2: Run the test to verify it fails**

Run:

```bash
bash .codex/skills/trello-etf-batch/tests/test_item_error_contract.sh
```

Expected: `FAIL` with a missing item-level `ERROR` contract because the current skill treats every `status: ERROR` as global.

- [ ] **Step 3: Commit the red test**

```bash
git add .codex/skills/trello-etf-batch/tests/test_item_error_contract.sh
git commit -m "test: require item-level ETF error routing"
```

### Task 2: Extend the coordinator skill contract

**Files:**
- Modify: `.codex/skills/trello-etf-batch/SKILL.md`

**Interfaces:**
- Consumes: the existing normalized downstream handoff envelope.
- Produces: an explicit item-level `ERROR` mapping and unchanged global mutation-failure boundary.

- [ ] **Step 1: Update blocker routing and failure classification**

Document that a selected single-ticker `ERROR` with `scope:item` or a reported `scope:global`, `durable_write:not_completed`, `exhausted:false`, and `confirmation:none` is accepted only with `research-sub-agent-unavailable` or `item-downstream-error`. State that the coordinator normalizes it to retryable `item_blocked`, writes `terminal:false`, moves the child to `Blocked`, checks the matching queue item after child mutation, increments `processed_count`, and continues.

Replace the blanket rule that every `status: ERROR` is global with a precedence rule: `scope:unknown`, global codes, missing/contradictory fields, and coordinator/Trello state failures remain global; only the explicit single-ticker error envelope may normalize a reported `scope:global` to item-level.

- [ ] **Step 2: Update execution and retry language**

Ensure the execution loop says the item-level `ERROR` branch uses the same child-card mutation order as other item blockers, and that an open item-error child is retryable and excluded from `Done` until closed by a later successful downstream run.

- [ ] **Step 3: Run the new contract test**

Run:

```bash
bash .codex/skills/trello-etf-batch/tests/test_item_error_contract.sh
```

Expected: `PASS` for the skill assertions; prompt assertions remain red until Task 3.

### Task 3: Mirror the behavior in the automation prompt

**Files:**
- Modify: `.codex/skills/trello-etf-batch/automation-prompt.md`

**Interfaces:**
- Consumes: the coordinator contract from Task 2.
- Produces: scheduler instructions that invoke the item-error child/check/continue flow.

- [ ] **Step 1: Add the item-level ERROR branch**

Add the explicit accepted envelope and required mutation order under the item-level blocker branch. State that `research-sub-agent-unavailable` from a single ticker downstream call is item-scoped when the downstream handoff says `scope:item`.

- [ ] **Step 2: Preserve the global branch**

State that global/unknown scope, invalid envelopes, Trello/tool/auth/configuration/checklist/claim errors, and exception-card mutation failures still leave the queue item unchecked and stop the parent.

- [ ] **Step 3: Run all contract tests**

Run:

```bash
for t in .codex/skills/trello-etf-batch/tests/test_*.sh; do bash "$t"; done
```

Expected: all tests pass with no output or error.

### Task 4: Update the scheduled automation definition

**Files:**
- Modify through Codex automation tool: automation `loops-trello-etf-batch`
- Verify: `/Users/mangkornkatawong/.codex/automations/loops-trello-etf-batch/automation.toml`

**Interfaces:**
- Consumes: the final `.codex/skills/trello-etf-batch/automation-prompt.md` contract.
- Produces: the same item-error routing prompt in the scheduled automation, preserving its current status unless explicitly changed.

- [ ] **Step 1: Read the current automation definition**

Confirm the current prompt, id, and `PAUSED` status before updating.

- [ ] **Step 2: Update only the prompt**

Use `codex_app__automation_update` with the existing id and the full prompt from `automation-prompt.md`; preserve the existing schedule and status unless the user separately asks to activate it.

- [ ] **Step 3: Read back and verify**

Confirm the deployed prompt contains the item-level `ERROR` branch and global mutation-failure stop.

### Task 5: Verify and hand off

**Files:**
- Verify: all changed files and git state.
- Update: automation memory file for `loops-trello-etf-batch`.

**Interfaces:**
- Consumes: tests and deployed automation state.
- Produces: a concise report of behavior, verification, and any activation/runtime blocker.

- [ ] **Step 1: Run tests and inspect diff**

Run the full contract-test loop, `git diff --check`, and `git status --short`; confirm no unrelated files are staged.

- [ ] **Step 2: Update automation memory**

Record the behavior change, test result, deployed prompt result, and whether the automation remains `PAUSED`.

- [ ] **Step 3: Commit project changes**

```bash
git add .codex/skills/trello-etf-batch/SKILL.md \
  .codex/skills/trello-etf-batch/automation-prompt.md \
  .codex/skills/trello-etf-batch/tests/test_item_error_contract.sh \
  docs/superpowers/plans/2026-08-12-trello-etf-batch-item-errors-plan.md
git commit -m "feat: continue ETF batches after item errors"
```
