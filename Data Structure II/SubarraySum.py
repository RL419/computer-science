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

def subarray_sum(nums, k):
    d = {0:1}

    count = 0

    sums = [nums[0]]

    for num in nums[1:]:
        sums.append(num + sums[-1])
    
    for num in sums:
        if num - k in sums or num == k:
            count += 1
    
    return count