'''Instructions
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
'''
'''Examples
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Input: head = [1,1,1,2,3]
Output: [2,3]
'''
'''Thoughts
1. Loop though head and keep track of the previous non repeating node
2. If Repeating found make the previous node's next the next node after the repeating one
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove(head):
    if not head:
        return head

    curr = head
    out = ListNode(-101, head)
    pre = out

    while curr:
        if curr.next and curr.next.val == curr.val:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            pre.next = curr.next
        else:
            pre = pre.next
        
        curr = curr.next
    return out.next