class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        first, last = 0, 0
        jump_times = 0
        while last < n - 1:
            # print(first, last)
            farest = 0
            for i in range(first, last + 1):
                farest = farest if farest > i + nums[i] else i + nums[i]
            first = last
            last = farest
            jump_times += 1
        return jump_times

print(Solution().jump([1,2]))