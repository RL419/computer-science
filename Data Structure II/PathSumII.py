'''Instructions
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
'''
'''Examples
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Input: root = [1,2,3], targetSum = 5
Output: []

Input: root = [1,2], targetSum = 0
Output: []
'''
'''Thoughts
1. Recursion to check all possible root to leaf paths and check if their sum is equal to the target sum
'''

def pathSum(root, targetSum):
    out = []

    def check_path(root, target, l):
        if not root:
            return
        target -= root.val
        l.append(root.val)

        if not root.right and not root.left and target == 0:
            out.append(l.copy())
        
        check_path(root.left, target, l.copy())
        check_path(root.right, target, l.copy())
    
    check_path(root, targetSum, [])
    return out

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
# pathSum(root,22)