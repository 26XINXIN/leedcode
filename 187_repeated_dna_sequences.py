class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        result = list()
        count = dict()
        for i in range(len(s)-9):
            w = s[i:i+10]
            if w not in count:
                count[w] = 1
            else:
                count[w] += 1
            if count[w] == 2:
                result.append(w)
        return result

    def kmp(self, w, t, s):
        i = j = 0
        result = list()
        while i < len(s):
            if j == len(w):
                result.append(i-len(w))
                j = t[j-1] + 1
            elif j == -1 or s[i] == w[j]:
                i += 1; j += 1
            else:
                j = t[j]
        if j == len(w):
            result.append(i - len(w))
        return result

    def build_kmp_table(self, w):
        t = [0] * len(w)
        t[0] = -1; t[1] = 0
        pos = 2; cnd = 0
        while pos < len(w):
            if w[pos-1] == w[cnd]:
                cnd += 1
                t[pos] = cnd
                pos += 1
            elif cnd > 0:
                cnd = t[cnd]
            else:
                t[pos] = 0
                pos = pos + 1
        return t