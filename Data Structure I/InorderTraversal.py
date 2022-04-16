'''Instructions
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''
'''Examples
Input: root = [1,null,2,3]
Output: [1,3,2]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
'''
'''Thoughts
1. If root is None return empty list
2. Recursion call on root.left and add to list
3. Add root.val to list
4. Recursion call on root.right and add to list
5. return list
'''

def inorder(root):
    if not root:
        return []
    l = []
    l.extend(inorder(root.left))
    l.append(root.val)
    l.extend(inorder(root.right))
    return l