'''Instructions
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
'''
'''Examples
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
'''
'''Thoughts
1. Create a counter for secret
2. Loop through guess
3. If guess[i] is in the right place add 1 to bulls and decrease cows if necessary
4. If guess[i] is not in the right place and the there is unmapped secret[i] add 1 to cows
'''

from collections import Counter


def bullcow(secret:str, guess:str):
    bulls = 0
    cows = 0

    c = Counter(secret)

    for i in range(len(guess)):
        if guess[i] in c.keys():
            if secret[i] == guess[i]:
                if c[guess[i]] == 0:
                    cows -= 1
                    c[guess[i]] += 1
                bulls += 1
                c[guess[i]] -= 1
            else:
                if c[guess[i]] > 0:
                    cows += 1
                    c[guess[i]] -= 1
    return f'{bulls}A{cows}B'