'''Instructions
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
'''
'''Examples
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''
'''Thoughts
Inorder Left Root Right, Preorder Root Left Right
1. The root of the tree is the first element of preorder
2. Get the left half of the tree and the right half of the tree by spliting inorder by the root
3. Recursion on the left half and right half
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder:list, inorder:list):
    if not preorder and not inorder:
        return None
    root = preorder[0]
    ri = inorder.index(root)

    out = TreeNode(root)

    if len(preorder) == 1 and len(inorder) == 1:
        return out

    inleft, inright = inorder[:ri], inorder[ri+1:]
    preleft, preright = preorder[1:len(inleft)+1], preorder[len(inleft)+1:]

    out.left = buildTree(preleft, inleft)
    out.right = buildTree(preright, inright)

    return out