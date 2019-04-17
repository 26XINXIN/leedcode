class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        u = [1]
        for _ in range(n-1):
            u2, u3, u5 = u[i2] * 2, u[i3] * 3, u[i5] * 5
            minu = min(u2, u3, u5)
            if minu == u2:
                i2 += 1
            if minu == u3:
                i3 += 1
            if minu == u5:
                i5 += 1
            u.append(minu)
        return u[-1]