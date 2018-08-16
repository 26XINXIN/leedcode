class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        diff = [prices[i + 1] - prices[i] for i in range(len(prices)-1)]
        return sum([d if d > 0 else 0 for d in diff])