'''Instructions
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
'''Examples
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Input: root = [1,2], p = 1, q = 2
Output: 1
'''
'''Thoughts
1. Check if root.val is equal to the vals of p and q if it is return True
2. recursion on root.left and root.right
3. if Left found nothing return right
4. if right found nothing return left
5. if both found return root
'''

def LCA(root, p, q):
    if not root:
        return None
    
    if root.val == p.val or root.val == q.val:
        return root
    
    left, right = LCA(root.left, p, q), LCA(root.right, p, q)

    if left is None:
        return right
    elif right is None:
        return left
    else:
        return root