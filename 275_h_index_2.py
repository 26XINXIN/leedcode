class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if all(c == 0 for c in citations):
            return 0
        if not citations: return 0
        citations = citations[::-1]
        index = self.binary_search(citations, 0, len(citations))
        return index + 1
    
    def binary_search(self, a, left, right):
        if right-left == 1:
            return left
        
        mid = (left + right) // 2
        if mid+1 <= a[mid]:
            return self.binary_search(a, mid, right)
        elif mid+1 > a[mid]:
            return self.binary_search(a, left, mid)