'''Instructions
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
'''
'''Examples
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
'''
'''Thoughts
1. Repeat nums twice to do circular array and create a output list contains -1s
2. Loop through 2 times nums
3. Loop until stack is empty or the element is less than the top of the stack
4. Remove the top of the stack and make out[remove value from the stack] the current element
5. If the index is smaller than the length of nums add the index to the stack
'''

def next_greater_element(nums:list):
    out = [-1]*len(nums)
    new = nums + nums

    stack = []

    for i in range(len(new)):
        while len(stack) != 0 and new[i] > nums[stack[-1]]:
            index = stack.pop()
            out[index] = new[i]
        if i < len(nums):
            stack.append(i)
    return out