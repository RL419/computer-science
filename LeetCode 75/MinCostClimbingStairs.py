'''Instructions
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''
'''Examples
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
'''
'''Thoughts
1. Recursion on climbing 1 step and 2 steps and get the minimum cost
2. Memo dictionary to reduce runtime
'''


def minCostClimbingStairs(self, cost: list[int], memo=None) -> int:
    if memo is None:
        memo = {}
    if len(cost) == 1:
        return 0
    if len(cost) == 2:
        return min(cost)
    if len(cost) not in memo.keys():
        memo[len(cost)] = min(cost[0] + minCostClimbingStairs(cost[1:], memo=memo), cost[1] + minCostClimbingStairs(cost[2:], memo=memo))
    return memo[len(cost)]