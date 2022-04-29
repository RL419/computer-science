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

# def distance_to_0(mat):
#     zeros = []
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if mat[i][j] == 0:
#                 zeros.append([i,j])
    
#     out = []
#     for row in range(len(mat)):
#         l = []
#         for col in range(len(mat[0])):
#             if mat[row][col] == 0:
#                 l.append(0)
#             else:
#                 nearest = 9999999999999999999999999
#                 for pos in zeros:
#                     distance = abs(row-pos[0]) + abs(col-pos[1])
#                     nearest = min(nearest, distance)
#                 l.append(nearest)
#         out.append(l)
#     return out