---
name: dcf-valuation
description: Use when the user asks for fair value, intrinsic value, DCF, valuation sensitivity, upside/downside, or a price target for an operating company stock.
---

# DCF Valuation

## Instrument Boundary

Use this skill for operating companies, not ETFs. If `instrument_type: ETF` or
an exchange-qualified fund identity is detected, do not request company FCF,
cash, debt, shares, or WACC and do not create a DCF memo. Route passive,
index-tracking equity ETFs to `official-source-etf-research` for price/NAV,
look-through, cost, tracking, yield, and peer-relative analysis. Return
`unsupported ETF type` for ETF categories outside that skill's v1 scope.

## Required References

Read `source-hierarchy.md`, `financial-ratios.md`,
`valuation-assumptions.md`, and `output-contract.md` from `wiki/reference/`.

## Required Inputs

- freshly checked stock price and timestamp
- verified historical or TTM FCF, or OCF minus capex
- cash and short-term investments
- total debt or debt-like obligations
- diluted shares
- business/sector basis for WACC
- explicit forecast growth and terminal growth assumptions

Prefer three to five annual FCF periods, current guidance, reinvestment context,
and margin/ROIC history.

## Stage Gate

Classify the run before writing:

- `calculation-ready`: inputs support a DCF or another explicit valuation model.
- `blocked`: a required input is missing, incompatible, or the model is
  unsuitable for the business.

For `blocked`, return a compact blocker in chat or the decision memo. Do not
create `TICKER DCF Valuation...md` unless the user explicitly asks for a gap
memo.

## Calculation Workflow

1. Read existing entity/fundamentals and freshly verify market data.
2. Reconcile FCF, cash, debt, shares, guidance, and period labels.
3. Label base, upside, and downside assumptions; choose WACC and terminal growth
   from the business risk and source-backed context.
4. Project FCF, discount it, calculate terminal value, enterprise value, equity
   value, and per-share value.
5. Add at least a 3x3 sensitivity table when a point estimate is meaningful.
6. Sanity-check implied FCF yield and relevant own-history/peer multiples when
   sourced.
7. Save `wiki/analysis/valuations/TICKER DCF Valuation YYYY-MM-DD.md`, update
   entity valuation watch items only when changed, and append one log bullet.

```text
FCF = operating cash flow - capex spend
EV = PV(projected FCF) + PV(terminal value)
Equity value = EV + cash - debt
Fair value/share = equity value / diluted shares
Terminal value = Year 5 FCF * (1 + g) / (WACC - g)
```

## Memo Recipe

Use a bottom line, compact source links, input table, assumptions, projection,
valuation summary, sensitivity, sanity checks, valuation-specific blockers, and
change triggers. Do not copy the entity thesis or decision bull/bear case.

Narrative limit: 500 words in `lean`, 900 in `full`; tables are exempt. Warn
when terminal value exceeds 85%-90% of EV.

## Model Boundary

Use reverse DCF, peer multiples, unit economics, or scenarios for pre-profit,
financial, highly cyclical, optionality-heavy, or unstable-FCF businesses. Label
each lens and avoid false precision.
