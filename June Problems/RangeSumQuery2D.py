'''Instructions
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
'''
'''Examples
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
'''
'''Thoughts
1. For init loop through matrix
2. For every list in matrix loop through it
3. For every element add the total of everything in this list until this elemtn to a list
4. For sumRegion get sums from row1 to row2
5. loop through the current list minus sums[col1] from sums[col2+1] and add it to the total
6. Return total
'''

class NumMatrix:
    def __init__(self, matrix: list[list[int]]) -> None:
        r, c = len(matrix), len(matrix[0])
        sums = [[0 for _ in range(c+1)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                sums[i][j+1] = sums[i][j] + matrix[i][j]
        self.sums = sums
    

    def sumRegion(self, row1, col1, row2, col2):
        out = 0
        current = self.sums[row1:row2+1]
        for l in current:
            out += l[col2+1] - l[col1]
        return out

    # def __init__(self, matrix: list[list[int]]) -> None:
    #     self.matrix = matrix

    # def sumRegion(self, row1, col1, row2, col2):
    #     out = 0
    #     current = self.matrix[row1:row2+1]
    #     for i in range(len(current)):
    #         current[i] = current[i][col1:col2+1]
    #         out += sum(current[i])
    #     return out

    # def sumRegion(self, row1, col1, row2, col2):
    #     out = 0
    #     current = self.matrix[row1:row2+1]
        
    #     r, c = len(current), len(current[0])
    #     sums = [[0 for _ in range(c+1)] for _ in range(r)]

    #     for i in range(r):
    #         for j in range(col2+1):
    #             sums[i][j+1] = sums[i][j] + current[i][j]
    #         out += sums[i][col2+1] - sums[i][col1]
    #     return out
