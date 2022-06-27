'''Instructions
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
'''
'''Examples
nput: num1 = "11", num2 = "123"
Output: "134"

Input: num1 = "456", num2 = "77"
Output: "533"

Input: num1 = "0", num2 = "0"
Output: "0"
'''
'''Thoguhts

'''

def add_string(num1, num2):
    out = ''
    jinwei = 0

    if len(num1) > len(num2):
        num1, num2 = num2, num1
    
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    for i in range(len(num2)):
        curr = int(num2[i])
        if i < len(num1):
            curr += int(num1[i])
        curr += jinwei
        jinwei = curr // 10
        out += str(curr%10)

    if jinwei:
        out += str(jinwei)
    return out[::-1]