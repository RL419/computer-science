'''Instructions
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
'''Examples
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[1] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
'''Thoughts
1. Sort nums
2. Loop through the indecies of nums for the start pointer
3. Create 2 pointer for mid and last
4. if nums[i, j and k] is equal to 0 add it to the output and decrease last the the next different element
5. else if nums[i, j and k] is less than 0 increase j by 1
6. else if nums[i, j and k] is greater than 0 decrease last by 1
'''

# def threeSum(nums):
#     out = []
    
#     length = len(nums)
    
#     i = 0
#     while i < length:
#         j = i + 1
#         while j < length:
#             k = j + 1
#             while k < length:
#                 curr = [nums[i], nums[j], nums[k]]
#                 curr.sort()
#                 if sum(curr) == 0 and curr not in out:
#                     out.append(curr)
#                 k += 1
#             j += 1
#         i += 1
#     return out

def threeSum(nums:list):
    nums.sort()

    out = []

    for i in range(len(nums)-2):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = len(nums) - 1

        while j < k:
            curr = [nums[i], nums[j], nums[k]]

            if sum(curr) == 0 and curr not in out:
                out.append(curr)

                k -= 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            
            elif sum(curr) < 0:
                j += 1
            elif sum(curr) > 0:
                k -= 1
    
    return out