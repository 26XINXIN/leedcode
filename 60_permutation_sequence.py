class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums_of_p = [0] * n
        for i in range(1, n):
            if i == 1: nums_of_p[i] = 1
            else:
                nums_of_p[i] = nums_of_p[i-1] * i
        
        nums = [i for i in range(1, n + 1)]
        result = ""
        k -= 1
        for i in range(n-1, 0, -1):
            idx = k // nums_of_p[i]
            result += str(nums[idx])
            nums.pop(idx)
            k %= nums_of_p[i]
        result += str(nums[0])
        return result

print(Solution().getPermutation(4, 9))