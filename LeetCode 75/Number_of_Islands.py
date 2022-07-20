'''Instructions
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
'''Examples
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
'''Thoughts
1. Loop though the grid and if you find an island change the entire island to water
'''

def islands(grid:list[list[str]]):
    if not grid:
        return 0

    out = 0

    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                out += 1

                def fill(i, j):
                    if i < 0 or j < 0 or i >= m or j >= n:
                        return
                    
                    if grid[i][j] == '0':
                        return
                    
                    grid[i][j] = '0'

                    fill(i+1,j)
                    fill(i-1,j)
                    fill(i,j+1)
                    fill(i,j-1)
                
                fill(i, j)
    return out