'''Instructions
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
'''Examples
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []
'''
'''Thoughts
1. Loop until head is not none and add the values to a list
2. Loop through the list and change it to a linked list
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode):
    l = []
    while head is not None:
        l.append(head.val)
        head = head.next
    
    l = l[::-1]

    node = ListNode()
    out = node

    for num in l:
        current = ListNode(num)
        out.next = current
        out = out.next
    return node.next