'''Instructions
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
'''Examples
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
'''Thoughts
1. Get a Counter of nums
2. return the key with the max value
'''
from collections import Counter

def majorityElement(nums: list[int]) -> int:
    a = Counter(nums)
    return max(a.keys(), key=a.get)