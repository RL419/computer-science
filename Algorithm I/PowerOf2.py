'''Instructions
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
'''
'''Examples
Input: n = 1
Output: true
Explanation: 20 = 1

Input: n = 16
Output: true
Explanation: 24 = 16

Input: n = 3
Output: false
'''
'''Thoughts
1. Check if the binary number only has 0 and 1 one
'''

def power_of_2(n):
    yes = bin(n)[2:]
    if (len(set(yes)) == 2 and '0' in set(yes)) or len(set(yes)) == 1:
        if yes.count('1') == 1:
            return True
    return False