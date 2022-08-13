'''Instructions
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''
'''Examples
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
'''Thoughts
1. Sort intervals from the earliest to the latest
2. Creat a output list with the first interval
3. Loop through the rest of intervals and check if it overlaps with the last interval in output list
4. if it does update the end of the last interval in output list
5. Else add the interval to output list
6. return output
'''

def merge(intervals: list[list[int]]):
    intervals.sort()
    out = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= out[-1][1]:
            out[-1][1] = max(end, out[-1][1])
        else:
            out.append([start,end])
        
    return out