# Chart Conventions

Use Obsidian `chart` blocks only with verified, comparable data backed by a
table in the same file or a linked normalized file.

## Limits

- `chat`: no durable chart
- `lean`: at most one decision-relevant chart
- `full`: at most three charts

Choose charts by decision value, not merely because data exists. Omit empty
chart sections and placeholders.

## Selection

| Data shape | Chart | Rule |
|---|---|---|
| Same fiscal quarter across years | bar | Compare the same quarter only. |
| Sequential quarters | line | Keep source period labels. |
| Comparable YTD periods | bar | Do not mix with single-quarter data. |
| Complete fiscal years | bar or line | Use complete years only. |
| Stable segments | bar | Use multiple periods only with stable taxonomy. |
| OCF, capex, FCF | bar | Show capex as positive spend and label it. |
| Balance-sheet snapshots | bar | Use point-in-time dates. |

## Required Shape

```chart
type: bar
labels: ["Period A", "Period B"]
series:
  - title: Metric
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [0, 0]
```

Never plot missing, estimated, implied, mixed-unit, or period-incompatible
values. Keep the table as the source of truth and the chart as a view.
