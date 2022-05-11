'''Instructions
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
'''
'''Examples
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
'''
'''Thoughts
1. Check if mat is equal to target Return True if it is
2. Loop 3 times
3. Everytime rotate mat by 90 degrees and check if mat is equal to target
'''
from copy import deepcopy

def if_obtainable(mat, target):
    if mat == target:
        return True
    
    for _ in range(4):
        mat = rotate(mat)
        if mat == target:
            return True
    return False
    
def rotate(matrix:list):
    old = deepcopy(matrix)
    m, n = len(old), len(old[0])
    for i in range(m):
        for j in range(n):
            matrix[j][n-i-1] = old[i][j]
    return matrix