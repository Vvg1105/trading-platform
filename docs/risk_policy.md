# Risk Policy (Sprint 1)

## Purpose
Define simple limits so the strategy cannot take outsized risk.

## Position & Portfolio Limits
- Per-position cap: max 2% of portfolio value in a single symbol
- Max gross exposure: 100% of portfolio value
  - (Gross = sum of absolute position values)

## Daily Loss Limit (planned for Sprint 2)
- If equity drops by 5% or more from start-of-day, stop opening new positions for that day.

## Enforcement (Sprint 1)
- We will document these limits and design for them.
- Hard enforcement (blocking orders) can be added in Sprint 2.

## Notes
- No leverage in Sprint 1.
- Shorting behavior is optional; if used later, caps apply to absolute exposure.
