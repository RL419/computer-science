'''Instructions
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''
'''Examples
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''
'''Thoughts
1. Loop throuth both strings and remove backspaced characters
2. return true if they are the same
'''

def backspace(s:str, t:str):
    sd = s.count('#')
    td = t.count('#')

    for _ in range(sd):
        i = s.index('#')
        if i > 0:
            s = s.replace(s[i-1:i+1], '', 1)
        else:
            s = s[1:]
    
    for _ in range(td):
        i = t.index('#')
        if i > 0:
            t = t.replace(t[i-1:i+1], '', 1)
        else:
            t = t[1:]
    
    return s == t