'''Instructions
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''
'''Examples
Input: s = "3+2*2"
Output: 7

Input: s = " 3/2 "
Output: 1

Input: s = " 3+5 / 2 "
Output: 5
'''
'''Thoughts
1. Break up the string into numbers and calculate division and multipication and add everything together
'''

def calculate(s:str):
    nums = []
    sign = '+'

    s = s.replace(' ', '')

    curr = ''
    for i in range(len(s)):
        if s[i].isdigit():
            curr += s[i]
        else:
            num = int(curr)
            curr = ''

            if sign == '+':
                nums.append(num)
            elif sign == '-':
                nums.append(-num)
            elif sign == '*':
                nums.append(nums.pop()*num)
            elif sign == '/':
                d = nums.pop()
                quo = abs(d) // abs(num)
                if (d < 0 and num < 0) or (d > 0 and num > 0):
                    nums.append(quo)
                else:
                    nums.append(-quo)
            
            sign = s[i]

    num = int(curr)

    if sign == '+':
        nums.append(num)
    elif sign == '-':
        nums.append(-num)
    elif sign == '*':
        nums.append(nums.pop()*num)
    elif sign == '/':
        d = nums.pop()
        quo = abs(d) // abs(num)
        if (d < 0 and num < 0) or (d > 0 and num > 0):
            nums.append(quo)
        else:
            nums.append(-quo)

    return sum(nums)

calculate("14-3/2")