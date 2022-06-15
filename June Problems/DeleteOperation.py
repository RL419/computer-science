'''June 14, 2022'''
'''Instructions
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
'''
'''Examples
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
'''
'''Thoughts

'''

def delete(word1:str, word2:str):
    if len(word1) > len(word2):
        word1, word2 = word2, word1
    
    for i in range(len(word1)):
        for j in range(len(word2)):
            pass

# def delete(word1:str, word2:str):
#     count = 0
    
#     a = set(word1)
#     b = set(word2)

#     if len(a) > len(b):
#         a, b = b, a
    
#     for c in a:
#         if c in b:
#             count += min(word1.count(c), word2.count(c))
    
#     return len(word1) + len(word2) - 2*count