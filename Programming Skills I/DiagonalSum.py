'''Instructions
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
'''
'''Examples
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Input: mat = [[5]]
Output: 5
'''
'''Thoughts
1. Loop through mat and get all of the diagonal values
2. If the length of mat is odd minus the middle number.
'''

def diagonal_sum(mat:list):
    total = 0
    for i in range(len(mat)):
        total += mat[i][i]
        total += mat[i][len(mat)-1-i]
    
    if len(mat) % 2 == 1:
        total -= mat[len(mat)//2][len(mat)//2]
    return total