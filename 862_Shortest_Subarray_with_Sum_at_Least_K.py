class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        i, j = 0, 0
        ans = 50001
        _sum = 0
        while j < len(A) and _sum < K:
            _sum += A[j]
            j += 1
        if j == len(A) and _sum < K:
            return -1
        ans = min(ans, j-i)
        while j < len(A):
            _sum += 
            j += 1
            
