'''Instructions
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''
'''Examples
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]
'''
'''Thoughts
1. Get a counter for nums
2. sort the counter keys
3. Loop through counter keys
4. Replace the corresponding part of nums with new nums
'''

from collections import Counter

def sort_colors(nums:list):
    d = Counter(nums)
    n = list(d.keys())
    n.sort()
    count = 0
    for i in n:
        nums[count:count+d[i]] = [i]*d[i]
        count += d[i]