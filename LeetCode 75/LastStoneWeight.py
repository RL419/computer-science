'''Instructions
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
'''
'''Examples
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Input: stones = [1]
Output: 1
'''
'''Thoughts
1. Sort stones
2. Remove 0s
3. If stones is empty return 0
4. If there is onlt one element in stones return the element
5. Get the stones with max weight and smash them
6. recursion on new stones
'''

def lastStoneWeight(stones:list):
    stones.sort()

    while 0 in stones:
        stones.remove(0)
    
    if len(stones) == 0:
        return 0

    if len(stones) == 1:
        return stones[0]

    x, y = stones[-2], stones[-1]

    stones[-2] = 0
    stones[-1] = y-x
    return lastStoneWeight(stones)