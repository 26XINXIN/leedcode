class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) == 0:
            return []
        nums.sort()
        return self.permute(nums)

    def permute(self, nums):

        if len(nums) == 1:
            return [nums]
        elif len(nums) == 0:
            return []

        result = list()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            sub_nums = list(nums)
            sub_nums.pop(i)
            sub_permute = self.permute(sub_nums)
            for p in sub_permute:
                result.append(p + [nums[i]])
        return result

