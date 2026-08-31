# 05: Recover expired claims with renewable leases and fencing

**What to build:** Make In Progress ownership safe across overlapping scheduled runs by adding a renewable two-hour lease, a fencing token, execution phases, and deterministic stale-claim recovery.

**Blocked by:** 04

**Status:** ready-for-agent

- [ ] Claiming a Ready card atomically records In Progress state, owner identity, lease expiry, fencing token, and the initial execution phase.
- [ ] The default lease expires two hours after its latest successful renewal.
- [ ] The current owner can renew before expiry, while another run cannot take over an unexpired claim.
- [ ] After expiry, exactly one contender can acquire a new fencing token and become the current owner.
- [ ] Every state transition and durable research write verifies the current fencing token immediately before mutation; a stale owner cannot finalize or write.
- [ ] An expired claim still in a demonstrably pre-write/no-output phase returns to Ready for retry.
- [ ] An expired claim in writing/finalizing, or with ambiguous partial output, moves to Blocked with a stable error code instead of retrying automatically.
- [ ] Recovery decisions are based on explicit phase and output evidence, not on generic `updated_at` activity alone.
- [ ] Tests use a controllable clock and cover renewal, overlap rejection, single-winner takeover, stale-owner fencing, safe retry, and ambiguous partial-write blocking.
