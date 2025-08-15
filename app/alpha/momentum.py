"""
Momentum Strategy (Sprint 1)
----------------------------
Goal: Select top-K symbols by recent return and hold them equally weighted.

Constructor params:
- lookback_days (int)
- top_k (int)
- dollar_per_position (float)

Methods:
- on_bar(ts, frame) -> list[Order]
    Inputs:
    - ts: current date
    - frame: DataFrame with all symbols at ts
      Columns: ts, symbol, open, high, low, close, volume
    Logic:
    - Compute momentum over lookback_days (will need precomputed history)
    - Rank symbols by momentum
    - Generate BUY orders for new entries in top K
    - Generate SELL orders for symbols dropped from top K
    - Generate adjustment orders if current qty != target qty
    Output: list of Order objects
"""
