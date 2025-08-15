# Test Plan (Sprint 1)

Goal:
- Validate core mechanics of backtester using small, deterministic toy datasets.

## Unit Scenarios

S1) Buy & Hold (single symbol)
- Toy data: 5 trading days with strictly rising closes (e.g., 100, 101, 102, 103, 104).
- Action: Buy fixed shares on day 1; hold.
- Expectation: Equity increases day-by-day by shares * delta(close).
- Edge: no orders after day 1; engine must still mark to market.

S2) Equal-Weight (two symbols, monthly rebalance)
- Toy data: 40 trading days; symbol A uptrend, symbol B downtrend.
- Action: Rebalance to 50/50 at day 1 and every 21st trading day.
- Expectation: Equity matches hand spreadsheet within small tolerance.

S3) Missing Dates (holiday/gap)
- Toy data: symbol A has days 1,2,4,5 (missing day 3); symbol B has all days 1..5.
- Action: Buy & hold both.
- Expectation: Engine does not crash on day 3; positions carry; equity computed using available prices.

S4) No-Leverage Constraint
- Toy data: price 100, initial cash 1000.
- Action: Strategy attempts to buy 20 shares (cost 2000).
- Expectation: Either order is rejected or clipped (define behavior before implementing). Cash never negative.

S5) Zero/NaN Price
- Toy data: one day has NaN close for one symbol.
- Expectation: Orders for that symbol on that day are ignored; run completes.

## Metrics Sanity Checks
- Equity series length equals number of unique trading days processed.
- Final equity >= 0 and is finite (no NaN/inf).
- Trades log entries have valid ts, symbol, integer qty, positive price.
