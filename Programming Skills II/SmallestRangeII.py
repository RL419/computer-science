'''Instructions
You are given an integer array nums and an integer k.

For each index i where 0 <= i < nums.length, change nums[i] to be either nums[i] + k or nums[i] - k.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after changing the values at each index.
'''
'''Examples
Input: nums = [1], k = 0
Output: 0
Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.

Input: nums = [0,10], k = 2
Output: 6
Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.

Input: nums = [1,3,6], k = 3
Output: 3
Explanation: Change nums to be [4, 6, 3]. The score is max(nums) - min(nums) = 6 - 3 = 3.
'''
'''Thoughts
1. Sort nums and calculate the current output with the minumum val and the maximum val
2. Loop through nums and check 2 elements at a time
3. Update output to be the smallest between the current one, and the largest between the largest element minus k, and the smaller number plus k, minus the smallest between the smallest number plus k and the larger number minus k
'''


def small_range(nums:list, k:int):
    nums.sort()

    big = nums[-1]
    small = nums[0]

    out = big-small

    for i in range(len(nums)-1):
        s = nums[i]
        b = nums[i+1]
        out = min(out, max(big-k, s+k) - min(small+k, b-k))
    return out