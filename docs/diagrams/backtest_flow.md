# Backtest Event Flow (Sprint 1)

For each trading day (ts) in chronological order:

  Load slice for this ts:
    frame(ts) = all rows where row.ts == ts (one row per symbol present)

  Strategy decision:
    orders = Strategy.on_bar(ts, frame(ts))

  Price snapshot:
    prices_at_ts = { row.symbol: row.close for row in frame(ts) if close is valid }

  Simulate execution:
    fills = Broker.simulate(orders, prices_at_ts)
      - Sprint 1: market orders fill at close
      - Ignore orders for symbols missing from prices_at_ts

  Update portfolio:
    Portfolio.apply_fills(fills, prices_at_ts)

  Mark to market:
    equity = Portfolio.mark_to_market(ts, prices_at_ts)

Outputs after loop:
  - equity_timeseries from Portfolio.equity_history
  - trades_log aggregated from fills
