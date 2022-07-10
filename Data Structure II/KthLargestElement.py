'''Instructions
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''
'''Examples
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''
'''Thoughts
1. Sort nums and return the kth element from the right
'''

def findkth(nums, k):
    nums.sort()
    return nums[-k]