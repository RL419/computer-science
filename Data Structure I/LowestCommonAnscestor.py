'''Instructions
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
'''Examples
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Input: root = [2,1], p = 2, q = 1
Output: 2
'''
'''Thoughts
1. If p and q is both less than root.val than move to left
2. If p and q is both more than root.val than move to right
3. else return root because it is in the middle
'''

def LCA(root, p, q):
    while root:
        if p.val>root.val and q.val>root.val:
            root=root.right
        elif p.val<root.val and q.val<root.val:
            root=root.left
        else:
            return root