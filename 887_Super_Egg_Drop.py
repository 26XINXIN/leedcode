class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        n = 0
        while K > 1 and N > 1:
            N = (N + 1) // 2
            K -= 1
            n += 1
        if K == 1:
            return n + N
        else:
            return n + 1