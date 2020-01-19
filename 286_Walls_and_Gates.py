class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n = len(rooms)
        m = len(rooms[0])
        self.inf = 2147483647
        self.n, self.m = n, m
        self.rooms = rooms
        frontier = set()
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    frontier.add((i, j))
        
        d = 1
        while frontier:
            new_frontier = set()
            for i, j in frontier:
                if self.isValid(i + 1, j):
                    rooms[i+1][j] = d
                    new_frontier.add((i+1, j))
                if self.isValid(i - 1, j):
                    rooms[i-1][j] = d
                    new_frontier.add((i-1, j))
                if self.isValid(i, j + 1):
                    rooms[i][j+1] = d
                    new_frontier.add((i, j+1))
                if self.isValid(i, j - 1):
                    rooms[i][j-1] = d
                    new_frontier.add((i, j-1))
            frontier = new_frontier
            d += 1
                      

    def isValid(self, i, j):
        return 0 <= i < self.n and 0 <= j < self.m and self.rooms[i][j] == self.inf