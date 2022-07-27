'''Instructions
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
'''Examples
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''
'''Thoughts
1. Get the total amount of nodes in the linked list and divide it by 2 which will be the middle one
2. Loop until i and return the value
'''

def middleNode(head):
    i = geti(head)
    for i in range(i):
        head = head.next
    return head
    
def geti(head):
    l = []
    while head.next is not None:
        l.append(head.val)
        head = head.next
    l.append(head.val)
    i = len(l)//2
    return i