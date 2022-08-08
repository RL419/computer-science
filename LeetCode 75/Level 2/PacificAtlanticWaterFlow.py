'''Instructions
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''
'''Examples
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
'''
'''Thoughts
1. 2 dictionaries to keep track of if the coords can reach atlantic and pacific
2. Loop through each coords and recursion on nearby coords to see if any reaches the oceans
'''

def pacific_atlantic(heights:list[list[int]]):
    pacific = {}
    atlantic = {}

    m, n = len(heights), len(heights[0])

    def check_p(x, y, pre, visited) -> bool:
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if heights[x][y] > pre or (x,y) in visited:
            return False
        
        visited.add((x,y))
        if x == 0 or y == 0:
            pacific[(x,y)] = True
        else:
            pacific[(x,y)] = check_p(x-1, y, heights[x][y], visited) or check_p(x+1, y, heights[x][y], visited) or check_p(x, y-1, heights[x][y], visited) or check_p(x, y+1, heights[x][y], visited)

        return pacific[(x,y)]
    
    def check_a(x, y, pre, visited):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if heights[x][y] > pre or (x,y) in visited:
            return False
        
        visited.add((x,y))
        if x == m-1 or y == n-1:
            atlantic[(x,y)] = True
        else:
            atlantic[(x,y)] = check_a(x-1, y, heights[x][y], visited) or check_a(x+1, y, heights[x][y], visited) or check_a(x, y-1, heights[x][y], visited) or check_a(x, y+1, heights[x][y], visited)

        return atlantic[(x,y)]

    out = []
    for i in range(m):
        for j in range(n):
            p, a = check_p(i,j,float('inf'),set()), check_a(i,j,float('inf'),set())
            if p and a:
                out.append([i,j])
    return out