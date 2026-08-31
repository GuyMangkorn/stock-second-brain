# 03: Add a Trello-independent ETF result boundary

**What to build:** Give the ETF-performance workflow a backward-compatible Research Queue caller contract and a deterministic result-routing boundary, without breaking the existing Trello caller during cutover.

**Blocked by:** None

**Status:** ready-for-agent

- [ ] The ETF-performance workflow can return a `research_handoff` containing exactly the seven approved fields: outcome, card ID, entity key, workflow, output paths, error code, and error summary.
- [ ] The new caller contract is additive and the legacy Trello caller continues to behave as before during the transition.
- [ ] A result router validates the handoff shape and refuses missing, extra, malformed, or mismatched fields.
- [ ] Only a verified success with durable expected outputs is eligible for Done.
- [ ] A failure scoped to one item maps to Blocked with a stable error code and permits the batch manager to continue.
- [ ] A global failure stops further processing and leaves unstarted cards unchanged.
- [ ] Success is never inferred from prose, process exit alone, or the mere presence of a file.
- [ ] Behavioral tests exercise valid success, item failure, global failure, invalid envelopes, and the unchanged legacy contract.
