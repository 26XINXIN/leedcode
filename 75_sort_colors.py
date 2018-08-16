class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = dict()
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        i = 0
        for color, times in count.items():
            for _ in range(times):
                nums[i] = color; i += 1
        