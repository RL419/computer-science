'''Instructions
Given the head of a linked list, return the list after sorting it in ascending order.
'''
'''Examples
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Input: head = []
Output: []
'''
'''Thoughts
1. Get all the valus in the list, sort them and replace the values
'''

def sort_list(head):
    v = []
    node = head
    while node:
        v.append(node.val)
        node = node.next
    
    v.sort()
    out = head
    while out:
        out.val = v.pop(0)
        out = out.next
    return head