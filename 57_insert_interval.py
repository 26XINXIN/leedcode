# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = list()
        tmp = list()
        for inter in intervals:
            if not self.overlap(inter, newInterval):
                result.append(inter)
            else:
                tmp.append(inter)
        tmp.append(newInterval)
        start = min([inter.start for inter in tmp])
        end = max([inter.end for inter in tmp])
        result.append(Interval(start, end))
        result.sort(key=self.get_key)
        return result
    
    @staticmethod
    def get_key(interval1):
        return interval1.start

    @staticmethod
    def overlap(interval1, interval2):
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