'''Instructions
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''
'''Examples
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''
'''Thoughts
1. Loop while head is not None
2. Check if the head is seen
3. If hasn't add the seen
4. If seen return True
5. Return False
'''

def has_cycle(head):
    s = set()
    while head is not None:
        if head in s:
            return True
        else:
            s.add(head)
        head = head.next
    return False