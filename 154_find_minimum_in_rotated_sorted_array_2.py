class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        min_num = nums[0]
        left = 0
        right = len(nums)
        while nums[right-1] == nums[0] and right >= 1:
            right -= 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < min_num:
                right = mid
                min_num = nums[mid]
            else:
                left = mid + 1
        return nums[0] if left == len(nums) else nums[left]
