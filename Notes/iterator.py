# iterator and generator

class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def __iter__(self):
        self.a = self.head
        return self

    def __next__(self):
        if not self.a:
            raise StopIteration
        x = self.a.val
        self.a = self.a.next
        return x

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
mylist = LinkedList(head)

for num in mylist:
    print(num)

i = iter(mylist)
print(next(i))
print(next(i))
print(next(i))
# print(next(i))



# x = [1, 2, 3]
# for num in x:
#     print(num)