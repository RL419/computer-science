'''Instructions
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
'''
'''Examples
Input: n = 12
Output: 21

Input: n = 21
Output: -1
'''
'''Thoughts
next permutaion algorithm
'''

def next_greater_element3(n):
    digits = [int(i) for i in str(n)][::-1]

    first_decrease = -1
    for i in range(1, len(digits)):
        if digits[i] < digits[i-1]:
            first_decrease = i
            break
    
    if first_decrease == -1:
        return -1
    
    current = float('inf')
    for j in range(len(digits[:first_decrease])):
        if digits[j] > digits[first_decrease] and digits[j] < current:
            current = digits[j]
            successor = j
    
    digits[first_decrease], digits[successor] = digits[successor], digits[first_decrease]
    digits[:first_decrease] = digits[:first_decrease][::-1]

    out = 0
    c = 0
    for num in digits:
        out += num * 10**c
        c += 1
    return out if out <= 2**32 else -1
    
            
# def next_greater_element3(n):
#     nums = [i for i in str(n)][::-1]
#     for i in range(len(nums)-1):
#         if int(nums[i]) > int(nums[i+1]):
#             nums[i], nums[i+1] = nums[i+1], nums[i]
#             break
#     num = int(''.join(nums[::-1]))
#     if num > n and len(bin(num)[2:]) < 32:
#         return num
#     return -1