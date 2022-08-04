'''Instructions
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''
'''Examples
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''
'''Thoughts
1. Get a dictionay of the index and the last value of the list
2. Check if terget is in range
'''

def search(matrix:list, target):
    for i in range(len(matrix)):
        if target <= matrix[i][-1]:
            if target in matrix[i]:
                return True
            return False
