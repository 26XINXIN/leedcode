class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        diff = n - m + 1
        order, power = 0, 1
        while diff > power:
            order, power = order + 1, power * 2
        order, power = order - 1, power // 2
        


print(Solution().rangeBitwiseAnd(0, 2147483647))