class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        return [n for n, _ in Counter(nums).most_common(len(nums) // 3 + 1)]