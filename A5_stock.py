#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_profit_loss(N, stocks_info, M, stock_prices, day):
    realized_profit = 0
    unrealized_profit = 0
    max1=max2=0
    for i in range(N):
        quantity, purchase_day, sell_day = stocks_info[i]
        if sell_day == 0 or sell_day > day:
            unrealized_profit += quantity * (stock_prices[i][day - 1] - stock_prices[i][purchase_day - 1])
        else:
            realized_profit += quantity * (stock_prices[i][sell_day - 1] - stock_prices[i][purchase_day - 1])
        
        if(max1<realized_profit):
            max1=realized_profit
        if(max2<unrealized_profit):
            max2=unrealized_profit
    return max1,max2


N = int(input())
stocks_info = [tuple(map(int, input().split())) for _ in range(N)]
M = int(input())
stock_prices = [list(map(int, input().split())) for _ in range(N)]
day = int(input())


realized_profit, unrealized_profit = calculate_profit_loss(N, stocks_info, M, stock_prices, day)
print(realized_profit)
print(unrealized_profit)

