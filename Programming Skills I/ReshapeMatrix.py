'''Instructions
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
'''
'''Examples
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
'''
'''Thoughts
1. Check if r*c == the matrix of the mat, if it isn't return the original mat
2. Transform mat into a 1d list
3. Loop through the 1d list amd change it to a 2d list with dimenstions r*c
'''

def reshape(mat:list, r:int, c:int):
    if r*c != len(mat) * len(mat[0]):
        return mat
    l = []
    for row in mat:
        l.extend(row)
    new_list = []
    for i in range(0,len(l), c):
        new_list.append(l[i:i+c])
    return new_list