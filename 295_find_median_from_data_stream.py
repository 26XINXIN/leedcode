from heapq import heappop, heappush

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hi = list()
        self.lo = list()
        
    def addNum(self, num: int) -> None:
        if len(self.hi) == 0:
            heappush(self.hi, (num, num))
            return
        _, hitop = self.hi[0]
        if num >= hitop:
            heappush(self.hi, (num, num))
            if len(self.hi) == len(self.lo) + 2:
                _, _num = heappop(self.hi)
                heappush(self.lo, (-_num, _num))
        else:
            heappush(self.lo, (-num, num))
            if len(self.lo) == len(self.hi) + 2:
                _, _num = heappop(self.lo)
                heappush(self.hi, (_num, _num))
            

        
    def findMedian(self) -> float:
        if len(self.hi) == len(self.lo):
            _, n1 = self.hi[0]
            _, n2 = self.lo[0]
            return 0.5 * n1 + 0.5 * n2
        else:
            _, n = self.hi[0] if len(self.hi) > len(self.lo) else self.lo[0]
            return n


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()