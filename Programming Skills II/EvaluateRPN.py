'''Instructions
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.
'''
'''Examples
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''
'''Thoughts
1. If token only contains 1 element return the number
2. Loop until a operation symbol
3. Replace the numbers and symbol with the completed calculation
4. Recursion on the new list
'''

def evaluate(tokens):
    if len(tokens) == 1:
        return int(tokens[0])
    symbols = ['+', '-', '*', '/']
    i = 0
    while tokens[i] not in symbols:
        i += 1
    first = tokens[:i-2]
    do = tokens[i-2:i+1]
    last = tokens[i+1:]
    first.append(calculate(do))
    first.extend(last)
    return evaluate(first)

def calculate(l):
    first = int(l[0])
    second = int(l[1])
    if l[-1] == '+':
        return str(int(first + second))
    if l[-1] == '-':
        return str(int(first - second))
    if l[-1] == '*':
        return str(int(first * second))
    if l[-1] == '/':
        return str(int(first / second))