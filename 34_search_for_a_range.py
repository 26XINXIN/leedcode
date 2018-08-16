class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        l = self.lower_bi_search(nums, 0, len(nums)-1, target)
        if l == -1:
            return [-1, -1]
        r = self.upper_bi_search(nums, l, len(nums)-1, target)
        return [l, r]
        
    def lower_bi_search(self, nums, l, r, target):
        if l == r:
            if nums[l] == target:
                return l
            else:
                return -1
        mid = (l + r) // 2
        if nums[mid] < target:
            return self.lower_bi_search(nums, mid+1, r, target)
        else:
            return self.lower_bi_search(nums, l, mid, target)

    def upper_bi_search(self, nums, l, r, target):
        if l == r:
            if nums[l] == target:
                return l
            else:
                return -1
        # if l + 1 == r:
        #     if nums[l] == target and nums[r] != target:
        #         return l
        #     elif nums[r] == target:
        #         return r
        #     else:
        #         return -1
        mid = (l + r + 1) // 2
        if nums[mid] > target:
            return self.upper_bi_search(nums, l, mid - 1, target)
        else:
            return self.upper_bi_search(nums, mid, r, target)

Solution().searchRange([5,7,7,8,8,10], 8)