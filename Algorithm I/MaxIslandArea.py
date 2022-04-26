'''Instructions
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''
'''Examples
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
'''
'''Thoughts
1. Create a empty list storing sizes of islands
2. Create an empty set containing all of the seen 1s
3. Loop through grid
4. If 1 is found recursion to add the size of the island to the list and add all of the points to the set
5. Return max(list)
'''

def area_of_island(grid):
    seen = set()
    islands = []

    def find(i, j):
        if grid[i][j] == 1 and (i,j) not in seen:
            seen.add((i,j))
            current_island.add((i,j))
            if i + 1 < len(grid):
                find(i+1, j)
            if i - 1 >= 0:
                find(i-1, j)
            if j + 1 < len(grid[0]):
                find(i, j+1)
            if j - 1 >= 0:
                find(i, j-1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and grid[i][j] not in seen:
                current_island = set()
                find(i,j)
                islands.append(len(current_island))
    return max(islands) if islands else 0