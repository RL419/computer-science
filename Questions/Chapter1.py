# Reinforcement
'''Demonstrate how to use Python’s list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].'''
a = [2**i for i in range(9)]
'''Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module in- cludes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function.'''
from random import randrange

def choice(data):
    return data(randrange(0,len(data)))

# Creativity
'''Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each possi- ble order occurs with equal probability. The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using only the randint function, implement your own version of the shuffle function.
'''
from random import randint

def shuffle(data):
    out = []
    for _ in range(len(data)):
        i = randint(0, len(data))
        out.append(data.pop(i))
    return out

'''Demonstrate how to use Python’s list comprehension syntax to produce thelist[ a , b , c ,..., z ],butwithouthavingtotypeall26such characters literally.'''

b = [chr(i) for i in range(97, 123)]

# Projects
'''Write a Python program that outputs all possible strings formed by using thecharacters c , a , t , d , o ,and g exactly once.'''

def generate(string: list):
    if len(string) == 1:
        return string
    out = []
    for character in string:
        no = string.copy()
        no.remove(character)
        previous = generate(no)
        for s in previous:
            out.append(character + s)
    return out

# print(generate(['c','a','t','d','o','g']))
# test = generate(['c','a','t','d','o','g'])
# print(len(test) == len(set(test)))

'''Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.'''
import math

def divideby2(num):
    return int(math.log(num, 2))

'''Write a Python program that can “make change.” Your program should take two numbers as input, one that is a monetary amount charged and the other that is a monetary amount given. It should then return the number of each kind of bill and coin to give back as change for the difference between the amount given and the amount charged. The values assigned to the bills and coins can be based on the monetary system of any current or former government. Try to design your program so that it returns as few bills and coins as possible.'''

def make_change(charged, given):
    d = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0, 0.25:0, 0.1:0, 0.05:0}
    needed = given - charged
    for k in d.keys():
        stuff = divmod(needed, k)
        d[k] += int(stuff[0])
        needed = stuff[1]

    out = ""
    for key, value in d.items():
        if value > 0:
            if key > 2:
                out += f'{value} {key} dollar bills, '
            else:
                out += f'{value} {key} dollar coins, '
    return out[:-2]

print(make_change(463.5, 1067.65))