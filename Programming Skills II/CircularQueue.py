'''Instructions
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 
'''
'''Examples
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
'''
'''Thoughts
1. init creates a list for the queue and keeps track of k
2. enQueue returns False if length of queue if equal to k, else appends value into queue and return True
3. deQueue returns False if queue is empty, else removes the first element.
4. Front returns  queue[0] if queue else -1
5. Rear returns queue[-1] if queue else -1
6. isEmpty returns True if it is empty else false
7. isFull returns True if length of queue is equal to k else False
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.count = k

    def enQueue(self, value: int) -> bool:
        if len(self.q) >= self.count:
            return False
        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        if self.q:
            self.q.pop(0)
            return True
        return False

    def Front(self) -> int:
        return self.q[0] if self.q else -1

    def Rear(self) -> int:
        return self.q[-1] if self.q else -1

    def isEmpty(self) -> bool:
        return False if self.q else True

    def isFull(self) -> bool:
        return True if len(self.q) == self.count else False