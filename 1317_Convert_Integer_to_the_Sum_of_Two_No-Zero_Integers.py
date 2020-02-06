class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        m = n
        a = ''
        carry = 0
        while n:
            d = n % 10 - carry
            n //= 10
            if d <= 0:
                if n == 0:
                    break
                a = '1' + a
                carry = 1
            elif d == 1:
                a = '2' + a
                carry = 1
            else:
                a = '1' + a
                carry = 0
        return [int(a), m - int(a)]