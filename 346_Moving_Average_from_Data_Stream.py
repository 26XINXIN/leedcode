from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.cap = size
        self.window = deque()
        self.ma = 0
        

    def next(self, val: int) -> float:
        size = len(self.window)
        if size < self.cap:
            self.window.append(val)
            self.ma = (self.ma * size + val) / (size + 1)
        else:
            first = self.window.popleft()
            self.window.append(val)
            self.ma = (self.ma * size + val - first) / size
        return self.ma
        
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)