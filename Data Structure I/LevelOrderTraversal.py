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
1. If root is None return empty list
2. Create a function to get the height of the tree
3. Loop until the height of the tree
4. Call current_level function on the level
5. recursion
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode):
    out = []
    for lvl in range(1, height(root)+1):
        out.append(current_level(root, lvl))
    return out

def height(root: TreeNode):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def current_level(root: TreeNode, level):
    if root is None:
        return []
    current = []
    if level == 1:
        current.append(root.val)
    else:
        current.extend(current_level(root.left, level-1))
        current.extend(current_level(root.right, level-1))
    return current

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# print(levelOrder(root))