class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        self.n = len(image)
        if self.n == 0:
            return 0
        self.m = len(image[0])
        self.visited = set()
        frontier = set([(x, y)])
        while frontier:
            new_frontier = set()
            for x, y in frontier:
                self.visited.add((x, y))
                if self.isValid(x+1, y) and image[x+1][y] == '1': new_frontier.add((x+1, y))
                if self.isValid(x-1, y) and image[x-1][y] == '1': new_frontier.add((x-1, y))
                if self.isValid(x, y+1) and image[x][y+1] == '1': new_frontier.add((x, y+1))
                if self.isValid(x, y-1) and image[x][y-1] == '1': new_frontier.add((x, y-1))
            frontier = new_frontier
        X, Y = set(), set()
        for x, y in self.visited:
            X.add(x)
            Y.add(y)
        xmax, xmin = max(X), min(X)
        ymax, ymin = max(Y), min(Y)
        print(X, Y)
        return (xmax + 1 - xmin) * (ymax + 1 - ymin)
        
    
    def isValid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m and (x, y) not in self.visited