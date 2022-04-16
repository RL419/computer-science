'''Instructions
Given the root of a binary tree, return the postorder traversal of its nodes' values.
'''
'''Examples
Input: root = [1,null,2,3]
Output: [3,2,1]

Input: root = []
Output: []

Input: root = [1]
Output: [1]
'''
'''Thoughts
1. If root is None return empty list
2. Recursion call on root.left and add to list
3. Recursion call on root.right and add to list
4. Add root.val to list
5. return list
'''

def postorder(root):
    if not root:
        return []
    l = []
    l.extend(postorder(root.left))
    l.extend(postorder(root.right))
    l.append(root.val)
    return l