'''Instructions
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''
'''Examples
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Input: n = 2
Output: false
'''
'''Thoughts
1. Create an empty set
2. Create a while loop that ends if n is 1 or n is in the set
3. adds the current value to the set and change the number to the next one
'''

def happy_number(n):
    previous = set()
    while n != 1 and n not in previous:
        previous.add(n)
        
        num = 0
        for digit in str(n):
            num += int(digit)**2
        
        n = num
    
    return n == 1