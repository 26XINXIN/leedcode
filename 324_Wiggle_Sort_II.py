class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        nums.sort()
        nums[::2], nums[1::2] = nums[:n//2], nums[n//2:]
