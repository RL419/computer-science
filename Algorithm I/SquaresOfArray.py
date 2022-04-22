'''Instructions
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''
'''Examples
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''
'''Thoughts
1. Loop through nums and add its square to a list and return the sorted version
'''

def squares(nums):
    l = [i**2 for i in nums]
    return sorted(l)