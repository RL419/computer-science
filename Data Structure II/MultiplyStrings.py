'''Instructions
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
'''Examples
Input: num1 = "2", num2 = "3"
Output: "6"

Input: num1 = "123", num2 = "456"
Output: "56088"
'''
'''Thoughts
1. Loop through every digit in num2 and multiply by by num1
'''

def multiply_str(num1, num2):
    l = []
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    for i in range(len(num2)):
        for j in range(len(num1)):
            l.append(int(num2[i]) * int(num1[j]) * 10**i * 10**j)
    return str(sum(l))