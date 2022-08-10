'''Instructions
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
'''
'''Examples
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''
'''Thoughts
1. Start form the start of s
2. Loop until every character in t has been found, update the output if the length of the current string is less than the output string
3. move the left pointer to the next element in s that occurs in t
'''

from collections import Counter

def min_window(s:str, t:str):
    if not s or not t:
        return ""
    
    out, out_len = (-1, -1), float('inf')

    c = Counter(t)
    required = len(t)

    left = 0

    curr = {}
    curr_len = 0

    for right in range(len(s)):
        if curr[s[right]] in curr.keys():
            curr[s[right]] += 1
        else:
            curr[s[right]] == 1
        
        if s[right] in c.keys() and curr[s[right]] <= c[s[right]]:
            curr_len += 1
        
        while curr_len == required:
            if right - left + 1 < out_len:
                out = (left, right)
                out_len = right - left + 1
            
            curr[s[left]] -= 1
            if s[left] in c and curr[s[left]] < c[s[left]]:
                curr_len -= 1

            left += 1

    return s[out[0]:out[1]+1] if out_len != float('inf') else ""