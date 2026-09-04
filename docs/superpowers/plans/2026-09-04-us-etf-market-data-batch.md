# US ETF Market Data Batch and Screen Cache Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task with checkpoints.

**Goal:** เปลี่ยน US ETF Portfolio Run จากหลักฐาน JSON แยกต่อ ticker เป็นหนึ่ง immutable evidence batch ต่อ run พร้อม rolling screen cache ที่คัด ETF จาก price history ได้โดยไม่สแกน historical evidence ทั้งหมด.

**Architecture:** `price-log.md` ยังคงเป็น append-only historical index และ `latest-prices.md` คง path เดิมแต่เปลี่ยนเป็น compact screen cache ที่มี recent completed-session context และ derived metrics. Direct market-data browser evidence ของหนึ่ง run จะรวมใน batch JSON เดียวใต้ `evidence/market-data/batches/`; helper จะ validate batch, append compact log rows และ merge cache แบบ incremental.

**Tech Stack:** Python 3 standard library, JSON, Markdown tables/frontmatter, `unittest`, existing `rebuild_portfolio.py`, and Codex automation update API for the scheduler record.

**Spec:** `docs/superpowers/specs/2026-09-04-us-etf-market-data-batch-design.md`

## Global Constraints

- `ledger/events.jsonl` remains the local Portfolio Ledger and accounting system of record.
- Existing dated evidence under `evidence/market-data/YYYY-MM-DD/` remains immutable legacy evidence; do not move, delete, or rewrite it.
- Every new verified market-data observation preserves discovery query, direct URL, page title, visible values/text, source-as-of, retrieval time, and SHA-256 content hash; local clock evidence records its local-command method instead of a web URL/query.
- `latest-prices.md` is preliminary screening only; a `BUY` proposal cites direct batch evidence and a final decision reference price.
- `price-log.md` remains append-only; one verified price observation produces exactly one compact log row.
- Scheduled-inline does not dispatch reviewers/subagents and does not call an order route.
- Existing admission, freshness, liquidity, overlap, risk, turnover, Proposal Phase, and open-ended lifecycle rules do not change.
- Normal runs read the compact screen cache and only the price-log tail; full price-log parsing is reserved for bootstrap/recovery or in-process idempotency checks.
- Use only Python standard-library dependencies and preserve the repository's `unittest` test style.

## File Map

| File | Responsibility in this change |
|---|---|
| `paper-portfolios/us-etf-competition/scripts/market_data_pipeline.py` | Pure batch validation, hash checks, compact log-row rendering, screen-cache parsing/merge, and one-time cache bootstrap logic. |
| `paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py` | CLI boundary that validates an already captured batch, writes the immutable batch, appends the log, and atomically updates the screen cache. |
| `tests/test_market_data_pipeline.py` | Unit and temporary-root integration tests for schema, hash/cutoff rules, cache metrics, idempotency, legacy preservation, and one-batch-per-run behavior. |
| `paper-portfolios/us-etf-competition/PROMPT.md` | Runtime instructions for cache-first screening, finalist-only direct refresh, batch evidence, and recovery behavior. |
| `paper-portfolios/us-etf-competition/config.yaml` | Canonical paths and explicit market-data storage/read policy. |
| `paper-portfolios/us-etf-competition/README.md` | Human-facing workflow and source/evidence documentation. |
| `paper-portfolios/us-etf-competition/evidence/market-data/README.md` | Evidence envelope, batch, cache, legacy, and append-only log contract. |
| `paper-portfolios/us-etf-competition/evidence/market-data/latest-prices.md` | Derived screen-cache projection, migrated in place from the current latest-row table. |
| `paper-portfolios/us-etf-competition/evidence/market-data/price-log.md` | Existing history plus new compact rows; no historical rewrite. |
| `paper-portfolios/us-etf-competition/evidence/market-data/batches/` | New one-file-per-Portfolio-Run full evidence store; created when the first new batch is recorded. |
| `/Users/mangkornkatawong/.codex/automations/us-etf-paper-portfolio-competition/automation.toml` | Scheduler record updated through `mcp__codex_app__automation_update`; keep the prompt concise and delegate detailed behavior to the project prompt. |

