# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = list()
        intervals.sort(key=self.get_key)
        while len(intervals) > 0:
            interval = intervals[0]
            intervals.pop(0)
            while len(intervals) > 0 and intervals[0].start <= interval.end:
                interval.end = interval.end if interval.end > intervals[0].end else intervals[0].end
                intervals.pop(0)
            result.append(interval)
        return result
                    

    @staticmethod
    def get_key(interval1):
        return interval1.start
