class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = self.binary_search(nums, 0, len(nums)-1, target)
        if ans == len(nums)-1 and target > nums[-1]:
            ans += 1
        return ans
    
    def binary_search(self, nums, l, r, target):
        if l == r:
            return l
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums, mid + 1, r, target)
        else:
            return self.binary_search(nums, l, mid, target)
