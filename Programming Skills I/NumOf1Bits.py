'''Instructions
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
'''
'''Examples
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
'''
'''Thoughts
1. Call bin on n and count the number of 1s
'''

def num_of1_bit(n):
    return bin(n)[2:].count('1')