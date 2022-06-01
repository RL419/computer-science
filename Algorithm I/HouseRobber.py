'''Instructions
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''
'''Examples
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''
'''Thoughts
1. If there are less than or equal to 2 houses return the highest amount
2. if there are 3 houses return the highest between the first and last and the middle
3. Else return the highest between first and everything after 3rd or the second and everything after 4th
4. memo to shorten run time
'''

def rob(nums, memory=None) -> int:
    if memory is None:
        memory = {}
    if len(nums) <=2:
        return max(nums)
    elif len(nums) == 3:
        return max(nums[1], nums[0]+nums[2])
    if len(nums) not in memory.keys():
        memory[len(nums)] = max(nums[0] + rob(nums[2:], memory=memory), nums[1] + rob(nums[3:], memory=memory))
    return memory[len(nums)]