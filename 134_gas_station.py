class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 0:
            return -1
        n = len(gas)
        
        remain = 0
        min_remain = 0
        min_index = 0
        for i in range(n):
            remain += (gas[i] - cost[i])
            if remain < min_remain:
                min_remain = remain
                min_index = (i + 1) % n
        if remain < 0:
            return -1
        else:
            return min_index
            