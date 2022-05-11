'''Instructions
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
'''Examples
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''
'''Thoughts
1. Create an output list with the same length of temperatures and fill it with 0s
2. Loop from the last element to the first
3. If the element is greater than the highest temperature recorded update the highest
4. Else check if the next element is higher than the current element
5. If it isnt than skip to the element greater than the next element
'''

def dailyTemp(temperatures):
    out = [0] * len(temperatures)

    highest = 0

    for i in range(len(temperatures)-1, -1, -1):
        if temperatures[i] >= highest:
            highest = temperatures[i]
        else:
            difference = 1
            while temperatures[i + difference] <= temperatures[i]:
                difference += out[i + difference]
            out[i] = difference
    return out