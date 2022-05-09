'''Instructions
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
'''
'''Examples
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
'''
'''Thoughts
1. Add num to k
2. Split the digits of k into list
'''

def add_to_array_form_int(num, k):
    num = num[::-1]
    for i in range(len(num)):
        k += num[i] * 10**i

    s = str(k)
    return [int(n) for n in s]