class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        i = 2
        self.result = set()
        while i * i <= n:
            if n % i == 0:
                j = n // i
                self.result.add((i, j))
                self.decomposeFactores([i], j)
            i += 1
        return [list(r) for r in self.result]
                
    def decomposeFactores(self, factors, n):
        if n < factors[-1]:
            return 
        i = factors[-1]
        while i * i <= n:
            if n % i == 0:
                j = n // i
                res = tuple(factors + [i, j])
                if res not in self.result:
                    self.result.add(res)
                    self.decomposeFactores(factors + [i], j)
            i += 1
