'''Instructions
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''
'''Examples
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0
'''
'''Thoughts
idk
'''

def coin_change(coins:list, amount:int):
    coins.sort()

    out = 0
    while amount > 0:
        if not coins:
            return -1
        big = coins.pop()
        out += amount // big
        amount %= big
    return out if amount == 0 else -1