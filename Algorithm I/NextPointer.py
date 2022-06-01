'''Instructions
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''
'''Examples
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Input: root = []
Output: []
'''
'''Thoughts
1. Loop though the tree
2. Make node.left.next node.right
3. If the node have a next make the node.right.next node.next.left
4. Move on to node.next if node.next is none go to node.left
'''

def connect(root):
    node = root
    left = root.left if root is not None else None # Empty tree

    while node is not None and left is not None:
        node.left.next = node.right

        if node.next is not None:
            node.right.next = node.next.left
        node = node.next

        if not node:
            node = left
            left = node.left
    return root