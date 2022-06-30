'''Instructions
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
'''Examples
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
'''Thoughts
1. Loop until l1, l2 is empty and the previous addition is less than 10
2. Add l1.val, l2.val and 进位 to the current sum
3. Change 进位 to the current sum//10
4. Create a node with val of the current sum % 10 and make it the next of the output LinkedList
5. Return the output LinkedList
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add2num(l1, l2):
    out = ListNode()
    curr = out

    jinwei = 0

    while l1 or l2 or jinwei != 0:
        s = 0

        if l1:
            s += l1.val
            l1 = l1.next
        
        if l2:
            s += l2.val
            l2 = l2.next
        
        s += jinwei
        jinwei = s//10
        s %= 10

        node  = ListNode(s)
        curr.next = node
        curr = curr.next
    return out.next