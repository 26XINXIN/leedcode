class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        times = dict()
        for n in nums:
            if n not in times:
                times[n] = 1
            else:
                times[n] += 1
        for n, t in times.items():
            if t == 1:
                return n