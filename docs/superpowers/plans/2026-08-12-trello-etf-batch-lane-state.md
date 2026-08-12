# Trello ETF Batch Lane-Only State Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Trello parent lanes the only runtime state for `trello-etf-batch` and stop reading, writing, validating, or deleting legacy parent status blocks.

**Architecture:** Keep queue progress in the `ETF queue` checklist and item failures in exception cards. Claim a parent only by moving it from `Ready for AI` to `In Progress` and re-reading its lane; derive normal and retry work from checklist/exception state, then finalize by moving the parent to `Ready for AI`, `Blocked`, or `Done`. Preserve legacy `trello-etf-batch-status` text as inert card-description content.

**Tech Stack:** Markdown skill contracts, Bash/Ripgrep contract tests, Codex skill validator, Codex automation tool, Git.

## Global Constraints

- Treat `Ready for AI`, `In Progress`, `Blocked`, and `Done` as the complete parent state machine.
- Never read, validate, write, or delete a legacy `trello-etf-batch-status` block.
- Treat a parent already in `In Progress` as active and make no mutation.
- Require at most one automation worker per parent; lane-only claim is operational, not an exactly-once distributed lock.
- Keep normal queue items ahead of eligible retries and derive both from checklist/exception state.
- Preserve all existing batch-size, downstream handoff, item-exception, and global-stop invariants.
- Preserve the live automation schedule, model, reasoning effort, execution environment, notification policy, and `PAUSED` status.

---

### Task 1: Add the failing lane-only state contract

**Files:**
- Create: `.codex/skills/trello-etf-batch/tests/test_lane_only_state_contract.sh`
- Test: `.codex/skills/trello-etf-batch/SKILL.md`
- Test: `.codex/skills/trello-etf-batch/automation-prompt.md`

**Interfaces:**
- Consumes: current skill and scheduled-prompt text.
- Produces: a static regression test that rejects parent status-block state and requires lane-only claim/finalization language.

- [ ] **Step 1: Write the failing test**

```bash
#!/usr/bin/env bash
set -euo pipefail

skill_file="${1:-.codex/skills/trello-etf-batch/SKILL.md}"
prompt_file="${2:-.codex/skills/trello-etf-batch/automation-prompt.md}"

assert_contains() {
  local file="$1"
  local needle="$2"
  rg -Fq "$needle" "$file" || {
    echo "missing lane-only contract in $file: $needle" >&2
    exit 1
  }
}

assert_not_contains() {
  local file="$1"
  local needle="$2"
  if rg -Fq "$needle" "$file"; then
    echo "unexpected parent-status contract in $file: $needle" >&2
    exit 1
  fi
}

for contract_file in "$skill_file" "$prompt_file"; do
  assert_contains "$contract_file" '`Ready for AI` is the only eligible parent lane'
  assert_contains "$contract_file" '`In Progress` means a worker may be active'
  assert_contains "$contract_file" 'Do not read, validate, write, or delete legacy `trello-etf-batch-status` blocks'
  assert_contains "$contract_file" 'move it to `In Progress`'
  assert_contains "$contract_file" 'read the exact parent directly again'
  assert_contains "$contract_file" 'normal items before eligible retries'
  assert_contains "$contract_file" 'move the parent to `Blocked`'
  assert_not_contains "$contract_file" 'claim_token'
  assert_not_contains "$contract_file" 'state: ready'
  assert_not_contains "$contract_file" 'state: running'
  assert_not_contains "$contract_file" 'list/status block'
  assert_not_contains "$contract_file" 'appropriate retry flag'
  assert_not_contains "$contract_file" 'Clear the claim'
  assert_not_contains "$contract_file" 'set the parent status'
done
```

- [ ] **Step 2: Run the test to verify RED**

Run:

```bash
bash .codex/skills/trello-etf-batch/tests/test_lane_only_state_contract.sh
```

Expected: FAIL because the current skill and prompt still require the status block and claim token.

- [ ] **Step 3: Commit the red test**

```bash
git add .codex/skills/trello-etf-batch/tests/test_lane_only_state_contract.sh
git commit -m "test: require lane-only ETF batch state"
```

### Task 2: Replace parent status-block state in the skill

**Files:**
- Modify: `.codex/skills/trello-etf-batch/SKILL.md:122`
- Modify: `.codex/skills/trello-etf-batch/SKILL.md:299`
- Test: `.codex/skills/trello-etf-batch/tests/test_lane_only_state_contract.sh`
- Test: `.codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh`
- Test: `.codex/skills/trello-etf-batch/tests/test_item_error_contract.sh`
- Test: `.codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh`

**Interfaces:**
- Consumes: Trello parent lane, canonical queue `S`, checklist state, and open exception-card metadata.
- Produces: lane-only parent selection, claim, retry derivation, global-stop, and finalization rules.

- [ ] **Step 1: Replace the controlled-status section**

Write a `Lane-only parent state and claim protocol` section defining:

```text
Ready for AI = only eligible lane
In Progress = worker may be active; do not mutate
Blocked = user must move to Ready for AI to retry
Done = validated no-op when queue is complete and no exception is open
```

State verbatim that legacy blocks are preserved but never read, validated, written, or deleted. Define claim as move to `In Progress`, direct re-read, stop without further mutation if the lane does not match, and disclose that the lane is not an exactly-once distributed lock.

- [ ] **Step 2: Remove status fields from the execution loop**

Make the loop validate configuration/input before claim; select only `Ready for AI`; keep the parent in `In Progress` while processing; select normal items before eligible retries; and finalize using direct lane moves. Keep `retry_pending` only as the computed set/count of retryable child exceptions, never as a parent description flag.

