class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        current, times = nums[0], 1
        insert = 1
        for i in range(1, len(nums)):
            if nums[i] == current:
                if times < 2:
                    times += 1
                    nums[insert] = nums[i]
                    insert += 1
                else:
                    pass
            else:
                current = nums[i]
                times = 1
                nums[insert] = nums[i]
                insert += 1
        return insert

nums = [0,0,1,1,1,1,2,3,3]
result = Solution().removeDuplicates(nums)
print(result)
print(nums)