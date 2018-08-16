class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)-1):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            try:
                j = numbers[i+1:].index(target-numbers[i])
            except:
                j = -1
            if j != -1:
                return [i + 1, j + i + 2]