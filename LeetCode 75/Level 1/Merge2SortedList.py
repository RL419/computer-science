'''Instructions
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
'''Examples
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
'''
'''Thoughts
1. Get a list and add all of the values in list1 and list2
2. sort the list
3. Loop through the list and turn it into a linked list
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge2lists(list1, list2):
    l = []
    while list1 is not None:
        l.append(list1.val)
        list1 = list1.next
        
    while list2 is not None:
        l.append(list2.val)
        list2 = list2.next
        
    l.sort()
    
    head = ListNode()
    node = head
    
    for num in l:
        n = ListNode(num)
        head.next = n
        head = head.next
    
    return node.next