## Batch Contract

The implementation must accept a batch object with this shape. The full
market-data browser envelope is retained inside `calendar` and each
`observations` item; the cache
and price log only project the fields needed for fast screening and audit.

```json
{
  "schema_version": 2,
  "kind": "market-data-batch",
  "competition_id": "us-etf-competition-2026",
  "run_id": "run-2026-09-04-040254-et",
  "analysis_at": "2026-09-04T08:02:54Z",
  "information_cutoff_at": "2026-09-04T08:02:54Z",
  "created_at": "2026-09-04T08:42:28Z",
  "evidence_status": "verified",
  "post_period_data_used": false,
  "clock": {"evidence_id": "run-2026-09-04-040254-et:clock", "provider": "system clock", "method": "local-time-command", "kind": "invocation-clock", "retrieved_at": "2026-09-04T08:42:28Z", "visible_response_text": "Invocation clock: 2026-09-04 04:02:54 EDT (America/New_York); UTC 2026-09-04T08:02:54Z; scheduled review is pre-market; latest completed U.S. session is September 3, 2026.", "content_hash": "sha256:3169ec8355d5d008d170abf156601e18b3b2d3c009fd3d08b0a5a5f33cf53c55", "information_cutoff_at": "2026-09-04T08:02:54Z", "post_period_data_used": false},
  "calendar": {"evidence_id": "run-2026-09-04-040254-et:calendar", "provider": "NYSE", "method": "browser-direct-web", "kind": "calendar", "discovery_method": "browser_search", "discovery_query": "site:nyse.com 2026 holidays trading calendar September 4 2026 NYSE official", "direct_url": "https://www.nyse.com/trade/hours-calendars", "page_title": "Holidays & Trading Hours", "retrieved_at": "2026-09-04T08:42:28Z", "visible_response_text": "All NYSE markets observe U.S. holidays as listed below for 2026, 2027, and 2028. Labor Day in 2026 is Monday, September 7. NYSE Arca Equities core trading session is 9:30 a.m. to 4:00 p.m. ET. September 4, 2026 is not listed as a holiday.", "content_hash": "sha256:30bb32a88b4d05c2f9ce19c565c3ea29df7949b33e77386e8bb3c7d0c32d41ec", "information_cutoff_at": "2026-09-04T08:02:54Z", "post_period_data_used": false},
  "observations": [
    {
      "evidence_id": "run-2026-09-04-040254-et:quote:VOO",
      "observation_kind": "quote-history",
      "ticker": "VOO",
      "exchange_qualified_identity": "NYSEARCA:VOO",
      "provider": "StockAnalysis.com",
      "underlying_data_source": "Tiingo",
      "method": "browser-direct-web",
      "discovery_method": "browser_search",
      "discovery_query": "site:stockanalysis.com/etf/voo/history VOO ETF historical price",
      "direct_url": "https://stockanalysis.com/etf/voo/history/",
      "page_title": "VOO Historical Stock Price Data",
      "visible_response_text": "Vanguard S&P 500 ETF (VOO) | NYSEARCA:VOO | Sep 3, 2026, 4:00 PM EDT - Market closed | Close 710.72 | Adj. Close 710.72 | Change 1.04% | Volume 8,536,838 | Historical rows: Sep 2 close 703.41 volume 7,702,258; Sep 1 close 700.28 volume 6,447,027; Aug 31 close 704.89 volume 5,719,456; Aug 28 close 707.24 volume 8,054,710 | Data Source Tiingo | Last updated Sep 3, 2026 | Last checked Sep 4, 2026",
      "content_hash": "sha256:6f5fef574ba1e2442454c44688a315e55fd7743f8640127d1ac5d4afef097d90",
      "response_sha256": "sha256:6f5fef574ba1e2442454c44688a315e55fd7743f8640127d1ac5d4afef097d90",
      "retrieved_at": "2026-09-04T08:42:28Z",
      "source_as_of": "2026-09-03T16:00:00-04:00",
      "price": 710.72,
      "currency": "USD",
      "price_basis": "completed-session close",
      "latest_completed_session": "2026-09-03",
      "five_session_observations": [],
      "median_daily_dollar_volume_usd": 5417845299.78,
      "decision_reference": true,
      "post_period_data_used": false
    }
  ]
}
```

