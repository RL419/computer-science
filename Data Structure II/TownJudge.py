'''Instructions
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
'''
'''Examples
Input: n = 2, trust = [[1,2]]
Output: 2

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
'''
'''Thoughts

'''

def identify(n:int, trust:list):
    if n == 1:
        return 1
    
    if not trust:
        return -1

    potential_judge = set()
    inocent_people = set()

    for truster, trusted in trust:
        inocent_people.add(truster)
        
        if truster in potential_judge:
            potential_judge.remove(truster)
            continue

        if trusted not in inocent_people:
            potential_judge.add(trusted)
    
    if len(potential_judge) == 0 or len(inocent_people) != n-1:
        return -1
    return potential_judge[0]