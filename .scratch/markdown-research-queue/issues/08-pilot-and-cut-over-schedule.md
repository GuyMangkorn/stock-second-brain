# 08: Pilot and cut over the scheduled Research Queue

**What to build:** Prove the complete flow with one manually processed card, then update the existing scheduled ETF job in place to use the Markdown Research Queue while preserving its approved operating settings.

**Blocked by:** 05, 06, 07

**Status:** ready-for-agent

- [ ] A manual pilot with count one starts from a Ready card and finishes with the expected lease lifecycle, valid handoff, durable ETF outputs, terminal card state, and scoped Git commit.
- [ ] The pilot confirms the ETF pre-save verification gate follows the scheduled-inline route and records the required local-review markers.
- [ ] The Base Board and monitor show the pilot transition and their counts reconcile with disk after completion.
- [ ] The existing ETF performance automation is updated in place rather than replaced by a second scheduled job.
- [ ] The cutover preserves the three-hour cadence, count ten, selected model and reasoning effort, project-local execution target, and scheduled-inline profile.
- [ ] Scheduled selection reads only Ready Research Cards from the Markdown queue and performs no Trello selection or mutation.
- [ ] A post-cutover verification confirms the automation configuration, next-run readiness, queue visibility, and absence of duplicate active automation.
- [ ] The legacy Trello skills remain available temporarily for rollback but are not called by the active automation.
- [ ] The final handoff records the pilot evidence, cutover outcome, and any remaining rollback or cleanup follow-up without claiming research completion for unprocessed cards.
