# Alpha Momentum Test Plan

## Dataset
3 symbols, 30 trading days, daily closes:
- AAA: strictly increasing prices (momentum always high)
- BBB: flat prices
- CCC: strictly decreasing prices

## Expectation
- AAA always ranked #1, BBB #2, CCC #3
- With K=2, we should always hold AAA and BBB
- No trades after initial buys until the end
- Final equity = starting_cash + gains from AAA (and flat from BBB)
