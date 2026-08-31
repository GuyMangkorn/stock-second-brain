# Markdown Research Queue cutover runbook

This runbook is intentionally executable without a migration schema. It keeps
Trello read-only and turns the existing scheduled job into a Research Queue
dispatcher only after the pilot is verified.

## 1. Read and seed

Immediately before cutover, read the live `Ready for AI` and `Blocked` lists on
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

Run one card with the existing ETF performance workflow in
`execution_profile: scheduled-inline` and the caller boundary
`caller: research-queue-manager`, `handoff: research_handoff`. Confirm:

- the card claim has a renewable two-hour lease and fencing token;
- the ETF pre-save gate records `verification_mode: scheduled-local` and
  `reviewer_dispatch: not-attempted-by-design`;
- only the complete seven-field handoff can route the card to Done or Blocked;
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
Acquire the project lease, select oldest-first, claim and reread each card,
invoke check-etf-performance with caller: research-queue-manager and
handoff: research_handoff, renew at safe phase boundaries, and route only the
complete structured result. Process sequentially and stop globally on lease,
configuration, claim-state, or contradictory-result failures. Continue after
item-scoped Blocked results. Never dispatch a sub-agent or select/mutate Trello.
Commit one terminal card with its scoped outputs and preserve unrelated edits.
```

## 4. Verify

After the automation update, verify there is still exactly one active ETF
dispatcher, its next run targets the Research Queue, and Trello remains
unchanged. Keep the legacy Trello skills available temporarily for rollback,
but do not call them from the active schedule.
