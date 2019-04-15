from typing import List

class Solution:
    def naive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_with_last = nums[0]
        max_without_last = 0
        for i in range(1, len(nums)):
            new_max_with_last = max_without_last + nums[i]
            new_max_without_last = max(max_with_last, max_without_last)
            max_with_last, max_without_last = new_max_with_last, new_max_without_last
        return max(max_with_last, max_without_last)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.naive(nums[:-1]), self.naive(nums[1:]))

nums = [2,1,1,1]
gain = Solution().rob(nums)
print(gain)
                