The sample text and hashes above are concrete examples copied from the verified
current evidence shape. The writer must reject empty visible text and invalid
hashes in a real batch. `content_hash` is computed from `visible_response_text`; when
`response_sha256` is present it must match the same digest. `source_as_of` must
not be after `information_cutoff_at`; a later `retrieved_at` is allowed only
when the source-as-of and period are before the cutoff and
`post_period_data_used` remains false.

## Tasks

### Task 1: Add failing contract and projection tests

**Files:**
- Create: `tests/test_market_data_pipeline.py`
- Reference: `paper-portfolios/us-etf-competition/evidence/market-data/latest-prices.md`
- Reference: `paper-portfolios/us-etf-competition/evidence/market-data/price-log.md`

**Interfaces:**
- Consumes: the batch shape in this plan and the current Markdown cache/log formats.
- Produces: executable tests that define `MarketDataError`, `validate_batch`, `render_price_log_rows`, `merge_screen_cache`, `bootstrap_screen_cache`, and `record_batch` before implementation.

- [ ] **Step 1: Create deterministic test helpers and a valid batch fixture.**

  Add a `sha256_text()` helper, a `valid_batch()` factory with one calendar,
  one clock, and a representative quote observation (`VOO`), and a Markdown cache
  fixture containing one legacy latest-price row. Use fixed timestamps and
  prices; do not call the network.

  Load the script under test with `importlib.util.spec_from_file_location`
  because the project directory name contains a hyphen. Keep all fixtures
  under `tempfile.TemporaryDirectory()` so the real portfolio evidence is not
  touched.

  ```python
  def sha256_text(value: str) -> str:
      return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()

  def valid_batch() -> dict[str, object]:
      visible = "VOO | NYSEARCA:VOO | At close: Sep 3, 2026 | Close 710.72"
      return {
          "schema_version": 2,
          "kind": "market-data-batch",
          "competition_id": "test",
          "run_id": "run-2026-09-04-040254-et",
          "analysis_at": "2026-09-04T08:02:54Z",
          "information_cutoff_at": "2026-09-04T08:02:54Z",
          "created_at": "2026-09-04T08:42:28Z",
          "evidence_status": "verified",
          "post_period_data_used": False,
          "clock": {"evidence_id": "clock", "visible_response_text": "clock", "content_hash": sha256_text("clock")},
          "calendar": {"evidence_id": "calendar", "visible_response_text": "calendar", "content_hash": sha256_text("calendar")},
          "observations": [{
              "evidence_id": "run-2026-09-04-040254-et:quote:VOO",
              "observation_kind": "quote-history",
              "ticker": "VOO",
              "exchange_qualified_identity": "NYSEARCA:VOO",
              "direct_url": "https://stockanalysis.com/etf/voo/history/",
              "page_title": "VOO Historical Stock Price Data",
              "discovery_query": "site:stockanalysis.com/etf/voo/history VOO ETF historical price",
              "visible_response_text": visible,
              "content_hash": sha256_text(visible),
              "retrieved_at": "2026-09-04T08:42:28Z",
              "source_as_of": "2026-09-03T16:00:00-04:00",
              "price": 710.72,
              "currency": "USD",
              "price_basis": "completed-session close",
              "latest_completed_session": "2026-09-03",
              "five_session_observations": [{"session_date": "2026-09-03", "close": 710.72, "volume_shares": 8536838}],
              "post_period_data_used": False,
          }],
      }
  ```

- [ ] **Step 2: Add validator failure tests and run them.**

  Cover missing direct URL, duplicate `evidence_id`, altered visible text with
  the old hash, source-as-of after the cutoff, `post_period_data_used: true`,
  and a quote missing `price_basis`.

  Run: `python3 -m unittest -v tests.test_market_data_pipeline`

  Expected: FAIL because `paper-portfolios/us-etf-competition/scripts/market_data_pipeline.py` does not exist yet.

