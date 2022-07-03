'''Instructions
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''
'''Examples
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''
'''Thoughts
1. Loop through head and add all nodes into a list
2. Loop from both ends of the list and repoint next
3. Last change the last node.next to None to avoid cycle
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder(head):
    l = []
    while head:
        l.append(head)
        head = head.next
    
    left, right = 0, len(l)-1

    while left<right:
        l[left].next = l[right]
        left += 1
        if left >= right:
            break
        l[right].next = l[left]
        right -= 1
    
    l[right].next = None