'''Instructions
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
'''
'''Examples
https://leetcode.com/problems/check-if-it-is-a-straight-line/

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
'''
'''Thoughts
1. If all of the x coords or all the y coords are the same return True
2. If there are only 2 coords return True
3. Calculate the slope and loop through coordinates
'''

def is_a_straight_line(coordinates):
    def get_slope(coord1, coord2):
        return (coord2[0] - coord1[0]) / (coord2[1]- coord1[1])

    if len(coordinates) == 2:
        return True
    if len(set([x[0] for x in coordinates])) == 1 or len(set([y[1] for y in coordinates])) == 1:
        return True
    if coordinates[1][1] - coordinates[0][1] == 0: #prevent zero division
        return False
    slope = get_slope(coordinates[0], coordinates[1])

    for i in range(2, len(coordinates)):
        if coordinates[i][1] - coordinates[i-1][1] == 0:
            return False
        if get_slope(coordinates[i-1], coordinates[i]) != slope:
            return False

    return True