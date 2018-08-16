import random
class Solution:

    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        if N >= K + W:
            return 1
        elif K == 0:
            return 1
        
        # p = 0
        # for i in range(0, min(W, N-K+1)):
        #     for j in range(i + 1, W + 1):
        #         p += self.P(K + i - j, W) * 1/W
        # return p
        return self.P3(N, K, W)
    
    def P(self, N, W): # P(sum == N)
        if N < 0:
            return 0
        elif N == 0:
            return 1
        
        p = 0
        for i in range(1, W + 1):
            p += 1/W * self.P(N-i, W)
        print("P({})={}".format(N, p))
        return p

    def P2(self, N, K, W):
        p = [0] * K
        p[0] = 1
        for i in range(1, K):
            for j in range(1, min(W, i) + 1):
                p[i] += 1/W * p[i - j]
        
        result = 0
        for i in range(0, min(W, N-K+1)):
            for j in range(i + 1, W + 1):
                if K + i - j < 0: continue
                result += p[K + i - j] * 1/W
        return result
    
    def P3(self, N, K, W):
        n = 0
        for _ in range(200000):
            if self.gen(K, W) <= N:
                n += 1
        return n / 200000

    def gen(self, K, W):
        total = 0
        while total < K:
            total += random.randint(1, W)
        return total

Solution().new21Game(10, 1, 10)