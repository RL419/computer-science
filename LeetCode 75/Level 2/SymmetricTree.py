'''Instructions
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''
'''Examples
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
'''
'''Thoughts
1. Check if root.left and root.right is None
2. If both is None return True else False
3. Check if root.right.val and root.left.val are the same
4. Repeat
'''

def symmetric(root):
    return check(root.left, root.right)

def check(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return check(root1.left, root2.right) and check(root1.right, root2.left)