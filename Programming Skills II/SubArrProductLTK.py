'''Instructions
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
'''
'''Examples
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Input: nums = [1,2,3], k = 0
Output: 0
'''
'''Thoughts
1. If k is less than or equal to 0 return 0
2. Loop through nums
3. Multiply the element to the product
4. If the product is not less than k divide product by the start of the subarray and update the start of the subarray.
5. Calculate how many ways in the current subarray using i- left +1
'''

def yes(nums, k):
    if k <= 0:
        return 0

    out = 0
    product = 1

    left = 0

    for i in range(len(nums)):
        product *= nums[i]

        while product >= k:
            product /= nums[left]
            left+=1

        out += i - left + 1
    return out