'''Instructions
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''
'''Examples
Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''
'''Thoughts
1. Loop until head is None
2. Create an empty set
3. Check if head.val is in the set
4. If it is re point head.next
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicate(head: ListNode):
    if head is None:
        return head
        
    s = set()
    s.add(head.val)

    node = head
    n = head.next
    while n is not None:
        if n.val in s:
            n = n.next
        else:
            node.next = n
            s.add(n.val)
            n = n.next
            node = node.next
    node.next = None
    return head