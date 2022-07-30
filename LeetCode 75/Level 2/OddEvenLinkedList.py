'''Instructions
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
'''
'''Examples
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
'''
'''Thoughts
1. Loop through head and move all the even nodes to another linked list
2. append the linked list to the end of head
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oell(head:ListNode):
    if not head:
        return head
    even = ListNode()

    node = head
    e = even

    while node and node.next:
        e.next = node.next
        e = e.next

        node.next = node.next.next
        if node.next:
            node = node.next
    
    e.next = None
    node.next = even.next
    return head