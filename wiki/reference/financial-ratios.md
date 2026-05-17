# Financial Ratios

Compute ratios only when inputs are fully supported and period-compatible.

| Ratio | Formula | Notes |
|---|---|---|
| Current Ratio | `current_assets / current_liabilities` | Use balance sheet values at period end. |
| Quick Ratio | `(cash + short_term_investments + accounts_receivable) / current_liabilities` | Do not estimate missing components. |
| D/E Ratio | `total_liabilities / total_equity` | Vault default unless a task specifies debt/equity. |
| Interest Coverage | `EBIT / interest_expense` | Requires verified EBIT and interest expense. |
| Gross Profit Margin | `gross_profit / revenue` | Display as percent. |
| Operating Margin | `operating_income / revenue` | Display as percent. |
| Net Profit Margin | `net_income / revenue` | Display as percent. |
| ROE | `net_income / average_equity` | Average equity requires beginning and ending equity. |
| P/E | `current_price / trailing_diluted_eps` | Requires fresh price and EPS basis. |
| P/BV | `current_price / book_value_per_share` | Requires book value per share or full inputs. |
| Dividend Yield | `annual_dividend_per_share / current_price` | Requires compatible DPS and price date. |
| Dividend Payout | `dividend_per_share / eps` | Use per-share approach by default. |

Rules:

- Label calculations.
- Do not mix annual and quarterly periods without saying so.
- If inputs are missing, mark unavailable and add the gap to
  `Missing / Unverified Data`.

