'''Instructions
Given the head of a singly linked list, return true if it is a palindrome.
'''
'''Examples
Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
'''
'''Thoughts
1. Loop to get all the values within the linked list and check if it is a palindrome.
'''

def isPalindrome(self, head) -> bool:
    l = []
    while head:
        l.append(head.val)
        head = head.next
    
    return l == l[::-1]