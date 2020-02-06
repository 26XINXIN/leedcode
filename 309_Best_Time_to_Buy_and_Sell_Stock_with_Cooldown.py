class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, rest, sell = -100000, 0, 0
        for i in range(1, len(prices)):
            buy, rest, sell = max(rest - prices[i], buy), buy + prices[i], max(rest, sell) 
        return max(rest, sell)