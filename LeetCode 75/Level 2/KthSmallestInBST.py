'''Instructions
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''
'''Examples
Input: root = [3,1,4,null,2], k = 1
Output: 1

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''
'''Thoughts
1. Get a list of all the values in the tree inorder and return the k-1th one
'''

def kthSmallest(root, k):
    values = inorder(root)
    return values[k-1]

def inorder(root):
    if not root:
        return []
    
    l = []
    l.extend(inorder(root.left))
    l.append(root.val)
    l.extend(inorder(root.right))
    return l