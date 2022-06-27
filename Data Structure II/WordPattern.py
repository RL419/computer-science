'''Instructions
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''
'''Examples
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''
'''Thoughts
1. Create a dictionary that matches pattern to words in s
2. Loop through pattern and s to check if they match
'''

def word_pattern(pattern:str, s:str):
    d = {}
    s = s.split(' ')
    if len(pattern) != len(s):
        return False
    for i in range(len(s)):
        if pattern[i] in d.keys():
            if d[pattern[i]] != s[i]:
                return False
        else:
            if s[i] in d.values():
                return False
            d[pattern[i]] = s[i]
    return True