# Market Data Evidence

Immutable JSON envelopes created by `scripts/fetch_alpaca_data.py` live under
dated subdirectories here. Each envelope records the documented endpoint,
non-secret parameters, request/response timestamps, raw response payload, and
SHA-256 payload hash.

Never edit or overwrite an evidence file. A corrected fetch creates a new file.
