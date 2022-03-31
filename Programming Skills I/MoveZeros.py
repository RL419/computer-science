'''Instructions
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''
'''Examples
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]
'''
'''Thoughts
1. Count all of the zeros
2. Remove all the zeros
3. Add the zeros
'''

def move_zeros(nums: list):
    c = nums.count(0)

    for i in range(c):
        nums.remove(0)
        nums.append(0)