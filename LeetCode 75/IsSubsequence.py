'''Instructions
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''
'''Examples
Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "axc", t = "ahbgdc"
Output: false
'''
'''Thougths
1. If s is an empty string return True
2. Have a pointer that points to the start of s
3. Loop through t
4. If element in t is equal to s at the pointer move the pointer to the next element
5. If the pointer went through all the string return True
'''

def is_subsequence(s, t):
    if not s:
        return True

    sub = 0

    for i in t:
        if s[sub] == i:
            sub += 1
        
        if len(s) == sub:
            return True
    return len(s) == sub