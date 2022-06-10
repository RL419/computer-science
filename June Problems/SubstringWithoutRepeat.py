'''Instructions
Given a string s, find the length of the longest substring without repeating characters.
'''
'''Examples
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
'''Thoughts
1. Get a empty string and a count
2. Loop though s
3. If the element in s is not in the empty string add it the the string
4. Else remove everything before the occurence of the element
5. Set count to the length of the string if it is greater than count
'''

def length(s):
    count = 0
    out = ''
    for e in s:
        if e not in out:
            out += e
        else:
            out = out[out.index(e)+1:] + e
        count = max(count, len(out))
    return count