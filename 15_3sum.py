class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if sum([nums[i], nums[j], nums[k]]) == 0:
                        a = nums[i]
                        b = nums[j]
                        c = nums[k]
                        if a < b:
                            if b < c:
                                result.add((a, b, c))
                            else:
                                if a < c:
                                    result.add((a, c, b))
                                else:
                                    result.add((c, a, b))
                        else:
                            if b < c:
                                if a < c:
                                    result.add((b, a, c))
                                else:
                                    result.add((b, c, a))
                            else:
                                result.add((c, b, a))
    
        return list(result)
