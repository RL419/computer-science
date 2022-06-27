'''Instructions
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''
'''Examples
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
'''Thoughts
1. Create an empty list
2. Loop through nums and add the product of everything before self to the list
3. Loop through nums again and add the product of everything after self to the list
4. return list
'''

def except_self(nums):
    out = []

    before_self = 1
    for num in nums:
        out.append(before_self)
        before_self *= num
    
    after_self = 1
    for i in range(len(nums)-1, -1, -1):
        out[i] *= after_self
        after_self *= nums[i]
    
    return out