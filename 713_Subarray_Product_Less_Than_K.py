class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sliding window
        if k <= 1:
            return 0
        left = ans = 0
        prod = 1
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans            