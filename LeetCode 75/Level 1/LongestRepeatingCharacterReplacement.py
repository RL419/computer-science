'''Instructions
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''
'''Examples
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''
'''Thoughts
1. Sliding window algorithm
2. dictionary to keep track of the occurence of each character in the current window
3. If the length of the current window minus the occurence of the character with the highest occurance is less than or equal to k, update the output
4. Else move the start of the window
5. return out
'''

def replacement(s, k):
    start = 0
    counter = {}

    out = 0

    for end in range(len(s)):
        if s[end] not in counter.keys():
            counter[s[end]] = 0
        counter[s[end]] += 1

        if end + 1 - start - max(counter.values()) > k:
            counter[s[start]] -= 1
            start += 1
        else:
            out = max(out, end + 1 - start)
        
    return out