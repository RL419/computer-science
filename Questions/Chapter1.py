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