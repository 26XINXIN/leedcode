class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if (nums[i-1] < nums[i]):
                break
            i -= 1

        for k in range(len(nums)-1, -1, -1):
            if nums[k] > nums[i-1]:
                tmp = nums[k]
                nums[k] = nums[i-1]
                nums[i-1] = tmp
                break

        self.my_reverse2(nums, i, len(nums)-1)

    def my_reverse2(nums, l, r):
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            self.my_reverse(nums, l+1, r-1)

    def my_reverse(nums, l, r):
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1
