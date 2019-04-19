class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        citations.sort(reverse=True)
        i = len(citations)
        while i > citations[i-1]: i -= 1
        return i