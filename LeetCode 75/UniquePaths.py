'''Instructions
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''
'''Examples
Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''
'''Thoughts
1. If m or n is 1 return 1
2. Return the sum of recurion on m - 1 and recursion on n - 1
3. Memo to shorten runtime
'''


def uniquePaths(m, n, memo=None):
    if memo is None:
        memo = {}
    if m == 1 or n == 1:
        return 1
    
    if (m,n) not in memo.keys():
        memo[(m,n)] = uniquePaths(m-1, n, memo) + uniquePaths(m, n-1, memo)
    return memo[(m,n)]