- [ ] **Step 3: Update failure-classification ownership language**

Keep `claim-state-error` as an accepted global failure code, but define it as a lane/ownership transition failure after this invocation moved the card. Remove token mismatch and parent-description status mutation language.

- [ ] **Step 4: Run the lane-only test against the skill**

```bash
bash .codex/skills/trello-etf-batch/tests/test_lane_only_state_contract.sh \
  .codex/skills/trello-etf-batch/SKILL.md \
  .codex/skills/trello-etf-batch/SKILL.md
```

Expected: PASS after the skill contains the lane-only contract.

### Task 3: Mirror lane-only behavior in the automation prompt

**Files:**
- Modify: `.codex/skills/trello-etf-batch/automation-prompt.md`
- Test: `.codex/skills/trello-etf-batch/tests/test_lane_only_state_contract.sh`

**Interfaces:**
- Consumes: open cards in the configured `Ready for AI` list.
- Produces: one oldest eligible exact parent URL and lane-only lifecycle instructions for `$trello-etf-batch`.

- [ ] **Step 1: Replace eligibility and claim language**

Require the dispatcher to select only an open `Ready for AI` parent with valid configuration, ignore every other lane, move the selected parent to `In Progress`, and re-read it. State that an `In Progress` card means a worker may be active and must not be touched.

- [ ] **Step 2: Replace global and finalization language**

Remove `Clear the claim`, `set the parent status`, and retry-flag instructions. Use direct lane transitions:

```text
global blocker -> Blocked
normal or retry work remains -> Ready for AI
only terminal/unconfirmed exceptions -> Blocked
all checked and no open exception -> Done + complete
```

State that normal items are selected before eligible retries and legacy status blocks are inert.

- [ ] **Step 3: Run the lane-only test against the real files**

```bash
bash .codex/skills/trello-etf-batch/tests/test_lane_only_state_contract.sh
```

Expected: PASS.

### Task 4: Validate and commit the complete skill contract

**Files:**
- Verify: `.codex/skills/trello-etf-batch/SKILL.md`
- Verify: `.codex/skills/trello-etf-batch/automation-prompt.md`
- Verify: `.codex/skills/trello-etf-batch/agents/openai.yaml`
- Verify: `.codex/skills/trello-etf-batch/tests/*.sh`

**Interfaces:**
- Consumes: final local skill folder.
- Produces: passing static contracts and valid skill metadata.

- [ ] **Step 1: Run all contract tests**

```bash
for test_file in .codex/skills/trello-etf-batch/tests/test_*.sh; do
  bash "$test_file"
done
```

Expected: all scripts exit `0` with no error output.

- [ ] **Step 2: Run the skill validator**

```bash
python3 /Users/mangkornkatawong/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  .codex/skills/trello-etf-batch
```

Expected: validator reports the skill is valid.

- [ ] **Step 3: Validate UI metadata remains aligned**

Confirm `agents/openai.yaml` still describes exact-card Trello ETF batch execution and retains `$trello-etf-batch` in `default_prompt`. Do not regenerate it because the trigger/interface did not change.

- [ ] **Step 4: Commit the green implementation**

```bash
git add .codex/skills/trello-etf-batch/SKILL.md \
  .codex/skills/trello-etf-batch/automation-prompt.md
git commit -m "feat: use Trello lanes for ETF batch state"
```

### Task 5: Sync and verify the scheduled automation

**Files:**
- Read: `/Users/mangkornkatawong/.codex/automations/loops-trello-etf-batch/automation.toml`
- Update through Codex automation tool: `loops-trello-etf-batch`

**Interfaces:**
- Consumes: final `.codex/skills/trello-etf-batch/automation-prompt.md`.
- Produces: the same prompt in the live automation while preserving all non-prompt fields.

- [ ] **Step 1: Read current automation fields**

Record `kind`, `name`, `rrule`, `status`, `model`, `reasoning_effort`, `execution_environment`, project id, and notification policy.

- [ ] **Step 2: Update only the prompt through the automation tool**

Call `automation_update` for id `loops-trello-etf-batch` with the full prompt and all existing non-prompt values. Preserve `status: PAUSED` and the six-hour schedule.

- [ ] **Step 3: Read back and compare**

Verify the deployed prompt includes lane-only eligibility, inert legacy blocks, normal-before-retry selection, and no claim-token/status-field instructions. Verify all non-prompt fields are unchanged.

### Task 6: Final verification and automation memory

**Files:**
- Verify: repository working tree and commits.
- Update: `/Users/mangkornkatawong/.codex/automations/loops-trello-etf-batch/memory.md`

**Interfaces:**
- Consumes: committed skill changes and deployed automation state.
- Produces: evidence-backed completion report and durable run memory.

- [ ] **Step 1: Run fresh final verification**

```bash
for test_file in .codex/skills/trello-etf-batch/tests/test_*.sh; do
  bash "$test_file"
done
python3 /Users/mangkornkatawong/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  .codex/skills/trello-etf-batch
git diff --check
git status --short
git log -3 --oneline
```

Expected: all tests and validation pass, diff check is clean, and only intentionally uncommitted files—if any—appear.

- [ ] **Step 2: Update automation memory**

Append the current Asia/Bangkok run time, lane-only behavior, test/validator result, commit ids, deployed automation verification, and preserved automation status.

- [ ] **Step 3: Report the result**

Link the updated skill and automation prompt, state that no Trello cards or legacy blocks were mutated, and note that `In Progress` recovery remains a manual user move back to `Ready for AI`.
