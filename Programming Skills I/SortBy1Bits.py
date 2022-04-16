'''Instructions
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.
'''
'''Examples
Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
Explantion: [0] is the only integer with 0 bits.
[1,2,4,8] all have 1 bit.
[3,5,6] have 2 bits.
[7] has 3 bits.
The sorted array by bits is [0,1,2,4,8,3,5,6,7]

Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output: [1,2,4,8,16,32,64,128,256,512,1024]
Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.
'''
'''Thoughts
1. No idea
'''

# def sortbybit(arr):
#     d = {i:bin(v)[2:] for i, v in enumerate(arr)}
#     k = list(d.values())
#     k.sort(key=len)
#     k.sort(key=ones)
#     out = [arr[(list(d.keys())[list(d.values()).index(i)])] for i in k]
#     return out

# def ones(s: str):
#     return s.count('1')