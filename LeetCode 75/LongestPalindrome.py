'''Instructions
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
'''
'''Examples
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
'''
'''Thoughts
1. Default longest palindrome is the lenght of s
1. Loop through the unique characters in s
2. If the count of s is odd default minus 1
3. If default changed return default + 1 else default 
'''

def longestPalindrome(s: str) -> int:
    out = len(s)
    
    for i in set(s):
        if s.count(i) % 2 == 1:
            out -= 1
    
    return out + 1 if out != len(s) else out