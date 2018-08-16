class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        if nums[0] < nums[1]  and nums[1] > nums[2]:
            return 1
        if nums[-3] < nums[-2] and nums[-2] > nums[-1]:
            return len(nums)-2 

        left = 1; right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid-1] < nums[mid] < nums[mid+1]:
                left = mid + 1
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                right = mid
            else:
                right = mid
        return left