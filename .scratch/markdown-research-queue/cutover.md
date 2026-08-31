# Markdown Research Queue cutover runbook

runbook นี้ทำตามได้โดยไม่ต้องมี migration schema ถาวร โดยคง
Trello read-only and turns the existing scheduled job into a Research Queue
dispatcher only after the pilot is verified.

## 1. Read and seed

ก่อน cutover ให้อ่าน live `Ready for AI` และ `Blocked` บน
the historical `stock-analysis-task` board. Extract only each card's ticker and
discard descriptions, Trello status, comments, provenance, and ARIs. Pass the
deduplicated values through normal Intake:

```bash
python3 scripts/research_queue.py seed --input-file <project-relative-ticker-list>
```

The input file is temporary cutover material and is not a migration artifact;
remove it after the command if it was created in the project. Do not mutate
Trello. Verify the created/reused/rejected counts against the fresh source set.

## 2. Pilot

รันหนึ่งการ์ดด้วย ETF performance workflow เดิมใน
`execution_profile: scheduled-inline` and the caller boundary
`caller: research-queue-manager`, `handoff: research_handoff`, and `mode: lean`.
แล้วตรวจยืนยันว่า:

- the card claim has a renewable two-hour lease and fencing token;
- the ETF pre-save gate records `verification_mode: scheduled-local` and
  `reviewer_dispatch: not-attempted-by-design`;
- only the complete seven-field handoff, at least one existing output path, and
  a scoped Git commit can route the card to Done or Blocked;
- the card, scoped outputs, and no unrelated user edits are in the terminal
  commit; and
- the Intake and Monitor projections reconcile with files on disk.

## 3. Update the existing automation in place

Keep the existing automation identity `etf-performance-check` and preserve its
active status, three-hour cadence, count ten, `gpt-5.6-luna` model, `max`
reasoning effort, project-local target, and scheduled-inline profile. Replace
only its prompt with the following behavior:

```text
Use [$research-queue-manager](.codex/skills/research-queue-manager/SKILL.md)

count: 10
execution_profile: scheduled-inline

Select only Ready Research Cards with workflow: check-etf-performance.
Acquire and retain the project lease from selection through the downstream
write (`claim-next --keep-lease`), select oldest-first, claim and reread each card,
invoke check-etf-performance with caller: research-queue-manager and
handoff: research_handoff, mode: lean, and execution_profile: scheduled-inline;
renew at safe phase boundaries with the lease token and route only the
complete structured result with explicit output paths and a scoped commit.
Process sequentially and stop globally on lease,
configuration, claim-state, or contradictory-result failures. Continue after
item-scoped Blocked results. Never dispatch a sub-agent or select/mutate Trello.
Release the retained lease after the bounded run. Commit one terminal card with
its scoped outputs and preserve unrelated edits.
```

## 4. Verify

After the automation update, verify there is still exactly one active ETF
dispatcher, its next run targets the Research Queue, and Trello remains
unchanged. Keep the legacy Trello skills available temporarily for rollback,
but do not call them from the active schedule.
