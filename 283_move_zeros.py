class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if j == len(nums):
                    return
                else:
                    nums[i], nums[j] = nums[j], nums[i]