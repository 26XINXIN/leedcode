class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)
        res = list()
        i = j = 0
        for _ in range(k):
            if i < len(nums1) and nums1[i] > nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        return res