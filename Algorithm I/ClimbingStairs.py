'''Instructions
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
'''Examples
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
'''Thoughts
1. If n is 0 return0= 0 if n is 1 return 1 and if n is 2 return 2
2. Recurison on taking one step and taking 2 steps and add them together
3. Memo to shorten runtime
'''

def climbStairs(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in memo.keys():
        memo[n] = climbStairs(n-1, memo=memo) + climbStairs(n-2, memo=memo)
    return memo[n]