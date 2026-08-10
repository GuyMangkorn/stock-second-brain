# Task 2 Report — Item-exception continuation contract

Date: 2026-08-10

## Scope completed

- Updated only `.codex/skills/trello-etf-batch/SKILL.md` for the coordinator contract change.
- Kept the change bounded to the approved design and Task 2 brief.

## What changed

Implemented the contract updates required by the brief:

1. Replaced checklist semantics so a checked queue item means the ticker was handled, either by downstream success or by a successful item-level exception-card mutation.
2. Updated pending-set definitions so:
   - `normal_pending` stays limited to unchecked items without open exceptions.
   - `retry_pending`, `confirmation_pending`, and `terminal_pending` derive from checked items with open exception metadata.
3. Reordered item-level failure handling so the coordinator:
   - keeps the parent claim,
   - creates/reuses exactly one exception card,
   - writes the exception metadata including `reason`,
   - moves the exception to `Blocked`,
   - only then checks the matching `ETF queue` item,
   - then increments run-local bookkeeping and continues while capacity remains.
4. Updated finalization rules so `Done` now requires all checklist items checked and zero open exceptions, unfinished non-terminal work releases back to `Ready for AI`, and only terminal/unconfirmed remainder stays `Blocked`.
5. Updated exception/automation wording to describe exception cards as Trello child records linked by `parent_ari` and `parent_url`, forbid child cards for success cases, and state that item-level blocks check the item and allow the current batch to continue.

## RED capture before editing

Ran the Task 1 focused static contract tests before editing:

```bash
bash .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh
bash .codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh
```

Observed RED failures against the pre-edit skill contract:

- `missing contract: create or reuse exactly one exception card`
- `missing contract: A checked item means the ticker has been handled`

## Focused verification after editing

Fresh commands run after the scoped skill edit:

```bash
bash .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh
bash .codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh
git diff --check -- .codex/skills/trello-etf-batch/SKILL.md .codex/skills/trello-etf-batch/tests
```

Results:

- `test_batch_size_contract.sh`: passed (`exit 0`)
- `git diff --check`: passed (`exit 0`)
- `test_item_exception_contract.sh`: still exits `1` with no emitted failure text

## Verification note on the second static test

The current `test_item_exception_contract.sh` script still exits nonzero after the contract wording changes because its `assert_not_contains` helper is written as:

```bash
rg -Fq "$needle" "$skill_file" && {
  echo "unexpected contract: $needle" >&2
  exit 1
}
```

Under the script's `set -euo pipefail`, the `rg` call in that helper exits the script when the string is absent, so the negative assertion cannot currently succeed as written.

Before stopping, I manually confirmed that the two forbidden legacy phrases are absent from `.codex/skills/trello-etf-batch/SKILL.md`:

- `A checked item means the downstream performance workflow explicitly returned success for that ticker.`
- `On an explicit downstream item-level failure, leave the item unchecked`

## Self-review

- Diff remains scoped to the intended skill contract plus this report.
- No tests were modified.
- Contract text now matches the approved design on checked-item semantics, exception identity, retry eligibility, failure ordering, finalization, and automation wording.

## Commit

Commit created after staging the scoped files from this task.

## GREEN verification after Task 1 fix

Task 1 fix `a316dbd` corrected the negative-assertion helper in
`.codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh`.

Fresh verification run against the existing committed Task 2 skill change
`aef71a8`:

```bash
bash .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh
bash .codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh
git diff --check -- .codex/skills/trello-etf-batch/SKILL.md .codex/skills/trello-etf-batch/tests
```

Results:

- `test_batch_size_contract.sh`: passed (`exit 0`)
- `test_item_exception_contract.sh`: passed (`exit 0`)
- `git diff --check -- .codex/skills/trello-etf-batch/SKILL.md .codex/skills/trello-etf-batch/tests`: passed (`exit 0`)

No additional contract gaps were revealed, so `.codex/skills/trello-etf-batch/SKILL.md`
did not require any further edits.

## Final status

DONE

## Fix round 1 — confirmation_required handled-item contract

Reviewer finding addressed:

- The `confirmation_required` mapping in
  `.codex/skills/trello-etf-batch/SKILL.md` still said to keep the queue item
  unchecked, which contradicted the handled-item/open-exception contract used
  everywhere else in the coordinator.

Scoped fix applied:

- Updated only `.codex/skills/trello-etf-batch/SKILL.md`.
- Changed the `WARNING` + `scope: item` + `durable_write: not_completed`
  mapping so `confirmation_required` follows the same safe item-level
  exception order as other explicit item blocks:
  - create or update the one exception card,
  - write confirmation metadata plus `reason`,
  - move it to `Blocked`,
  - only then check the matching `ETF queue` item,
  - leave the exception open so it remains handled, blocks `Done`, and still
    allows the current run to continue while capacity remains.
- Preserved the existing global-failure rule for scope-free or
  `scope: unknown` warnings.

Fresh verification for this fix round:

```bash
bash .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh
bash .codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh
git diff --check -- .codex/skills/trello-etf-batch/SKILL.md .codex/skills/trello-etf-batch/tests
```

Results:

- `test_batch_size_contract.sh`: passed (`exit 0`)
- `test_item_exception_contract.sh`: passed (`exit 0`)
- `git diff --check -- .codex/skills/trello-etf-batch/SKILL.md .codex/skills/trello-etf-batch/tests`: passed (`exit 0`)

Fix round 1 status: DONE
