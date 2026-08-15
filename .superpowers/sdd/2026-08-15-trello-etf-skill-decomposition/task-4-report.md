# Task 4 Report: Implement Skill 3 ETF processing

## Outcome

Implemented `trello-etf-processing` in the isolated Trello ETF skill decomposition worktree. The skill is limited to claiming one exact ETF child card and forwarding a complete processing result to `trello-etf-result`.

## Files changed

- `.codex/skills/trello-etf-processing/SKILL.md`
- `.codex/skills/trello-etf-processing/agents/openai.yaml`
- `.superpowers/sdd/2026-08-15-trello-etf-skill-decomposition/task-4-report.md`

The focused contract test was not modified because the existing assertions covered the required processing boundary after the skill wording was aligned to their exact contract strings.

## Contract implemented

- Requires one exact child card in `Ready for AI`.
- Validates `workflow: trello-etf-item`, `parent_ari`, canonical uppercase ticker, and title equal to ticker.
- Does not touch cards in `In Progress`, `Blocked`, or `Done`.
- Moves the selected card to `In Progress` and directly rereads the same card.
- Returns global `claim-state-error` and does not invoke downstream unless the reread confirms `In Progress`.
- Invokes one ticker only with `$check-etf-performance <TICKER>` and `mode: lean`.
- Waits for research delegation, reconciliation, pre-save review, and durable write result.
- Requires the complete seven-field result envelope.
- Normalizes missing, malformed, or contradictory output to `ERROR`, global scope, and `unknown-result`.
- Forwards the envelope and downstream links to `trello-etf-result`.
- Never moves the child to `Done` or `Blocked` directly.
- Explicitly prohibits local source discovery, research delegation, reviewer work, and vault writes.

## Validation

Passed:

```text
bash .codex/skills/trello-etf-batch/tests/test_processing_contract.sh
python3 /Users/mangkornkatawong/.codex/skills/.system/skill-creator/scripts/quick_validate.py .codex/skills/trello-etf-processing
```

`git diff --check` also passed.

## Concerns

- `init_skill.py` created the requested directory and template but rejected the brief's exact `short_description` because its length is 66 characters, above the generator's 25–64 character validation rule. The required exact metadata was therefore written manually to `agents/openai.yaml`; the skill validator accepts the result.
- No live Trello access or vault write was performed, per the task boundary.

## Commit

`feat: add Trello ETF processing skill` (final commit hash reported by the task handoff)
