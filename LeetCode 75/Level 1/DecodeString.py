'''Instructions
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
'''
'''Examples
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''
'''Thougths
1. Break up the strings into number and alphabet characters
2. Loop through s and decode when you find a closing square bracket to deal with nested braackets
'''

def decode_string(s:str):
    l = []

    i = 0
    while i < len(s):
        if s[i] == ']':
            yes = ''
            while l[-1] != '[':
                yes = l.pop() + yes
            l.pop()
            times = int(l.pop())
            l.append(yes * times)
            i += 1
        else:
            if s[i].isdigit():
                num = ''
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                l.append(num)
            elif s[i] == '[':
                l.append(s[i])
                i += 1
            else:
                curr = ''
                while i < len(s) and s[i].isalpha():
                    curr += s[i]
                    i += 1
                l.append(curr)
    return ''.join(l)