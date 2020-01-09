class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0
        if n == 1:
            return k
        dup = k
        nodup = k * (k-1)
        for _ in range(3, n+1):
            dup, nodup = nodup, (nodup + dup) * (k-1)
        return nodup + dup
        

class NaiveSolution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0
        self.ways = 0
        self.n = n
        self.k = k
        self.assign([], 0)
        return self.ways
    
    def assign(self, path, i):
        if i == self.n:
            self.ways += 1
            # print(path)
            return
        for c in range(self.k):
            if len(path) > 1 and c == path[-1] and c == path[-2]:
                continue
            path.append(c)
            self.assign(path, i+1)
            path.pop()
        
