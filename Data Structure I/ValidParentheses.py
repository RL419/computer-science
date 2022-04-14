'''Insturctions
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
'''Examples
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
'''
'''Thoughts
1. Check if the length of s is even
2. Loop through s
3. If it is a open bracket add it to a list
4. Else check if the list is empty return False if it is
5. Check if it is the same type of brackets as the last element in the list
6. If it is remove the last element
7. Else return False
8. Return True if the list is empty else False
'''

def is_valid(s: str):
    if len(s) % 2 != 0:
        return False

    l = []
    for bracket in s:
        if bracket == '(' or bracket == '[' or bracket == '{':
            l.append(bracket)
        else:
            if len(l) == 0:
                return False
            else:
                if bracket == ')' and l[-1] == '(':
                    l.pop()
                elif bracket == ']' and l[-1] == '[':
                    l.pop()
                elif bracket == '}' and l[-1] == '{':
                    l.pop()
                else:
                    return False
    
    return True if len(l) == 0 else False