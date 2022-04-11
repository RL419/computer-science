'''Instructions
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''
'''Examples
Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''
'''Thoughts
1. Loop through set ramsomNote
2. If the count of the character in ransomNote is more than the count of the charcater in magazine return False
3. return True
'''

def canConstruct(ransomNote: str, magazine: str):
    for char in set(ransomNote):
        if ransomNote.count(char) > magazine.count(char):
            return False
    return True