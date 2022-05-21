'''Write a Python program that inputs a document and then outputs a bar- chart plot of the frequencies of each alphabet character that appears in that document.'''


import collections


def barchart(file_name):
    with open(file_name, 'r') as f:
        l = f.read()

    d = collections.Counter(l)
    print(d)

barchart('/Users/raymond/Desktop/Life And Death/253-288.sgf')