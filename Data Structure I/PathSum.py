'''Instructions
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''
'''Examples
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
'''
'''Thoughts
1. Check if root is None if it is return False
2. Check if the root is a leaf and the value is equal to the target if it is return true
3. Recursion on root.right and root.left target minus root.val
'''

def path_sum(root, targetSum):
    if not root:
        return False
    if not root.right and not root.left and root.val == targetSum:
        return True
    return path_sum(root.left, targetSum-root.val) or path_sum(root.right, targetSum-root.val)