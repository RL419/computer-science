'''Instructions
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.
You may assume that each input would have exactly one solution.
'''
'''Examples
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Input: nums = [0,0,0], target = 1
Output: 0
'''
'''Thoughts
1. Loop through sorted nums and for every element get the sum cloestest to target
'''

def sum_closest(nums:list, target):
    out = float('inf')
    nums.sort()

    for i in range(len(nums)-2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == target:
                return target
            
            if abs(s-target) < abs(out-target):
                out = s

            if s > target:
                k -= 1
            elif s < target:
                j += 1
    return out