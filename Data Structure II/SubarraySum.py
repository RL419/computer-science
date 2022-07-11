'''Instructions
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
'''
'''Examples
Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2
'''
'''Thoughts

'''

def subarray_sum(nums:list, k):
    count = 0
    d = {0:1}

    s = 0
    for n in nums:
        s += n

        if s - k in d.keys():
            count += d[s-k]
        
        if s in d.keys():
            d[s] += 1
        else:
            d[s] = 1
    return count