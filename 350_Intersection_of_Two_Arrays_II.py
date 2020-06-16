from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        cnt = cnt1 & cnt2
        res = list()
        for n, c in cnt.items():
            res += [n] * c
        return res