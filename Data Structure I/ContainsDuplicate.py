'''Instructions
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
'''Examples
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
'''Thoughts
1. Turn nums to a set
2. Check if the set is equal to nums
'''

def contains_duplicate(nums:list):
    s = set(nums)
    return False if len(s) == len(nums) else True