- [ ] **Step 3: Add projection and integration failure tests.**

  Define tests that require the following behavior:

  ```python
  def test_merge_screen_cache_keeps_one_row_and_calculates_returns(self):
      rendered = merge_screen_cache(legacy_cache, valid_batch())
      self.assertIn("etf-price-screen-cache", rendered)
      self.assertIn("VOO", rendered)
      self.assertEqual(rendered.count("| VOO |"), 1)

  def test_record_batch_creates_one_batch_and_no_ticker_json_files(self):
      result = record_batch(root, batch_path)
      self.assertEqual(result["batch_files_created"], 1)
      canonical = root / "evidence/market-data/batches/run-2026-09-04-040254-et.json"
      self.assertEqual(list((root / "evidence/market-data/batches").glob("*.json")), [canonical])
      self.assertEqual(list((root / "evidence/market-data/batches").glob("quote_*.json")), [])

  def test_recording_same_batch_twice_is_idempotent(self):
      first = record_batch(root, batch_path)
      log_after_first = price_log.read_text(encoding="utf-8")
      second = record_batch(root, batch_path)
      self.assertEqual(second["duplicate_batch"], True)
      self.assertEqual(price_log.read_text(encoding="utf-8"), log_after_first)
  ```

  Run the same unittest command; these tests must fail for missing interfaces or
  incorrect behavior before implementation begins.

- [ ] **Step 4: Commit the test contract.**

  ```bash
  git add tests/test_market_data_pipeline.py
  git commit -m "test: define ETF market data batch contract"
  ```

### Task 2: Implement batch validation and immutable batch writing

**Files:**
- Create: `paper-portfolios/us-etf-competition/scripts/market_data_pipeline.py`
- Create: `paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py`
- Test: `tests/test_market_data_pipeline.py`

**Interfaces:**
- Consumes: `valid_batch()` fixtures and batch JSON supplied by the scheduled agent.
- Produces:
  - `class MarketDataError(ValueError)`
  - `def load_batch(path: Path) -> dict[str, Any]`
  - `def validate_batch(batch: Mapping[str, Any]) -> None`
  - `def render_price_log_rows(batch: Mapping[str, Any]) -> list[str]`
  - `def merge_screen_cache(cache_text: str, batch: Mapping[str, Any]) -> str`
  - `def bootstrap_screen_cache(log_text: str) -> str`
  - `def record_batch(root: Path, batch_path: Path, *, check_only: bool = False) -> dict[str, Any]`
  - CLI: `python3 record_market_data_batch.py --root ROOT --batch BATCH [--check]`
  - CLI recovery mode: `python3 record_market_data_batch.py --root ROOT --bootstrap-cache [--check]`

- [ ] **Step 1: Implement strict parsing and hash/cutoff validation.**

  In `market_data_pipeline.py`, parse ISO-8601 timestamps with timezone
  awareness, compute `sha256:` digests from UTF-8 visible text, and raise
  `MarketDataError` with the evidence ID and field name in every failure.
  Require `schema_version == 2`, `kind == "market-data-batch"`, non-empty
  `run_id`, `analysis_at`, `information_cutoff_at`, `created_at`, clock,
  calendar, and an observations list. Require unique evidence IDs across clock,
  calendar, and observations. Require clock and calendar envelopes to contain
  an evidence ID, kind, retrieval time, visible text, content hash,
  `information_cutoff_at`, and `post_period_data_used`; calendar additionally
  requires provider, discovery method/query, direct URL, and page title. The
  local clock uses its recorded command method in place of web discovery fields.
  Require direct observations to contain a ticker,
  exchange-qualified identity, discovery query, direct URL, page title, visible
  text, content hash, source-as-of, price, currency, and price basis.

  Reject a source-as-of after the information cutoff, a hash mismatch including
  a present `response_sha256`, a true
  post-period flag, a non-finite price, a timezone-less timestamp, or a missing
  completed-session date when `price_basis` contains `completed-session`.

