'''Instructions
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
'''Examples
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
'''Thoughts
1. Loop throught the shortest word in the list and check if the character is in all string if it is add it to the output
'''

def longestCommonPrefix(self, strs: list[str]) -> str:
        a = min(strs, key=len)
        
        out = ''
        for i in range(len(a)):
            for s in strs:
                if a[i] != s[i]:
                    return out
            out += a[i]
        return out