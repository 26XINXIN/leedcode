# DP solution

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            min_coins = -1
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    if min_coins == -1:
                        min_coins = dp[i - coin] + 1
                    else:
                        min_coins = min(min_coins, dp[i - coin] + 1)
            dp[i] = min_coins
        return dp[-1]