- [ ] **Step 2: Implement the CLI and immutable batch file rule.**

  Treat `batch_path` and the CLI `--batch` value as a read-only captured-batch
  input. The helper must load and validate it before any project file is
  changed, derive the canonical destination as
  `root/evidence/market-data/batches/{run_id}.json`, and create the destination
  directory when needed. If the destination already exists, compare canonical
  JSON bytes: identical content returns a duplicate summary; different content
  raises `MarketDataError` and never overwrites the batch. This lets a scheduled
  run capture into a temporary staging file and still guarantees one immutable
  project batch per run.
  `--check` validates and prints a JSON summary without modifying any file.

  ```python
  summary = {
      "status": "PASS",
      "run_id": batch["run_id"],
      "observations": len(batch["observations"]),
      "duplicate_batch": existing_bytes == canonical_bytes,
  }
  ```

- [ ] **Step 3: Run validator and CLI tests.**

  Run: `python3 -m unittest -v tests.test_market_data_pipeline`

  Expected: all schema, hash, cutoff, duplicate-ID, immutable-file, and
  check-only tests PASS.

- [ ] **Step 4: Commit the batch validator.**

  ```bash
  git add paper-portfolios/us-etf-competition/scripts/market_data_pipeline.py paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py tests/test_market_data_pipeline.py
  git commit -m "feat: validate ETF market data batches"
  ```

### Task 3: Implement compact price-log projection and rolling screen cache

**Files:**
- Modify: `paper-portfolios/us-etf-competition/scripts/market_data_pipeline.py`
- Modify: `paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py`
- Modify: `tests/test_market_data_pipeline.py`
- Modify: `paper-portfolios/us-etf-competition/evidence/market-data/latest-prices.md`
- Preserve: `paper-portfolios/us-etf-competition/evidence/market-data/price-log.md` historical rows

**Interfaces:**
- Consumes: validated quote observations, current cache text, and the existing compact log table.
- Produces: one compact price-log row per quote, one cache row per ticker, rolling metrics, and a bootstrap command that reads old history once.

- [ ] **Step 1: Define and test the new cache table schema.**

  Use these columns in `latest-prices.md` so the agent sees meaningful history
  without opening raw evidence:

  ```text
  Ticker | Exchange-qualified identity | Latest Price | Currency | Price Basis |
  Source As-of | Retrieved At | Recent Completed Closes | 1-Session Return |
  5-Session Return | 20-Session Return | Recent Drawdown |
  Five-Session Median Dollar Volume | Evidence Batch | Evidence ID | Status
  ```

  Store recent closes as a bounded semicolon-separated series such as
  `2026-09-03:710.72;2026-09-02:703.41`; retain no more than 20 completed-session
  points per ticker. Use the same `price_basis` for all return calculations.
  Use `not disclosed` when a window has insufficient points, and never mix
  intraday rows with completed-session returns.

- [ ] **Step 2: Implement log-row rendering.**

  `render_price_log_rows()` must preserve the existing Markdown header and emit
  one row per quote observation. The row keeps ticker, identity, price, USD
  basis, source-as-of, retrieved-at, provider, direct URL, a local evidence
  reference of the form `[batch quote](batches/run-2026-09-04-040254-et.json)`
  plus the evidence ID `run-2026-09-04-040254-et:quote:VOO`, and status. It must
  not copy visible response text into the log.

- [ ] **Step 3: Implement incremental cache merge.**

  `merge_screen_cache()` must parse the current cache, merge only quote
  observations from the validated batch, retain the prior 20 completed-session
  closes, and replace the affected ticker rows without duplicating them. If a
  batch contains multiple quote observations for one ticker, use the newest
  completed-session observation for rolling metrics; otherwise use the newest
  verified observation and mark the row `PRELIMINARY` or `REFRESH_REQUIRED`.
  Keep every observation in the price log even when only one becomes the cache
  row. Compute
  1-session, 5-session, and 20-session returns as
  `(latest / prior) - 1`, using percentages rounded to two decimals. Compute
  recent drawdown as `latest / rolling_high - 1`, also rounded to two decimals.
  Compute five-session median dollar volume only from observations with both
  close and volume. Preserve `LIQUIDITY_FAIL`, `STALE`, `PRELIMINARY`, and
  `REFRESH_REQUIRED` flags supplied by the observation; do not downgrade a
  failure to PASS because the price changed.

