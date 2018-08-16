class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        inserted = 0
        while i < m + inserted and j < n:
            # if nums1[i] == 0:
            #     nums1[i] = nums2[j]
            #     i += 1; j += 1
            if nums1[i] < nums2[j]:
                i += 1
            else:
                for k in range(m + n - 1, i, -1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                i += 1; j += 1
                inserted += 1
        while j < n:
            nums1[i] = nums2[j]
            i += 1; j += 1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)