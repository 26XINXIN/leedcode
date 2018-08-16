class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = -10000000000000
        lateset_max_sum = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                if lateset_max_sum < 0:
                    lateset_max_sum = nums[i]
                else:
                    lateset_max_sum += nums[i]
            else:
                if lateset_max_sum < 0:
                    lateset_max_sum = nums[i]
                else:
                    lateset_max_sum += nums[i]
            max_sum = max_sum if lateset_max_sum < max_sum else lateset_max_sum
        return max_sum