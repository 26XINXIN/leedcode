class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for n in nums:
            l = len(result)
            for i in range(l):
                result.append(result[i] + [n])
            # result.append([])
        return result