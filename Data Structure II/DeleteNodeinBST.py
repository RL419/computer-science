'''Instructions
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
'''
'''Examples
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Input: root = [], key = 0
Output: []
'''
'''Thoughts
1. Get all the vals of the tree in a list
2. Remove key and construct a tree using the rest of the vals
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete(root, key):
    if not root:
        return None

    vals = inorder(root)
    if key in vals:
        vals.remove(key)
    else:
        return root

    if not vals:
        return None

    vals.sort()
    mid = len(vals)//2
    out = TreeNode(vals[mid])

    l, r = mid -1, mid+1

    left, right = TreeNode(), TreeNode()
    ln, rn = left, right

    while l >= 0:
        curr = TreeNode(vals[l])
        ln.left = curr
        ln = ln.left
        l -= 1
    
    while r < len(vals):
        curr = TreeNode(vals[r])
        rn.right = curr
        rn = rn.right
        r += 1
    
    out.left = left.left
    out.right = right.right
    return out

def inorder(root):
    if not root:
        return []
    l = []
    l.extend(inorder(root.left))
    l.append(root.val)
    l.extend(inorder(root.right))
    return l