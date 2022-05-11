'''Instructions
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
'''
'''Examples
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''
'''Thoughts
1. Split s with spaces to get a list of words and return the length last element 
'''

def len_of_last_word(s:str):
    s = s.strip()
    l = s.split(' ')
    return len(l[-1])