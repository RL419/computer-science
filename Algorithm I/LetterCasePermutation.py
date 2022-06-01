'''Instructions
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.
'''
'''Examples
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Input: s = "3z4"
Output: ["3z4","3Z4"]
'''
'''Thoughts
1. Recursion through the string
2. If there is a alphabet character recurion on the uppercase and lowercase
'''

def letter_case(s:str):
    out = []

    def UwU(first:str, last:str):
        if len(first) == 0:
            out.append(last)
            return
        
        if first[0].isalpha():
            UwU(first[1:], last + first[0].upper())
            UwU(first[1:], last + first[0].lower())
        
        else:
            UwU(first[1:], last + first[0])
    
    UwU(s, '')
    return out