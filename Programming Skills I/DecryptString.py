'''Instructions
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.
'''
'''Examples
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Input: s = "1326#"
Output: "acz"
'''
'''Thoughts
1. Generate a dictionary of code to alphebet characters
2. Loop through s and get the alph from the dict
'''

def freqAlphabets(s:str):
    code = list('123456789')
    for num in range(10,27):
        code.append(f'{num}#')
    alph = list('abcdefghijklmnopqrstuvwxyz')
    d = {code[i]: alph[i] for i in range(len(code))}

    output = ''
    i = 0
    while i < len(s):
        if i < len(s)-2:
            if s[i+2] == "#":
                output += d[s[i:i+3]]
                i += 3
            else:
                output += d[s[i]]
                i += 1
        else:
            output += d[s[i]]
            i += 1
    
    return output