'''Instructions
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
'''
'''Examples
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
'''
'''Thoughts
1. Create a dictionary that maps the count to a list of words
2. Get the k elements with the highest occurence
'''

def top_k(words:list, k:int):
    d = {}

    for word in set(words):
        c = words.count(word)
        if c in d.keys():
            d[c].append(word)
        else:
            d[c] = [word]
    
    keys = list(d.keys())
    keys.sort()

    out = []
    while len(out) != k:
        curr = sorted(d[keys.pop()])

        if len(curr) > k - len(out):
            out.extend(curr[:k-len(out)])
        else:
            out.extend(curr)
    return out