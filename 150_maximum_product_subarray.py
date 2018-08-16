class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_product = nums[0]
        upper = lower = nums[0]
        
        for n in nums[1:]:
            new_upper = max(n, upper * n, lower * n)
            new_lower = min(n, lower * n, upper * n)
            upper, lower = new_upper, new_lower
            max_product = max(upper, max_product)
        return max_product