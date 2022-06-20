'''June 20, 2022'''
'''Instructions
A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.
'''
'''Examples
Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].
'''
'''Thoughts
1. Get a set to get all unique elements in words
2. Loop through the set
3. For every word loop through to get all the suffix and if they are in the set remove them
4. return the sum of the length of remaining words in set and plus one for every word for #
'''

def encode(words):
    good = set(words)
    s = good.copy()
    for w in s:
        for i in range(1, len(w)):
            good.discard(w[i:])
    
    return sum([len(word)+1 for word in good])