class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        minCost = [0] * len(costs[0])
        for cost in costs:
            nextMinCost = list()
            for i in range(len(minCost)):
                nextMinCost.append(min(cost[i] + c for c in minCost[:i] + minCost[i+1:]))
            minCost = nextMinCost
        return min(minCost)
                    