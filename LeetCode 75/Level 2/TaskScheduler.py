'''Instructions
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.
'''
'''Examples
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
'''
'''Thoughts
1. The key here is you do not actually need to generate the way to get the result - so yo just need pure math. Consider slots with n+1 placeholders (1 character + n for cooldown). You can not have such slots less than a number of occurrences of most frequent character. All other characters you can simply fit into placeholders or expand each slot if # of unique characters to fit into slot is larger than slot size. So the only corner case is when some characters are as frequent as the most frequent one. They will be also in every slot. Last slot is a bit different from any other one as it must not be aligned to n+1. That slot will only be populated with the most frequent characters. Say f is a frequency of most frequent character then for slots [1 .. f-1] you can just compare what is larger size of a slot n +1 or characters to fit into and for the last slot you just take # of most frequent characters. That is it.
Big brain
'''

from collections import Counter

def task(tasks, n):
    if n == 0:
        return len(tasks)
    c = Counter(tasks)

    maxCount = max(c.values())

    countMaxCount = 0
    for t in c.values():
        if t == maxCount:
            countMaxCount += 1
    return max((n+1) * (maxCount-1) + countMaxCount, len(tasks))