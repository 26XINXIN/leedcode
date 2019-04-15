from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            for j in range(len(nums)-2, i-1, -1):
                if nums[j] < nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[k-1]