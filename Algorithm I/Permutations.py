'''Instructions
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
'''
'''Examples
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]
'''
'''Thoughts
1. Loop through nums and get permutations for the other numbers using recursion
2. Add the element to the beginning of the previous permutation and add them to the output lsit
'''

def permutations(nums):
    if len(nums) <= 1:
        return [nums]
    out = []
    for i in nums:
        new = nums.copy()
        new.remove(i)
        previous = permutations(new)
        for l in previous:
            alist = [i]
            alist.extend(l)
            out.append(alist)
    return out