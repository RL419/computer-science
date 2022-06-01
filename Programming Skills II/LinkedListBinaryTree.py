'''Instructions
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.
'''
'''Examples
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  

Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
'''
'''Thoughts
1. Recuison through the tree
2. If root.val is equal to head.val recursion to check if it contains the following elements in the linked list
3. If it does return true
4. Else keep checking
'''

def yes(head, root):
    if not head:
        return True
    if not root:
        return False
    
    if root.val == head.val:
        check = help(head.next, root.right) or help(head.next, root.left)
        if check:
            return check
    return yes(head, root.right) or yes(head, root.left)


def help(head, root):
    if not head:
        return True
    if not root:
        return False

    if root.val == head.val:
        return help(head.next, root.right) or help(head.next, root.left)
    else:
        return False