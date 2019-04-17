class Solution:
    def isUgly(self, num: int) -> bool:
        while num > 1:
            individable = True
            for factor in [2, 3, 5]:
                if num % factor == 0:
                    num //= factor
                    individable = False
                    break
            if individable:
                return True
        return True