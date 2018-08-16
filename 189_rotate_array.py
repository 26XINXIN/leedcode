from fractions import gcd

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = gcd(n, k)
        for i in range(l):
            tmp = nums[i]
            j = i
            while j != (i + k) % n:
                nums[j] = nums[(j-k)%n]
                j = (j - k) % n
            nums[j] = tmp
        # return nums

        