- [ ] **Step 4: Add one-time bootstrap from the existing price log.**

  `bootstrap_screen_cache(log_text)` parses the existing 13-column Markdown
  price-log table, ignores prose after the table, groups rows by ticker, and
  selects only completed-session close rows for rolling metrics. It preserves
  the latest source URL/evidence reference and marks rows with `PRELIMINARY` or
  stale statuses as supplied by history. It must not create new full evidence
  JSON files and must not edit any historical price-log row.

- [ ] **Step 5: Write atomic cache updates and test idempotency.**

  Write the cache to a sibling temporary file and replace it with `os.replace`
  only after rendering and parsing succeed. Before appending log rows, detect
  an existing evidence reference for the same batch observation; skip it and
  report `duplicate_observations` rather than append a second row. A retry of
  the exact same batch must leave both log and cache byte-for-byte unchanged.

- [ ] **Step 6: Bootstrap the current cache and verify the projection.**

  Run the new bootstrap command against the current `price-log.md`, inspect that
  each current ticker appears exactly once, and verify that old source links are
  still present. Do not move or delete the dated JSON evidence.

  Run:

  ```bash
  python3 paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py \
    --root paper-portfolios/us-etf-competition --bootstrap-cache --check
  ```

  Expected: `PASS`, with the number of input price rows and projected ticker
  rows reported; no project file changes in `--check` mode.

- [ ] **Step 7: Run focused tests and commit.**

  Run: `python3 -m unittest -v tests.test_market_data_pipeline`

  Expected: PASS for rolling metrics, missing-window handling, legacy bootstrap,
  duplicate suppression, atomic cache behavior, and old-link preservation.

  ```bash
  git add paper-portfolios/us-etf-competition/scripts/market_data_pipeline.py paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py tests/test_market_data_pipeline.py
  git commit -m "feat: add ETF price screen cache projections"
  ```

### Task 4: Migrate project instructions to batch-first evidence

**Files:**
- Modify: `paper-portfolios/us-etf-competition/PROMPT.md`
- Modify: `paper-portfolios/us-etf-competition/config.yaml`
- Modify: `paper-portfolios/us-etf-competition/README.md`
- Modify: `paper-portfolios/us-etf-competition/evidence/market-data/README.md`
- Modify: `paper-portfolios/us-etf-competition/runs/README.md`
- Test: `tests/test_market_data_pipeline.py`

**Interfaces:**
- Consumes: the batch/cache CLI contract from Tasks 2–3.
- Produces: one authoritative project workflow that the scheduled automation and future agents can follow without scanning legacy evidence.

- [ ] **Step 1: Add canonical config paths and policy flags.**

  Extend `config.yaml` without removing current compatibility keys:

  ```yaml
  market_data:
    provider: browser-direct-web
    evidence_root: evidence/market-data
    batch_root: evidence/market-data/batches
    legacy_evidence_root: evidence/market-data/YYYY-MM-DD
    screen_cache_path: evidence/market-data/latest-prices.md
    append_only_log_path: evidence/market-data/price-log.md
    normal_read_policy: screen-cache-plus-price-log-tail
    full_log_read_policy: bootstrap-or-recovery-only
    one_batch_per_run: true
  ```

  Keep `price_cache.latest_path` and `price_cache.append_only_log_path` as
  compatibility aliases until all readers use the new names.

- [ ] **Step 2: Replace duplicated evidence instructions in `PROMPT.md`.**

  Update the source-discipline and required-run sections with these exact rules:

  ```text
  Read latest-prices.md as the compact screen cache and only the tail of price-log.md before discovery. Do not scan historical evidence directories during a normal run.
  Use the screen cache and existing research to form a shortlist. Open direct quote pages only for current holdings, SPY, and candidates whose price can change the decision.
  Store all full market-data browser evidence captured in this Portfolio Run in one immutable evidence batch under evidence/market-data/batches/. Do not create a new JSON file per ticker for new runs.
  After validation, run record_market_data_batch.py to append compact price-log rows and update latest-prices.md. A BUY proposal must cite the direct batch evidence ID, never cache alone.
  Existing dated evidence is legacy and remains read-only. Use bootstrap/recovery parsing only when the screen cache is missing or invalid.
  ```

  Keep all existing calendar, freshness, admission, ledger, no-trade, and
  Proposal Phase requirements unchanged.

