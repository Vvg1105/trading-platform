"""
Portfolio (Sprint 1)
--------------------
Role:
- Track cash, positions per symbol, and equity over time.
- Apply Fills to update cash/positions.
- Mark portfolio to market with current prices and record equity history.

State (intended):
- cash: float
- positions: dict[symbol -> shares]
- equity_history: list[dict(ts, equity)]

Key responsibilities:
- apply_fills(fills, prices_at_ts):
    For each fill, decrease/increase cash by qty*price and update positions.
    No leverage: if a buy would make cash negative, reject or clip (decide in engine spec).
- mark_to_market(ts, prices_at_ts):
    Compute equity = cash + sum(positions[s]*prices[s] for all s with price).
    Append {"ts": ts, "equity": equity} to equity_history.

Constraints (Sprint 1):
- No margin/leverage; cash cannot go below zero.
- Shorting optional in later sprint; if added, track borrow via negative positions.
"""
