'''Instructions
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''
'''Examples
Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1
'''
'''Thoughts
1. Get a dictionary of the character and its count
2. Loop through the the string and check if the count is 1
'''

def unique_char(s:str):
    d = {}
    for c in set(s):
        d[c] = s.count(c)
    
    for i in range(len(s)):
        if d[s[i]] == 1:
            return i
    return -1