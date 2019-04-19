from math import sqrt

class SolutionTimeExceeded:
    def numSquares(self, n: int) -> int:
        nums = [0, 1, 2, 3]
        squares = [i * i for i in range(1, int(sqrt(n))+1)]
        for i in range(4, n+1):
            nums.append(min(nums[i-sq] for sq in squares if i-sq >= 0 and i - sq < sq))
        return nums[i]
        
        
class Solution:
    def numSquares(self, n: int) -> int:   
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
    	    dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        return dp[n]

def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
    	    dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        return dp[n]