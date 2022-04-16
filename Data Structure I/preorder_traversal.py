'''Instructions
Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''
'''Examples
Input: root = [1,null,2,3]
Output: [1,2,3]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
'''
'''Thoughts
1. If root is None return empty list
2. Add root.val to a list
3. Recursion call on root.left and root.right and add to list
4. return list
'''

def preorder(root):
    if not root:
        return []
    l = [root.val]
    l.extend(preorder(root.left))
    l.extend(preorder(root.right))
    return l