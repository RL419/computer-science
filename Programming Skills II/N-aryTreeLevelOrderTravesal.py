'''Instructions
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
'''
'''Examples
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
'''
'''Thoughts
1. Return empty list if root is None
2. Loop until root is empty
3. Loop through each level and add the level's nodes's valye to the output
'''

def level_order(root):
    if not root:
        return []

    out = []
    current = [root]

    while current:
        out.append([i.val for i in current])
        temp = []
        for parent in current:
            for children in parent:
                if children:
                    temp.append(children)
        current = temp
    return out