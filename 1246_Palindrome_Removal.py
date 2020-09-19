class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        min_moves = dict()
        for i in range(n):
            min_moves[(i, i)] = 1

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if l == 2:
                    min_moves[(i, j)] = 1 if arr[i] == arr[j] else 2
                else:
                    moves = min(min_moves[(i, k)] + min_moves[(k + 1, j)] for k in range(i, j))
                    if arr[i] == arr[j]:
                        moves = min(moves, min_moves[(i + 1, j - 1)])
                    min_moves[(i, j)] = moves
        return min_moves[(0, n-1)]
        
        