class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left, right = 0, sum(nums[1:])
        if left == right:
            return 0
        pivot = 1
        while pivot < len(nums):
            left += nums[pivot-1]
            right -= nums[pivot]
            if left == right:
                return pivot
            pivot += 1
        return -1