'''June 11, 2022'''
'''Instructions
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
'''
'''Examples
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
'''
'''Thoughts
1. Find the longest subarray of nums with the sum of sum(nums) minus x
2. Loop through nums and add value to current
3. If current is greater than the target value loop until it isn't by minusing the start value of the current subarray
4. If current is equal to target than update longest subarray
'''

def operate(nums, x):
    target = sum(nums) - x
    start = 0

    current = 0
    max_length = 0
    found = False

    for end in range(len(nums)):
        current += nums[end]
        while start <= end and current > target:
            current -= nums[start]
            start += 1
        if current == target:
            found = True
            max_length = max(max_length, end - start + 1)
        
    return len(nums) - max_length if found else -1