'''Instructions
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
'''Examples
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''
'''Thoughts
1. Use counter and return the top k keys with the highest occurance.
'''

from collections import Counter

def k_frequent(nums, k):
    d = Counter(nums)

    l = list(d.keys())
    l.sort(key=d.get)

    return l[-k:]