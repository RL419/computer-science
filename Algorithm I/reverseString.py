'''Instructions
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''
'''Examples
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
'''Thoughts
1. Loop through s and move evev
'''

def reverse(s):
    for i in range(len(s)):
        s.insert(0,s.pop(i))