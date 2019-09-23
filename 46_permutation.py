class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        elif len(nums) == 0:
            return []

        result = list()
        for i in range(len(nums)):
            sub_nums = list(nums)
            sub_nums.pop(i)
            sub_permute = self.permute(sub_nums)
            for p in sub_permute:
                result.append(p + [nums[i]])
        return result
    
    def permutes(self, nums):
        from itertools import permutations
        return permutations(nums)