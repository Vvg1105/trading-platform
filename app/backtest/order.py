"""
Order & Fill Models (Sprint 1)
------------------------------
Purpose:
- Define the minimal data needed to express trading intentions (Order)
  and the result after simulated execution (Fill).

Order (intended fields):
- ts: timestamp of decision
- symbol: string ticker
- qty: integer number of shares (+ long, - short)
- note: optional string for audit/debug (e.g., "momentum long leg")

Fill (intended fields):
- ts: timestamp of execution
- symbol: string ticker
- qty: integer filled (can be <= order qty in other sprints)
- price: executed price (Sprint 1: bar close)
- note: optional string for audit/debug

Notes:
- Market-only in Sprint 1 (fills at close).
- Direction: qty > 0 buy; qty < 0 sell.
- Later sprints can add order_id, limit price, partial fills, fees, slippage.
"""
