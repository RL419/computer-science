'''Instructions
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
'''
'''Examples
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
'''
'''Thoughts
1. Create a list for the triplet
2. Loop through nums
3. if the number is greater than the last element of the triplet list add it to the list and if the length of the triplet is 3 return True
4. Else if the number is less than the start of the triplet make the number the start
5. Or if the number is less than the second element make it the second element
6. Return False if triplet never reached 3
'''

def triplet(nums):
    tplt = [nums[0]]
    for num in nums:
        if num > tplt[-1]:
            tplt.append(num)
            if len(tplt) == 3:
                return True
        else:
            if num <= tplt[0]:
                tplt[0] = num
            elif len(tplt) == 2 and num < tplt[1]:
                tplt[1] = num
    return False