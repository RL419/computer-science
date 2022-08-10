'''Instructions
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''
'''Examples
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false
'''
'''Thoughts
1. Recursion on every node in both trees to check if they are the same
'''

def isSameTree(self, p, q) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    left = isSameTree(p.left, q.left)
    right = isSameTree(p.right, q.right)
    
    return left and right