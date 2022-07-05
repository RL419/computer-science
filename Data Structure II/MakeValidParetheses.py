'''Instructions
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
'''
'''Examples
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Input: s = "a)b(c)d"
Output: "ab(c)d"

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
'''
'''Thoughts
1. Create a list to keep track of the indecies of all the open brackets
2. Loop through s
3. If you find an open bracket store the index
4. If you find a closed bracket and there are previous open brackets remove the last open bracket
5. else remove the closed bracket
6. Last loop through the unmatched open brackets and remove them
'''

def min_remove_make_valid(s:str):
    brackets = []
    out = list(s)
    for i in range(len(s)):
        if s[i] == '(':
            brackets.append(i)
        elif s[i] == ')':
            if len(brackets) > 0:
                brackets.pop()
            else:
                out[i] = ''
    for b in brackets:
        out[b] = ''
    return ''.join(out)