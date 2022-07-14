'''Instructions
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''
'''Examples
Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s = "paper", t = "title"
Output: true
'''
'''Thoughts
1. First check if the length of s and t are the same
2. Create a dictionary to map characters in s to t
3. if character in t is already mapped return False
4. If the mapped character for the current element in s is different than the element in t at the same index return False
5. Return True
'''

def isomorphic(s:str, t:str):
    if len(s) != len(t):
        return False

    d = {}

    for i in range(len(s)):
        if s[i] not in d.keys():
            if t[i] in d.values():
                return False
            else:
                d[s[i]] = t[i]

        if d[s[i]] != t[i]:
            return False

    return True