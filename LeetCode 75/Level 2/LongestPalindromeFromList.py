'''Instructions
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.
'''
'''Examples
Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
'''
'''Thoughts
1. Counter words
2. Loop through each word in counter
3. Keep track of all of the palindrome words, extra palindrome words and normal words
4. Add them together
'''

from collections import Counter

def palindrome(words:list):
    c = Counter(words)
    
    same = center = normal = 0

    for word, count in c.items():
        if word[::-1] == word:
            if count % 2 == 1:
                center = 1
                same += count - 1
            else:
                same += count
        else:
            if word[::-1] in c.keys():
                normal += min(c[word], c[word[::-1]])
    return 2 * (same + center + normal)