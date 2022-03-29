'''Instructions
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
'''
'''Examples
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
'''
'''Thoughts
1. Check if 0 is in nums, if it si return 0
2. Count the number of negative numbers in nums
3. If odd return -1 if even return 1
'''

def sign_of_product(nums: list):
    nums.sort()
    if 0 in nums:
        return 0

    count = 0
    for i in nums:
        if i < 0:
            count += 1
        else:
            break
    return 1 if count % 2 == 0 else -1