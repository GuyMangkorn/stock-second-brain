---
status: accepted
---

# Keep the Paper Portfolio Ledger Local

Use one project-local append-only Portfolio Ledger as the system of record for the ETF Paper Portfolio Competition, while treating the Alpaca paper account as a planned Execution Mirror for order submission and fill evidence. This preserves reproducible total-return accounting, dividends, corporate actions, corrections, and benchmark comparison because paper-broker fills and liquidity are simulated and the Alpaca paper environment does not simulate dividends; making the broker canonical would couple competition history to those limitations, while keeping two equal state owners would create unreconcilable ambiguity. The currently connected Alpaca app exposes market-data GET tools only in this workspace, so automatic execution remains blocked until an order-capable paper connector is explicitly available and authorized.
