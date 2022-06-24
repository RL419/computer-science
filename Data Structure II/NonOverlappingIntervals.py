'''Instructions
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
'''
'''Examples
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''
'''Thoughts
1. Create indecies for current and previous
2. Loop through sorted intervals
3. if the start of the current interval overlaps with the end of the previous interval increase count by 1
    4. update previous equal to current if the current end is less than or equal to previous end since we are finding the minimum
5. else update previous equal to curr
6 return count
'''

def no_overlap(intervals):
    intervals.sort()
    count = 0
    pre = 0
    curr = 1
    while curr < len(intervals):
        if intervals[curr][0] < intervals[pre][1]:
            count += 1
            if intervals[curr][1] <= intervals[pre][1]:
                pre = curr
        
        else:
            pre = curr
        curr += 1
    return count