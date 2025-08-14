# Backtester Specification (Sprint 1)

## Goal (plain English)
Play historical prices one day at a time. At each day, ask the strategy
“what orders do you want?”, simulate those orders, update cash/positions,
and track total account value (equity). Produce an equity curve and a trades log.

## Data In (from parquet)
Columns: ts (UTC), symbol, open, high, low, close, volume
Frequency: daily bars

## Core Concepts
- Order: an instruction to buy/sell a symbol and quantity at this timestamp
- Fill: the executed result of an order (ts, symbol, qty, price actually filled)
- Portfolio: tracks cash, positions per symbol, and total equity over time

## Interfaces to Implement (Sprint 1)
- Strategy interface:
  - `on_bar(ts, frame) -> list[Order]`
  - Input `frame`: all rows for this timestamp (one per symbol), includes at least `symbol` and `close`.
- Broker simulation:
  - `simulate(orders, prices_at_ts) -> list[Fill]`
  - Sprint 1 simplification: all market orders fill at the `close` price of that day.
- Portfolio:
  - `apply_fills(fills, prices_at_ts) -> None` (update cash & positions)
  - `mark_to_market(ts, prices_at_ts) -> equity_value` (record equity history)

## Assumptions (Sprint 1)
- Daily bars only
- Market orders only (fill at close)
- Transaction cost placeholder (we may ignore in Sprint 1; add later as fixed bps)
- No leverage (cannot spend more cash than available)
- If a symbol is missing for a day, we just trade the ones present

## Outputs
- Equity time series: `[ {ts, equity}, ... ]`
- Trades log: `[ {ts, symbol, qty, price}, ... ]`

## Acceptance Scenarios (become tests)
1) **Buy & Hold (1 symbol)**
   - Start with $1,000,000. Buy fixed number of shares on first day.
   - Equity should rise/fall exactly with price afterward (ignoring costs).
2) **Equal-Weight (2 symbols)**
   - Rebalance to 50/50 at start of each month.
   - Equity should match a hand-calculated spreadsheet within tolerance.
3) **Missing Dates / Holidays**
   - If some dates are missing for a symbol, the run does not crash, and positions carry over correctly to the next available date.
