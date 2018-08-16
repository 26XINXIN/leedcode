class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        diff = list()
        for i in range(len(prices) - 1):
            diff.append(prices[i+1] - prices[i])
        max_profit = 0
        latest_max_profit = 0
        for d in diff:
            latest_max_profit = max(d, latest_max_profit + d)
            max_profit = max(latest_max_profit, max_profit)
        return max_profit
                