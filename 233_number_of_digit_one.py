class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 0:
            return 0
        n = str(n)
        digit_one = 0
        for i in range(len(n)):
            h, d, l = n[:i], n[i], n[i+1:]
            if h:
                digit_one += int(h) * 10 ** (len(l))
            if int(d) > 1:
                digit_one += 10 ** (len(l))
            elif int(d) == 1:
                if len(l):
                    digit_one += int(l) + 1
                else:
                    digit_one += 1
        return digit_one