'''Instructions
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''
'''Examples
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
'''
'''Thoughts
1. 1. Create an output list
2. For every level add the vals of the node into a list as well as the left ad right nodes for the next level into another list
3. Add the current layer to the output list
4. Move on to the next layer
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode):
    if not root:
        return []

    out = []

    currlevel = [root]
    while currlevel:
        temp = []
        nextlevel = []
        for node in currlevel:
            temp.append(node.val)
            if node.left:
                nextlevel.append(node.left)
            if node.right:
                nextlevel.append(node.right)

        out.append(temp)

        currlevel = nextlevel
    return out