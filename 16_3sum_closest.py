class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mini = 10000000
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if abs(summ - target) < abs(mini - target):
                    mini = summ
                if summ > target:
                    r -= 1
                if summ <= target:
                    l += 1
        return mini

res = Solution().threeSumClosest([1,1,1,0], 100)
print(res)