from DataStructures.BST import Tree, Node
from random import randint, seed

seed(8)
t = Tree()
for _ in range(20):
    t.insert(randint(1, 20))

# Inorder generator for BST
def inorder(head: Node):
    if not head:
        return None
    yield from inorder(head.left)
    yield head.val
    yield from inorder(head.right)

g = inorder(t.root)
for i in g:
    print(i)


# example with generator
# x = [1,2,3,4,5]
# def gen(x: list[int]):
#     for i in x:
#         yield i

# g = gen(x)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))