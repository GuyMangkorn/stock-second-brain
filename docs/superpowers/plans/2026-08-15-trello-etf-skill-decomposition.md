# Trello ETF Skill Decomposition Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (- [ ]) syntax for tracking.

**Goal:** แยก trello-etf-batch ออกเป็น backlog splitter, processing worker, result router และ manager/router ที่เลือกงานตาม task และ count จาก scheduler prompt

**Architecture:** คง trello-etf-batch เป็น public Skill 4 manager และเพิ่ม 3 skills ที่มี owner เดียวต่อหนึ่ง responsibility. Child card ใช้ parent_ari + ticker เป็น identity, เริ่มใน Ready for AI, ถูก claim ไป In Progress ก่อนเรียก $check-etf-performance, แล้วให้ result router ย้ายไป Done หรือ Blocked. check-etf-performance ยังคงเป็นเจ้าของ research, review gate และ durable vault writes.

**Tech Stack:** Markdown skill contracts, YAML agents/openai.yaml metadata, Bash/Ripgrep static contract tests, Codex Trello connector, existing check-etf-performance handoff envelope

## Global Constraints

- trello-etf-batch remains the public manager/router entry point.
- Child identity is exactly parent_ari + ticker; child title is the canonical uppercase ticker.
- A child is created in Ready for AI; processing claims it to In Progress; result routing sends strict success to Done and every other result to Blocked with a reason.
- Scheduler prompts must provide task: backlog|etf-performance and count: positive base-10 integer; manager processes no more than count cards sequentially.
- check-etf-performance remains the sole owner of ETF research and durable vault writes; Trello skills do not browse sources or write wiki/, raw/, index.md, or log.md.
- Invalid input/configuration, Trello/auth/board/list failures, and contradictory result envelopes are global failures; do not claim a state transition that did not succeed.
- Use Thai-first narrative with English headings, frontmatter keys, field names, ticker labels and finance terms.
- Preserve historical design/spec documents; update only active skills, automation prompt, focused tests and agent metadata in this implementation.

---

## File map

Create:

- .codex/skills/trello-etf-backlog/SKILL.md — Skill 1: parse a master input, create missing child cards, and finalize the master.
- .codex/skills/trello-etf-backlog/agents/openai.yaml — Skill 1 display metadata; implicit invocation disabled because the manager owns routing.
- .codex/skills/trello-etf-processing/SKILL.md — Skill 3: claim one Ready-for-AI child and invoke the ETF worker.
- .codex/skills/trello-etf-processing/agents/openai.yaml — Skill 3 display metadata.
- .codex/skills/trello-etf-result/SKILL.md — Skill 2: validate one result envelope and move the selected child to Done/Blocked.
- .codex/skills/trello-etf-result/agents/openai.yaml — Skill 2 display metadata.

Modify:

- .codex/skills/trello-etf-batch/SKILL.md — replace the monolithic queue coordinator with Skill 4 manager/router.
- .codex/skills/trello-etf-batch/automation-prompt.md — replace exact-parent scheduling with explicit task and count routing.
- .codex/skills/trello-etf-batch/agents/openai.yaml — keep the public name but enable manager routing for Trello ETF requests.

Replace the old monolith-specific shell assertions with:

- .codex/skills/trello-etf-batch/tests/test_backlog_split_contract.sh
- .codex/skills/trello-etf-batch/tests/test_processing_contract.sh
- .codex/skills/trello-etf-batch/tests/test_result_transition_contract.sh
- .codex/skills/trello-etf-batch/tests/test_manager_routing_contract.sh

The current five tests assert checklist/exception behavior that the approved design removes. Delete those obsolete tests after the four replacement tests exist; the final validation task must run all replacement tests successfully.

## Interfaces

### Master card

```text
workflow: trello-etf-backlog
input: /absolute/or/project-relative/path/to/etf-list.md
```

Accept legacy workflow: trello-etf-batch only when the card is in Backlog and has input. Resolve exactly one Markdown table column named Symbol or Ticker, normalize each nonempty value to uppercase after trimming whitespace/backticks, preserve source order, and deduplicate by first occurrence.

### Child card

```text
title: <CANONICAL_TICKER>
workflow: trello-etf-item
parent_ari: <MASTER_CARD_ARI>
ticker: <CANONICAL_TICKER>
list: Ready for AI | In Progress | Blocked | Done
```

parent_ari + ticker is the idempotency key. An unarchived matching child in any lane counts as already created for backlog completion; Skill 3 selects only children currently in Ready for AI.

### Result envelope

