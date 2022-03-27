'''Instructions
You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).
'''
'''Examples
Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.

Input: x = 3, y = 4, points = [[3,4]]
Output: 0
Explanation: The answer is allowed to be on the same location as your current location.

Input: x = 3, y = 4, points = [[2,3]]
Output: -1
Explanation: There are no valid points.
'''

'''Thoughts
1. Loop through points and check if they are on the same x or y coords.
2. If it is then calculate its Manhattan distance
3. Check if the Manhattan distance is less than the one stored, if it is than update the index and the distance
'''

def nearest_point(x, y, points: list):
    i = -1
    for point in points:
        if point[0] == x or point[1] == y:
            if i == -1:
                i = points.index(point)
                distance = abs(x-point[0]) + abs(y-point[1])
            elif abs(x-point[0]) + abs(y-point[1]) < distance:
                distance = abs(x-point[0]) + abs(y-point[1])
                i = points.index(point)
    return i