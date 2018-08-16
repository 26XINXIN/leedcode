class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: 
            return 0
        ranges = list()
        for n in nums:
            self.insert(ranges, n)
        result = max([high - low for low, high in ranges])
        return result
        
    def insert(self, ranges, n):
        for i in range(len(ranges)):
            low, high = ranges[i]
            if n + 1 < low:
                ranges.insert(i, [n, n+1])
                return
            elif n + 1 == low:
                if i != 0 and low - 1 == ranges[i-1][1]:
                    ranges.pop(i)
                    ranges[i-1][1] = high
                else:
                    ranges[i] = [low - 1, high]
                return
            elif low <= n < high:
                return
            elif n == high:
                if i != len(ranges) - 1 and high + 1 == ranges[i + 1][0]:
                    ranges[i+1][0] = low
                    ranges.pop(i)
                else:
                    ranges[i] = [low, high + 1]
                return
            else:
                continue
        ranges.append([n, n+1])