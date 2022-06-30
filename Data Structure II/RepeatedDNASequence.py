'''Instructions
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
'''
'''Examples
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
'''
'''Thoughts
1. Slid window to find every DNA sequence with the length of 10
2. Create a dictionary that holds the occurance of each substring
3. Return the substrings with length greater than 1
'''


def find(s:str):
    if len(s) < 10:
        return []
    
    temp = s[:10]
    d = {temp:1}

    for i in range(10, len(s)):
        temp = temp[1:] + s[i]
        if temp in d.keys():
            d[temp] += 1
        else:
            d[temp] = 1
    
    out = []
    for k in d.keys():
        if d[k] > 1:
            out.append(k)
    return out