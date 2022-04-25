'''Instructions
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''
'''Examples
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Input: s = "God Ding"
Output: "doG gniD"
'''
'''Instructions
1. Split the string into a list of words
2. Reverse the words in the list
3. Join them back into a string
'''

def reverse(s:str):
    l = s.split(' ')
    l = [i[::-1] for i in l]
    a = " ".join(l)
    return a