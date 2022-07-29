'''Instructions
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
'''Examples
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''
'''Thoughts
1. If n is 0 return head
2. Get the length of head
3. If the length is equal to n retrun head.next
4. Loop size minus n times and make next next.next
'''

def remove(head, n):
    if n == 0:
        return head
    length = size(head)
    if length == n:
        return 
    node = head
    for _ in range(length-n-1):
        node = node.next
    node.next = node.next.next
    return head

def size(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count