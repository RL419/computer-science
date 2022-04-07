'''Instructions
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''
'''Examples
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
'''
'''Thoughts
1. Create a list containing the first element of nums
2. Loop through nums from the second element to the last
3. For each element add the maximum of the element on its own and the previous number plus the element
4. return the maximum of the list
'''

def max_subarr(nums):
    s = nums[0]
    l = [s]
    for i in range(1, len(nums)):
        s = max(nums[i], s+nums[i])
        l.append(s)
    return max(l)