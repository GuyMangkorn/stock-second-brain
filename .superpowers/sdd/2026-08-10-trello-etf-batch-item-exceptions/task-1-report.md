# Task 1 Report — Trello ETF Batch Item Exceptions

Date: 2026-08-10

## Status

RED contract coverage added for the approved item-exception design.

## Files changed

- Added `.codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh`
- Updated `.codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh`

## What changed

- Added a new shell contract test that checks the new item-exception language and excludes the old contradictory success-only wording.
- Extended the existing batch-size contract test with the four approved exception-card/batch-continuation assertions.
- Left `.codex/skills/trello-etf-batch/SKILL.md` untouched, per the TDD RED-phase requirement.

## RED evidence

Ran:

```bash
bash .codex/skills/trello-etf-batch/tests/test_item_exception_contract.sh
bash .codex/skills/trello-etf-batch/tests/test_batch_size_contract.sh
```

Observed failures:

- `test_item_exception_contract.sh`:
  - `missing contract: A checked item means the ticker has been handled`
- `test_batch_size_contract.sh`:
  - `missing contract: create or reuse exactly one exception card`

## Self-review

- The two required contract-test changes are isolated and match the brief.
- Failure output is specific and proves the new contract language is still absent.
- No skill or production workflow code was edited.

## Notes

- Next step is the GREEN phase: update the Trello ETF batch skill to satisfy these contract assertions.
