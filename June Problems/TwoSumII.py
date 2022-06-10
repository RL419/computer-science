'''June 9, 2022'''
'''Instructions
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''
'''Examples
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''
'''Thoughts
1. Loop while small < big
2. If nums[small] plus nums[big] is greater than target big minus 1
3. If nums[small] plus nums[big] is less than target small plus 1
4. Return small + 1 and big + 1
'''

def twoSum(self, numbers: list[int], target: int) -> list[int]:
    big = len(numbers) - 1
    small = 0
    while small < big:
        if numbers[small] + numbers[big] > target:
            big -= 1
        elif numbers[small] + numbers[big] < target:
            small += 1
        else:
            return [small+1, big+1]