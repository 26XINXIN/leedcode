# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class RangeModule:
    def __init__(self):
        self.intervals = list()

    @staticmethod
    def get_key(interval1):
        return interval1.start

    @staticmethod
    def overlap(interval1, interval2):
        if interval1.start <= interval2.start:
            if interval2.start < interval1.end:
                return True
            else:
                return False
        else:
            if interval1.start < interval2.end:
                return True
            else:
                return False
    
    @staticmethod
    def can_merge(interval1, interval2):
        if interval1.start <= interval2.start:
            if interval2.start <= interval1.end:
                return True
            else:
                return False
        else:
            if interval1.start <= interval2.end:
                return True
            else:
                return False

    def insert(self, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = list()
        tmp = list()
        for inter in self.intervals:
            if not self.can_merge(inter, newInterval):
                result.append(inter)
            else:
                tmp.append(inter)
        tmp.append(newInterval)
        start = min([inter.start for inter in tmp])
        end = max([inter.end for inter in tmp])
        result.append(Interval(start, end))
        result.sort(key=self.get_key)
        self.intervals = result
    
    def minus(self, interval1, interval2):
        if interval1.start < interval2.start:
            if interval1.end > interval2.end:
                return [Interval(interval1.start, interval2.start), Interval(interval2.end, interval1.end)]
            else:
                new_interval = Interval(interval1.start, min(interval1.end, interval2.start))
                return [new_interval]
        elif interval1.end > interval2.end:
            new_interval = Interval(max(interval1.start, interval2.end), interval1.end)
            return [new_interval]
        else:
            return None

    def subsumption(self, interval1, interval2):
        if interval1.start >= interval2.start and interval1.end <= interval2.end:
            return True
        else:
            return False

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        self.insert(Interval(left, right))
        

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        query_interval = Interval(left, right)
        for inter in self.intervals:
            if self.subsumption(query_interval, inter):
                return True
        return False

        

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        interval_to_remove = Interval(left, right)
        new_intervals = list()
        for inter in self.intervals:
            if self.overlap(inter, interval_to_remove):
                removed_interval = self.minus(inter, interval_to_remove)
                if removed_interval != None:
                    new_intervals += removed_interval
            else:
                new_intervals.append(inter)
        self.intervals = new_intervals
            
    def print_stat(self):
        print("[", end="")
        for inter in self.intervals:
            print("[{}, {}], ".format(inter.start, inter.end), end="")
        print("]")    
        
        


# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.print_stat()
obj.addRange(6, 8)
obj.print_stat()
obj.removeRange(7, 8)
obj.print_stat()
obj.removeRange(8, 9)
obj.print_stat()
obj.addRange(8, 9)
obj.print_stat()
obj.removeRange(1, 3)
obj.print_stat()
obj.addRange(1, 8)
obj.print_stat()
