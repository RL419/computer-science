'''Instructions
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
'''
'''Examples
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Input: root = [1]
Output: 0
'''
'''Thoughts
1. Check if root.left is a leaf
2. If it is add root.left.val to the total
3. Recursive call on root.left and root.right and add to the total
4. Return total
'''

def left_leaves(root):
    total = 0
        
    left = root.left
    right = root.right
    
    if left:
        if not left.right and not left.left:
            total += left.val
        else:
            total += left_leaves(left)
    if right:
        total += left_leaves(right)
    
    return total