class Solution:
    def threeSum(self, nums, target):
        res = list()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ < target:
                    l += 1
                elif summ > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l +=1; r -= 1
                
        return res

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = list()
        for i in range(len(muns) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            three_target = target - nums[i]
            three_res = self.threeSum(nums[i+1:], three_target)
            for e in three_res:
                res.append([nums[i]] + e)
        return res
