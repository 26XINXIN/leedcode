class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 1
        while i != len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return i