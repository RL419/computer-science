'''Instructions
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.
'''
'''Examples
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
'''
'''Thoughts
1. Turn the words into alphabet letter
2. Check if they are the same after sorting
'''

def alien_dict(words: list[str], order:str):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_list = []
    for word in words:
        s = ''
        for letter in word:
            s += alph[order.index(letter)]
        new_list.append(s)
    return sorted(new_list) == new_list