class Stack():
    def __init__(self):
        self.stack = list()
    
    def push(self, x):
        self.stack.append(x)
    
    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = Stack()
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s.push(x)
        if self.s.size() == 1:
            self.front = self.s.peek()
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        s2 = Stack()
        while self.s.size() > 0:
            s2.push(self.s.pop())
        x = s2.pop()
        if s2.size() > 0:
            self.front = s2.peek()
        else:
            self.front = None
        while s2.size() > 0:
            self.s.push(s2.pop())
        return x
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s.size() == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()