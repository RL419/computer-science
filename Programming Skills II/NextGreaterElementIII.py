'''Instructions
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
'''
'''Examples
Input: n = 12
Output: 21

Input: n = 21
Output: -1
'''
'''Thoughts
idk
'''

# def next_greater_element3(n):
#     nums = [i for i in str(n)][::-1]
#     for i in range(len(nums)-1):
#         if int(nums[i]) > int(nums[i+1]):
#             nums[i], nums[i+1] = nums[i+1], nums[i]
#             break
#     num = int(''.join(nums[::-1]))
#     if num > n and len(bin(num)[2:]) < 32:
#         return num
#     return -1