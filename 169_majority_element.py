class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = dict()
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        for n, cnt in count.items():
            if cnt > len(nums) // 2:
                return n