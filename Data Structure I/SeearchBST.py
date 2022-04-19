'''Instructions
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
'''
'''Examples
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Input: root = [4,2,7,1,3], val = 5
Output: []
'''
'''Thoughts
1. If root is None return None
2. If root.val is equal to val return root
3. Recursion on root.left and root.right
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    if not root:
        return TreeNode().right
    if root.val == val:
        return root
    left = searchBST(root.left, val)
    right = searchBST(root.right, val)
    return right if right else left