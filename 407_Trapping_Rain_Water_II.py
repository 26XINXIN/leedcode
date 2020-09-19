from heapq import *
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        if n <= 1:
            return 0
        m = len(heightMap[0])
        if m <= 1:
            return 0
        
        edges = []
        for i in range(n):
            edges.append((heightMap[i][0], i, 0))
            edges.append((heightMap[i][m - 1], i, m - 1))
        for j in range(m):
            edges.append((heightMap[0][j], 0, j))
            edges.append((heightMap[n - 1][j], n - 1, j))
        heapify(edges)

        visited = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            visited[i][0] = 1
            visited[i][m - 1] = 1
        for j in range(m):
            visited[0][j] = 1
            visited[n - 1][j] = 1
        
        water = 0
        while len(edges) > 0:
            height, i, j = heappop(edges)
            for ii, jj in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if 0 <= ii < n and 0 <= jj < m and visited[ii][jj] == 0:
                    visited[ii][jj] = 1
                    if heightMap[ii][jj] >= height:
                        heappush(edges, (heightMap[ii][jj], ii, jj))
                    else:
                        water += height - heightMap[ii][jj]
                        heappush(edges, (height, ii, jj))
        
        return water
        