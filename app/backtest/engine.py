"""
Backtest Engine (Sprint 1)

--------------------------

Role:
- Orchestrates the backtest loop over daily bars.
- For each timestamp (ts) it:
    1) Provides the full cross-section to the Strategy
    2) Receives zero-or-more Orders from the Strategy.
    3) Sends Orders + current prices to Broker to simulate Fills.
    4) Applies Fills to the Portfolio (cash, positions).
    5) Marks the Portfolio to market and records equity.

Inputs:
- Bars DataFrame with columns: [ts, symbol, open, high, low, close, volume]
- Strategy instance exposing: on_bar(ts, frame) -> list[Order]
- Broker instance exposing: simulate(orders, prices_at_ts) -> list[Fill]
- Portfolio instance exposing:
    apply_fills(fills, prices_at_ts) -> None
    mark_to_market(ts, prices_at_ts) -> float (equity)

Outputs:
- equity_timeseries: list[dict(ts, equity)]
- trades_log: list[dict(ts, symbol, qty, price)]

Assumptions (Sprint 1):
- Daily bars; market orders fill at close.
- No leverage; ignore transaction costs for now.
- Missing symbols at a ts are allowed; trade only what's present.

Edge Cases to handle (later in code):
- Empty order list.
- Missing symbol price when filling (skip that order).
- NaN prices: skip trading for that symbol on this ts.

"""