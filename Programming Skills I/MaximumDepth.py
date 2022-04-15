'''Instructions
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
'''Examples
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2
'''
'''Thoughts
1. Return 0 if root is none
2. Recursion
'''

def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.right), maxDepth(root.left))