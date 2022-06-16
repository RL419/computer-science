'''June 16, 2022'''
'''Instructions
Given a string s, return the longest palindromic substring in s.
'''
'''Examples
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
'''
'''Thoughts
1. Loop through the indexes of s
2. For every index get the longest palindrom with the center being the index and the center being the index and the next index
3. Return longest
'''

def longestPalindrome(s: str) -> str:
    longest = ''
    for i in range(len(s)):
        longest = max(longest, center(s, i, i), center(s, i, i+1), key=len)
    return longest
    
def center(s, start, end):
    while start >= 0 and end < len(s):
        if s[start] == s[end]:
            start -= 1
            end += 1
        else:
            break
    return s[start+1: end]