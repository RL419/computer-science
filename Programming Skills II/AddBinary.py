'''Instructions
Given two binary strings a and b, return their sum as a binary string.
'''
'''Examples
Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"
'''
'''Thoughts
1. Turn the binary numbers back to normal numbers and add then togerther and turn it back to binary
'''

def add_binary(a,b):
    return bin(int(a,2) + int(b,2))[2:]