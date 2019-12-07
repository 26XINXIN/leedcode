class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.v = v
        self.n = len(self.v)
        self.i, self.j = 0, 0
        while self.i < self.n and self.j == len(self.v[self.i]):
            self.i += 1
            self.j = 0

    def next(self) -> int:
        value = self.v[self.i][self.j]
        self.j += 1
        while self.i < self.n and self.j == len(self.v[self.i]):
            self.i += 1
            self.j = 0
        return value

    def hasNext(self) -> bool:
        return not self.i == self.n


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()