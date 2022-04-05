'''Instructions
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
'''Examples
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Input: head = [0]
Output: 0
'''
'''Thoughts
1. While node.next is not None and the val to a list
2. Reverse the list
3. Loop through the list and turn it into binary
'''

def binary_to_int(head):
    l = [head.val]
    while head.next is not None:
        head = head.next
        l.append(head.val)
    output = 0
    l = l[::-1]
    for i in range(len(l)):
        output += l[i] * 2**i
    return output