class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        totalCost = costs[0]
        for i in range(1, len(costs), 1):
            r = costs[i][0] + min(totalCost[1:])
            g = costs[i][1] + min(totalCost[0], totalCost[2])
            b = costs[i][2] + min(totalCost[:-1])
            totalCost = [r, g, b]
        return min(totalCost)