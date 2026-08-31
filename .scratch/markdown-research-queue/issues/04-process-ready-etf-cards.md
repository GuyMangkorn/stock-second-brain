# 04: Process and commit Ready ETF cards end to end

**What to build:** Deliver the first operational Research Queue manager slice: select Ready ETF cards, claim and process them sequentially through ETF performance, route results, and create one scoped terminal commit per card.

**Blocked by:** 02, 03

**Status:** ready-for-agent

- [ ] The manager requires a positive count and rejects zero, negative, missing, or non-numeric counts without changing cards.
- [ ] Eligible Ready cards are selected in oldest-first deterministic order, with a stable tie-breaker.
- [ ] Only supported ETF-performance cards are claimed in V1; unsupported or malformed cards receive a stable, inspectable disposition.
- [ ] The manager rereads a card after claiming it and before invoking research so that it does not process a lost or changed claim.
- [ ] Scheduled execution runs inline in the top-level context and processes one card at a time without dispatching sub-agents.
- [ ] A valid successful handoff moves the card to Done and links its durable outputs instead of copying their contents into the card.
- [ ] An item-scoped failure moves only that card to Blocked and processing continues until the requested count is exhausted; a global failure stops the run.
- [ ] Each terminal card transition and its scoped research outputs are committed together in exactly one Git commit.
- [ ] Unrelated working-tree changes remain unstaged and unmodified.
- [ ] Behavioral tests cover selection order, count limits, item continuation, global stop, result routing, linked outputs, and scoped commit contents.
