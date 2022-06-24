'''Instructions
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''
'''Examples
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
'''
'''Thoughts
1. Loop through every list in matrix and binary search it
'''

def search_matrix(matrix, target):
    r = 0
    while r < len(matrix) and matrix[r][0] <= target:
        check = binary_search(matrix[r], target)
        if check:
            return True
        r += 1
    return False

def binary_search(l, target):
    start, end = 0, len(l)-1

    while start <= end:
        mid = (start + end) // 2
        if l[mid] == target:
            return True
        elif l[mid] > target:
            end = mid-1
        elif l[mid] < target:
            start = mid +1
    return False