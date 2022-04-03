'''Instructions
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
'''
'''Examples
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
'''
'''Thoughts
1. Loop until the shortest length of the strings.
2. Chack if there are unused letters and add to the output
'''

def merge_string(word1:str, word2:str):
    output = ''
    for _ in range(min(len(word1), len(word2))):
        output += word1[0] + word2[0]
        word1 = word1[1:]
        word2 = word2[1:]
    
    output += word1+word2
    return output