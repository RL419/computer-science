'''Instructions
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
'''
'''Examples
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
'''
'''Thoughts
1. Get a list of list of all of the indexes of all the zeros
2. Loop through the list and add their distance to 0
'''

from typing import List
from collections import deque

def distance_to_0(mat: list[list[int]]):
    m,n = len(mat), len(mat[0])
    visited = [[0]*n for _ in range(m)]

    q = deque()
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i,j, 0))

    while q:
        i, j, d = q.popleft()
        if visited[i][j]:
            continue
        visited[i][j] = 1
        mat[i][j] = d
        for x, y in [(i-1, j), (i+1,j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n:
                q.append((x,y, d+1))
    
    return mat