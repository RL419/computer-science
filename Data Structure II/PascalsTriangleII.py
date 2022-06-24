'''Instructions
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''
'''Examples
Input: rowIndex = 3
Output: [1,3,3,1]

Input: rowIndex = 0
Output: [1]

Input: rowIndex = 1
Output: [1,1]
'''
'''Thoughts
1. recursion
'''

def triangle(rowIndex):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    
    previous = triangle(rowIndex-1)

    out = [1]
    for i in range(len(previous)-1):
        out.append(previous[i]+previous[i+1])
    out.append(1)
    return out