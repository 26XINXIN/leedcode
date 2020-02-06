import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        idx = [0] * len(primes)
        ugly = [1]
        
        for _ in range(n-1):
            u = min(ugly[idx[i]] * primes[i] for i in range(len(primes)))
            for i in range(len(primes)):
                idx[i] += u == ugly[idx[i]] * primes[i]
            ugly.append(u)
        return ugly[-1]
            