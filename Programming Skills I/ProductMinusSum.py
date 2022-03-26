'''Instructions
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''
'''Examples
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
'''
'''Thoughts
1. Create a list of the digits
2. Product minus sum
'''

def prosum(n):
    nums = [int(x) for x in str(n)]
    product = 1
    for i in nums:
        product *= i
    return product - sum(nums)