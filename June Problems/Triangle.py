'''June 13, 2022'''
'''Instructions
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
'''
'''Example
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Input: triangle = [[-10]]
Output: -10
'''
'''Thoughts
1. Return 0 if the indexes are outside the triangle
2. Recrusion on the next layer below
3. Memo to shorten runtime
'''

def min_total(triangle):
    
    def yes(index, level, memo = None):
        if memo == None:
            memo = {}
        if level >= len(triangle):
            return 0
        if index >= len(triangle[level]) or index < 0:
            return 0
        if (index, level) not in memo.keys():
            memo[(index, level)] = min(triangle[level][index] + yes(index, level+1, memo), triangle[level][index] + yes(index+1, level+1, memo))
        return memo[(index, level)]
    
    return yes(0,0)