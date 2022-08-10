'''Instructions
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''
'''Examples
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []
'''
'''Thoughts
1. Get all the values in the tree by from left to right and layer by layer
2. Return the last element of every layer
'''

def right_side_view(root):
    layers = bfs(root)
    out = []
    for l in layers:
        out.append(l[-1])
    return out

def bfs(root):
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