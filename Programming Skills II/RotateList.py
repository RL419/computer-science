'''Instructions
Given the head of a linked list, rotate the list to the right by k places.
'''
'''Examples
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''
'''Thoughts
1. Get the last node and the node before the kth node from the end
2. make the new head kth node, make the end node's next to head and make the node before kth node from the end's next None to prevent cycle 
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate(head, k):
    if not head or k == 0:
        return head

    out = ListNode(next=head)

    kth, end = find_kth(out, k)
    
    if kth == out:
        return head

    end.next = head
    new_start = kth.next
    kth.next = None
    
    return new_start

def find_kth(head, k):
    n = 0
    end = head
    kth = head

    while end.next:
        end = end.next
        n += 1
        if n > k:
            kth = kth.next
        
    if k > n:
        return find_kth(head, k%n)
    return kth, end