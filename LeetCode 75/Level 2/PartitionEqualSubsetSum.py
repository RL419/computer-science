'''Instructions
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
'''
'''Examples
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''
'''Thoughts
1. If the sum of nums is odd return False
2. Get all possible partitions and see if half of the sum is in the partition
'''

def partition(nums:list):
    if sum(nums) % 2 == 1:
        return False
    
    partitions = set([0])
    for n in nums:
        curr = set()
        for v in partitions:
            curr.add(v+n)

        partitions = partitions.union(curr)
    
    return sum(nums) // 2 in partitions