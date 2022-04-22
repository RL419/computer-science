'''Instructions
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''
'''Examples
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''
'''Thoughts
1. Make k less than length of nums
2. Loop length of nums minus k times and move the first element to the last
'''

def rotate(nums, k):
    k %= len(nums)
    for _ in range(len(nums)-k):
        nums.append(nums.pop(0))