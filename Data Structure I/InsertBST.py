'''InstructionsYou are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
'''
'''Examples
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
'''
'''Thoughts
1. If val is less than root.val go left and left exist
2. If val is greater than root.val go right exist
3. else break and add the value
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, val):
    if not root:
        return TreeNode(val)
    
    node = root

    while node is not None:
        if val < node.val and node.left is not None:
            node = node.left
        elif val > node.val and node.right is not None:
            node  = node.right
        else:
            break
        
    if val < node.val:
        node.left = TreeNode(val)
    else:
        node.right = TreeNode(val)
    return root