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

def helper(ans:list, n, k, current, i) -> None:
	if len(current) == k or i > n:
		if len(current) == k:
			ans.append(current)
		return
		
	helper(ans, n, k, current+[i], i+1)
	helper(ans, n, k, current, i+1)

def function(n,k):
	ans = []

	helper(ans, n, k, [], 1)
	
	return ans

# print(function(4,2))