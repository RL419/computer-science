'''June 15, 2022'''
'''Instructions
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.
'''
'''Examples
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
'''
'''Thoughts
1. Loop through words starting from the shortest
2. For each word set a default predecessor length of 1
3. Loop through each word and remove each character to check if it is in words
4. If it is set the predecessor length to the highest between the current length and the predecessor's predecessor length
5. Return the longest predecessor length
'''

def longest_str_chain(words:list):
    d = {}
    words.sort(key=len)

    for w in words:
        d[w] = 1
        for i in range(len(w)):
            previous = w[:i] + w[i+1:]
            if previous in d.keys():
                d[w] = max(d[w] ,1 + d[previous])
    
    return max(d.values())