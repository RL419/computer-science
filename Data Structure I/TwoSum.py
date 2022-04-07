'''Instructions
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
'''Examples
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
'''
'''Thoughts
1. Loop through nums
2. Loop through nums again to check if any other numbers add up to target
'''

def two_sum(nums: list, target):
    for i in range(len(nums)-1):
        difference = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == difference:
                return [i,j]