```text
status: PASS|WARNING|CHANGES_REQUIRED|BLOCKED|ERROR
scope: item|global|unknown
durable_write: completed|not_completed|unknown
exhausted: true|false
confirmation: none|required|confirmed
code: <normalized-stable-code>
reason: <concise-one-sentence-reason>
```

Only this combination is success: PASS + scope item + durable_write completed + exhausted false + confirmation none + success or durable-write-complete.

## Task 1: Replace stale monolith tests with decomposition contracts

**Files:**
- Create the four replacement tests listed in the file map.
- Delete after replacement tests pass: the five existing test_*_contract.sh files.

**Interfaces:**
- Consumes: the future three skill files, manager file and automation prompt.
- Produces: deterministic Bash/Ripgrep tests that fail until each new contract is present.

- [ ] Step 1: Write test_backlog_split_contract.sh. Use set -euo pipefail and an assert_contains helper. Assert workflow: trello-etf-backlog, legacy master acceptance, exactly-one Symbol/Ticker alias validation, uppercase/source-order/dedup normalization, parent_ari + ticker, child creation in Ready for AI, continuation after item-specific create failure, master retention in Backlog, and Done only after all children exist. Assert no ETF queue or exception-card ownership.
- [ ] Step 2: Write test_processing_contract.sh. Assert one exact child in Ready for AI, validation of parent_ari and ticker, move to In Progress, direct reread, $check-etf-performance <TICKER> with mode: lean, forwarding to trello-etf-result, and no downstream call after a failed claim.
- [ ] Step 3: Write test_result_transition_contract.sh. Assert all seven envelope fields, strict PASS criteria, Done plus complete on success, Blocked plus persisted reason on every failure, preservation of workflow/parent_ari/ticker, and explicit prohibition on exception cards.
- [ ] Step 4: Write test_manager_routing_contract.sh. Assert task: backlog|etf-performance, positive base-10 count, backlog to Skill 1, ETF performance to Skill 3 then Skill 2, sequential up-to-count behavior, attempted_this_run, lane filtering and no overlapping workers.
- [ ] Step 5: Run the tests before implementation:
```bash
for test_file in .codex/skills/trello-etf-batch/tests/test_*.sh; do bash "$test_file"; done
```
Expected: FAIL because the new skill directories and manager contract do not exist.
- [ ] Step 6: Delete only the five obsolete monolith tests with apply_patch after the four replacements are present. Do not delete historical specs or plans.
- [ ] Step 7: Commit:
```bash
git add .codex/skills/trello-etf-batch/tests
git commit -m "test: define Trello ETF skill decomposition contracts"
```

## Task 2: Implement Skill 1 backlog splitting

**Files:**
- Create .codex/skills/trello-etf-backlog/SKILL.md and agents/openai.yaml.
- Test .codex/skills/trello-etf-batch/tests/test_backlog_split_contract.sh.

**Interfaces:**
- Consumes: one master card in Backlog with workflow and input; local Markdown ETF list.
- Produces: child cards with workflow trello-etf-item, parent_ari, canonical ticker, and list Ready for AI; master Done only when every child identity exists.

- [ ] Step 1: Add this frontmatter and boundary:
```yaml
---
name: trello-etf-backlog
description: "Use when a Trello master card in Backlog must be split into idempotent ETF ticker cards in Ready for AI."
---
```
State that the skill owns input parsing and card creation only; it does not call check-etf-performance, browse sources, create performance pages, or manage child result state.
- [ ] Step 2: Require a resolved master in Backlog; accept canonical trello-etf-backlog and legacy trello-etf-batch only with input; resolve project-relative paths from the stock-second-brain root; validate exactly one Symbol/Ticker column before mutation; return input-malformed for missing/unreadable files, both aliases, neither alias, empty rows or zero canonical symbols.
- [ ] Step 3: Require this child description, title equal to ticker, creation in Ready for AI, lookup by parent_ari + ticker, no duplicate for an unarchived match in any lane, and continuation through remaining missing tickers after an item-specific create error:
```text
workflow: trello-etf-item
parent_ari: <resolved master card ARI>
ticker: <CANONICAL_UPPERCASE_TICKER>
```
- [ ] Step 4: Keep the master in Backlog if any identity is missing. When every identity exists, move master to Done and complete it. A child in Blocked or Done counts as created.
- [ ] Step 5: Add agent metadata:
```yaml
interface:
  display_name: "Trello ETF Backlog Splitter"
  short_description: "Split a Trello ETF master card into ticker cards"
  default_prompt: "Use $trello-etf-backlog on an eligible master card in Backlog."
policy:
  allow_implicit_invocation: false
```
- [ ] Step 6: Run:
```bash
bash .codex/skills/trello-etf-batch/tests/test_backlog_split_contract.sh
```
Expected: PASS.
- [ ] Step 7: Commit:
```bash
git add .codex/skills/trello-etf-backlog
git commit -m "feat: add Trello ETF backlog splitter skill"
```

