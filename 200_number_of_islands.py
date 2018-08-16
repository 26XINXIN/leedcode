try:
    from Queue import Queue
except:
    from queue import Queue

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        island_num = list()
        n_island = 0
        for _ in range(n):
            island_num.append([0] * m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and island_num[i][j] == 0:
                    n_island += 1
                    self.extend_island(grid, island_num, i, j, n, m)
        return n_island

    def extend_island(self, grid, island_num, i, j, n, m):
        q = Queue()
        q.put((i, j))
        island = set()
        island.add((i, j))
        while not q.empty():
            i, j = q.get()
            if i != 0 and grid[i-1][j] == '1' and (i-1, j) not in island:
                island.add((i-1, j))
                q.put((i-1, j))
            if i != n-1 and grid[i+1][j] == '1' and (i+1, j) not in island:
                island.add((i+1, j))
                q.put((i+1, j))
            if j != 0 and grid[i][j-1] == "1" and (i, j-1) not in island:
                island.add((i, j-1))
                q.put((i, j-1))
            if j != m-1 and grid[i][j+1] == "1" and (i, j+1) not in island:
                island.add((i, j+1))
                q.put((i, j+1))
            
        for i, j in island:
            island_num[i][j] = 1
            
                