# Market Data Evidence

Immutable browser evidence envelopes live under dated subdirectories here. Each
envelope records the discovery query, direct page URL, page title, visible
response text/values, source as-of timestamp, retrieval timestamp, and a
SHA-256 content hash. Search-result snippets are discovery context only, never
the sole evidence for a price or market-status decision.

[`latest-prices.md`](latest-prices.md) is the derived latest-price table used for
fast preliminary screening. [`price-log.md`](price-log.md) is the append-only
history of verified browser price observations. A stale cache can narrow the
refresh scope but cannot replace a fresh quote required by the decision gate.

Never edit or overwrite an evidence file. A corrected fetch creates a new file.
