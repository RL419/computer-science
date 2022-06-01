'''Instructions
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
'''Examples
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''
'''Thoughts
1. Create a list and loop through strs and add the sorted version of strings to the list
2. Create a dictionary that will store list of elements from strs with characters used
3. Loop through the new created list and add strs at the same index with the key of list[i]
4. Loop through the keys of the dictionary and add d[key] to the out put list
5. Return the output
'''

def group(strs):
    out = []
    chars = []
    d = {}

    for s in strs:
        chars.append(''.join(sorted(s)))
    
    for i in range(len(chars)):
        if chars[i] in d.keys():
            d[chars[i]].append(strs[i])
        else:
            d[chars[i]] = [strs[i]]
    
    for k in d.keys():
        out.append(d[k])
    return out