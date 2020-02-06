class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for f in range(1, len(num) // 2):
            if s[0] == '0' and f > 1:
                continue
            n1 = int(num[:f])
            for s in range(f, f + (len(num) - f) // 2):
                if num[f] == '0' and s > 1:
                    continue
                n2 = int(num[f:s])
                i = s
                while i < len(num):
                    if not num[s:].startswith(str(n1 + n2)):
                        break
                    else:
                        n1, n2 = n2, n1 + n2
                        i += len(str(n1 + n2))
                if i == len(num):
                    return True
        return False