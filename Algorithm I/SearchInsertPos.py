'''Instructions
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
'''Examples
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4
'''
'''Thoughts
1. Try to find the value if it is found return the index
2. Return midpoint plus one if nums[midpoint] is less than target
3. Else return midpoint 
'''

def insertpos(nums, target):
    first = 0
    last = len(nums) -1
        
    while first <= last:
    
        midpoint = (first+last)//2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] > target:
            last = midpoint - 1
        elif nums[midpoint] < target:
            first = midpoint + 1

    ni = midpoint+1 if nums[midpoint] < target else midpoint
    return ni