- [ ] **Step 3: Update human-facing README contracts.**

  Explain the three layers (`price-log`, screen cache, batch), show one new run
  layout, state that old dated JSON remains legacy, and link the batch CLI. Update
  `runs/README.md` so new run notes cite one batch path plus evidence IDs while
  old notes retain their existing links.

- [ ] **Step 4: Add documentation contract tests.**

  Assert that `PROMPT.md` contains `one immutable evidence batch`,
  `record_market_data_batch.py`, and `Do not create a new JSON file per ticker`;
  `config.yaml` contains `batch_root`, `screen_cache_path`, and
  `one_batch_per_run: true`; and the evidence README identifies dated folders as
  legacy and `price-log.md` as append-only.

- [ ] **Step 5: Run documentation and project checks, then commit.**

  Run:

  ```bash
  python3 -m unittest -v tests.test_market_data_pipeline tests.test_paper_portfolio
  git diff --check
  ```

  Expected: all tests PASS and no whitespace errors.

  ```bash
  git add paper-portfolios/us-etf-competition/PROMPT.md paper-portfolios/us-etf-competition/config.yaml paper-portfolios/us-etf-competition/README.md paper-portfolios/us-etf-competition/evidence/market-data/README.md paper-portfolios/us-etf-competition/runs/README.md tests/test_market_data_pipeline.py
  git commit -m "docs: define batch-first ETF evidence workflow"
  ```

### Task 5: Update the scheduled automation prompt without changing cadence

**Files/API:**
- Update via `mcp__codex_app__automation_update` for automation name `US ETF Paper Portfolio Competition`.
- Reference: `/Users/mangkornkatawong/.codex/automations/us-etf-paper-portfolio-competition/automation.toml`
- Reference: `paper-portfolios/us-etf-competition/PROMPT.md`
- Test: `tests/test_market_data_pipeline.py` and a read-back of the automation record.

**Interfaces:**
- Consumes: the project prompt and batch CLI contract.
- Produces: an ACTIVE weekday 15:00 ET scheduler whose prompt is concise and points to the project-local source of truth.

- [ ] **Step 1: Read and snapshot the current automation record.**

  Use the automation view before updating. Preserve its current `ACTIVE` status,
  weekday 15:00 rule, local execution environment, project target, model, and
  reasoning effort. Only the prompt body should change.

- [ ] **Step 2: Replace the duplicated long prompt with this concise scheduler prompt.**

  ```text
  Run exactly one Portfolio Run for paper-portfolios/us-etf-competition. Read PROMPT.md, config.yaml, ledger/events.jsonl, state/portfolio.json, the latest run note, and the screen cache before analysis. Use the project batch-first market-data workflow: cache-first shortlist, direct quote only for decision-relevant candidates, one immutable market-data evidence batch per run, compact price-log append, and incremental screen-cache update. Preserve legacy dated evidence, never scan the full historical evidence tree during a normal run, and never dispatch subagents/reviewers or place orders under scheduled-inline. If mandatory data is missing, stale, conflicting, or unavailable, record BLOCKED/NO_TRADE and preserve the portfolio. Keep the open-ended lifecycle and Proposal Phase rules from the project prompt.
  ```

- [ ] **Step 3: Read back the automation and verify cadence.**

  Confirm the automation remains `ACTIVE`, retains the weekday 15:00 rule, points
  to the same local project, and contains the batch/cache rules. Do not create a
  second automation and do not change notification policy.

- [ ] **Step 4: Record the scheduler change in the project log.**

  Add one concise dated `portfolio-policy` bullet to `log.md` naming the batch-
  first evidence change and stating that cadence, portfolio rules, and old
  evidence paths were preserved. Stage only `log.md` for this documentation
  entry and commit:

  ```bash
  git add log.md
  git commit -m "chore: route ETF automation through batch evidence"
  ```

