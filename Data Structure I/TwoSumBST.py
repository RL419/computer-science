'''Instructions
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
'''
'''Examples
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
'''
'''Thoughts
1. Get a list of all the values
2. Loop through the values and check if k-val is in the list
'''

def find_target(root, k):
    l = preorder(root)
    l.sort()
    i = 0
    j = len(l)-1
    while i < j:
        if l[i] + l[j] == k:
            return True
        if l[i] + l[j] < k:
            i += 1
        else:
            j -= 1
    return False


def preorder(root):
    if not root:
        return []
    l = [root.val]
    l.extend(preorder(root.left))
    l.extend(preorder(root.right))
    return l