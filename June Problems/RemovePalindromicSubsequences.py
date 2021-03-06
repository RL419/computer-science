'''June 8, 2022'''
'''Instructions
You are given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string if it is generated by deleting some characters of a given string without changing its order. Note that a subsequence does not necessarily need to be contiguous.

A string is called palindrome if is one that reads the same backward as well as forward.
'''
'''Examples
Input: s = "ababa"
Output: 1
Explanation: s is already a palindrome, so its entirety can be removed in a single step.

Input: s = "abb"
Output: 2
Explanation: "abb" -> "bb" -> "". 
Remove palindromic subsequence "a" then "bb".

Input: s = "baabb"
Output: 2
Explanation: "baabb" -> "b" -> "". 
Remove palindromic subsequence "baab" then "b".
'''
'''Thoughts
For some reason this works
'''

def remove(s: str):
    return 1 if s[::-1] == s else 2

# def center(s, start, end):
#     while start >= 0 and end < len(s):
#         if s[start] == s[end]:
#             start -= 1
#             end += 1
#         else:
#             break
#     return s[start+1: end]

# def longest_palindrome(s):
#     longest = ''
#     for i in range(len(s)):
#         longest = max(longest, center(s, i, i), center(s, i, i+1), key=len)
#     return longest

# def remove(s:str):
#     count = 0
#     while len(s) != 0:
#         s = s.replace(longest_palindrome(s), '', 1)
#         count += 1
#     return count