### Task 6: End-to-end rollout and verification

**Files:**
- Modify: `paper-portfolios/us-etf-competition/evidence/market-data/latest-prices.md` through the bootstrap command
- Create on first real run: `paper-portfolios/us-etf-competition/evidence/market-data/batches/run-YYYY-MM-DD-HHMMSS-et.json`
- Modify on first real run: `paper-portfolios/us-etf-competition/evidence/market-data/price-log.md`, ledger, run note, state, and dashboard
- Test: `tests/test_market_data_pipeline.py`, `tests/test_paper_portfolio.py`

**Interfaces:**
- Consumes: all previous task contracts and the project-local portfolio state.
- Produces: a verified rollout that future runs can execute with one batch per run and no historical migration.

- [ ] **Step 1: Run the cache bootstrap in write mode.**

  ```bash
  python3 paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py \
    --root paper-portfolios/us-etf-competition --bootstrap-cache
  ```

  Verify that only the derived `latest-prices.md` changes, historical
  `price-log.md` rows are byte-for-byte unchanged, and no legacy JSON file is
  moved or deleted.

- [ ] **Step 2: Run a local synthetic batch through the write path.**

  Use the fixed `valid_batch()` fixture with a temporary project root. Confirm
  one batch file, one log row per observation, one cache row per ticker, and no
  `quote_*.json` files in the batch directory. Run the same batch twice and
  confirm no duplicate rows.

- [ ] **Step 3: Validate the real portfolio state before and after rollout.**

  ```bash
  python3 paper-portfolios/us-etf-competition/scripts/rebuild_portfolio.py --check
  python3 -m unittest -v tests.test_market_data_pipeline tests.test_paper_portfolio
  git diff --check
  ```

  Expected: ledger check PASS, portfolio value and positions unchanged, no
  order/fill events, and all focused tests PASS.

- [ ] **Step 4: Verify the next scheduled-run contract without placing orders.**

  Inspect the prompt/cache paths and confirm the next run will read the compact
  screen cache, read only the log tail, refresh only shortlisted direct pages,
  and write one batch. Do not invoke a live or paper order route.

- [ ] **Step 5: Inspect scoped Git state and commit the rollout only.**

  ```bash
  git status --short
  git diff --stat
  git diff --check
  ```

  Preserve unrelated worktree changes. Stage only the migration/cache/batch,
  portfolio documentation, and focused test files from this plan. Commit:

  ```bash
  git add paper-portfolios/us-etf-competition/evidence/market-data/latest-prices.md paper-portfolios/us-etf-competition/evidence/market-data/README.md paper-portfolios/us-etf-competition/evidence/market-data/price-log.md paper-portfolios/us-etf-competition/scripts/market_data_pipeline.py paper-portfolios/us-etf-competition/scripts/record_market_data_batch.py tests/test_market_data_pipeline.py
  git commit -m "feat: roll out ETF market data batch workflow"
  ```

## Final Acceptance Checklist

- A synthetic run refreshing SPY plus three candidates creates one batch JSON and zero new per-ticker JSON files.
- A real batch rejects missing metadata, duplicate evidence IDs, mismatched hashes, post-cutoff source-as-of, and unsupported/missing price basis before any projection write.
- `latest-prices.md` has one compact rolling summary per ticker and can form a shortlist without opening historical evidence.
- `price-log.md` receives exactly one compact row per verified observation, preserves all old rows, and does not duplicate a retried batch.
- A `BUY` proposal cites direct batch evidence and a decision reference price; cache-only evidence cannot pass the final gate.
- Cache bootstrap works once from existing history and does not create retroactive full evidence batches.
- Old dated evidence and old run-note links remain readable.
- `rebuild_portfolio.py --check`, focused market-data tests, portfolio tests, JSON parsing, hash checks, and link checks pass.
- The scheduler remains ACTIVE on weekdays at 15:00 ET with the same project target, and scheduled-inline still does not dispatch reviewers or place orders.
- No unrelated research-queue or ETF-performance worktree change is staged or committed.
