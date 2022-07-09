'''Instructions
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
'''
'''Examples
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []

Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
'''
'''Thoughts
1. Serialize will store the inorder traversal and preorde traversal into a string
2. Deserialize will decode the string into 2 lists of the travesals and will construct the tree using the same algorithm as the inorder preorder to tree
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def __init__(self) -> None:
        self.duplicates = {}

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        i, p = self.inorder(root), self.preorder(root)

        return ' '.join(i) + ',' + ' '.join(p)
    
    def inorder(self, root):
        '''Left Root Right'''
        if not root:
            return []
        l = []
        l.extend(self.inorder(root.left))

        if root.val in self.duplicates.keys():
            self.duplicates[root.val] += 1
            root.val += 2001 * self.duplicates[root.val]
        else:
            self.duplicates[root.val] = 0

        l.append(str(root.val))
        l.extend(self.inorder(root.right))
        return l

    
    def preorder(self, root):
        '''Root Left Right'''
        if not root:
            return []
        l = [str(root.val)]
        l.extend(self.preorder(root.left))
        l.extend(self.preorder(root.right))
        return l
    

    def deserialize(self, data:str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == ',':
            return None
        i, p = data.split(',')
        i = i.split(' ')
        p = p.split(' ')

        i = list(map(int, i))
        p = list(map(int, p))

        out = self.buildTree(p, i)
        return out

    def buildTree(self, preorder:list, inorder:list):
        if not preorder and not inorder:
            return None
        root = preorder[0]
        ri = inorder.index(root)

        while root > 1000:
            root -= 2001

        out = TreeNode(root)

        if len(preorder) == 1 and len(inorder) == 1:
            return out

        inleft, inright = inorder[:ri], inorder[ri+1:]
        preleft, preright = preorder[1:len(inleft)+1], preorder[len(inleft)+1:]

        out.left = self.buildTree(preleft, inleft)
        out.right = self.buildTree(preright, inright)

        return out