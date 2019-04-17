class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        single = set()
        for n in nums:
            if n not in single:
                single.add(n)
            else:
                single.remove(n)
        return list(single)
                