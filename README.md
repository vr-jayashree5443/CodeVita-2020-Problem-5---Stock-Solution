Certainly, let's break down the provided solution step by step:

1. **Function `calculate_profit_loss`:**
   - The function takes five parameters: `N` (number of stocks), `stocks_info` (information about each stock - quantity bought, time of purchase, and time of sell), `M` (number of days for which stock prices are provided), `stock_prices` (stock prices for each day for each stock), and `day` (the specific day for which the profit/loss needs to be computed).
   - It initializes `realized_profit` and `unrealized_profit` to 0, which will store the calculated realized and unrealized profits, respectively.
   - It iterates through each stock, checking if it has been sold or not.
     - If the stock is not sold (`sell_day == 0` or `sell_day > day`), it calculates the unrealized profit by subtracting the purchase price from the current market price and multiplies it by the quantity.
     - If the stock is sold, it calculates the realized profit by subtracting the purchase price from the sell price and multiplies it by the quantity.
   - It keeps track of the maximum realized profit (`max1`) and maximum unrealized profit (`max2`) encountered during the iterations.
   - The function returns `max1` (maximum realized profit) and `max2` (maximum unrealized profit).

2. **Main Function:**
   - The main function starts by taking input for the number of stocks (`N`).
   - It then takes input for each stock's information (`stocks_info`) - quantity bought, time of purchase, and time of sell.
   - It takes input for the number of days (`M`).
   - It takes input for the stock prices (`stock_prices`) for each day for each stock.
   - It takes input for the specific day (`day`) for which the profit/loss needs to be computed.
   - It calls the `calculate_profit_loss` function with the provided inputs and prints the results.

### Example:

Let's take the first example provided:
- `N = 3`
- `stocks_info = [(10, 4, 20), (10, 1, 11), (100, 6, 0)]`
- `M = 22`
- `stock_prices = [[113, 115, 112, ..., 121, 122], [52, 53, ..., 72, 73], [101, 102, ..., 121, 122]]`
- `day = 5`

The function `calculate_profit_loss` is called with these inputs, and it calculates both realized and unrealized profits at the end of Day 5. The results are printed.

The output will be:
```
0
60
```

The second example is similar, but the specific day for calculating profit/loss is Day 20. The output will be:
```
120
1400
```

This means that the realized profit is 120, and the unrealized profit is 1400 at the end of Day 20.
