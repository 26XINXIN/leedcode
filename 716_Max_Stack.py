class MaxStack:

    class Node:
        def __init__(self, x):
            self.val = x
            self.next = None
            self.pre = None

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = MaxStack.Node(None)
        self.last = self.stack
        self.max = self.stack
        

    def push(self, x: int) -> None:
        node = MaxStack.Node(x)
        self.last.next = node
        node.pre = self.last
        self.last = node
        if self.max.val is None or self.max.val <= x:
            self.max = self.last

    def pop(self) -> int:
        val = self.last.val
        if self.max == self.last:
            self.max = self.stack
        
        self.last = self.last.pre
        self.last.next = None
        
        if self.max == self.stack:
            self.findMax()
        return val

    def top(self) -> int:
        return self.last.val

    def peekMax(self) -> int:
        return self.max.val
        

    def popMax(self) -> int:
        val = self.max.val
        self.max.pre.next = self.max.next
        if self.max.next is not None:
            self.max.next.pre = self.max.pre
        if self.last == self.max:
            self.last = self.max.pre
        self.findMax()
        return val

    def findMax(self):
        max_val = -1e7
        self.max = self.stack
        it = self.stack.next
        while it is not None:
            if it.val > max_val:
                max_val = it.val
                self.max = it
            it = it.next


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()