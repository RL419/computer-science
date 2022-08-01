'''Instructions
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''
'''Examples
Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Input: root = []
Output: true
'''
'''Thoughts
1. If root is None return True
2. if the difference between height of root.right and height of root.left is greater than 1 return False
3. Recursion on root.right and root.left
'''

def get_height(root):
    if not root:
        return 0
    return 1 + max(get_height(root.right), get_height(root.left))

def balanced(root):
    if not root:
        return True
    if abs(get_height(root.right)-get_height(root.left)) > 1:
        return False
    return balanced(root.left) and balanced(root.right)