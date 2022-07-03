'''Instructions
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''
'''Examples
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3    [-1, 2,1,3,4,5]   [-1, 3,2,1,4,5]
Output: [3,2,1,4,5]
'''
'''Thoughts
1. Similar to SwapNodesInPairs except loop k-1 times for each swap
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_k(head: ListNode, k: int):
    if not head or k == 1:
        return head
    out = ListNode(-1,head)

    length = get_length(head)

    pre = out
    curr = head
    
    while length >= k:
        nxt = curr.next
        for i in range(k-1):
            curr.next = nxt.next
            nxt.next = pre.next
            
            pre.next = nxt

            nxt = curr.next
        
        length -= k
        pre = curr
        curr = pre.next
    
    return out.next

def get_length(head: ListNode):
    count = 0
    while head:
        count += 1
        head = head.next
    return count