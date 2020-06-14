class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missed = 1
        i = 0
        max_cover = 0
        cnt = 0
        while max_cover < n:
            if i < len(nums):
                if nums[i] <= missed:
                    max_cover += nums[i]
                    missed = max_cover + 1
                    i += 1
                else:
                    max_cover += missed
                    missed = max_cover + 1
                    cnt += 1
        return cnt