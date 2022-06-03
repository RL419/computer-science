'''June 1, 2022'''
'''Instructions
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''
'''Examples
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
'''
'''Thoughts
1. Loop through nums add the value to the total and add total to list
2. return list
'''

def running_sum(nums):
    total = 0
    out = []
    for num in nums:
        total += num
        out.append(total)
    return out