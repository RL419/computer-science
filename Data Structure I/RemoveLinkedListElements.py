'''Instructions
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''
'''Examples
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []
'''
'''Thoughts
1. Get a ListNode and make the node.next head to deal with lists like [7,7,7,7]
2. Loop until head is None
3. Check if the node.val is equal to val
4. If it is re point next
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_elementsll(head, val):
    node = ListNode()
    node.next = head

    out = node

    while head is not None:
        if head.val == val:
            node.next = head.next
        else:
            node = node.next
        head = head.next
    return out.next