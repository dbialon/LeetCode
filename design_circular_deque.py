# https://leetcode.com/problems/design-circular-deque/
# Design your implementation of the circular double-ended queue (deque).

class Node:

    def __init__(self, val, link):
        self.val = val
        self.link = link


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.max_l = k
        self.curr_l = 0
        self.deque = None
    

    def __repr__(self):
        """
        Prints the values in deque from front to rear in order
        """
        if self.isEmpty():
            print("Deque empty")
            return None
        tmp = self.deque
        print("F -> ", end="")
        while tmp:
            print(tmp.val, end=" -> ")
            tmp = tmp.link
        print("R")


    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.deque:
            new = Node(value, self.deque)
            self.deque = new
        else:
            self.deque = Node(value, None)
        self.curr_l += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.deque:
            tmp = self.deque
            while tmp.link:
                tmp = tmp.link
            new = Node(value, None)
            tmp.link = new
        else:
            self.deque = Node(value, None)
        self.curr_l += 1
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.deque = self.deque.link
        self.curr_l -= 1
        return True


    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        tmp = self.deque
        prev = None
        while tmp.link:
            prev = tmp
            tmp = tmp.link
        if prev:
            prev.link = None
        else:
            self.deque = None
        self.curr_l -= 1
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.deque.val
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        tmp = self.deque
        while tmp.link:
            tmp = tmp.link
        return tmp.val


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.curr_l == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.curr_l == self.max_l
        

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()