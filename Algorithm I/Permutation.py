'''Instructions
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
'''
'''Examples
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''
'''Thoughts
1. Loop through s2 and get every possible substring with the same length of s1
2. If s1 and the substring has the same characters return True
3. Return False
'''

def permutations(s1,s2):
    for i in range(len(s2)-len(s1) + 1):
        sub = s2[i:i+len(s1)]
        if sorted(sub) == sorted(s1):
            return True
    return False