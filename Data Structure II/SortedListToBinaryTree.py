'''Instructions
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''
'''Examples
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
'''
'''Thoughts

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def toBST(nums):
    if len(nums) == 0:
        return None
    mid = len(nums) // 2
    out = TreeNode(nums[mid])

    out.left = toBST(nums[:mid])
    out.right = toBST(nums[mid+1:])

    return out

# Not height balanced smh
# def toBST(nums):
#     mid = len(nums)//2
#     out = TreeNode(nums[mid])

#     l, r = mid -1, mid+1

#     left, right = TreeNode(), TreeNode()
#     ln, rn = left, right

#     while l >= 0:
#         curr = TreeNode(nums[l])
#         ln.left = curr
#         ln = ln.left
#         l -= 1
    
#     while r < len(nums):
#         curr = TreeNode(nums[r])
#         rn.right = curr
#         rn = rn.right
#         r += 1
    
#     out.left = left.left
#     out.right = right.right
#     return out