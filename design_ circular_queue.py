# https://leetcode.com/problems/design-circular-queue/
# Design your implementation of the circular queue. The circular queue
# is a linear data structure in which the operations are performed
# based on FIFO (First In First Out) principle and the last position
# is connected back to the first position to make a circle. It is also
# called "Ring Buffer".
# One of the benefits of the circular queue is that we can make use
# of the spaces in front of the queue. In a normal queue, once the queue
# becomes full, we cannot insert the next element even if there is
# a space in front of the queue. But using the circular queue, we can
# use the space to store new values.

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None] * k
        self.start = 0
        self.end = 0
        self.size = 0


    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.size += 1
        self.queue[self.end%len(self.queue)] = value
        self.end += 1
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.size -= 1
        self.queue[self.start%len(self.queue)] = None
        self.start += 1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.start%len(self.queue)]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[(self.end-1)%len(self.queue)]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
