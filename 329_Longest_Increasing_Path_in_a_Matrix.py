class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        longest_paths = [[1] * m for _ in range(n)]
        directions = self.get_directions(matrix)
        changed = True
        while changed:
            new_longest_paths = [[longest_paths[i][j] for j in range(m)] for i in range(n)]
            changed = False
            for i in range(n):
                for j in range(m):
                    if len(directions[(i, j)]) > 0:
                        lp = 1 + max(longest_paths[ii][jj] for ii, jj in directions[(i, j)])
                    else:
                        lp = 1
                    if lp != longest_paths[i][j]:
                        changed = True
                    new_longest_paths[i][j] = lp
            longest_paths = new_longest_paths
        return max(max(longest_paths[i]) for i in range(n))
                    
    
    def get_directions(self, matrix):
        directions = dict()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                dirs = list()
                if i > 0 and matrix[i - 1][j] > matrix[i][j]:
                    dirs.append((i - 1, j))
                if i < n - 1 and matrix[i + 1][j] > matrix[i][j]:
                    dirs.append((i + 1, j))
                if j > 0 and matrix[i][j - 1] > matrix[i][j]:
                    dirs.append((i, j - 1))
                if j < m - 1 and matrix[i][j + 1] > matrix[i][j]:
                    dirs.append((i, j + 1))
                directions[(i, j)] = dirs
        return directions