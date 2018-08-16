class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        begin = end = 0
        min_length = len(nums) + 1
        current_sum = 0
        current_len = 0
        while end < len(nums):
            current_sum += nums[end]
            end += 1
            current_len += 1
            if current_sum >= s:
                while current_sum - nums[begin] >= s:
                    current_sum -= nums[begin]
                    current_len -= 1
                    begin += 1
                min_length = min(min_length, current_len)
        return min_length if min_length <= len(nums) else 0
        