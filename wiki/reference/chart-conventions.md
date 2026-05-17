# Chart Conventions

Use Obsidian `chart` blocks only with verified data. Every chart must be backed
by a Markdown table in the same file or a linked source note. Do not plot values
that are missing, estimated, or only implied.

## Chart Selection Rules

Choose the chart from the shape of the verified data:

| Data shape | Chart section | Rule |
|---|---|---|
| Same fiscal quarter across different years, such as FY25 Q3 vs FY26 Q3 | `## Quarterly YoY Comparison` | Compare the same quarter only. Do not mix 9M or annual data in this chart. |
| Sequential quarters, such as Q1, Q2, Q3, Q4 | `## Quarterly Trend` | Use source labels exactly as reported. |
| Year-to-date periods, such as 9M FY25 vs 9M FY26 | `## YTD Comparison` | Keep YTD separate from single-quarter charts. |
| Full fiscal years, such as FY2023, FY2024, FY2025 | `## Annual Trend` | Use only complete fiscal years. |
| Segment data with stable taxonomy | `## Segment Revenue Chart` | Use multiple periods only if segment definitions are comparable. |
| Cash flow and capex data | `## Cash Flow And Capex Chart` | Plot capex as positive spend when helpful, and label it clearly. |
| Balance sheet snapshots | `## Balance Sheet Snapshot Chart` | Use point-in-time labels, not income-statement periods. |

## Quarterly YoY Comparison

```chart
type: bar
labels: ["FY25 Q3", "FY26 Q3"]
series:
  - title: Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [0, 0]
  - title: Operating Income
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [0, 0]
  - title: Net Income
    backgroundColor: rgba(251, 191, 36, 0.72)
    borderColor: rgba(252, 211, 77, 1)
    data: [0, 0]
```

## Quarterly Trend

Use this when the source provides a sequence of quarters.

```chart
type: line
labels: ["FY25 Q4", "FY26 Q1", "FY26 Q2", "FY26 Q3"]
series:
  - title: Revenue
    backgroundColor: rgba(16, 185, 129, 0.18)
    borderColor: rgba(52, 211, 153, 1)
    data: [0, 0, 0, 0]
  - title: Net Income
    backgroundColor: rgba(56, 189, 248, 0.18)
    borderColor: rgba(125, 211, 252, 1)
    data: [0, 0, 0, 0]
```

## YTD Comparison

```chart
type: bar
labels: ["9M FY25", "9M FY26"]
series:
  - title: Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [0, 0]
  - title: Net Income
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [0, 0]
  - title: Free Cash Flow
    backgroundColor: rgba(251, 191, 36, 0.72)
    borderColor: rgba(252, 211, 77, 1)
    data: [0, 0]
```

## Annual Trend

Use this only for complete fiscal years.

```chart
type: bar
labels: ["FY2023", "FY2024", "FY2025"]
series:
  - title: Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [0, 0, 0]
  - title: Operating Income
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [0, 0, 0]
  - title: Net Income
    backgroundColor: rgba(251, 191, 36, 0.72)
    borderColor: rgba(252, 211, 77, 1)
    data: [0, 0, 0]
```

## Segment Revenue Chart

Use multiple periods only when segment taxonomy is stable. If taxonomy changes,
use latest-period-only and explain why.

```chart
type: bar
labels: ["Segment A", "Segment B", "Segment C"]
series:
  - title: FY26 Q3 Revenue
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [0, 0, 0]
  - title: FY25 Q3 Revenue
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [0, 0, 0]
```

## Cash Flow And Capex Chart

Use positive values for capex spend when the source table reports capex as a
cash outflow. Label it as `Capex Spend`.

```chart
type: bar
labels: ["FY25 Q3", "FY26 Q3"]
series:
  - title: Operating Cash Flow
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [0, 0]
  - title: Capex Spend
    backgroundColor: rgba(244, 63, 94, 0.64)
    borderColor: rgba(251, 113, 133, 1)
    data: [0, 0]
  - title: Free Cash Flow
    backgroundColor: rgba(251, 191, 36, 0.72)
    borderColor: rgba(252, 211, 77, 1)
    data: [0, 0]
```

## Balance Sheet Snapshot Chart

```chart
type: bar
labels: ["2025-06-30", "2026-03-31"]
series:
  - title: Assets
    backgroundColor: rgba(16, 185, 129, 0.72)
    borderColor: rgba(52, 211, 153, 1)
    data: [0, 0]
  - title: Liabilities
    backgroundColor: rgba(244, 63, 94, 0.64)
    borderColor: rgba(251, 113, 133, 1)
    data: [0, 0]
  - title: Equity
    backgroundColor: rgba(56, 189, 248, 0.68)
    borderColor: rgba(125, 211, 252, 1)
    data: [0, 0]
```

Palette order:

- emerald: `rgba(16, 185, 129, 0.72)`
- sky: `rgba(56, 189, 248, 0.68)`
- amber: `rgba(251, 191, 36, 0.72)`
- violet: `rgba(139, 92, 246, 0.68)`
- rose: `rgba(244, 63, 94, 0.64)`

Avoid charts when units conflict, source coverage is incomplete, period labels
are not comparable, or a chart would make the data look more certain than it is.
