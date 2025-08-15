# Alpha Design (Sprint 1)

## Strategy 1 — Cross-Sectional Momentum (Long-Only, Simplified)

### Goal
Own the few assets that have performed best recently, expecting them to keep performing well.

### Logic
1. For each trading day (ts), calculate the percentage return from N days ago to today’s close for each symbol:
   momentum = (close_today / close_N_days_ago) - 1
2. Rank all symbols by momentum, highest to lowest.
3. Select the top K symbols (e.g., top 2) to buy/hold.
4. Sell any symbols currently held that are no longer in the top K.
5. Rebalance daily so each top symbol has the same dollar amount invested.

### Parameters
- Lookback period (N days): 20
- Number of symbols to hold (K): 2
- Dollar allocation per position: $50,000
- Trading cost: ignored in Sprint 1 (will add later)

### Position sizing (Sprint 1)
- Fixed-dollar sizing: qty = floor(dollar_allocation / close_price)

### Edge cases
- If fewer than K symbols have valid data: hold fewer positions that day.
- If momentum is NaN (missing data), skip that symbol for the day.
- If close_price <= 0, skip that symbol.

### Outputs from on_bar()
- List of Orders:
    - If symbol is in top K and not currently held: BUY qty shares.
    - If symbol was held but not in top K: SELL all shares.
    - If symbol is still in top K but qty differs from target: BUY/SELL the difference.
