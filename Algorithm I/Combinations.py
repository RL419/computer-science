'''Instructions
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.
'''
'''Examples
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Input: n = 1, k = 1
Output: [[1]]
'''
'''Thoughts

'''

# def combine(n,k):
#     if  k <= 0:
#         return [[]]
#     if k > n:
#         return []
#     if n == 1:
#         return [[1]]

#     nums = [i for i in range(1,n+1)]


# def get(l:list,k):
#     if k == 0:
#         return []
#     out = set()
#     for i in l:
#         new = l.copy()
#         new.remove(i)
#         previous = get(new,k-1)
#         for j in previous:
#             alist = [i]
#             alist.extend(j)
#             out.add(sorted(alist))
#     return out

# print(get([1,2,3,4], 2))