'''Instuctions
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
'''Examples
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
'''
'''Thoughts
1. Loop through set t
2. If the count the charcater in s is less than the count of the character in t return False
3. return True
'''

def valid_anagram(s: str, t: str):
    for char in set(max(s,t, key=len)):
        if s.count(char) != t.count(char):
            return False
    return True