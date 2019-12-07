class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        endtime = list()
        for s, e in intervals:
            if not endtime:
                endtime.append(e)
            else:
                available = False
                for j in range(len(endtime)):
                    if endtime[j] <= s:
                        endtime[j] = e
                        available = True
                        break
                if not available:
                    endtime.append(e)
        return len(endtime)