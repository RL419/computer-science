'''Instructions
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
'''
'''Examples
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Input: s = "aba"
Output: false

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
'''
'''Thoughts
1. Loop until the substring length is equal to half of s length
2. If the length of s is divisible by length of substring and the substring times length of s divided by length of substring is equal to s return True
3. Return False
'''

def substring(s):
    i = 1
    while i <= len(s) // 2:
        if len(s) % i == 0:
            if s[:i] * (len(s)//i) == s:
                return True
        i += 1
    return False