'''Instructions
Given the root of a binary tree, invert the tree, and return its root.
'''
'''Examples
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []
'''
'''Thoughts
1. Make root.left to root.right and root.right to root.left
2. recursion on root.left and root.right
'''

def invert_tree(root):
    yes(root)
    return root
    
def yes(root):
    if root is None:
        return root
    root.left, root.right = root.right, root.left
    yes(root.left)
    yes(root.right)