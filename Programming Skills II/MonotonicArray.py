'''Instructions
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
'''
'''Examples
Input: nums = [1,2,2,3]
Output: true

Input: nums = [6,5,4,4]
Output: true

Input: nums = [1,3,2]
Output: false
'''
'''Thoughts
1. Return nums is equal to the sorted or reverse sorted nums
'''

def monotonic(nums):
    return sorted(nums) == nums or sorted(nums, reverse=True) == nums