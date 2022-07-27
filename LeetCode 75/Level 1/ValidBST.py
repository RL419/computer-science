'''Instructions
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
'''Examples
Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
'''Thoughts
1. If root is None return True
2. Use infinity and negative infinity for initial minimum and maximum values
3. Check if root.val if greater or equal to max or less than or equal to min
4. Recursion on root.right and root.left change min or max to root.val
'''

def is_valid(root):
    return dostuff(root, -float('inf'), float('inf'))


def dostuff(root, minimum, maximum):
    if not root:
        return True
    if root.val >= maximum or root.val <= minimum:
        return False
    
    return dostuff(root.left, minimum, root.val) and dostuff(root.right, root.val, maximum)