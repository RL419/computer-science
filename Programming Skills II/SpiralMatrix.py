'''Instructions
Given an m x n matrix, return all elements of the matrix in spiral order.
'''
'''Examples
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
'''Thoughts
1. Loop unitl matrix is empty
2. Add the first list of matrix to the output and remove it
3. Rotate matrix counter clockwise
'''

def spiralOrder(matrix:list):
    out = []
    while len(matrix) != 0:
        out.extend(matrix.pop(0))
        matrix = rotate(matrix)
    return out

def rotate(matrix:list):
    '''Rotates a 2D array counter clockwise by 90 degrees'''
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    out = [[0]*m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            out[n-j-1][i] = matrix[i][j]
    return out

# print(spiralOrder([[1,2,3],
#                    [4,5,6],
#                    [7,8,9]]))