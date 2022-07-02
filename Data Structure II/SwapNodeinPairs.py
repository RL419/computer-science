'''Instructions
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
'''Examples
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Input: head = [1]
Output: [1]
'''
'''Thoughts
1. create a output linked list 
2. Keep track of the previous and the next nodes
3. Loop through head
4. make the previous node.next the next node, make the current node.next next node.next, and make next node.next curr
5. Skip to the node after the next node
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not head:
        return head

    out = ListNode(-1,head)

    pre = out
    curr = head

    while curr and curr.next:
        nxt = curr.next

        pre.next = nxt

        curr.next = nxt.next
        nxt.next = curr

        pre = curr
        curr = pre.next
    
    return out.next