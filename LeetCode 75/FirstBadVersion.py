'''Instructions
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''
'''Examples
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Input: n = 1, bad = 1
Output: 1
'''
'''Thoughts
1. If n[midpoint] is bad and n[midpoint -1] is not bad return the midpoint
2. Change first or last
'''

def isBadVersion(n):
    return True or False

def bad_version(n):
    first = 1
    last = n
    
    while first <= last:
        midpoint = (first+last)//2
        i = isBadVersion(midpoint)
        if i == True and isBadVersion(midpoint-1) == False:
            return midpoint
        if i == False:
            first = midpoint+1
        elif i == True:
            last = midpoint-1