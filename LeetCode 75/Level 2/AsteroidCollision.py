'''Instructions
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
'''
'''Examples
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
'''
'''Thoughts
1. Loop through asteroids
2. If an asteroid going right encounters an asteroid going left, if they have the same weight remove the right one and dont add the left one, if the right one is heavier dont add the left one, if the left one is heavier loop until the left one gets destroyed or encounters an asteroid going in the same direction
'''

# def collide(asteroids:list):
#     out = []

#     for a in asteroids:
#         if len(out) == 0:
#             out.append(a)
#         elif (out[-1] < 0 and a < 0) or (out[-1] > 0 and a > 0):
#             out.append(a)
#         else:
#             ifadd = True
#             while out and out[-1] * a < 0:
#                 if abs(out[-1]) > abs(a):
#                     ifadd = False
#                     break
#                 elif abs(out[-1]) == abs(a):
#                     out.pop()
#                     ifadd = False
#                     break
#                 else:
#                     out.pop()
#             if ifadd:
#                 out.append(a)
    
#     return out

def collide(asteroids:list[int]):
    out = []

    for a in asteroids:
        ifadd = True
        if out and a < 0 and out[-1] > 0:
            while out and a < 0 and out[-1] > 0:
                if abs(out[-1]) == abs(a):
                    out.pop()
                    ifadd = False
                    break
                elif abs(out[-1]) > abs(a):
                    ifadd = False
                    break
                elif abs(out[-1]) < abs(a):
                    out.pop()
        if ifadd:
            out.append(a)
    return out