## Task 3: Implement Skill 2 result routing

**Files:**
- Create .codex/skills/trello-etf-result/SKILL.md and agents/openai.yaml.
- Test .codex/skills/trello-etf-batch/tests/test_result_transition_contract.sh.

**Interfaces:**
- Consumes: one selected child card and the complete result envelope from Skill 3.
- Produces: child in Done and complete for strict success, or child in Blocked with persisted failure metadata and reason.

- [ ] Step 1: Add this frontmatter and input contract:
```yaml
---
name: trello-etf-result
description: "Use when a Trello ETF child card needs to be moved to Done or Blocked from a validated processing result."
---
```
Require an exact card target, workflow trello-etf-item, parent_ari, ticker and all seven result fields. Normalize code by trimming, lowercasing and replacing spaces/underscores with hyphens.
- [ ] Step 2: Accept only PASS + scope item + durable_write completed + exhausted false + confirmation none + success or durable-write-complete; move to Done, complete it, preserve metadata and return card/output links.
- [ ] Step 3: For every non-success or invalid envelope, append/update result_status, result_scope, result_code, result_reason, durable_write and confirmation in the child description, preserve workflow/parent_ari/ticker, then move to Blocked. Do not complete it or create an exception card. Trello mutation/auth failure is global.
- [ ] Step 4: Add agent metadata:
```yaml
interface:
  display_name: "Trello ETF Result Router"
  short_description: "Move ETF child cards to Done or Blocked from results"
  default_prompt: "Use $trello-etf-result with one child card and its result envelope."
policy:
  allow_implicit_invocation: false
```
- [ ] Step 5: Run:
```bash
bash .codex/skills/trello-etf-batch/tests/test_result_transition_contract.sh
```
Expected: PASS.
- [ ] Step 6: Commit:
```bash
git add .codex/skills/trello-etf-result
git commit -m "feat: add Trello ETF result router skill"
```

## Task 4: Implement Skill 3 ETF processing

**Files:**
- Create .codex/skills/trello-etf-processing/SKILL.md and agents/openai.yaml.
- Test .codex/skills/trello-etf-batch/tests/test_processing_contract.sh.

**Interfaces:**
- Consumes: one exact child card in Ready for AI with workflow, parent_ari and canonical ticker.
- Produces: one complete result envelope and downstream links for Skill 2; no durable vault files.

- [ ] Step 1: Add this frontmatter and boundary:
```yaml
---
name: trello-etf-processing
description: "Use when a Trello ETF child card in Ready for AI must be processed by check-etf-performance."
---
```
State that the skill owns the child claim and handoff only; it must not perform source discovery, research delegation, reviewer work or vault writes locally.
- [ ] Step 2: Require Ready for AI, read ticker, move to In Progress and directly reread the same card. If the lane does not confirm In Progress, return global claim-state-error and do not invoke downstream. Do not touch cards in In Progress, Blocked or Done.
- [ ] Step 3: After a confirmed claim invoke:
```text
$check-etf-performance <TICKER>
mode: lean
```
Wait for research delegation, reconciliation, pre-save review and durable-write result. Require the complete envelope; normalize missing/contradictory output to ERROR, scope global, code unknown-result. Forward it to trello-etf-result and never move the child to Done/Blocked directly.
- [ ] Step 4: Add agent metadata:
```yaml
interface:
  display_name: "Trello ETF Performance Processor"
  short_description: "Claim a Ready-for-AI ETF card and run its ticker performance check"
  default_prompt: "Use $trello-etf-processing on one Ready for AI ETF child card."
policy:
  allow_implicit_invocation: false
```
- [ ] Step 5: Run:
```bash
bash .codex/skills/trello-etf-batch/tests/test_processing_contract.sh
```
Expected: PASS.
- [ ] Step 6: Commit:
```bash
git add .codex/skills/trello-etf-processing
git commit -m "feat: add Trello ETF processing skill"
```

## Task 5: Rewrite trello-etf-batch as Skill 4 manager/router

**Files:**
- Modify .codex/skills/trello-etf-batch/SKILL.md, automation-prompt.md and agents/openai.yaml.
- Test .codex/skills/trello-etf-batch/tests/test_manager_routing_contract.sh.

