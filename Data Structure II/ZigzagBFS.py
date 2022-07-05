'''Instructions
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
'''
'''Examples
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
'''
'''Thoughts
1. Create an output list and a boolean for whether is zigzaging or not
2. For every level add the vals of the node into a list as well as the left ad right nodes for the next level into another list
3. Every other layer reverse the vals and add it to the output list
'''

def zigzag(root):
    if not root:
        return []

    out = []

    zz = False

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
        if zz:
            zz = False
            out.append(temp[::-1])
        else:
            zz = True
            out.append(temp)

        currlevel = nextlevel
    return out