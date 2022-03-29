'''Instructions
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
'''
'''Examples
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
'''
'''Thoughts
1. Sort the 2 strings to make sure they have the same characters.
2. Loop through both strings and check if the differences is less than 3.
'''

def are_almost_equal(s1: str, s2: str):
    if sorted(s1) != sorted(s2):
        return False
    differences = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            differences.append(i)
        if len(differences) > 2:
            return False
    
    return True