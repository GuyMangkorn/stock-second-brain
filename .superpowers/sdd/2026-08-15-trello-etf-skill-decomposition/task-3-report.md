# Task 3 Report: Implement Skill 2 result routing

## Status

Complete.

## Scope delivered

- Initialized `.codex/skills/trello-etf-result` with the required
  `init_skill.py` command.
- Replaced the generated template with the exact `trello-etf-result`
  frontmatter and result-routing contract.
- Added the exact seven-field Skill 3 result envelope:
  `status`, `scope`, `durable_write`, `exhausted`, `confirmation`, `code`, and
  `reason`.
- Added exact-card targeting, `workflow: trello-etf-item` identity checks,
  `parent_ari` and `ticker` preservation, and stable-code normalization.
- Added strict success routing only for PASS/item/completed/false/none with
  `success` or `durable-write-complete`; it moves the selected child to Done,
  completes it, and returns card/output links.
- Added non-success and invalid-envelope routing that persists result metadata,
  preserves child identity metadata, moves the selected child to Blocked, and
  leaves it incomplete.
- Made exception-card creation prohibited and Trello/auth/mutation failures
  global.
- Added the required agent metadata with implicit invocation disabled.
- The existing focused contract test was sufficient; it was not modified.

## Verification

- `bash .codex/skills/trello-etf-batch/tests/test_result_transition_contract.sh` — PASS
- `python3 /Users/mangkornkatawong/.codex/skills/.system/skill-creator/scripts/quick_validate.py .codex/skills/trello-etf-result` — PASS
- `git diff --check` — PASS

## Commit

`2f3ed43 feat: add Trello ETF result router skill`

## Scope review and concerns

Only the new result-router skill and this required task report are in scope.
No backlog, processing, manager, automation prompt, historical documentation,
vault files, or live Trello data were modified. No focused test change was
needed. No concerns remain; live Trello access was intentionally not used.

## Fix round 1

### Corrections

- Removed the contradiction between invalid-envelope global handling and the
  required selected-child failure path.
- For a resolved exact child target and identity, invalid or contradictory
  envelopes now persist `result_status: BLOCKED`, `result_scope: global`,
  `result_code: unknown-result`, a validation reason, `durable_write: unknown`,
  and `confirmation: none`, then move that child to `Blocked`.
- The router returns `global_blocked` only after both mutations are confirmed;
  the manager must stop and not continue to other cards.
- Unresolved targets/identity and Trello/auth/lookup/mutation failures remain
  global pre-mutation or global state failures and never claim unconfirmed
  transitions.
- Updated the focused contract test to assert the known-child
  `global_blocked` behavior while retaining metadata preservation and the
  no-exception-card assertions.

### Verification

Commands and outputs:

```text
$ bash .codex/skills/trello-etf-batch/tests/test_result_transition_contract.sh && python3 /Users/mangkornkatawong/.codex/skills/.system/skill-creator/scripts/quick_validate.py .codex/skills/trello-etf-result && git diff --check
Skill is valid!
```

All commands exited with status 0. The focused contract test and
`git diff --check` were silent on success; `quick_validate.py` printed
`Skill is valid!`.

### Commit

`7e7b602 fix: clarify Trello ETF invalid result routing`
