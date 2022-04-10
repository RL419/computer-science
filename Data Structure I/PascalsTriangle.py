'''Instructions
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''
'''Examples
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]
'''
'''Thoughts
1. Base case if numRows is 1 return [1], if numRows is 2 return [1,1]
2. Loop until numRows use the previous row to calculate the next row and add it to a list
'''

def pascalTriangle(numRows):
    output = []
    for row in range(1,numRows+1):
        if row == 1:
            output.append([1])
        elif row == 2:
            output.append([1,1])
        else:
            l = [1]
            for i in range(len(output[-1])-1):
                l.append(output[-1][i]+output[-1][i+1])
            l.append(1)
            output.append(l)
    return output