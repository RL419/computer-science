'''Instructions
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''
'''Examples
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Input: root = [1,2]
Output: 1
'''
'''Thoughts
1. For every node check the height of the left and right and update out to the max
'''

class Solution:
    def __init__(self) -> None:
        self.out = 0
    
    def diameter(self, root):
    
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)

            self.out = max(self.out, left+right)
            return 1 + max(left, right)
        check(root)
        return self.out