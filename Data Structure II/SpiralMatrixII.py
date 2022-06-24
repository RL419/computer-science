'''Instructions
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''
'''Examples
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Input: n = 1
Output: [[1]]
'''
'''Thoughts
[
    [1, 2, 3, 4, 5]
    [16,17,18,19,6]
    [15,24,25,20,7],
    [14,23,22,21,8],
    [13,12,11,10,9]
]
1. Loop from the outside layer to the inside layer
2. (n+1)/2 works for both even and odd layers
3. For every layer add in a circle order
'''

def generate(n):
    out = [[-1]*n for _ in range(n)]
    count = 1

    for layer in range((n+1)//2):
        
        r = layer
        while r < n - layer:
            out[layer][r] = count
            count += 1
            r += 1
        
        c = layer + 1
        while c < n - layer:
            out[c][n-layer-1] = count
            count += 1
            c += 1
        
        r = n - layer - 2
        while r >= layer:
            out[n-layer-1][r] = count
            count += 1
            r -= 1
        
        c = n - layer - 2
        while c > layer:
            out[c][layer] = count
            count += 1
            c -= 1
    return out