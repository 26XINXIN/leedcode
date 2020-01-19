class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.i, self.j = 0, 0
        

    def next(self) -> int:
        if self.i == len(self.v1):
            self.j += 1
            return self.v2[self.j-1]
        if self.j == len(self.v2):
            self.i += 1
            return self.v1[self.i-1]
        if self.i == self.j:
            self.i += 1
            return self.v1[self.i-1]
        else:
            self.j += 1
            return self.v2[self.j-1]
            
        

    def hasNext(self) -> bool:
        return self.i < len(self.v1) or self.j < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())