**Interfaces:**
- Consumes: scheduler prompt with task and positive count; Trello cards in configured lanes.
- Produces: sequential Skill 1 calls for backlog, or Skill 3 then Skill 2 calls for ETF performance, bounded by count.

- [ ] Step 1: Keep name trello-etf-batch; rewrite description/body as manager/router. Remove active exact-parent, ETF queue, batch_size and exception-card runtime ownership. Preserve a short note that old checklist/exception text is inert history.
- [ ] Step 2: Require:
```text
task: backlog|etf-performance
count: <positive base-10 integer>
```
Reject missing, duplicate, zero, negative, fractional or nonnumeric values as workflow-config-mismatch before mutation. Never infer count.
- [ ] Step 3: For task backlog, select at most count open master cards in Backlog, order oldest-first, track attempted_this_run by master ARI, call $trello-etf-backlog sequentially, and never select the same master twice while it remains in Backlog.
- [ ] Step 4: For task etf-performance, select at most count valid child cards in Ready for AI, order oldest-first, and run:
```text
trello-etf-processing(child card)
→ trello-etf-result(child card, processing result)
```
Continue after an accepted ticker-specific failure once Skill 2 blocks that child. Stop on global Trello/auth/board/list/configuration failures. Never touch other lanes or select a card twice in one run.
- [ ] Step 5: Rewrite automation-prompt.md with:
```text
task: etf-performance
count: 1
```
State that the scheduler may change count, must not overlap manager workers for the same board, and only the requested number is processed sequentially.
- [ ] Step 6: Update manager metadata:
```yaml
interface:
  display_name: "Trello ETF Workflow Manager"
  short_description: "Route Trello ETF backlog and performance tasks"
  default_prompt: "Use $trello-etf-batch with task and count in the scheduler prompt."
policy:
  allow_implicit_invocation: true
```
Constrain the description to Trello ETF workflow prompts, not unrelated Trello actions.
- [ ] Step 7: Run:
```bash
bash .codex/skills/trello-etf-batch/tests/test_manager_routing_contract.sh
```
Expected: PASS.
- [ ] Step 8: Commit:
```bash
git add .codex/skills/trello-etf-batch/SKILL.md \
  .codex/skills/trello-etf-batch/automation-prompt.md \
  .codex/skills/trello-etf-batch/agents/openai.yaml
git commit -m "feat: route Trello ETF workflow through focused skills"
```

## Task 6: Validate the complete skill set and clean stale references

**Files:** Verify the four active SKILL.md files, their agents/openai.yaml files, manager prompt and all focused tests.

**Interfaces:**
- Consumes: all four active skill contracts and focused tests.
- Produces: validated contracts with no active skill claiming old monolithic runtime state.

- [ ] Step 1: Validate metadata:
```bash
for skill_dir in \
  .codex/skills/trello-etf-backlog \
  .codex/skills/trello-etf-processing \
  .codex/skills/trello-etf-result \
  .codex/skills/trello-etf-batch; do
  python3 /Users/mangkornkatawong/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill_dir"
done
```
Expected: all four pass.
- [ ] Step 2: Run all focused tests:
```bash
for test_file in .codex/skills/trello-etf-batch/tests/test_*.sh; do
  bash "$test_file"
done
```
Expected: all four pass.
- [ ] Step 3: Search active contracts for stale ownership:
```bash
rg -n "ETF queue|trello-etf-batch-status|create or reuse exactly one exception card|batch_size|exact parent card URL" \
  .codex/skills/trello-etf-backlog \
  .codex/skills/trello-etf-processing \
  .codex/skills/trello-etf-result \
  .codex/skills/trello-etf-batch
```
Expected: no active skill uses the old checklist, legacy status block, exception-card or batch_size runtime contract.
- [ ] Step 4: Run diff checks:
```bash
git diff --check
git status --short
```
Confirm only intended skills, prompt, metadata and tests changed; preserve unrelated work and the committed design/ADR/glossary.
- [ ] Step 5: If validation required a tracked correction, stage only active skill/test files and commit:
```bash
git add .codex/skills/trello-etf-backlog \
  .codex/skills/trello-etf-processing \
  .codex/skills/trello-etf-result \
  .codex/skills/trello-etf-batch
git commit -m "test: validate Trello ETF skill decomposition"
```
If no correction was needed, do not create an empty commit.

## Final handoff

After execution, report the four active skill paths, scheduler prompt format, test/validator results, commit hashes and any limitation such as unavailable live Trello connector access. Do not claim that real Trello cards moved unless a connected Trello run actually performed and confirmed those mutations.
