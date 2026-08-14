# Task 2 Report: Implement Skill 1 backlog splitting

## Status

Complete.

## Scope delivered

- Initialized the new skill with the required `skill-creator` script.
- Added `.codex/skills/trello-etf-backlog/SKILL.md` with the exact backlog-splitting contract:
  - resolved master-card and workflow/legacy-alias eligibility;
  - project-relative Markdown input resolution;
  - exactly one `Symbol` or `Ticker` column;
  - canonical uppercase normalization, source-order preservation, and first-occurrence deduplication;
  - `input-malformed` handling before mutation;
  - `parent_ari + ticker` idempotency;
  - exact child description, ticker title, and `Ready for AI` creation;
  - matching-child detection across lanes;
  - continuation after item-specific create errors;
  - master retention in `Backlog` until all identities exist, then move to `Done` and complete;
  - `Blocked` and `Done` children counted as created;
  - explicit boundary excluding performance research, source browsing, performance pages, and child result state.
- Added `.codex/skills/trello-etf-backlog/agents/openai.yaml` with the planned interface values and disabled implicit invocation.

## Verification

- `bash .codex/skills/trello-etf-batch/tests/test_backlog_split_contract.sh` — PASS
- `python3 /Users/mangkornkatawong/.codex/skills/.system/skill-creator/scripts/quick_validate.py .codex/skills/trello-etf-backlog` — PASS
- `git diff --check` and committed-patch check — PASS

## Commit

`038db02 feat: add Trello ETF backlog splitter skill`

## Scope review and concerns

Only the requested new skill directory was staged in the implementation commit. No manager, processing, result skills, tests, historical docs, vault files, or live Trello data were modified. No concerns remain for this task; live Trello access was intentionally not used.

## Fix round 1

### Corrections

- Added case-insensitive matching for exactly one `Symbol` or `Ticker` header and explicit `input-malformed` handling when both aliases or neither alias are present.
- Added the global-failure branch: authentication, Trello, board, list, lookup, mutation, and configuration failures stop further mutations; not-yet-confirmed tickers remain unclaimed; only confirmed master/child state is reported; failed master move/completion is never reported as successful.
- Added focused regression assertions for both contracts.

### Exact verification commands and output

Command:

```bash
bash .codex/skills/trello-etf-batch/tests/test_backlog_split_contract.sh && python3 /Users/mangkornkatawong/.codex/skills/.system/skill-creator/scripts/quick_validate.py .codex/skills/trello-etf-backlog && git diff --check
```

Output:

```text
Skill is valid!
```

The focused contract test is silent on success and exited with status 0; `quick_validate.py` printed `Skill is valid!`; `git diff --check` was silent and exited with status 0.
