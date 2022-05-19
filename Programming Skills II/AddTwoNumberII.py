'''Instructions
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
'''Examples
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Input: l1 = [0], l2 = [0]
Output: [0]
'''
'''Thoughts
1. Loop through l1 and l2 and turn them into 2 string numbers
2. Add these 2 numbers together as int and convert back to str again
3. Loop through the total and add each digit to the output LinkedList
4. Return output LinkedList 
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add2num(l1, l2):
    num1 = ''
    num2 = ''

    while l1 or l2:
        if l1:
            num1 += str(l1.val)
            l1 =l1.next
        
        if l2:
            num2 += str(l2.val)
            l2 = l2.next

    total = str(int(num1) + int(num2))
    out = ListNode()

    curr = out

    for digit in total:
        node = ListNode(int(digit))
        curr.next = node
        curr = curr.next
    return out.next