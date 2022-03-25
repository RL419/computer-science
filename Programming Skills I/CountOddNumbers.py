''' Instructions
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
'''
'''Examples
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
'''
'''Thoughts
1. Loop through range(low, high+1)
2. Count the odd numbers
Time limit exceded
1. All of the numbers with in the range is high-low+1
2. If there are even numbers of numbers in range then odd numbers will take up half of numbers
3. If there are odd nubers of numbers in range
    if high and low are odd ex. 3,7 odd numbers will take up the larger half
    if high and low are even ex. 4,8 odd numbers will take up the smaller half
'''

def con(low, high):
    num_in_range = high-low+1
    if num_in_range % 2 == 0:
        return num_in_range//2
    else:
        if high % 2 == 0 and low % 2 == 0:
            return num_in_range//2
        else:
            return num_in_range//2 + 1