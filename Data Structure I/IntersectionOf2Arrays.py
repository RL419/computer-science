'''Instructions
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''
'''Examples
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''
'''Thoughts
1. Loop through the shortest list
2. If an element of the short list is in the long list
3. Add the element to the output list.
4. Remove the element from the long list.
5. Return the output list
'''

def intersect(nums1:list, nums2:list):
    output = []
    if len(nums1) > len(nums2):
        for num in nums2:
            if num in nums1:
                output.append(num)
                nums1.remove(num)
    else:
        for num in nums1:
            if num in nums2:
                output.append(num)
                nums2.remove(num)
    return output