# Trello ETF Batch Symbol/Ticker Alias Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update `trello-etf-batch` so a Markdown ETF table may use either `Symbol` or `Ticker` as its single canonical ticker column.

**Architecture:** Keep the coordinator's existing queue normalization and all Trello/downstream semantics unchanged. Expand only the input-column resolution contract: select exactly one case-insensitive alias, reject both aliases or neither alias as `input-malformed`, then apply the existing trim, uppercase, source-order, and deduplication rules.

**Tech Stack:** Markdown skill instructions, Bash contract tests, `rg`-based assertions.

## Global Constraints

- `Symbol` and `Ticker` are equivalent aliases for the canonical ticker field.
- A table containing both aliases is ambiguous and must fail as `input-malformed`.
- A table containing neither alias must fail as `input-malformed`.
- Preserve trim/backtick removal, uppercase normalization, source order, and first-occurrence deduplication.
- Do not change checklist, exception-card, lane, downstream handoff, or durable-output ownership semantics.
- Do not mutate Trello or durable vault research outputs for this instruction-only change.

---

### Task 1: Add the input-column alias contract test

**Files:**
- Create: `.codex/skills/trello-etf-batch/tests/test_input_column_alias_contract.sh`

**Interfaces:**
- Consumes: `.codex/skills/trello-etf-batch/SKILL.md` and `automation-prompt.md` as text contracts.
- Produces: A nonzero exit when either contract omits alias support or the ambiguity rule.

- [ ] **Step 1: Write the failing contract test**

Create a Bash test that accepts optional skill and prompt paths, asserts both files
describe resolving exactly one `Symbol`/`Ticker` alias case-insensitively, asserts
the both/neither cases are `input-malformed`, and asserts the normalization rules
remain present. Also reject the stale single-column wording.

```bash
#!/usr/bin/env bash
set -euo pipefail

skill_file="${1:-.codex/skills/trello-etf-batch/SKILL.md}"
prompt_file="${2:-.codex/skills/trello-etf-batch/automation-prompt.md}"

assert_contains() {
  local file="$1"
  local needle="$2"
  rg -Fq "$needle" "$file" || {
    echo "missing input-column contract in $file: $needle" >&2
    exit 1
  }
}

assert_not_contains() {
  local file="$1"
  local needle="$2"
  if rg -Fq "$needle" "$file"; then
    echo "stale input-column contract in $file: $needle" >&2
    exit 1
  fi
}

for contract_file in "$skill_file" "$prompt_file"; do
  assert_contains "$contract_file" 'Symbol` or `Ticker'
  assert_contains "$contract_file" 'case-insensitively'
  assert_contains "$contract_file" 'both aliases'
  assert_contains "$contract_file" 'neither alias'
  assert_contains "$contract_file" 'input-malformed'
done

assert_contains "$skill_file" 'Trim whitespace and backticks'
assert_contains "$skill_file" 'normalize each symbol to uppercase'
assert_contains "$skill_file" 'preserve source order'
assert_contains "$skill_file" 'deduplicate repeated symbols by keeping'
assert_not_contains "$prompt_file" 'must contain a Markdown table with a `Symbol` column'
```

- [ ] **Step 2: Run the new test to verify it fails**

Run:

```bash
bash .codex/skills/trello-etf-batch/tests/test_input_column_alias_contract.sh
```

Expected: FAIL because the current skill and automation prompt still require a
single `Symbol` column and do not state the both/neither ambiguity rule.

### Task 2: Update the coordinator input contract

**Files:**
- Modify: `.codex/skills/trello-etf-batch/SKILL.md:95-103`
- Modify: `.codex/skills/trello-etf-batch/automation-prompt.md:25-29`

**Interfaces:**
- Consumes: The Markdown input table supplied by each parent card.
- Produces: One canonical symbol sequence `S`, or a global `input-malformed`
  result before any claim/checklist/Trello mutation.

- [ ] **Step 1: Replace the single-column wording in `SKILL.md`**

Change the queue-input paragraph to say that the coordinator resolves exactly
one case-insensitive table column named `Symbol` or `Ticker`, treats the aliases
as equivalent, rejects both aliases and neither alias as `input-malformed`, and
then retains the existing trim/backtick, uppercase, order, and deduplication
rules. Update the global failure bullet to mention both invalid alias states.

- [ ] **Step 2: Replace the automation prompt's input requirement**

Change the scheduler prompt so selected cards are validated against the same
alias contract before claiming. Keep the wording aligned with `SKILL.md`,
including the rule that both aliases are ambiguous and neither alias is
malformed.

- [ ] **Step 3: Run the new contract test**

Run:

```bash
bash .codex/skills/trello-etf-batch/tests/test_input_column_alias_contract.sh
```

Expected: PASS.

### Task 3: Validate the complete skill contract and sample input

**Files:**
- Test: `.codex/skills/trello-etf-batch/tests/*.sh`
- Read: `/Users/mangkornkatawong/Documents/Codex/2026-08-09/new-chat/outputs/filtered-etfs-40-no-duplicates.md`

**Interfaces:**
- Consumes: The revised skill text and the user's ETF list.
- Produces: Passing contract tests and a validation note that the sample's
  `Ticker` header is now an accepted alias.

- [ ] **Step 1: Verify the sample header and canonical row count**

Use a read-only shell check to confirm the table contains one `Ticker` header,
40 non-empty ticker rows, and no `Symbol` header. Confirm the normalized sample
sequence begins `VTWG`, `VTWV`, `SCHC` and ends `CALF`, `IWMI`, `FYC`.

- [ ] **Step 2: Run every existing contract test**

Run:

```bash
for test_file in .codex/skills/trello-etf-batch/tests/*.sh; do
  bash "$test_file"
done
```

Expected: PASS for the existing lane, exception, item-error, batch-size, and
new input-column alias contracts.

- [ ] **Step 3: Inspect the diff and verify scope**

Run:

```bash
git diff --check
git diff -- .codex/skills/trello-etf-batch docs/superpowers/plans/2026-08-13-trello-etf-batch-symbol-ticker-alias.md
```

Confirm that the approved process-artifact scope includes the brainstorming
design spec, implementation plan, skill instructions, automation prompt, and
contract test; no Trello API call or vault output was created.

- [ ] **Step 4: Commit the implementation**

Stage only the approved files and create a concise commit:

```bash
git add .codex/skills/trello-etf-batch/SKILL.md \
  .codex/skills/trello-etf-batch/automation-prompt.md \
  .codex/skills/trello-etf-batch/tests/test_input_column_alias_contract.sh \
  docs/superpowers/plans/2026-08-13-trello-etf-batch-symbol-ticker-alias.md \
  docs/superpowers/specs/2026-08-13-trello-etf-batch-symbol-ticker-alias-design.md
git commit -m "feat: accept ticker alias in ETF batch input"
```
