import bisect

class Inteval:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __le__(self, i):
        return self.left <= i.left
    
    def __lt__(self, i):
        return self.left < i.left

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ranges = []
                

    def addNum(self, val: int) -> None:
        loc = bisect.bisect_left(self.ranges, Inteval(val + 1, 0), 0, len(self.ranges))
        if loc != 0 and self.ranges[loc - 1].right >= val:
            return
        if loc != len(self.ranges) and self.ranges[loc].left == val + 1:
            if loc != 0 and self.ranges[loc - 1].right == val - 1:
                self.ranges[loc - 1].right = self.ranges[loc].right
                self.ranges.pop(loc)
            else:
                self.ranges[loc].left = val
        else:
            if loc != 0 and self.ranges[loc - 1].right == val - 1:
                self.ranges[loc-1].right = val
            else:
                self.ranges.insert(loc, Inteval(val, val))
                
    def getIntervals(self) -> List[List[int]]:
        return [[i.left, i.right] for i in self.ranges]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()