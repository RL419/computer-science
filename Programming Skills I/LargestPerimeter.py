'''Instructions
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
'''
'''Examples
Input: nums = [2,1,2]
Output: 5

Input: nums = [1,2,1]
Output: 0
'''
'''Thoughts
1. Sort nums form largest to smallest.
2. The sum of 2 other sides must be larger than the hypotenuse to make a triangle a <= b <= c, a+b > c
3. Make the largest element in the list the hypotenuse and check if the sum of the next 2 is greater than the hypotenuse
4. If true, than return the sum of the 3 integers.
5. If false, make the second largest element the hypotenuse and repeat.
'''

def largest_perimeter(nums: list):
    nums.sort(reverse=True)
    while len(nums) > 2:
        if nums[1] + nums[2] > nums[0]:
            return nums[0] + nums[1] + nums[2]
        nums.pop(0)
    return 0