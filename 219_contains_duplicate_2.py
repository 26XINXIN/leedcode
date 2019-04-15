from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        if k >= len(nums):
            return self.naive(nums)
        num_set = set()
        for i in range(0, k+1):
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])
        for i in range(0, len(nums)-k-1):
            num_set.remove(nums[i])
            if nums[i+k+1] in num_set:
                return True
            num_set.add(nums[i+k+1])
        return False

    def naive(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

