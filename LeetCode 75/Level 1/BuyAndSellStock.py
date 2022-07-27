'''Thoughts
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
'''Examples
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''
'''Thoughts
1. Get the minimum of the list
2. Get the maximum of the list after the index of the minimum
Failed to [3,2,6,5,0,3]

1. Set buy to 0 and sell to 1 and max_profit to 0
2. Loop while sell < the length of prices
3. current_profit is prices[sell] - prices[buy]
4. If sell is less than buy, set buy to sell
5. If buy is less than sell, set max_profit to max(max_profit, current_profit)
6. Increase sell by 1
7. return max_profit
'''

# def stonks(prices:list):
#     if len(prices) < 2:
#         return 0
#     buy = min(prices[:-1])
#     sell = max(prices[prices.index(buy)+1:])
#     profit = sell - buy
#     if profit < 0:
#         return 0
#     return profit

def stonks(prices:list):
    buy = 0
    sell = 1
    max_profit = 0
    while sell < len(prices):
        current_profit = prices[sell] - prices[buy]
        if prices[sell] <= prices[buy]:
            buy = sell
        else:
            max_profit = max(max_profit, current_profit)
        sell += 1
    return max_profit