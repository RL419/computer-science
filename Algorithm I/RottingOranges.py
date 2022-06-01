'''Instructions
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''
'''Examples
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''
'''Thoughts
1. Get a list of lists of indexes of rotten oranges
2. Loop through the rotten places and make touching oranges rotten
3. If the grid changed recusion on the new grid and count plus 1
4. else return -1 if there are still not rotten oranges and return the count if everything is rotten
'''
def orangesRotting(grid):
    return rotting_oranges(grid)

def rotting_oranges(grid:list[list[int]], count=0):
    rotten = []
    old = []
    for row in range(len(grid)):
        l = []
        for i in range(len(grid[row])):
            l.append(grid[row][i])
            if grid[row][i] == 2:
                rotten.append([row, i])
        old.append(l)

    for orange in rotten:
        r = orange[0]
        c = orange[1]
        if r - 1 >= 0:
            if grid[r-1][c] == 1:
                grid[r-1][c] = 2
        if r + 1 < len(grid):
            if grid[r+1][c] == 1:
                grid[r+1][c] = 2
        if c - 1 >= 0:
            if grid[r][c-1] == 1:
                grid[r][c-1] = 2
        if c + 1 < len(grid[0]):
            if grid[r][c+1] == 1:
                grid[r][c+1] = 2

    if old == grid:
        for a in grid:
            if 1 in a:
                return -1
        return count
    else:
        count +=1
        return rotting_oranges(grid, count)

print(rotting_oranges([[2,1,1],[1,1,0],[0,1,1]]))